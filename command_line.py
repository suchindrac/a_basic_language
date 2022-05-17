from antlr4 import *
from dist.BasicLangLexer import BasicLangLexer
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangParser import BasicLangParser
from link import Link
import sys
import re

eresult = None
class MyVisitor(BasicLangVisitor):
    def visitExecScript(self, ctx):
        for blk in list(ctx.getChildren()):
            self.visit(blk)
    

    def visitIfBlock(self, ctx):
        global eresult
        ifblk = ctx.ifblk
        act = ctx.act

        if ifblk != None:
            ifblk = ifblk.text
            for st in globals()[ifblk]:
                self.visit(st)
            
            if eresult:
                if act != None:
                    act = act.text
                    
                for st in globals()[act]:
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
            eresult = globals()[varid]
        

    def visitInsertFile(self, ctx):
    
        fname = ctx.fname
        if fname != None:
            fname = fname.text
        else:
            return "Filename not specified"

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


    def visitBlk(self, ctx):
        if ctx.bid != None:
            bid = ctx.bid.text
        else:
            return "Block definition error"

        statements = list(ctx.getChildren())

        if bid != None:
            globals()[bid] = statements
        
        if bid == "MAINBLOCK":
            mb_statements = globals()[bid]
            for st in mb_statements:
                self.visit(st)
            
        
    def visitExecBlock(self, ctx):
        blkid = ctx.blkid
        
        if blkid != None:
            blkid = ctx.blkid.text
        else:
            return "Block definition error"

        if ctx.times != None:
            times = ctx.times.text
            if times == "max":
                times = sys.maxsize
            elif times in globals().keys():
                times = globals()[times]
            elif times.isdigit():
                times = int(times)
            else:
                return "Invalid value"
        else:
            times = 1

        for i in range(times):
            for st in globals()[blkid]:
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

        vars = re.findall(r"{([a-z]+)}", words_str)

        for var in vars:
            try:
                value = globals()[var]
            except:
                print(f"Variable {var} not found")
                return ""

            words_str = words_str.replace("{" + var + "}", str(value))
        
        vars = re.findall(r"(([a-z]+)\[([a-z]+|[0-9]+)\])", words_str)
        
        for tup in vars:
            var = tup[1]
            inner = tup[2]
            
            if inner in globals().keys():
                if isinstance(globals()[inner], Link):
                    inner_val = globals()[inner]
            else:
                inner_val = inner

            try:
                value = globals()[var][inner_val]
                
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

        if link_name not in globals().keys():
            return f"{link_name} variable not found"

        if value in globals().keys():
            value = globals()[value]

        globals()[link_name].append(value)


    def visitLinkModEqn(self, ctx):
        link_name = ctx.name
        elem = ctx.elem
        value = ctx.value

        if (link_name == None) or (elem == None) or (value == None):
            return "Invalid link modification statement"

        link_name = link_name.text
        elem = elem.text
        value = value.text

        if link_name not in globals().keys():
            return f"{link_name} variable not found"

        if value in globals().keys():
            value = globals()[value]

        globals()[link_name][elem] = value


    def visitLinkModExprEqn(self, ctx):
        link_name = ctx.name
        elem = ctx.elem
        value = ctx.value

        if (link_name == None) or (elem == None) or (value == None):
            return "Invalid link modification expression statement"

        link_name = link_name.text
        elem = elem.text

        value = self.visit(value)

        if link_name not in globals().keys():
            return f"{link_name} variable not found"

        if value in globals().keys():
            value = globals()[value]

        globals()[link_name][elem] = value

  
    def visitLinkDefExprEqn(self, ctx):
        link_name = ctx.name
        lname = ctx.lid
        rname = ctx.rid

        if (link_name == None) or (lname == None) or (rname == None):
            return "Invalid link expression"
        
        link_name = link_name.text
        lname = lname.text

        rname = self.visit(rname)

        if lname in globals().keys():
            if isinstance(globals()[lname], Link):
                lname = globals()[lname]

        if rname in globals().keys():
            if isinstance(globals()[rname], Link):
                rname = globals()[rname]

        globals()[link_name] = Link(lname, rname)


    def visitLinkDefEqn(self, ctx):
        link_name = ctx.name
        lname = ctx.lid
        rname = ctx.rid

        if (link_name == None) or (lname == None) or (rname == None):
            return "Invalid link definition equation"
        
        link_name = link_name.text
        lname = lname.text
        rname = rname.text

        if lname in globals().keys():
            if isinstance(globals()[lname], Link):
                lname = globals()[lname]

        if rname in globals().keys():
            if isinstance(globals()[rname], Link):
                rname = globals()[rname]


        globals()[link_name] = Link(lname, rname)


    def visitExprEqn(self, ctx):
        var = ctx.var
        if var == None:
            return "Invalid expression equation"
        
        var = var.text

        value = ctx.value
        if isinstance(value, BasicLangParser.InfixExprContext):
            value = self.visit(value)
        elif isinstance(value, BasicLangParser.ParenExprContext):
            value = self.visit(value)

        globals()[var] = value


    def visitIntEqn(self, ctx):
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

        globals()[var] = value


    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)


    def visitIDExpr(self, ctx):
        value = ctx.getText()
        
        if value in globals().keys():
            return globals()[value]
        else:
            return f"Variable {value} not defined"


    def visitStrEqn(self, ctx):
        var = ctx.var
        if var == None:
            return "Invalid string equation"

        value = ctx.value
        if value == None:
            return "Invalid string equation"

        var = var.text
        value = value.text

        if value in globals().keys():
            value = globals()[value]

        globals()[var] = value


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
