from antlr4 import *
from dist.BasicLangLexer import BasicLangLexer
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangParser import BasicLangParser
from link import Link
import sys
import re
from memory import Memory

orig_memory = Memory()
memory = orig_memory

class MyVisitor(BasicLangVisitor):
    def switch_context(self, to_what=None):
        global memory
        global orig_memory

        if to_what != None:
            memory = memory.get_obj(to_what)
        else:
            memory = orig_memory

    def visitExecScript(self, ctx):
        for blk in list(ctx.getChildren()):
            self.visit(blk)
    
    def visitIfCondition(self, ctx):
        global memory

        leftcond = ctx.leftcond
        iftrueid = ctx.iftrueid
        iftrueeqn = ctx.iftrueeqn
        iffalseid = ctx.iffalseid
        iffalseeqn = ctx.iffalseeqn
        iftrueval = ctx.iftrueval
        iffalseval = ctx.iffalseval

        leftcond = self.visit(leftcond)

        if leftcond:
            if iftrueval:
                if iftrueval.text == 'none':
                    print("No true expression/ID")
            if iftrueid != None:
                iftrueid = iftrueid.text
                for st in memory.get(iftrueid):
                    result = self.visit(st)
                    if result != None:
                        print(result)
            if iftrueeqn != None:
                self.visit(iftrueeqn)
        else:
            if iffalseval:
                if iffalseval.text == 'none':
                    print("No false expression")
            if iffalseid != None:
                iffalseid = iffalseid.text
                for st in memory.get(iffalseid):
                    result = self.visit(st)
                    if result != None:
                        print(result)
            if iffalseeqn != None:
                self.visit(iffalseeqn)

    def visitIfBlock(self, ctx):
        global memory
        ifblk = ctx.ifblk
        acttrueid = ctx.acttrueid
        acttrueeqn = ctx.acttrueeqn
        actfalseid = ctx.actfalseid
        actfalseeqn = ctx.actfalseeqn

        if ifblk != None:
            ifblk = ifblk.text
            for st in memory.get(ifblk):
                self.visit(st)
            
            if memory.eresult:
                if acttrueid != None:
                    acttrueid = acttrueid.text
                    
                    for st in memory.get(acttrueid):
                        result = self.visit(st)
                        if result != None:
                            print(result)
                if acttrueeqn != None:
                    self.visit(acttrueeqn)
            else:
                if actfalseid != None:
                    actfalseid = actfalseid.text
                    
                    for st in memory.get(actfalseid):
                        result = self.visit(st)
                        if result != None:
                            print(result)
                if actfalseeqn != None:
                    self.visit(actfalseeqn)

    def visitCondParenExpr(self, ctx):
        return self.visit(ctx.cond())


    def visitCondExpr(self, ctx):
        if (ctx.op == None) or (ctx.left == None) or (ctx.right == None):
            return "__INVALID_CONDITION__"

        left = ctx.left.text
        right = ctx.right.text
        op = ctx.op.text

        if isinstance(left, int):
            left = int(left)
        else:
            left = memory.get(left)

        if isinstance(right, int):
            right = int(right)
        else:
            right = memory.get(right)

        ops = ['le', 'ge', 'lt', 'gt', 'eq']

        if not op in ops:
            return "__INVALID_CONDITION__"
        
        op_dict =  {
        'le': lambda: left <= right,
        'ge': lambda: left >= right,
        'lt': lambda: left < right,
        'gt': lambda: left > right,
        'eq': lambda: left == right
        }
        
        return op_dict.get(op, lambda: None)()

    def visitGetResult(self, ctx):
        global memory
        if ctx.var == None:
            return "__NOT_FOUND__"

        var = ctx.var.text
        value = "eresult"

        memory.set(var, value)


    def visitSetResult(self, ctx):
        global memory
        varint = ctx.varint
        varid = ctx.varid
        
        if varint != None:
            varint = int(varint.text)
            memory.eresult = varint
        
        if varid != None:
            varid = varid.text
            memory.eresult = memory.get(varid)


    def visitInsertFile(self, ctx):
        global memory
        fname = ctx.fname
        if fname != None:
            fname = fname.text
        else:
            return "__FILENAME_NOT_SPECIFIED__"

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
            print("__ERROR_PARSING_IMPORTED_FILE__")

        memory = prev_memory


    def visitBlk(self, ctx):
        global memory
        if ctx.bid != None:
            bid = ctx.bid.text
        else:
            return "__BLOCK_DEFINITION_ERROR__"

        statements = list(ctx.getChildren())

        if bid != None:
            memory.set(bid, statements)
        

        if ("MAINBLOCK" in bid) or ("mainblock" in bid):
            if "." in bid:
                self.switch_context(bid)

            for st in memory.get(bid):
                self.visit(st)

            self.switch_context()


    def visitExecBlock(self, ctx):
        global memory
        blkid = ctx.blkid
        
        if blkid != None:
            blkid = ctx.blkid.text
        else:
            return "__INVALID_BLOCK_DEFINITION__"

        if ctx.times != None:
            times = ctx.times.text
            
            if times == "max":
                times = sys.maxsize
            elif (not times.isdigit()) and (memory.get(times) != False):
                times = memory.get(times)
            elif times.isdigit():
                times = int(times)
            else:
                return "__INVALID_TIMES_VALUE__"
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
                value = "__NOT_FOUND__"

            words_str = words_str.replace("{" + var + "}", str(value))
        
        vars = re.findall(r"(([a-z]+)\[([a-z]+|[0-9]+)\])", words_str)
        
        for tup in vars:
            var = tup[1]
            inner = tup[2]
            
            inner_val = memory.get(inner)
            if not inner_val:
                inner_val = inner

            if not memory.get(var):
                value = "__NOT_FOUND__"

            try:
                obj = memory.get(var)
                value = obj[inner_val]                
            except:
                value = "__NOT_FOUND__"

            words_str = words_str.replace(var + "[" + inner + "]", str(value))

        print(f"{words_str}")


    def visitQuit(self, ctx):
        print("Bye")
        sys.exit(1)

    def visitLinkAppEqn(self, ctx):
        link_name = ctx.name
        value = ctx.value

        if (link_name == None) or (value == None):
            return "__INVALID_LINK_APPEND_EQN__"
        
        link_name = link_name.text
        value = value.text

        if not memory.get(link_name):
            return "__NO_SUCH_LINK__"

        link_obj = memory.get(link_name)
        link_obj.append(value)


    def visitLinkModEqn(self, ctx):
        global memory
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

        if elem.isdigit():
            elem = int(elem)

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

        if elem.isdigit():
            elem = int(elem)
            
        link_obj = memory.get(link_name)
        link_obj[elem] = value
  
    def visitLinkDefExprEqn(self, ctx):
        link_name = ctx.name
        lname = ctx.lid
        rname = ctx.rid

        
        if (link_name == None) or (lname == None) or (rname == None):
            return "__INVALID_LINK_DEF_EXPN__"
        
        link_name = link_name.text
        lname = lname.text

        rname = self.visit(rname)

        memory.set(link_name, Link(lname, rname))

    def visitLinkDefEqn(self, ctx):
        link_name = ctx.name
        lname = ctx.lid
        rname = ctx.rid

        if (link_name == None) or (lname == None) or (rname == None):
            return "__INVALID_LINK_DEF_EQN__"
        
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
            return "__INVALID_EXPN_EQN__"
        
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
            return "__INVALID_INT_EQN__"

        var = var.text
        value = value.text
        
        try:
            value = int(value)
        except:
            return f"__VALUE_NOT_AN_INT__"

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
                if "NOT_FOUND" not in value_prev:
                    value = value_prev

        memory.set(var, value)

    def visitNumberCondExpr(self, ctx):
        value = ctx.getText()
        return int(value)


    def visitIDCondExpr(self, ctx):
        value = ctx.getText()

        value = memory.get(value)

        return value

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
        if (ctx.op == None) or (ctx.left == None) or (ctx.right == None):
            return "__INVALID_EQUATION__"

        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        l = int(l)
        r = int(r)

        op = ctx.op

        for i in (l, r, op):
            if i == None:
                return "__INVALID_EQUATION__"
        
        op = op.text

        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()


def main():
    while True:
        lexer = BasicLangLexer(InputStream(input(">>> ")))
        stream = CommonTokenStream(lexer)
        stream.fill()
        # print([token.text for token in stream.tokens])
        parser = BasicLangParser(stream)
        tree = parser.statement()
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)

if __name__ == '__main__':
    main()
