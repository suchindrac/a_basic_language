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
        4,1,19,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,3,0,28,8,
        0,1,1,1,1,3,1,32,8,1,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,57,8,6,1,
        6,1,6,1,6,1,6,1,6,1,6,5,6,65,8,6,10,6,12,6,68,9,6,1,7,1,7,5,7,72,
        8,7,10,7,12,7,75,9,7,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,0,1,12,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,0,2,3,
        1,0,4,5,0,1,2,0,12,12,15,15,88,0,27,1,0,0,0,2,31,1,0,0,0,4,35,1,
        0,0,0,6,37,1,0,0,0,8,41,1,0,0,0,10,45,1,0,0,0,12,56,1,0,0,0,14,69,
        1,0,0,0,16,78,1,0,0,0,18,80,1,0,0,0,20,82,1,0,0,0,22,28,3,2,1,0,
        23,28,3,12,6,0,24,28,3,14,7,0,25,28,3,16,8,0,26,28,3,18,9,0,27,22,
        1,0,0,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,0,0,
        28,1,1,0,0,0,29,32,3,4,2,0,30,32,3,10,5,0,31,29,1,0,0,0,31,30,1,
        0,0,0,32,3,1,0,0,0,33,36,3,6,3,0,34,36,3,8,4,0,35,33,1,0,0,0,35,
        34,1,0,0,0,36,5,1,0,0,0,37,38,5,12,0,0,38,39,5,1,0,0,39,40,5,12,
        0,0,40,7,1,0,0,0,41,42,5,12,0,0,42,43,5,1,0,0,43,44,5,15,0,0,44,
        9,1,0,0,0,45,46,5,12,0,0,46,47,5,1,0,0,47,48,3,12,6,0,48,11,1,0,
        0,0,49,50,6,6,-1,0,50,51,5,6,0,0,51,52,3,12,6,0,52,53,5,7,0,0,53,
        57,1,0,0,0,54,57,5,15,0,0,55,57,5,12,0,0,56,49,1,0,0,0,56,54,1,0,
        0,0,56,55,1,0,0,0,57,66,1,0,0,0,58,59,10,5,0,0,59,60,7,0,0,0,60,
        65,3,12,6,6,61,62,10,4,0,0,62,63,7,1,0,0,63,65,3,12,6,5,64,58,1,
        0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,
        13,1,0,0,0,68,66,1,0,0,0,69,73,5,8,0,0,70,72,8,2,0,0,71,70,1,0,0,
        0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,
        1,0,0,0,76,77,5,0,0,1,77,15,1,0,0,0,78,79,5,9,0,0,79,17,1,0,0,0,
        80,81,3,20,10,0,81,19,1,0,0,0,82,83,5,12,0,0,83,84,5,10,0,0,84,85,
        7,3,0,0,85,86,5,11,0,0,86,87,7,3,0,0,87,21,1,0,0,0,7,27,31,35,56,
        64,66,73
    ]

