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
     
        return ""
    
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
        
        return ""

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
        
        return ""

    def visitInsertFile(self, ctx):
    
        fname = ctx.fname.text
        fname = f"{fname}.bl"

        fs = FileStream(fname)
        lexer = BasicLangLexer(fs)
        stream = CommonTokenStream(lexer)
        parser = BasicLangParser(stream)
        tree = parser.script()
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)

    def visitBlk(self, ctx):
        if ctx.bid != None:
            bid = ctx.bid.text
        else:
            return ""

        statements = list(ctx.getChildren())

        if bid != None:
            globals()[bid] = statements
        
        if bid == "MAINBLOCK":
            mb_statements = globals()[bid]
            for st in mb_statements:
                self.visit(st)
            
        return f"Created block {bid}"
        
    def visitExecBlock(self, ctx):
        blkid = ctx.blkid.text

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

        return ""

    def visitShowStrExpr(self, ctx):
        tokens = ctx.getChildren()
        words = [token.getText() for token in tokens]
        
        words.remove("print")

        words_str = " ".join(words)

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

            words_str = words_str.replace(var + "[" + inner + "]", str(value))

        print(f"{words_str}")

    def visitQuit(self, ctx):
        print("Bye")
        sys.exit(1)

    def visitLinkAppEqn(self, ctx):
        link_name = ctx.name.text
        value = ctx.value.text

        if link_name not in globals().keys():
            return f"{link_name} variable not found"

        if value in globals().keys():
            value = globals()[value]

        globals()[link_name].append(value)

        return ""

    def visitLinkModEqn(self, ctx):
        link_name = ctx.name.text
        elem = ctx.elem.text
        value = ctx.value.text

        if link_name not in globals().keys():
            return f"{link_name} variable not found"

        if value in globals().keys():
            value = globals()[value]

        globals()[link_name][elem] = value

        return ""

    def visitLinkModExprEqn(self, ctx):
        link_name = ctx.name.text
        elem = ctx.elem.text
        value = ctx.value
        
        value = self.visit(value)

        if link_name not in globals().keys():
            return f"{link_name} variable not found"

        if value in globals().keys():
            value = globals()[value]

        globals()[link_name][elem] = value

        return "Link modified"
  
    def visitLinkDefExprEqn(self, ctx):
        link_name = ctx.name.text
        lname = ctx.lid.text
        rname = ctx.rid
        
        rname = self.visit(rname)

        if lname in globals().keys():
            if isinstance(globals()[lname], Link):
                lname = globals()[lname]

        if rname in globals().keys():
            if isinstance(globals()[rname], Link):
                rname = globals()[rname]

        globals()[link_name] = Link(lname, rname)

        return "Link created"

    def visitLinkDefEqn(self, ctx):
        link_name = ctx.name.text
        lname = ctx.lid.text
        rname = ctx.rid.text

        if lname in globals().keys():
            if isinstance(globals()[lname], Link):
                lname = globals()[lname]

        if rname in globals().keys():
            if isinstance(globals()[rname], Link):
                rname = globals()[rname]


        globals()[link_name] = Link(lname, rname)

        return "Link created"

    def visitExprEqn(self, ctx):
        var = ctx.var.text
        value = ctx.value
        if isinstance(value, BasicLangParser.InfixExprContext):
            value = self.visit(value)
        elif isinstance(value, BasicLangParser.ParenExprContext):
            value = self.visit(value)

        globals()[var] = value

        return f"{var} set to {value}"

    def visitIntEqn(self, ctx):
        var = ctx.var.text
        value = ctx.value
        value = value.text
        
        try:
            value = int(value)
        except:
            pass

        globals()[var] = value
        return f"Set {var} to {value}"

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
        var = ctx.var.text
        value = ctx.value.text

        if value in globals().keys():
            value = globals()[value]

        globals()[var] = value
        return f"Set {var} to {value}"

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text

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
