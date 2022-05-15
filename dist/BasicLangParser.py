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
        4,1,25,153,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,3,0,38,8,0,1,0,3,0,41,
        8,0,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,3,0,50,8,0,1,1,1,1,1,1,1,
        1,1,1,3,1,57,8,1,1,2,1,2,3,2,61,8,2,1,3,1,3,3,3,65,8,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,3,7,86,8,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,94,8,7,10,7,12,7,97,9,7,
        1,8,1,8,5,8,101,8,8,10,8,12,8,104,9,8,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,3,10,113,8,10,1,11,1,11,3,11,117,8,11,1,12,1,12,3,12,121,8,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,0,1,14,18,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,0,4,1,0,2,3,1,0,4,5,0,1,2,0,17,17,22,22,153,
        0,37,1,0,0,0,2,56,1,0,0,0,4,60,1,0,0,0,6,64,1,0,0,0,8,66,1,0,0,0,
        10,70,1,0,0,0,12,74,1,0,0,0,14,85,1,0,0,0,16,98,1,0,0,0,18,107,1,
        0,0,0,20,112,1,0,0,0,22,116,1,0,0,0,24,120,1,0,0,0,26,122,1,0,0,
        0,28,128,1,0,0,0,30,135,1,0,0,0,32,141,1,0,0,0,34,148,1,0,0,0,36,
        38,5,15,0,0,37,36,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,41,5,20,
        0,0,40,39,1,0,0,0,40,41,1,0,0,0,41,45,1,0,0,0,42,44,3,2,1,0,43,42,
        1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,
        47,45,1,0,0,0,48,50,5,16,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,1,1,
        0,0,0,51,57,3,4,2,0,52,57,3,14,7,0,53,57,3,16,8,0,54,57,3,18,9,0,
        55,57,3,20,10,0,56,51,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,
        1,0,0,0,56,55,1,0,0,0,57,3,1,0,0,0,58,61,3,6,3,0,59,61,3,12,6,0,
        60,58,1,0,0,0,60,59,1,0,0,0,61,5,1,0,0,0,62,65,3,8,4,0,63,65,3,10,
        5,0,64,62,1,0,0,0,64,63,1,0,0,0,65,7,1,0,0,0,66,67,5,17,0,0,67,68,
        5,1,0,0,68,69,5,17,0,0,69,9,1,0,0,0,70,71,5,17,0,0,71,72,5,1,0,0,
        72,73,5,22,0,0,73,11,1,0,0,0,74,75,5,17,0,0,75,76,5,1,0,0,76,77,
        3,14,7,0,77,13,1,0,0,0,78,79,6,7,-1,0,79,80,5,6,0,0,80,81,3,14,7,
        0,81,82,5,7,0,0,82,86,1,0,0,0,83,86,5,22,0,0,84,86,5,17,0,0,85,78,
        1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,95,1,0,0,0,87,88,10,5,0,0,
        88,89,7,0,0,0,89,94,3,14,7,6,90,91,10,4,0,0,91,92,7,1,0,0,92,94,
        3,14,7,5,93,87,1,0,0,0,93,90,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,
        95,96,1,0,0,0,96,15,1,0,0,0,97,95,1,0,0,0,98,102,5,8,0,0,99,101,
        8,2,0,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,
        0,0,0,103,105,1,0,0,0,104,102,1,0,0,0,105,106,5,0,0,1,106,17,1,0,
        0,0,107,108,5,9,0,0,108,19,1,0,0,0,109,113,3,22,11,0,110,113,3,24,
        12,0,111,113,3,34,17,0,112,109,1,0,0,0,112,110,1,0,0,0,112,111,1,
        0,0,0,113,21,1,0,0,0,114,117,3,26,13,0,115,117,3,30,15,0,116,114,
        1,0,0,0,116,115,1,0,0,0,117,23,1,0,0,0,118,121,3,28,14,0,119,121,
        3,32,16,0,120,118,1,0,0,0,120,119,1,0,0,0,121,25,1,0,0,0,122,123,
        5,17,0,0,123,124,5,10,0,0,124,125,7,3,0,0,125,126,5,11,0,0,126,127,
        7,3,0,0,127,27,1,0,0,0,128,129,5,17,0,0,129,130,5,12,0,0,130,131,
        7,3,0,0,131,132,5,13,0,0,132,133,5,1,0,0,133,134,7,3,0,0,134,29,
        1,0,0,0,135,136,5,17,0,0,136,137,5,10,0,0,137,138,7,3,0,0,138,139,
        5,11,0,0,139,140,3,14,7,0,140,31,1,0,0,0,141,142,5,17,0,0,142,143,
        5,12,0,0,143,144,7,3,0,0,144,145,5,13,0,0,145,146,5,1,0,0,146,147,
        3,14,7,0,147,33,1,0,0,0,148,149,5,17,0,0,149,150,5,14,0,0,150,151,
        7,3,0,0,151,35,1,0,0,0,14,37,40,45,49,56,60,64,85,93,95,102,112,
        116,120
    ]

