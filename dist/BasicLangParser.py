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
        4,1,30,213,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,5,0,52,8,0,10,0,12,
        0,55,9,0,1,0,1,0,1,1,1,1,1,1,3,1,62,8,1,1,1,1,1,3,1,66,8,1,4,1,68,
        8,1,11,1,12,1,69,1,1,1,1,3,1,74,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,87,8,2,1,3,1,3,1,3,1,4,1,4,3,4,94,8,4,1,4,3,
        4,97,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,107,8,6,1,6,3,6,110,
        8,6,1,6,3,6,113,8,6,1,6,3,6,116,8,6,1,7,1,7,1,7,1,8,1,8,3,8,123,
        8,8,1,9,1,9,3,9,127,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,148,
        8,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,156,8,13,10,13,12,13,159,
        9,13,1,14,1,14,5,14,163,8,14,10,14,12,14,166,9,14,1,15,1,15,1,16,
        1,16,1,16,3,16,173,8,16,1,17,1,17,3,17,177,8,17,1,18,1,18,3,18,181,
        8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,0,1,26,24,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,4,1,0,7,8,1,0,9,10,1,
        0,28,28,2,0,22,22,27,27,220,0,48,1,0,0,0,2,58,1,0,0,0,4,86,1,0,0,
        0,6,88,1,0,0,0,8,91,1,0,0,0,10,98,1,0,0,0,12,103,1,0,0,0,14,117,
        1,0,0,0,16,122,1,0,0,0,18,126,1,0,0,0,20,128,1,0,0,0,22,132,1,0,
        0,0,24,136,1,0,0,0,26,147,1,0,0,0,28,160,1,0,0,0,30,167,1,0,0,0,
        32,172,1,0,0,0,34,176,1,0,0,0,36,180,1,0,0,0,38,182,1,0,0,0,40,188,
        1,0,0,0,42,195,1,0,0,0,44,201,1,0,0,0,46,208,1,0,0,0,48,53,3,2,1,
        0,49,50,5,28,0,0,50,52,3,2,1,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,
        1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,1,0,0,0,56,57,5,0,0,1,
        57,1,1,0,0,0,58,59,5,22,0,0,59,61,5,20,0,0,60,62,5,28,0,0,61,60,
        1,0,0,0,61,62,1,0,0,0,62,67,1,0,0,0,63,65,3,4,2,0,64,66,5,28,0,0,
        65,64,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,63,1,0,0,0,68,69,1,
        0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,73,5,21,0,0,72,
        74,5,28,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,3,1,0,0,0,75,87,3,16,
        8,0,76,87,3,26,13,0,77,87,3,28,14,0,78,87,3,30,15,0,79,87,3,32,16,
        0,80,87,3,12,6,0,81,87,3,14,7,0,82,87,3,8,4,0,83,87,3,10,5,0,84,
        87,3,6,3,0,85,87,3,2,1,0,86,75,1,0,0,0,86,76,1,0,0,0,86,77,1,0,0,
        0,86,78,1,0,0,0,86,79,1,0,0,0,86,80,1,0,0,0,86,81,1,0,0,0,86,82,
        1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,5,1,0,0,0,88,
        89,5,22,0,0,89,90,5,22,0,0,90,7,1,0,0,0,91,93,5,1,0,0,92,94,5,27,
        0,0,93,92,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,97,5,22,0,0,96,
        95,1,0,0,0,96,97,1,0,0,0,97,9,1,0,0,0,98,99,5,22,0,0,99,100,5,2,
        0,0,100,101,5,3,0,0,101,102,5,22,0,0,102,11,1,0,0,0,103,104,5,4,
        0,0,104,106,5,22,0,0,105,107,5,25,0,0,106,105,1,0,0,0,106,107,1,
        0,0,0,107,109,1,0,0,0,108,110,5,27,0,0,109,108,1,0,0,0,109,110,1,
        0,0,0,110,112,1,0,0,0,111,113,5,5,0,0,112,111,1,0,0,0,112,113,1,
        0,0,0,113,115,1,0,0,0,114,116,5,22,0,0,115,114,1,0,0,0,115,116,1,
        0,0,0,116,13,1,0,0,0,117,118,5,6,0,0,118,119,5,22,0,0,119,15,1,0,
        0,0,120,123,3,18,9,0,121,123,3,24,12,0,122,120,1,0,0,0,122,121,1,
        0,0,0,123,17,1,0,0,0,124,127,3,20,10,0,125,127,3,22,11,0,126,124,
        1,0,0,0,126,125,1,0,0,0,127,19,1,0,0,0,128,129,5,22,0,0,129,130,
        5,2,0,0,130,131,5,22,0,0,131,21,1,0,0,0,132,133,5,22,0,0,133,134,
        5,2,0,0,134,135,5,27,0,0,135,23,1,0,0,0,136,137,5,22,0,0,137,138,
        5,2,0,0,138,139,3,26,13,0,139,25,1,0,0,0,140,141,6,13,-1,0,141,142,
        5,11,0,0,142,143,3,26,13,0,143,144,5,12,0,0,144,148,1,0,0,0,145,
        148,5,27,0,0,146,148,5,22,0,0,147,140,1,0,0,0,147,145,1,0,0,0,147,
        146,1,0,0,0,148,157,1,0,0,0,149,150,10,5,0,0,150,151,7,0,0,0,151,
        156,3,26,13,6,152,153,10,4,0,0,153,154,7,1,0,0,154,156,3,26,13,5,
        155,149,1,0,0,0,155,152,1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,
        157,158,1,0,0,0,158,27,1,0,0,0,159,157,1,0,0,0,160,164,5,13,0,0,
        161,163,8,2,0,0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,
        164,165,1,0,0,0,165,29,1,0,0,0,166,164,1,0,0,0,167,168,5,14,0,0,
        168,31,1,0,0,0,169,173,3,34,17,0,170,173,3,36,18,0,171,173,3,46,
        23,0,172,169,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,173,33,1,0,
        0,0,174,177,3,38,19,0,175,177,3,42,21,0,176,174,1,0,0,0,176,175,
        1,0,0,0,177,35,1,0,0,0,178,181,3,40,20,0,179,181,3,44,22,0,180,178,
        1,0,0,0,180,179,1,0,0,0,181,37,1,0,0,0,182,183,5,22,0,0,183,184,
        5,15,0,0,184,185,7,3,0,0,185,186,5,16,0,0,186,187,7,3,0,0,187,39,
        1,0,0,0,188,189,5,22,0,0,189,190,5,17,0,0,190,191,7,3,0,0,191,192,
        5,18,0,0,192,193,5,2,0,0,193,194,7,3,0,0,194,41,1,0,0,0,195,196,
        5,22,0,0,196,197,5,15,0,0,197,198,7,3,0,0,198,199,5,16,0,0,199,200,
        3,26,13,0,200,43,1,0,0,0,201,202,5,22,0,0,202,203,5,17,0,0,203,204,
        7,3,0,0,204,205,5,18,0,0,205,206,5,2,0,0,206,207,3,26,13,0,207,45,
        1,0,0,0,208,209,5,22,0,0,209,210,5,19,0,0,210,211,7,3,0,0,211,47,
        1,0,0,0,21,53,61,65,69,73,86,93,96,106,109,112,115,122,126,147,155,
        157,164,172,176,180
    ]

