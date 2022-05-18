from antlr4 import *
from dist.BasicLangLexer import BasicLangLexer
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangParser import BasicLangParser
from link import Link
import sys
import argparse
import re
from memory import Memory

eresult = None
orig_memory = Memory()
memory = orig_memory

class MyVisitor(BasicLangVisitor):
    def set_memory(self, to_what=None):
        global memory
        global orig_memory

        if to_what != None:
            memory = memory.get_obj(to_what)
        else:
            memory = orig_memory

    def visitExecScript(self, ctx):
        for blk in list(ctx.getChildren()):
            self.visit(blk)
    

    def visitIfBlock(self, ctx):
        global eresult
        ifblk = ctx.ifblk
        act = ctx.act

        if ifblk != None:
            ifblk = ifblk.text
            for st in memory.__dict__[ifblk]:
                self.visit(st)
            
            if eresult:
                if act != None:
                    act = act.text
                    
                for st in memory.__dict__[act]:
                    result = self.visit(st)
                    if result != None:
                        print(result)


    def visitSetResult(self, ctx):
        global eresult
        varint = ctx.varint
        varid = ctx.varid
        
        if varint != None:
            varint = int(varint.text)
            eresult = varint
        
        if varid != None:
            varid = varid.text
            eresult = memory.__dict__[varid]
        

    def visitInsertFile(self, ctx):
        global memory
        fname = ctx.fname
        if fname != None:
            fname = fname.text
        else:
            return "Filename not specified"

        memory.set(fname, Memory())
        prev_memory = memory
        memory = getattr(memory, fname)

        fname = f"{fname}.bl"
        try:
            fs = FileStream(fname)
            lexer = BasicLangLexer(fs)
            stream = CommonTokenStream(lexer)
            parser = BasicLangParser(stream)
            tree = parser.script()
            visitor = MyVisitor()
            output = visitor.visit(tree)
            print(output)
        except:
            print("Error importing file")

        memory = prev_memory


    def visitBlk(self, ctx):
        global memory
        if ctx.bid != None:
            bid = ctx.bid.text
        else:
            return "Block definition error"

        statements = list(ctx.getChildren())

        if bid != None:
            memory.set(bid, statements)
        

        if "MAINBLOCK" in bid:
            if "." in bid:
                self.set_memory(bid)

            for st in memory.get(bid):
                self.visit(st)

            self.set_memory()


    def visitExecBlock(self, ctx):
        global memory
        blkid = ctx.blkid
        
        if blkid != None:
            blkid = ctx.blkid.text
        else:
            return "Block definition error"

        if ctx.times != None:
            times = ctx.times.text
            
            if times == "max":
                times = sys.maxsize
            elif times in memory.__dict__.keys():
                times = memory.__dict__[times]
            elif times.isdigit():
                times = int(times)
            else:
                return "Invalid value"
        else:
            times = 1
        
        for i in range(times):
            for st in memory.get(blkid):
                result = self.visit(st)
                if result != None:
                    print(result)

    def visitShowStrExpr(self, ctx):
        token_source = ctx.start.getTokenSource()
        input_stream = token_source.inputStream
        start, stop  = ctx.start.start, ctx.stop.stop
        words_str = input_stream.getText(start, stop)
        words_str = words_str.replace("print ", "")

        patterns = ["{ ", " }", "[ ", " ]", " [", " :", ": "]

        for pattern in patterns:
            to_rep = pattern.replace(" ", "")
            words_str = words_str.replace(pattern, to_rep)

        vars = re.findall(r"{([a-z.]+)}", words_str)

        for var in vars:      
            try:
                value = memory.get(var)
            except:
                print(f"Variable {var} not found")
                return ""
            words_str = words_str.replace("{" + var + "}", str(value))
        
        vars = re.findall(r"(([a-z]+)\[([a-z]+|[0-9]+)\])", words_str)
        
        for tup in vars:
            var = tup[1]
            inner = tup[2]
            
            if inner in memory.__dict__.keys():
                if isinstance(memory.__dict__[inner], Link):
                    inner_val = memory.__dict__[inner]
            else:
                inner_val = inner

            try:
                value = memory.__dict__[var][inner_val]
                
            except:
                print(f"Variable {var}[{inner}] not found")
                return ""

            words_str = words_str.replace(var + "[" + inner + "]", str(value))

        print(f"{words_str}")

    def visitQuit(self, ctx):
        print("Bye")
        sys.exit(1)

    def visitLinkAppEqn(self, ctx):
        link_name = ctx.name
        value = ctx.value

        if (link_name == None) or (value == None):
            return "Link definition error"
        
        link_name = link_name.text
        value = value.text

        if not memory.get(link_name):
            return "Invalid link modification expression statement"

        link_obj = memory.get(link_name)
        link_obj.append(value)


    def visitLinkModEqn(self, ctx):
        link_name = ctx.name
        elem = ctx.elem
        value = ctx.value

        if (link_name == None) or (elem == None) or (value == None):
            return "__INVALID_LINK_MOD_EQN__"

        link_name = link_name.text
        elem = elem.text
        value = value.text

        if not memory.get(link_name):
            return "__NO_SUCH_LINK__"

        link_obj = memory.get(link_name)

        link_obj[elem] = value
  

    def visitLinkModExprEqn(self, ctx):
        global memory
        link_name = ctx.name
        elem = ctx.elem
        value = ctx.value

        if (link_name == None) or (elem == None) or (value == None):
            return "__INVALID_LINK_MOD_EXPR_EQN__"

        link_name = link_name.text
        elem = elem.text

        value = self.visit(value)

        if not memory.get(link_name):
            return "__NO_SUCH_LINK__"

        link_obj = memory.get(link_name)
        link_obj[elem] = value
  
    def visitLinkDefExprEqn(self, ctx):
        link_name = ctx.name
        lname = ctx.lid
        rname = ctx.rid

        
        if (link_name == None) or (lname == None) or (rname == None):
            return "Invalid link expression"
        
        link_name = link_name.text
        lname = lname.text

        rname = self.visit(rname)

        memory.set(link_name, Link(lname, rname))

    def visitLinkDefEqn(self, ctx):
        link_name = ctx.name
        lname = ctx.lid
        rname = ctx.rid

        if (link_name == None) or (lname == None) or (rname == None):
            return "Invalid link definition equation"
        
        link_name = link_name.text
        lname = lname.text
        rname = rname.text
        
        lname_prev = memory.get(lname)
        if lname_prev:
            if lname_prev != "__VALUE_NOT_FOUND__":
                lname = lname_prev

        rname_prev = memory.get(rname)
        if rname_prev:
            if rname_prev != "__VALUE_NOT_FOUND__":
                rname = rname_prev

        memory.set(link_name, Link(lname, rname))


    def visitExprEqn(self, ctx):
        global memory
        var = ctx.var
        if var == None:
            return "Invalid expression equation"
        
        var = var.text

        value = ctx.value
        if isinstance(value, BasicLangParser.InfixExprContext):
            value = self.visit(value)
        elif isinstance(value, BasicLangParser.ParenExprContext):
            value = self.visit(value)

        memory.set(var, value)


    def visitIntEqn(self, ctx):
        global memory
        var = ctx.var
        value = ctx.value

        if (var == None) or (value == None):
            return "Invalid int equation"

        var = var.text
        value = value.text
        
        try:
            value = int(value)
        except:
            return f"{value} not an int"

        memory.set(var, value)


    def visitStrEqn(self, ctx):
        global memory
        var = ctx.var
        value = ctx.value
        if (var == None) or (value == None):
            return "__INVALID_STRING_EQUATION__"

        var = var.text
        value = value.text

        value_prev = memory.get(value)
        if value_prev:
            if isinstance(value_prev, int):
                value = value_prev
            else:
                if "__VALUE_NOT_FOUND__" not in value_prev:
                    value = value_prev

        memory.set(var, value)


    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)


    def visitIDExpr(self, ctx):
        value = ctx.getText()

        value = memory.get(value)
        return value
 

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())


    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        op = ctx.op

        for i in (l, r, op):
            if i == None:
                return "Invalid equation"
        
        op = op.text

        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()


def main(file):
    lexer = BasicLangLexer(FileStream(file))
    stream = CommonTokenStream(lexer)
    parser = BasicLangParser(stream)
    tree = parser.script()
    visitor = MyVisitor()
    output = visitor.visit(tree)
    print(output)

    # memory.print_dict()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", 
                        "--script_file", 
                        required=True, 
                        type=str, 
                        help="Script file")
    args = parser.parse_args()

    file = args.script_file
    main(file)
