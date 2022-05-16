# Generated from BasicLang.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BasicLangParser import BasicLangParser
else:
    from BasicLangParser import BasicLangParser

# This class defines a complete listener for a parse tree produced by BasicLangParser.
class BasicLangListener(ParseTreeListener):

    # Enter a parse tree produced by BasicLangParser#ExecScript.
    def enterExecScript(self, ctx:BasicLangParser.ExecScriptContext):
        pass

    # Exit a parse tree produced by BasicLangParser#ExecScript.
    def exitExecScript(self, ctx:BasicLangParser.ExecScriptContext):
        pass


    # Enter a parse tree produced by BasicLangParser#Blk.
    def enterBlk(self, ctx:BasicLangParser.BlkContext):
        pass

    # Exit a parse tree produced by BasicLangParser#Blk.
    def exitBlk(self, ctx:BasicLangParser.BlkContext):
        pass


    # Enter a parse tree produced by BasicLangParser#statement.
    def enterStatement(self, ctx:BasicLangParser.StatementContext):
        pass

    # Exit a parse tree produced by BasicLangParser#statement.
    def exitStatement(self, ctx:BasicLangParser.StatementContext):
        pass


    # Enter a parse tree produced by BasicLangParser#ExecBlock.
    def enterExecBlock(self, ctx:BasicLangParser.ExecBlockContext):
        pass

    # Exit a parse tree produced by BasicLangParser#ExecBlock.
    def exitExecBlock(self, ctx:BasicLangParser.ExecBlockContext):
        pass


    # Enter a parse tree produced by BasicLangParser#InsertFile.
    def enterInsertFile(self, ctx:BasicLangParser.InsertFileContext):
        pass

    # Exit a parse tree produced by BasicLangParser#InsertFile.
    def exitInsertFile(self, ctx:BasicLangParser.InsertFileContext):
        pass


    # Enter a parse tree produced by BasicLangParser#equation.
    def enterEquation(self, ctx:BasicLangParser.EquationContext):
        pass

    # Exit a parse tree produced by BasicLangParser#equation.
    def exitEquation(self, ctx:BasicLangParser.EquationContext):
        pass


    # Enter a parse tree produced by BasicLangParser#normal_equation.
    def enterNormal_equation(self, ctx:BasicLangParser.Normal_equationContext):
        pass

    # Exit a parse tree produced by BasicLangParser#normal_equation.
    def exitNormal_equation(self, ctx:BasicLangParser.Normal_equationContext):
        pass


    # Enter a parse tree produced by BasicLangParser#StrEqn.
    def enterStrEqn(self, ctx:BasicLangParser.StrEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#StrEqn.
    def exitStrEqn(self, ctx:BasicLangParser.StrEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#IntEqn.
    def enterIntEqn(self, ctx:BasicLangParser.IntEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#IntEqn.
    def exitIntEqn(self, ctx:BasicLangParser.IntEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#ExprEqn.
    def enterExprEqn(self, ctx:BasicLangParser.ExprEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#ExprEqn.
    def exitExprEqn(self, ctx:BasicLangParser.ExprEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#IDExpr.
    def enterIDExpr(self, ctx:BasicLangParser.IDExprContext):
        pass

    # Exit a parse tree produced by BasicLangParser#IDExpr.
    def exitIDExpr(self, ctx:BasicLangParser.IDExprContext):
        pass


    # Enter a parse tree produced by BasicLangParser#NumberExpr.
    def enterNumberExpr(self, ctx:BasicLangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by BasicLangParser#NumberExpr.
    def exitNumberExpr(self, ctx:BasicLangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by BasicLangParser#ParenExpr.
    def enterParenExpr(self, ctx:BasicLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by BasicLangParser#ParenExpr.
    def exitParenExpr(self, ctx:BasicLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by BasicLangParser#InfixExpr.
    def enterInfixExpr(self, ctx:BasicLangParser.InfixExprContext):
        pass

    # Exit a parse tree produced by BasicLangParser#InfixExpr.
    def exitInfixExpr(self, ctx:BasicLangParser.InfixExprContext):
        pass


    # Enter a parse tree produced by BasicLangParser#ShowStrExpr.
    def enterShowStrExpr(self, ctx:BasicLangParser.ShowStrExprContext):
        pass

    # Exit a parse tree produced by BasicLangParser#ShowStrExpr.
    def exitShowStrExpr(self, ctx:BasicLangParser.ShowStrExprContext):
        pass


    # Enter a parse tree produced by BasicLangParser#quit.
    def enterQuit(self, ctx:BasicLangParser.QuitContext):
        pass

    # Exit a parse tree produced by BasicLangParser#quit.
    def exitQuit(self, ctx:BasicLangParser.QuitContext):
        pass


    # Enter a parse tree produced by BasicLangParser#link.
    def enterLink(self, ctx:BasicLangParser.LinkContext):
        pass

    # Exit a parse tree produced by BasicLangParser#link.
    def exitLink(self, ctx:BasicLangParser.LinkContext):
        pass


    # Enter a parse tree produced by BasicLangParser#link_def.
    def enterLink_def(self, ctx:BasicLangParser.Link_defContext):
        pass

    # Exit a parse tree produced by BasicLangParser#link_def.
    def exitLink_def(self, ctx:BasicLangParser.Link_defContext):
        pass


    # Enter a parse tree produced by BasicLangParser#link_mod.
    def enterLink_mod(self, ctx:BasicLangParser.Link_modContext):
        pass

    # Exit a parse tree produced by BasicLangParser#link_mod.
    def exitLink_mod(self, ctx:BasicLangParser.Link_modContext):
        pass


    # Enter a parse tree produced by BasicLangParser#LinkDefEqn.
    def enterLinkDefEqn(self, ctx:BasicLangParser.LinkDefEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#LinkDefEqn.
    def exitLinkDefEqn(self, ctx:BasicLangParser.LinkDefEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#LinkModEqn.
    def enterLinkModEqn(self, ctx:BasicLangParser.LinkModEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#LinkModEqn.
    def exitLinkModEqn(self, ctx:BasicLangParser.LinkModEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#LinkDefExprEqn.
    def enterLinkDefExprEqn(self, ctx:BasicLangParser.LinkDefExprEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#LinkDefExprEqn.
    def exitLinkDefExprEqn(self, ctx:BasicLangParser.LinkDefExprEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#LinkModExprEqn.
    def enterLinkModExprEqn(self, ctx:BasicLangParser.LinkModExprEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#LinkModExprEqn.
    def exitLinkModExprEqn(self, ctx:BasicLangParser.LinkModExprEqnContext):
        pass


    # Enter a parse tree produced by BasicLangParser#LinkAppEqn.
    def enterLinkAppEqn(self, ctx:BasicLangParser.LinkAppEqnContext):
        pass

    # Exit a parse tree produced by BasicLangParser#LinkAppEqn.
    def exitLinkAppEqn(self, ctx:BasicLangParser.LinkAppEqnContext):
        pass



del BasicLangParser