class BasicLangParser ( Parser ):

    grammarFileName = "BasicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'print'", "'exit'", "':'", "'<->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "CAPID", "ANY", "INT", "NL", "WS", "VALUE_OF_VAR", 
                      "VALUE_OF_LINK" ]

    RULE_statement = 0
    RULE_equation = 1
    RULE_normal_equation = 2
    RULE_str_equation = 3
    RULE_num_equation = 4
    RULE_exp_equation = 5
    RULE_expr = 6
    RULE_show = 7
    RULE_quit = 8
    RULE_link = 9
    RULE_link_def = 10

    ruleNames =  [ "statement", "equation", "normal_equation", "str_equation", 
                   "num_equation", "exp_equation", "expr", "show", "quit", 
                   "link", "link_def" ]

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
    ID=12
    CAPID=13
    ANY=14
    INT=15
    NL=16
    WS=17
    VALUE_OF_VAR=18
    VALUE_OF_LINK=19

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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.show()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.quit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.link()
                pass


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
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.normal_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
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

        def str_equation(self):
            return self.getTypedRuleContext(BasicLangParser.Str_equationContext,0)


        def num_equation(self):
            return self.getTypedRuleContext(BasicLangParser.Num_equationContext,0)


        def getRuleIndex(self):
            return BasicLangParser.RULE_normal_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormal_equation" ):
                listener.enterNormal_equation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormal_equation" ):
                listener.exitNormal_equation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_equation" ):
                return visitor.visitNormal_equation(self)
            else:
                return visitor.visitChildren(self)




    def normal_equation(self):

        localctx = BasicLangParser.Normal_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_normal_equation)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.str_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.num_equation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_equationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_str_equation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrEqnContext(Str_equationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Str_equationContext
            super().__init__(parser)
            self.var = None # Token
            self.value = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrEqn" ):
                listener.enterStrEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrEqn" ):
                listener.exitStrEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrEqn" ):
                return visitor.visitStrEqn(self)
            else:
                return visitor.visitChildren(self)



    def str_equation(self):

        localctx = BasicLangParser.Str_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_str_equation)
        try:
            localctx = BasicLangParser.StrEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 38
            self.match(BasicLangParser.T__0)
            self.state = 39
            localctx.value = self.match(BasicLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_equationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_num_equation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntEqnContext(Num_equationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Num_equationContext
            super().__init__(parser)
            self.var = None # Token
            self.value = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntEqn" ):
                listener.enterIntEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntEqn" ):
                listener.exitIntEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntEqn" ):
                return visitor.visitIntEqn(self)
            else:
                return visitor.visitChildren(self)



    def num_equation(self):

        localctx = BasicLangParser.Num_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_num_equation)
        try:
            localctx = BasicLangParser.IntEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 42
            self.match(BasicLangParser.T__0)
            self.state = 43
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
        self.enterRule(localctx, 10, self.RULE_exp_equation)
        try:
            localctx = BasicLangParser.ExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 46
            self.match(BasicLangParser.T__0)
            self.state = 47
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicLangParser.T__5]:
                localctx = BasicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 50
                self.match(BasicLangParser.T__5)
                self.state = 51
                self.expr(0)
                self.state = 52
                self.match(BasicLangParser.T__6)
                pass
            elif token in [BasicLangParser.INT]:
                localctx = BasicLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                localctx.atom = self.match(BasicLangParser.INT)
                pass
            elif token in [BasicLangParser.ID]:
                localctx = BasicLangParser.IDExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                localctx.atom = self.match(BasicLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__1 or _la==BasicLangParser.T__2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__3 or _la==BasicLangParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 68
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



    class ShowStrExprContext(ShowContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ShowContext
            super().__init__(parser)
            self.text = None # Token
            self.copyFrom(ctx)

        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.EOF)
            else:
                return self.getToken(BasicLangParser.EOF, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowStrExpr" ):
                listener.enterShowStrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowStrExpr" ):
                listener.exitShowStrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStrExpr" ):
                return visitor.visitShowStrExpr(self)
            else:
                return visitor.visitChildren(self)



    def show(self):

        localctx = BasicLangParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_show)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ShowStrExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(BasicLangParser.T__7)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__0) | (1 << BasicLangParser.T__1) | (1 << BasicLangParser.T__2) | (1 << BasicLangParser.T__3) | (1 << BasicLangParser.T__4) | (1 << BasicLangParser.T__5) | (1 << BasicLangParser.T__6) | (1 << BasicLangParser.T__7) | (1 << BasicLangParser.T__8) | (1 << BasicLangParser.T__9) | (1 << BasicLangParser.T__10) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.CAPID) | (1 << BasicLangParser.ANY) | (1 << BasicLangParser.INT) | (1 << BasicLangParser.NL) | (1 << BasicLangParser.WS) | (1 << BasicLangParser.VALUE_OF_VAR) | (1 << BasicLangParser.VALUE_OF_LINK))) != 0):
                self.state = 70
                localctx.text = self._input.LT(1)
                _la = self._input.LA(1)
                if _la <= 0 or _la==BasicLangParser.EOF:
                    localctx.text = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(BasicLangParser.EOF)
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
        self.enterRule(localctx, 16, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(BasicLangParser.T__8)
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
        self.enterRule(localctx, 18, self.RULE_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.link_def()
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
        self.enterRule(localctx, 20, self.RULE_link_def)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 83
            self.match(BasicLangParser.T__9)
            self.state = 84
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 85
            self.match(BasicLangParser.T__10)
            self.state = 86
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
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
         