class BasicLangParser ( Parser ):

    grammarFileName = "BasicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'print'", "'exit'", "':'", "'<->'", "'['", 
                     "']'", "'+='", "'<#'", "'#>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BSTART", "BFIN", 
                      "ID", "DOT", "DASH", "CAPID", "ANY", "INT", "NL", 
                      "WS", "BRACES" ]

    RULE_block = 0
    RULE_statement = 1
    RULE_equation = 2
    RULE_normal_equation = 3
    RULE_str_equation = 4
    RULE_num_equation = 5
    RULE_exp_equation = 6
    RULE_expr = 7
    RULE_show = 8
    RULE_quit = 9
    RULE_link = 10
    RULE_link_def = 11
    RULE_link_mod = 12
    RULE_link_def_n = 13
    RULE_link_mod_n = 14
    RULE_link_def_expr = 15
    RULE_link_mod_expr = 16
    RULE_link_app = 17

    ruleNames =  [ "block", "statement", "equation", "normal_equation", 
                   "str_equation", "num_equation", "exp_equation", "expr", 
                   "show", "quit", "link", "link_def", "link_mod", "link_def_n", 
                   "link_mod_n", "link_def_expr", "link_mod_expr", "link_app" ]

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
    T__13=14
    BSTART=15
    BFIN=16
    ID=17
    DOT=18
    DASH=19
    CAPID=20
    ANY=21
    INT=22
    NL=23
    WS=24
    BRACES=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_block

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlkContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.BlockContext
            super().__init__(parser)
            self.bst = None # Token
            self.bid = None # Token
            self.bstmt = None # StatementContext
            self.bfn = None # Token
            self.copyFrom(ctx)

        def BSTART(self):
            return self.getToken(BasicLangParser.BSTART, 0)
        def CAPID(self):
            return self.getToken(BasicLangParser.CAPID, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicLangParser.StatementContext,i)

        def BFIN(self):
            return self.getToken(BasicLangParser.BFIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlk" ):
                listener.enterBlk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlk" ):
                listener.exitBlk(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlk" ):
                return visitor.visitBlk(self)
            else:
                return visitor.visitChildren(self)



    def block(self):

        localctx = BasicLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_block)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.BlkContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.BSTART:
                self.state = 36
                localctx.bst = self.match(BasicLangParser.BSTART)


            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.CAPID:
                self.state = 39
                localctx.bid = self.match(BasicLangParser.CAPID)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__5) | (1 << BasicLangParser.T__7) | (1 << BasicLangParser.T__8) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.INT))) != 0):
                self.state = 42
                localctx.bstmt = self.statement()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.BFIN:
                self.state = 48
                localctx.bfn = self.match(BasicLangParser.BFIN)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.show()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.quit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
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
        self.enterRule(localctx, 4, self.RULE_equation)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.normal_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
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
        self.enterRule(localctx, 6, self.RULE_normal_equation)
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.str_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
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
        self.enterRule(localctx, 8, self.RULE_str_equation)
        try:
            localctx = BasicLangParser.StrEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 67
            self.match(BasicLangParser.T__0)
            self.state = 68
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
        self.enterRule(localctx, 10, self.RULE_num_equation)
        try:
            localctx = BasicLangParser.IntEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 71
            self.match(BasicLangParser.T__0)
            self.state = 72
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
            self.state = 74
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 75
            self.match(BasicLangParser.T__0)
            self.state = 76
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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicLangParser.T__5]:
                localctx = BasicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 79
                self.match(BasicLangParser.T__5)
                self.state = 80
                self.expr(0)
                self.state = 81
                self.match(BasicLangParser.T__6)
                pass
            elif token in [BasicLangParser.INT]:
                localctx = BasicLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 83
                localctx.atom = self.match(BasicLangParser.INT)
                pass
            elif token in [BasicLangParser.ID]:
                localctx = BasicLangParser.IDExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                localctx.atom = self.match(BasicLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 93
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 87
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 88
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__1 or _la==BasicLangParser.T__2):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 89
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 90
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 91
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__3 or _la==BasicLangParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 92
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_show)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ShowStrExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(BasicLangParser.T__7)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__0) | (1 << BasicLangParser.T__1) | (1 << BasicLangParser.T__2) | (1 << BasicLangParser.T__3) | (1 << BasicLangParser.T__4) | (1 << BasicLangParser.T__5) | (1 << BasicLangParser.T__6) | (1 << BasicLangParser.T__7) | (1 << BasicLangParser.T__8) | (1 << BasicLangParser.T__9) | (1 << BasicLangParser.T__10) | (1 << BasicLangParser.T__11) | (1 << BasicLangParser.T__12) | (1 << BasicLangParser.T__13) | (1 << BasicLangParser.BSTART) | (1 << BasicLangParser.BFIN) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.DOT) | (1 << BasicLangParser.DASH) | (1 << BasicLangParser.CAPID) | (1 << BasicLangParser.ANY) | (1 << BasicLangParser.INT) | (1 << BasicLangParser.NL) | (1 << BasicLangParser.WS) | (1 << BasicLangParser.BRACES))) != 0):
                self.state = 99
                localctx.text = self._input.LT(1)
                _la = self._input.LA(1)
                if _la <= 0 or _la==BasicLangParser.EOF:
                    localctx.text = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
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
        self.enterRule(localctx, 18, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
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


        def link_mod(self):
            return self.getTypedRuleContext(BasicLangParser.Link_modContext,0)


        def link_app(self):
            return self.getTypedRuleContext(BasicLangParser.Link_appContext,0)


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
        self.enterRule(localctx, 20, self.RULE_link)
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.link_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.link_mod()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.link_app()
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

        def link_def_n(self):
            return self.getTypedRuleContext(BasicLangParser.Link_def_nContext,0)


        def link_def_expr(self):
            return self.getTypedRuleContext(BasicLangParser.Link_def_exprContext,0)


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink_def" ):
                listener.enterLink_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink_def" ):
                listener.exitLink_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink_def" ):
                return visitor.visitLink_def(self)
            else:
                return visitor.visitChildren(self)




    def link_def(self):

        localctx = BasicLangParser.Link_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_link_def)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.link_def_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.link_def_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_modContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def link_mod_n(self):
            return self.getTypedRuleContext(BasicLangParser.Link_mod_nContext,0)


        def link_mod_expr(self):
            return self.getTypedRuleContext(BasicLangParser.Link_mod_exprContext,0)


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_mod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLink_mod" ):
                listener.enterLink_mod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLink_mod" ):
                listener.exitLink_mod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLink_mod" ):
                return visitor.visitLink_mod(self)
            else:
                return visitor.visitChildren(self)




    def link_mod(self):

        localctx = BasicLangParser.Link_modContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_link_mod)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.link_mod_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.link_mod_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_def_nContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_def_n

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkDefEqnContext(Link_def_nContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_def_nContext
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



    def link_def_n(self):

        localctx = BasicLangParser.Link_def_nContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_link_def_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 123
            self.match(BasicLangParser.T__9)
            self.state = 124
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 125
            self.match(BasicLangParser.T__10)
            self.state = 126
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


    class Link_mod_nContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_mod_n

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkModEqnContext(Link_mod_nContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_mod_nContext
            super().__init__(parser)
            self.name = None # Token
            self.elem = None # Token
            self.value = None # Token
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
            if hasattr( listener, "enterLinkModEqn" ):
                listener.enterLinkModEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkModEqn" ):
                listener.exitLinkModEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkModEqn" ):
                return visitor.visitLinkModEqn(self)
            else:
                return visitor.visitChildren(self)



    def link_mod_n(self):

        localctx = BasicLangParser.Link_mod_nContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_link_mod_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 129
            self.match(BasicLangParser.T__11)
            self.state = 130
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self.match(BasicLangParser.T__12)
            self.state = 132
            self.match(BasicLangParser.T__0)
            self.state = 133
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.value = self._errHandler.recoverInline(self)
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


    class Link_def_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_def_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkDefExprEqnContext(Link_def_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_def_exprContext
            super().__init__(parser)
            self.name = None # Token
            self.lid = None # Token
            self.rid = None # ExprContext
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def expr(self):
            return self.getTypedRuleContext(BasicLangParser.ExprContext,0)

        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkDefExprEqn" ):
                listener.enterLinkDefExprEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkDefExprEqn" ):
                listener.exitLinkDefExprEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkDefExprEqn" ):
                return visitor.visitLinkDefExprEqn(self)
            else:
                return visitor.visitChildren(self)



    def link_def_expr(self):

        localctx = BasicLangParser.Link_def_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_link_def_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 136
            self.match(BasicLangParser.T__9)
            self.state = 137
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self.match(BasicLangParser.T__10)
            self.state = 139
            localctx.rid = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_mod_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_mod_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkModExprEqnContext(Link_mod_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_mod_exprContext
            super().__init__(parser)
            self.name = None # Token
            self.elem = None # Token
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def expr(self):
            return self.getTypedRuleContext(BasicLangParser.ExprContext,0)

        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkModExprEqn" ):
                listener.enterLinkModExprEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkModExprEqn" ):
                listener.exitLinkModExprEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkModExprEqn" ):
                return visitor.visitLinkModExprEqn(self)
            else:
                return visitor.visitChildren(self)



    def link_mod_expr(self):

        localctx = BasicLangParser.Link_mod_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_link_mod_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 142
            self.match(BasicLangParser.T__11)
            self.state = 143
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 144
            self.match(BasicLangParser.T__12)
            self.state = 145
            self.match(BasicLangParser.T__0)
            self.state = 146
            localctx.value = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Link_appContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_link_app

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LinkAppEqnContext(Link_appContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.Link_appContext
            super().__init__(parser)
            self.name = None # Token
            self.value = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinkAppEqn" ):
                listener.enterLinkAppEqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinkAppEqn" ):
                listener.exitLinkAppEqn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinkAppEqn" ):
                return visitor.visitLinkAppEqn(self)
            else:
                return visitor.visitChildren(self)



    def link_app(self):

        localctx = BasicLangParser.Link_appContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_link_app)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkAppEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 149
            self.match(BasicLangParser.T__13)
            self.state = 150
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.value = self._errHandler.recoverInline(self)
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
         




