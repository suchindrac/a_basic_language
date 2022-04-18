# Generated from BasicLang.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,3,0,26,8,0,1,1,1,1,
        3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,
        4,45,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,62,8,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,70,8,7,10,7,12,7,73,9,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,82,8,8,1,9,1,9,1,9,0,1,14,10,0,
        2,4,6,8,10,12,14,16,18,0,3,1,0,14,15,1,0,6,7,1,0,8,9,86,0,25,1,0,
        0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,37,1,0,0,0,8,44,1,0,0,0,10,46,1,
        0,0,0,12,50,1,0,0,0,14,61,1,0,0,0,16,81,1,0,0,0,18,83,1,0,0,0,20,
        26,3,8,4,0,21,26,3,14,7,0,22,26,3,16,8,0,23,26,3,18,9,0,24,26,3,
        2,1,0,25,20,1,0,0,0,25,21,1,0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,25,
        24,1,0,0,0,26,1,1,0,0,0,27,30,3,4,2,0,28,30,3,6,3,0,29,27,1,0,0,
        0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,5,14,0,0,32,33,5,1,0,0,33,34,
        7,0,0,0,34,35,5,2,0,0,35,36,7,0,0,0,36,5,1,0,0,0,37,38,5,14,0,0,
        38,39,5,3,0,0,39,40,7,0,0,0,40,41,5,4,0,0,41,7,1,0,0,0,42,45,3,10,
        5,0,43,45,3,12,6,0,44,42,1,0,0,0,44,43,1,0,0,0,45,9,1,0,0,0,46,47,
        5,14,0,0,47,48,5,5,0,0,48,49,5,15,0,0,49,11,1,0,0,0,50,51,5,14,0,
        0,51,52,5,5,0,0,52,53,3,14,7,0,53,13,1,0,0,0,54,55,6,7,-1,0,55,62,
        5,15,0,0,56,57,5,10,0,0,57,58,3,14,7,0,58,59,5,11,0,0,59,62,1,0,
        0,0,60,62,5,14,0,0,61,54,1,0,0,0,61,56,1,0,0,0,61,60,1,0,0,0,62,
        71,1,0,0,0,63,64,10,5,0,0,64,65,7,1,0,0,65,70,3,14,7,6,66,67,10,
        4,0,0,67,68,7,2,0,0,68,70,3,14,7,5,69,63,1,0,0,0,69,66,1,0,0,0,70,
        73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,15,1,0,0,0,73,71,1,0,0,
        0,74,75,5,12,0,0,75,82,7,0,0,0,76,77,5,12,0,0,77,78,5,14,0,0,78,
        79,5,3,0,0,79,80,7,0,0,0,80,82,5,4,0,0,81,74,1,0,0,0,81,76,1,0,0,
        0,82,17,1,0,0,0,83,84,5,13,0,0,84,19,1,0,0,0,7,25,29,44,61,69,71,
        81
    ]

