from antlr4 import *
from dist.BasicLangLexer import BasicLangLexer
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangParser import BasicLangParser
from link import Link
import sys
import argparse
import re

class MyVisitor(BasicLangVisitor):
    def visitShowStrExpr(self, ctx):
        tokens = ctx.getChildren()
        words = [token.getText() for token in tokens]
        words.remove("print")
        words.remove("<EOF>")

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

        return words_str

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

        return ""
  
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

        return ""

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

        return ""

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
