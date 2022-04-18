from antlr4 import *
from dist.BasicLangLexer import BasicLangLexer
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangVisitor import BasicLangVisitor
from dist.BasicLangParser import BasicLangParser
from link import Link
import sys
import argparse

class MyVisitor(BasicLangVisitor):
    def visitShowIDExpr(self, ctx):
        if ctx.INT() != None:
            return ctx.INT()
        if ctx.ID() != None:
            id = ctx.ID().getText()
    
            try:
                return globals()[id]
            except:
                return id

    def visitShowLinkExpr(self, ctx):
        link_name = ctx.name.text
        what = ctx.what.text

        if what in globals().keys():
            if isinstance(globals()[what], Link):
                what = globals()[what]
 
        return globals()[link_name][what]

    def visitQuit(self, ctx):
        print("Bye")
        sys.exit(1)

    def visitLinkAccEqn(self, ctx):
        link_name = ctx.name.text
        what = ctx.what.text

        if what in globals().keys():
            if isinstance(globals()[what], Link):
                what = globals()[what]

        return globals()[link_name][what]

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
        if isinstance(value, BasicLangParser.ParenExprContext):
            value = self.visit(value)

        globals()[var] = value

        return f"{var} set to {value}"

    def visitEqn(self, ctx):
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

def main(content):
        lines = content.split("\n")
        for line in lines:
            lexer = BasicLangLexer(InputStream(line))
            stream = CommonTokenStream(lexer)
            parser = BasicLangParser(stream)
            tree = parser.statement()
            visitor = MyVisitor()
            output = visitor.visit(tree)
            print(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", 
                        "--script_file", 
                        required=True, 
                        type=str, 
                        help="Script file")
    args = parser.parse_args()

    file = args.script_file
  
    content = ""
    try:
        fd = open(file, 'r')
        content = fd.read()
        fd.close()
    except:
        print("Unable to read script file")

    main(content)