class BasicLangParser ( Parser ):

    grammarFileName = "BasicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'<->'", "'['", "']'", "'='", "'*'", 
                     "'/'", "'+'", "'-'", "'('", "')'", "'print'", "'exit'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_statement = 0
    RULE_link = 1
    RULE_link_def = 2
    RULE_link_acc = 3
    RULE_equation = 4
    RULE_normal_equation = 5
    RULE_exp_equation = 6
    RULE_expr = 7
    RULE_show = 8
    RULE_quit = 9

    ruleNames =  [ "statement", "link", "link_def", "link_acc", "equation", 
                   "normal_equation", "exp_equation", "expr", "show", "quit" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    ID=14
    INT=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equation(self):
            return self.getTypedRuleContext(BasicLangParser.EquationContext,0)


        def expr(self):
            return self.getTypedRuleContext(BasicLangParser.ExprContext,0)


        def show(self):
            return self.getTypedRuleContext(BasicLangParser.ShowContext,0)


        def quit(self):
            return self.getTypedRuleContext(BasicLangParser.QuitContext,0)


        def link(self):
            return self.getTypedRuleContext(BasicLangParser.LinkContext,0)


        def getRuleIndex(self):
            return BasicLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasicLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statement)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.show()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.quit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 24
                self.link()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LinkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link_def(self):
            return self.getTypedRuleContext(BasicLangParser.Link_defContext,0)


        def link_acc(self):
            return self.getTypedRuleContext(BasicLangParser.Link_accContext,0)


        def getRuleIndex(self):
            return BasicLangParser.RULE_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink" ):
                listener.enterLink(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink" ):
                listener.exitLink(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink" ):
                return visitor.visitLink(self)
            else:
                return visitor.visitChildren(self)




    def link(self):

        localctx = BasicLangParser.LinkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_link)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.link_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.link_acc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_def

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkDefEqnContext(Link_defContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_defContext
            super().__init__(parser)
            self.name = None # Token
            self.lid = None # Token
            self.rid = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.INT)
            else:
                return self.getToken(BasicLangParser.INT, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkDefEqn" ):
                listener.enterLinkDefEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkDefEqn" ):
                listener.exitLinkDefEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkDefEqn" ):
                return visitor.visitLinkDefEqn(self)
            else:
                return visitor.visitChildren(self)



    def link_def(self):

        localctx = BasicLangParser.Link_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_link_def)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 32
            self.match(BasicLangParser.T__0)
            self.state = 33
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 34
            self.match(BasicLangParser.T__1)
            self.state = 35
            localctx.rid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.rid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_accContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_acc

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkAccEqnContext(Link_accContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_accContext
            super().__init__(parser)
            self.name = None # Token
            self.what = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkAccEqn" ):
                listener.enterLinkAccEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkAccEqn" ):
                listener.exitLinkAccEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkAccEqn" ):
                return visitor.visitLinkAccEqn(self)
            else:
                return visitor.visitChildren(self)



    def link_acc(self):

        localctx = BasicLangParser.Link_accContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_link_acc)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkAccEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 38
            self.match(BasicLangParser.T__2)
            self.state = 39
            localctx.what = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.what = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 40
            self.match(BasicLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_equation(self):
            return self.getTypedRuleContext(BasicLangParser.Normal_equationContext,0)


        def exp_equation(self):
            return self.getTypedRuleContext(BasicLangParser.Exp_equationContext,0)


        def getRuleIndex(self):
            return BasicLangParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = BasicLangParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equation)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.normal_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.exp_equation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_equationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_normal_equation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqnContext(Normal_equationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Normal_equationContext
            super().__init__(parser)
            self.var = None # Token
            self.value = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqn" ):
                listener.enterEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqn" ):
                listener.exitEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqn" ):
                return visitor.visitEqn(self)
            else:
                return visitor.visitChildren(self)



    def normal_equation(self):

        localctx = BasicLangParser.Normal_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_normal_equation)
        try:
            localctx = BasicLangParser.EqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 47
            self.match(BasicLangParser.T__4)
            self.state = 48
            localctx.value = self.match(BasicLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_equationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_exp_equation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprEqnContext(Exp_equationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Exp_equationContext
            super().__init__(parser)
            self.var = None # Token
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(BasicLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprEqn" ):
                listener.enterExprEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprEqn" ):
                listener.exitExprEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprEqn" ):
                return visitor.visitExprEqn(self)
            else:
                return visitor.visitChildren(self)



    def exp_equation(self):

        localctx = BasicLangParser.Exp_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exp_equation)
        try:
            localctx = BasicLangParser.ExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 51
            self.match(BasicLangParser.T__4)
            self.state = 52
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IDExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIDExpr" ):
                listener.enterIDExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIDExpr" ):
                listener.exitIDExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIDExpr" ):
                return visitor.visitIDExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BasicLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(BasicLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasicLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicLangParser.INT]:
                localctx = BasicLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 55
                localctx.atom = self.match(BasicLangParser.INT)
                pass
            elif token in [BasicLangParser.T__9]:
                localctx = BasicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(BasicLangParser.T__9)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(BasicLangParser.T__10)
                pass
            elif token in [BasicLangParser.ID]:
                localctx = BasicLangParser.IDExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                localctx.atom = self.match(BasicLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__5 or _la==BasicLangParser.T__6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__7 or _la==BasicLangParser.T__8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ShowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_show

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ShowLinkExprContext(ShowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ShowContext
            super().__init__(parser)
            self.name = None # Token
            self.what = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowLinkExpr" ):
                listener.enterShowLinkExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowLinkExpr" ):
                listener.exitShowLinkExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowLinkExpr" ):
                return visitor.visitShowLinkExpr(self)
            else:
                return visitor.visitChildren(self)


    class ShowIDExprContext(ShowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ShowContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowIDExpr" ):
                listener.enterShowIDExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowIDExpr" ):
                listener.exitShowIDExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowIDExpr" ):
                return visitor.visitShowIDExpr(self)
            else:
                return visitor.visitChildren(self)



    def show(self):

        localctx = BasicLangParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_show)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = BasicLangParser.ShowIDExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(BasicLangParser.T__11)
                self.state = 75
                _la = self._input.LA(1)
                if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = BasicLangParser.ShowLinkExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(BasicLangParser.T__11)
                self.state = 77
                localctx.name = self.match(BasicLangParser.ID)
                self.state = 78
                self.match(BasicLangParser.T__2)
                self.state = 79
                localctx.what = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                    localctx.what = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 80
                self.match(BasicLangParser.T__3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_quit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuit" ):
                listener.enterQuit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuit" ):
                listener.exitQuit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuit" ):
                return visitor.visitQuit(self)
            else:
                return visitor.visitChildren(self)




    def quit(self):

        localctx = BasicLangParser.QuitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(BasicLangParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