class BasicLangParser ( Parser ):

    grammarFileName = "BasicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'setres'", "'='", "'getres'", "'exec'", 
                     "'max'", "'import'", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'print'", "'exit'", "':'", "'<->'", "'['", 
                     "']'", "'+='", "'<#'", "'#>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BSTART", "BFIN", "ID", "DOT", "DASH", "COMMA", "ANY", 
                      "INT", "NL", "WS", "BRACES" ]

    RULE_script = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_ifblock = 3
    RULE_setres = 4
    RULE_getres = 5
    RULE_exec = 6
    RULE_insert = 7
    RULE_equation = 8
    RULE_normal_equation = 9
    RULE_str_equation = 10
    RULE_num_equation = 11
    RULE_exp_equation = 12
    RULE_expr = 13
    RULE_show = 14
    RULE_quit = 15
    RULE_link = 16
    RULE_link_def = 17
    RULE_link_mod = 18
    RULE_link_def_n = 19
    RULE_link_mod_n = 20
    RULE_link_def_expr = 21
    RULE_link_mod_expr = 22
    RULE_link_app = 23

    ruleNames =  [ "script", "block", "statement", "ifblock", "setres", 
                   "getres", "exec", "insert", "equation", "normal_equation", 
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
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    BSTART=20
    BFIN=21
    ID=22
    DOT=23
    DASH=24
    COMMA=25
    ANY=26
    INT=27
    NL=28
    WS=29
    BRACES=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_script

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExecScriptContext(ScriptContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ScriptContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(BasicLangParser.BlockContext,i)

        def EOF(self):
            return self.getToken(BasicLangParser.EOF, 0)
        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.NL)
            else:
                return self.getToken(BasicLangParser.NL, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecScript" ):
                listener.enterExecScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecScript" ):
                listener.exitExecScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecScript" ):
                return visitor.visitExecScript(self)
            else:
                return visitor.visitChildren(self)



    def script(self):

        localctx = BasicLangParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ExecScriptContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.block()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicLangParser.NL:
                self.state = 49
                self.match(BasicLangParser.NL)
                self.state = 50
                self.block()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(BasicLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
            self.bid = None # Token
            self.copyFrom(ctx)

        def BSTART(self):
            return self.getToken(BasicLangParser.BSTART, 0)
        def BFIN(self):
            return self.getToken(BasicLangParser.BFIN, 0)
        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)
        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.NL)
            else:
                return self.getToken(BasicLangParser.NL, i)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicLangParser.StatementContext,i)


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
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.BlkContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            localctx.bid = self.match(BasicLangParser.ID)
            self.state = 59
            self.match(BasicLangParser.BSTART)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.NL:
                self.state = 60
                self.match(BasicLangParser.NL)


            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BasicLangParser.NL:
                    self.state = 64
                    self.match(BasicLangParser.NL)


                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__0) | (1 << BasicLangParser.T__3) | (1 << BasicLangParser.T__5) | (1 << BasicLangParser.T__10) | (1 << BasicLangParser.T__12) | (1 << BasicLangParser.T__13) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.INT))) != 0)):
                    break

            self.state = 71
            self.match(BasicLangParser.BFIN)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 72
                self.match(BasicLangParser.NL)


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


        def exec(self):
            return self.getTypedRuleContext(BasicLangParser.ExecContext,0)


        def insert(self):
            return self.getTypedRuleContext(BasicLangParser.InsertContext,0)


        def setres(self):
            return self.getTypedRuleContext(BasicLangParser.SetresContext,0)


        def getres(self):
            return self.getTypedRuleContext(BasicLangParser.GetresContext,0)


        def ifblock(self):
            return self.getTypedRuleContext(BasicLangParser.IfblockContext,0)


        def block(self):
            return self.getTypedRuleContext(BasicLangParser.BlockContext,0)


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
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.show()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.quit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.link()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 80
                self.exec()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 81
                self.insert()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 82
                self.setres()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 83
                self.getres()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 84
                self.ifblock()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 85
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_ifblock

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfBlockContext(IfblockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.IfblockContext
            super().__init__(parser)
            self.ifblk = None # Token
            self.act = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)



    def ifblock(self):

        localctx = BasicLangParser.IfblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifblock)
        try:
            localctx = BasicLangParser.IfBlockContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            localctx.ifblk = self.match(BasicLangParser.ID)
            self.state = 89
            localctx.act = self.match(BasicLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_setres

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SetResultContext(SetresContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.SetresContext
            super().__init__(parser)
            self.varint = None # Token
            self.varid = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)
        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetResult" ):
                listener.enterSetResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetResult" ):
                listener.exitSetResult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetResult" ):
                return visitor.visitSetResult(self)
            else:
                return visitor.visitChildren(self)



    def setres(self):

        localctx = BasicLangParser.SetresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_setres)
        try:
            localctx = BasicLangParser.SetResultContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BasicLangParser.T__0)
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 92
                localctx.varint = self.match(BasicLangParser.INT)


            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 95
                localctx.varid = self.match(BasicLangParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_getres

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class GetResultContext(GetresContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.GetresContext
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
            if hasattr( listener, "enterGetResult" ):
                listener.enterGetResult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetResult" ):
                listener.exitGetResult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetResult" ):
                return visitor.visitGetResult(self)
            else:
                return visitor.visitChildren(self)



    def getres(self):

        localctx = BasicLangParser.GetresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_getres)
        try:
            localctx = BasicLangParser.GetResultContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 99
            self.match(BasicLangParser.T__1)
            self.state = 100
            self.match(BasicLangParser.T__2)
            self.state = 101
            localctx.value = self.match(BasicLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_exec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExecBlockContext(ExecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.ExecContext
            super().__init__(parser)
            self.blkid = None # Token
            self.times = None # Token
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def COMMA(self):
            return self.getToken(BasicLangParser.COMMA, 0)
        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecBlock" ):
                listener.enterExecBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecBlock" ):
                listener.exitExecBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecBlock" ):
                return visitor.visitExecBlock(self)
            else:
                return visitor.visitChildren(self)



    def exec(self):

        localctx = BasicLangParser.ExecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exec)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ExecBlockContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BasicLangParser.T__3)
            self.state = 104
            localctx.blkid = self.match(BasicLangParser.ID)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.COMMA:
                self.state = 105
                self.match(BasicLangParser.COMMA)


            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 108
                localctx.times = self.match(BasicLangParser.INT)


            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.T__4:
                self.state = 111
                localctx.times = self.match(BasicLangParser.T__4)


            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 114
                localctx.times = self.match(BasicLangParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_insert

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InsertFileContext(InsertContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.InsertContext
            super().__init__(parser)
            self.fname = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertFile" ):
                listener.enterInsertFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertFile" ):
                listener.exitInsertFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertFile" ):
                return visitor.visitInsertFile(self)
            else:
                return visitor.visitChildren(self)



    def insert(self):

        localctx = BasicLangParser.InsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_insert)
        try:
            localctx = BasicLangParser.InsertFileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BasicLangParser.T__5)
            self.state = 118
            localctx.fname = self.match(BasicLangParser.ID)
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
        self.enterRule(localctx, 16, self.RULE_equation)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.normal_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
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
        self.enterRule(localctx, 18, self.RULE_normal_equation)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.str_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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
        self.enterRule(localctx, 20, self.RULE_str_equation)
        try:
            localctx = BasicLangParser.StrEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 129
            self.match(BasicLangParser.T__1)
            self.state = 130
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
        self.enterRule(localctx, 22, self.RULE_num_equation)
        try:
            localctx = BasicLangParser.IntEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 133
            self.match(BasicLangParser.T__1)
            self.state = 134
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
        self.enterRule(localctx, 24, self.RULE_exp_equation)
        try:
            localctx = BasicLangParser.ExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 137
            self.match(BasicLangParser.T__1)
            self.state = 138
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicLangParser.T__10]:
                localctx = BasicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 141
                self.match(BasicLangParser.T__10)
                self.state = 142
                self.expr(0)
                self.state = 143
                self.match(BasicLangParser.T__11)
                pass
            elif token in [BasicLangParser.INT]:
                localctx = BasicLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                localctx.atom = self.match(BasicLangParser.INT)
                pass
            elif token in [BasicLangParser.ID]:
                localctx = BasicLangParser.IDExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                localctx.atom = self.match(BasicLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 155
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 149
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 150
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__6 or _la==BasicLangParser.T__7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 151
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 152
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 153
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__8 or _la==BasicLangParser.T__9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 154
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.NL)
            else:
                return self.getToken(BasicLangParser.NL, i)

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
        self.enterRule(localctx, 28, self.RULE_show)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ShowStrExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BasicLangParser.T__12)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    localctx.text = self._input.LT(1)
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==BasicLangParser.NL:
                        localctx.text = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(BasicLangParser.T__13)
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
        self.enterRule(localctx, 32, self.RULE_link)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.link_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.link_mod()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
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
        self.enterRule(localctx, 34, self.RULE_link_def)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.link_def_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
        self.enterRule(localctx, 36, self.RULE_link_mod)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.link_mod_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
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
        self.enterRule(localctx, 38, self.RULE_link_def_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 183
            self.match(BasicLangParser.T__14)
            self.state = 184
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 185
            self.match(BasicLangParser.T__15)
            self.state = 186
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
        self.enterRule(localctx, 40, self.RULE_link_mod_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 189
            self.match(BasicLangParser.T__16)
            self.state = 190
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 191
            self.match(BasicLangParser.T__17)
            self.state = 192
            self.match(BasicLangParser.T__1)
            self.state = 193
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
        self.enterRule(localctx, 42, self.RULE_link_def_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 196
            self.match(BasicLangParser.T__14)
            self.state = 197
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 198
            self.match(BasicLangParser.T__15)
            self.state = 199
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
        self.enterRule(localctx, 44, self.RULE_link_mod_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 202
            self.match(BasicLangParser.T__16)
            self.state = 203
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 204
            self.match(BasicLangParser.T__17)
            self.state = 205
            self.match(BasicLangParser.T__1)
            self.state = 206
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
        self.enterRule(localctx, 46, self.RULE_link_app)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkAppEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 209
            self.match(BasicLangParser.T__18)
            self.state = 210
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
        self._predicates[13] = self.expr_sempred
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
         




