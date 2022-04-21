# Generated from BasicLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicLangParser import BasicLangParser
else:
    from BasicLangParser import BasicLangParser

# This class defines a complete generic visitor for a parse tree produced by BasicLangParser.

class BasicLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BasicLangParser#statement.
    def visitStatement(self, ctx:BasicLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#equation.
    def visitEquation(self, ctx:BasicLangParser.EquationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#normal_equation.
    def visitNormal_equation(self, ctx:BasicLangParser.Normal_equationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#StrEqn.
    def visitStrEqn(self, ctx:BasicLangParser.StrEqnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#IntEqn.
    def visitIntEqn(self, ctx:BasicLangParser.IntEqnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#ExprEqn.
    def visitExprEqn(self, ctx:BasicLangParser.ExprEqnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#IDExpr.
    def visitIDExpr(self, ctx:BasicLangParser.IDExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#NumberExpr.
    def visitNumberExpr(self, ctx:BasicLangParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#ParenExpr.
    def visitParenExpr(self, ctx:BasicLangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#InfixExpr.
    def visitInfixExpr(self, ctx:BasicLangParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#ShowStrExpr.
    def visitShowStrExpr(self, ctx:BasicLangParser.ShowStrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#quit.
    def visitQuit(self, ctx:BasicLangParser.QuitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#link.
    def visitLink(self, ctx:BasicLangParser.LinkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLangParser#LinkDefEqn.
    def visitLinkDefEqn(self, ctx:BasicLangParser.LinkDefEqnContext):
        return self.visitChildren(ctx)



del BasicLangParser