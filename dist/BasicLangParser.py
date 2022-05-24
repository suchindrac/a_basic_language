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
        4,1,37,267,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,3,1,66,8,1,1,1,
        1,1,3,1,70,8,1,4,1,72,8,1,11,1,12,1,73,1,1,1,1,3,1,78,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,3,1,3,3,3,
        96,8,3,1,3,3,3,99,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,5,108,8,5,1,
        5,3,5,111,8,5,1,5,3,5,114,8,5,1,5,3,5,117,8,5,1,6,1,6,1,6,1,7,1,
        7,3,7,124,8,7,1,8,1,8,3,8,128,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        149,8,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,157,8,12,10,12,12,12,
        160,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,171,8,
        13,1,14,1,14,1,14,3,14,176,8,14,1,14,3,14,179,8,14,1,14,3,14,182,
        8,14,1,14,1,14,3,14,186,8,14,1,14,3,14,189,8,14,1,14,3,14,192,8,
        14,1,15,1,15,1,15,3,15,197,8,15,1,15,3,15,200,8,15,1,15,3,15,203,
        8,15,1,15,1,15,3,15,207,8,15,1,15,3,15,210,8,15,1,15,3,15,213,8,
        15,1,16,1,16,5,16,217,8,16,10,16,12,16,220,9,16,1,17,1,17,1,18,1,
        18,1,18,3,18,227,8,18,1,19,1,19,3,19,231,8,19,1,20,1,20,3,20,235,
        8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,0,1,24,26,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,5,1,0,7,8,1,0,
        9,10,2,0,29,29,34,34,1,0,13,17,1,0,35,35,288,0,52,1,0,0,0,2,62,1,
        0,0,0,4,91,1,0,0,0,6,93,1,0,0,0,8,100,1,0,0,0,10,104,1,0,0,0,12,
        118,1,0,0,0,14,123,1,0,0,0,16,127,1,0,0,0,18,129,1,0,0,0,20,133,
        1,0,0,0,22,137,1,0,0,0,24,148,1,0,0,0,26,170,1,0,0,0,28,172,1,0,
        0,0,30,193,1,0,0,0,32,214,1,0,0,0,34,221,1,0,0,0,36,226,1,0,0,0,
        38,230,1,0,0,0,40,234,1,0,0,0,42,236,1,0,0,0,44,242,1,0,0,0,46,249,
        1,0,0,0,48,255,1,0,0,0,50,262,1,0,0,0,52,57,3,2,1,0,53,54,5,35,0,
        0,54,56,3,2,1,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,
        1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,
        63,5,29,0,0,63,65,5,27,0,0,64,66,5,35,0,0,65,64,1,0,0,0,65,66,1,
        0,0,0,66,71,1,0,0,0,67,69,3,4,2,0,68,70,5,35,0,0,69,68,1,0,0,0,69,
        70,1,0,0,0,70,72,1,0,0,0,71,67,1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,
        0,73,74,1,0,0,0,74,75,1,0,0,0,75,77,5,28,0,0,76,78,5,35,0,0,77,76,
        1,0,0,0,77,78,1,0,0,0,78,3,1,0,0,0,79,92,3,14,7,0,80,92,3,24,12,
        0,81,92,3,32,16,0,82,92,3,34,17,0,83,92,3,36,18,0,84,92,3,10,5,0,
        85,92,3,12,6,0,86,92,3,6,3,0,87,92,3,8,4,0,88,92,3,28,14,0,89,92,
        3,30,15,0,90,92,3,2,1,0,91,79,1,0,0,0,91,80,1,0,0,0,91,81,1,0,0,
        0,91,82,1,0,0,0,91,83,1,0,0,0,91,84,1,0,0,0,91,85,1,0,0,0,91,86,
        1,0,0,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,
        92,5,1,0,0,0,93,95,5,1,0,0,94,96,5,34,0,0,95,94,1,0,0,0,95,96,1,
        0,0,0,96,98,1,0,0,0,97,99,5,29,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,
        7,1,0,0,0,100,101,5,29,0,0,101,102,5,2,0,0,102,103,5,3,0,0,103,9,
        1,0,0,0,104,105,5,4,0,0,105,107,5,29,0,0,106,108,5,32,0,0,107,106,
        1,0,0,0,107,108,1,0,0,0,108,110,1,0,0,0,109,111,5,34,0,0,110,109,
        1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,114,5,5,0,0,113,112,
        1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,117,5,29,0,0,116,115,
        1,0,0,0,116,117,1,0,0,0,117,11,1,0,0,0,118,119,5,6,0,0,119,120,5,
        29,0,0,120,13,1,0,0,0,121,124,3,16,8,0,122,124,3,22,11,0,123,121,
        1,0,0,0,123,122,1,0,0,0,124,15,1,0,0,0,125,128,3,18,9,0,126,128,
        3,20,10,0,127,125,1,0,0,0,127,126,1,0,0,0,128,17,1,0,0,0,129,130,
        5,29,0,0,130,131,5,2,0,0,131,132,5,29,0,0,132,19,1,0,0,0,133,134,
        5,29,0,0,134,135,5,2,0,0,135,136,5,34,0,0,136,21,1,0,0,0,137,138,
        5,29,0,0,138,139,5,2,0,0,139,140,3,24,12,0,140,23,1,0,0,0,141,142,
        6,12,-1,0,142,143,5,11,0,0,143,144,3,24,12,0,144,145,5,12,0,0,145,
        149,1,0,0,0,146,149,5,34,0,0,147,149,5,29,0,0,148,141,1,0,0,0,148,
        146,1,0,0,0,148,147,1,0,0,0,149,158,1,0,0,0,150,151,10,5,0,0,151,
        152,7,0,0,0,152,157,3,24,12,6,153,154,10,4,0,0,154,155,7,1,0,0,155,
        157,3,24,12,5,156,150,1,0,0,0,156,153,1,0,0,0,157,160,1,0,0,0,158,
        156,1,0,0,0,158,159,1,0,0,0,159,25,1,0,0,0,160,158,1,0,0,0,161,162,
        7,2,0,0,162,163,7,3,0,0,163,171,7,2,0,0,164,165,5,11,0,0,165,166,
        3,26,13,0,166,167,5,12,0,0,167,171,1,0,0,0,168,171,5,34,0,0,169,
        171,5,29,0,0,170,161,1,0,0,0,170,164,1,0,0,0,170,168,1,0,0,0,170,
        169,1,0,0,0,171,27,1,0,0,0,172,173,5,29,0,0,173,175,5,18,0,0,174,
        176,5,29,0,0,175,174,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,
        179,3,14,7,0,178,177,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,0,180,
        182,5,19,0,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,1,0,0,0,183,
        185,5,20,0,0,184,186,5,29,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,
        188,1,0,0,0,187,189,5,19,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,
        191,1,0,0,0,190,192,3,14,7,0,191,190,1,0,0,0,191,192,1,0,0,0,192,
        29,1,0,0,0,193,194,3,26,13,0,194,196,5,18,0,0,195,197,5,29,0,0,196,
        195,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,200,3,14,7,0,199,
        198,1,0,0,0,199,200,1,0,0,0,200,202,1,0,0,0,201,203,5,19,0,0,202,
        201,1,0,0,0,202,203,1,0,0,0,203,204,1,0,0,0,204,206,5,20,0,0,205,
        207,5,29,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,
        210,5,19,0,0,209,208,1,0,0,0,209,210,1,0,0,0,210,212,1,0,0,0,211,
        213,3,14,7,0,212,211,1,0,0,0,212,213,1,0,0,0,213,31,1,0,0,0,214,
        218,5,21,0,0,215,217,8,4,0,0,216,215,1,0,0,0,217,220,1,0,0,0,218,
        216,1,0,0,0,218,219,1,0,0,0,219,33,1,0,0,0,220,218,1,0,0,0,221,222,
        5,22,0,0,222,35,1,0,0,0,223,227,3,38,19,0,224,227,3,40,20,0,225,
        227,3,50,25,0,226,223,1,0,0,0,226,224,1,0,0,0,226,225,1,0,0,0,227,
        37,1,0,0,0,228,231,3,42,21,0,229,231,3,46,23,0,230,228,1,0,0,0,230,
        229,1,0,0,0,231,39,1,0,0,0,232,235,3,44,22,0,233,235,3,48,24,0,234,
        232,1,0,0,0,234,233,1,0,0,0,235,41,1,0,0,0,236,237,5,29,0,0,237,
        238,5,20,0,0,238,239,7,2,0,0,239,240,5,23,0,0,240,241,7,2,0,0,241,
        43,1,0,0,0,242,243,5,29,0,0,243,244,5,24,0,0,244,245,7,2,0,0,245,
        246,5,25,0,0,246,247,5,2,0,0,247,248,7,2,0,0,248,45,1,0,0,0,249,
        250,5,29,0,0,250,251,5,20,0,0,251,252,7,2,0,0,252,253,5,23,0,0,253,
        254,3,24,12,0,254,47,1,0,0,0,255,256,5,29,0,0,256,257,5,24,0,0,257,
        258,7,2,0,0,258,259,5,25,0,0,259,260,5,2,0,0,260,261,3,24,12,0,261,
        49,1,0,0,0,262,263,5,29,0,0,263,264,5,26,0,0,264,265,7,2,0,0,265,
        51,1,0,0,0,34,57,65,69,73,77,91,95,98,107,110,113,116,123,127,148,
        156,158,170,175,178,181,185,188,191,196,199,202,206,209,212,218,
        226,230,234
    ]

class BasicLangParser ( Parser ):

    grammarFileName = "BasicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'setres'", "'='", "'getres'", "'exec'", 
                     "'max'", "'import'", "'*'", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'eq'", "'gt'", "'lt'", "'ge'", "'le'", "'?'", 
                     "'none'", "':'", "'print'", "'exit'", "'<->'", "'['", 
                     "']'", "'+='", "'<#'", "'#>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BSTART", "BFIN", 
                      "ID", "DOT", "DASH", "COMMA", "ANY", "INT", "NL", 
                      "WS", "BRACES" ]

    RULE_script = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_setres = 3
    RULE_getres = 4
    RULE_exec = 5
    RULE_insert = 6
    RULE_equation = 7
    RULE_normal_equation = 8
    RULE_str_equation = 9
    RULE_num_equation = 10
    RULE_exp_equation = 11
    RULE_expr = 12
    RULE_cond = 13
    RULE_ifblock = 14
    RULE_ifcond = 15
    RULE_show = 16
    RULE_quit = 17
    RULE_link = 18
    RULE_link_def = 19
    RULE_link_mod = 20
    RULE_link_def_n = 21
    RULE_link_mod_n = 22
    RULE_link_def_expr = 23
    RULE_link_mod_expr = 24
    RULE_link_app = 25

    ruleNames =  [ "script", "block", "statement", "setres", "getres", "exec", 
                   "insert", "equation", "normal_equation", "str_equation", 
                   "num_equation", "exp_equation", "expr", "cond", "ifblock", 
                   "ifcond", "show", "quit", "link", "link_def", "link_mod", 
                   "link_def_n", "link_mod_n", "link_def_expr", "link_mod_expr", 
                   "link_app" ]

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
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    BSTART=27
    BFIN=28
    ID=29
    DOT=30
    DASH=31
    COMMA=32
    ANY=33
    INT=34
    NL=35
    WS=36
    BRACES=37

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
            self.state = 52
            self.block()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicLangParser.NL:
                self.state = 53
                self.match(BasicLangParser.NL)
                self.state = 54
                self.block()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
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
            self.state = 62
            localctx.bid = self.match(BasicLangParser.ID)
            self.state = 63
            self.match(BasicLangParser.BSTART)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.NL:
                self.state = 64
                self.match(BasicLangParser.NL)


            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BasicLangParser.NL:
                    self.state = 68
                    self.match(BasicLangParser.NL)


                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__0) | (1 << BasicLangParser.T__3) | (1 << BasicLangParser.T__5) | (1 << BasicLangParser.T__10) | (1 << BasicLangParser.T__20) | (1 << BasicLangParser.T__21) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.INT))) != 0)):
                    break

            self.state = 75
            self.match(BasicLangParser.BFIN)
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 76
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


        def ifcond(self):
            return self.getTypedRuleContext(BasicLangParser.IfcondContext,0)


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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.show()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.quit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.link()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.exec()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 85
                self.insert()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.setres()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 87
                self.getres()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 88
                self.ifblock()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 89
                self.ifcond()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 90
                self.block()
                pass


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
        self.enterRule(localctx, 6, self.RULE_setres)
        try:
            localctx = BasicLangParser.SetResultContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(BasicLangParser.T__0)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 94
                localctx.varint = self.match(BasicLangParser.INT)


            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 97
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
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)

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
        self.enterRule(localctx, 8, self.RULE_getres)
        try:
            localctx = BasicLangParser.GetResultContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 101
            self.match(BasicLangParser.T__1)
            self.state = 102
            self.match(BasicLangParser.T__2)
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
        self.enterRule(localctx, 10, self.RULE_exec)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ExecBlockContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(BasicLangParser.T__3)
            self.state = 105
            localctx.blkid = self.match(BasicLangParser.ID)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.COMMA:
                self.state = 106
                self.match(BasicLangParser.COMMA)


            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 109
                localctx.times = self.match(BasicLangParser.INT)


            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.T__4:
                self.state = 112
                localctx.times = self.match(BasicLangParser.T__4)


            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 115
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
        self.enterRule(localctx, 12, self.RULE_insert)
        try:
            localctx = BasicLangParser.InsertFileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(BasicLangParser.T__5)
            self.state = 119
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
        self.enterRule(localctx, 14, self.RULE_equation)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.normal_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
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
        self.enterRule(localctx, 16, self.RULE_normal_equation)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.str_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
        self.enterRule(localctx, 18, self.RULE_str_equation)
        try:
            localctx = BasicLangParser.StrEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 130
            self.match(BasicLangParser.T__1)
            self.state = 131
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
        self.enterRule(localctx, 20, self.RULE_num_equation)
        try:
            localctx = BasicLangParser.IntEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 134
            self.match(BasicLangParser.T__1)
            self.state = 135
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
        self.enterRule(localctx, 22, self.RULE_exp_equation)
        try:
            localctx = BasicLangParser.ExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 138
            self.match(BasicLangParser.T__1)
            self.state = 139
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicLangParser.T__10]:
                localctx = BasicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 142
                self.match(BasicLangParser.T__10)
                self.state = 143
                self.expr(0)
                self.state = 144
                self.match(BasicLangParser.T__11)
                pass
            elif token in [BasicLangParser.INT]:
                localctx = BasicLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                localctx.atom = self.match(BasicLangParser.INT)
                pass
            elif token in [BasicLangParser.ID]:
                localctx = BasicLangParser.IDExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                localctx.atom = self.match(BasicLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 156
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 150
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 151
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__6 or _la==BasicLangParser.T__7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 152
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 154
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__8 or _la==BasicLangParser.T__9):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 155
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberCondExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.CondContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(BasicLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberCondExpr" ):
                listener.enterNumberCondExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberCondExpr" ):
                listener.exitNumberCondExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberCondExpr" ):
                return visitor.visitNumberCondExpr(self)
            else:
                return visitor.visitChildren(self)


    class CondParenExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(BasicLangParser.CondContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondParenExpr" ):
                listener.enterCondParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondParenExpr" ):
                listener.exitCondParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondParenExpr" ):
                return visitor.visitCondParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IDCondExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.CondContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(BasicLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIDCondExpr" ):
                listener.enterIDCondExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIDCondExpr" ):
                listener.exitIDCondExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIDCondExpr" ):
                return visitor.visitIDCondExpr(self)
            else:
                return visitor.visitChildren(self)


    class CondExprContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.CondContext
            super().__init__(parser)
            self.left = None # Token
            self.op = None # Token
            self.right = None # Token
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
            if hasattr( listener, "enterCondExpr" ):
                listener.enterCondExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondExpr" ):
                listener.exitCondExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondExpr" ):
                return visitor.visitCondExpr(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = BasicLangParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = BasicLangParser.CondExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                localctx.left = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                    localctx.left = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__12) | (1 << BasicLangParser.T__13) | (1 << BasicLangParser.T__14) | (1 << BasicLangParser.T__15) | (1 << BasicLangParser.T__16))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                localctx.right = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                    localctx.right = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = BasicLangParser.CondParenExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(BasicLangParser.T__10)
                self.state = 165
                self.cond()
                self.state = 166
                self.match(BasicLangParser.T__11)
                pass

            elif la_ == 3:
                localctx = BasicLangParser.NumberCondExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                localctx.atom = self.match(BasicLangParser.INT)
                pass

            elif la_ == 4:
                localctx = BasicLangParser.IDCondExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 169
                localctx.atom = self.match(BasicLangParser.ID)
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
            self.op = None # Token
            self.acttrueid = None # Token
            self.acttrueeqn = None # EquationContext
            self.acttrueval = None # Token
            self.sep = None # Token
            self.actfalseid = None # Token
            self.actfalseval = None # Token
            self.actfalseeqn = None # EquationContext
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLangParser.EquationContext)
            else:
                return self.getTypedRuleContext(BasicLangParser.EquationContext,i)


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
        self.enterRule(localctx, 28, self.RULE_ifblock)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.IfBlockContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            localctx.ifblk = self.match(BasicLangParser.ID)
            self.state = 173
            localctx.op = self.match(BasicLangParser.T__17)
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 174
                localctx.acttrueid = self.match(BasicLangParser.ID)


            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.ID:
                self.state = 177
                localctx.acttrueeqn = self.equation()


            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.T__18:
                self.state = 180
                localctx.acttrueval = self.match(BasicLangParser.T__18)


            self.state = 183
            localctx.sep = self.match(BasicLangParser.T__19)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 184
                localctx.actfalseid = self.match(BasicLangParser.ID)


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.T__18:
                self.state = 187
                localctx.actfalseval = self.match(BasicLangParser.T__18)


            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 190
                localctx.actfalseeqn = self.equation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfcondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicLangParser.RULE_ifcond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfConditionContext(IfcondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLangParser.IfcondContext
            super().__init__(parser)
            self.leftcond = None # CondContext
            self.op = None # Token
            self.iftrueid = None # Token
            self.iftrueeqn = None # EquationContext
            self.iftrueval = None # Token
            self.sep = None # Token
            self.iffalseid = None # Token
            self.iffalseval = None # Token
            self.iffalseeqn = None # EquationContext
            self.copyFrom(ctx)

        def cond(self):
            return self.getTypedRuleContext(BasicLangParser.CondContext,0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.ID)
            else:
                return self.getToken(BasicLangParser.ID, i)
        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLangParser.EquationContext)
            else:
                return self.getTypedRuleContext(BasicLangParser.EquationContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCondition" ):
                listener.enterIfCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCondition" ):
                listener.exitIfCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCondition" ):
                return visitor.visitIfCondition(self)
            else:
                return visitor.visitChildren(self)



    def ifcond(self):

        localctx = BasicLangParser.IfcondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifcond)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.IfConditionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            localctx.leftcond = self.cond()
            self.state = 194
            localctx.op = self.match(BasicLangParser.T__17)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 195
                localctx.iftrueid = self.match(BasicLangParser.ID)


            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.ID:
                self.state = 198
                localctx.iftrueeqn = self.equation()


            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.T__18:
                self.state = 201
                localctx.iftrueval = self.match(BasicLangParser.T__18)


            self.state = 204
            localctx.sep = self.match(BasicLangParser.T__19)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 205
                localctx.iffalseid = self.match(BasicLangParser.ID)


            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BasicLangParser.T__18:
                self.state = 208
                localctx.iffalseval = self.match(BasicLangParser.T__18)


            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 211
                localctx.iffalseeqn = self.equation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 32, self.RULE_show)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ShowStrExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(BasicLangParser.T__20)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 215
                    localctx.text = self._input.LT(1)
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==BasicLangParser.NL:
                        localctx.text = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 220
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(BasicLangParser.T__21)
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
        self.enterRule(localctx, 36, self.RULE_link)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.link_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.link_mod()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
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
        self.enterRule(localctx, 38, self.RULE_link_def)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.link_def_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
        self.enterRule(localctx, 40, self.RULE_link_mod)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.link_mod_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
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
        self.enterRule(localctx, 42, self.RULE_link_def_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 237
            self.match(BasicLangParser.T__19)
            self.state = 238
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 239
            self.match(BasicLangParser.T__22)
            self.state = 240
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
        self.enterRule(localctx, 44, self.RULE_link_mod_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 243
            self.match(BasicLangParser.T__23)
            self.state = 244
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 245
            self.match(BasicLangParser.T__24)
            self.state = 246
            self.match(BasicLangParser.T__1)
            self.state = 247
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
        self.enterRule(localctx, 46, self.RULE_link_def_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 250
            self.match(BasicLangParser.T__19)
            self.state = 251
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 252
            self.match(BasicLangParser.T__22)
            self.state = 253
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
        self.enterRule(localctx, 48, self.RULE_link_mod_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 256
            self.match(BasicLangParser.T__23)
            self.state = 257
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 258
            self.match(BasicLangParser.T__24)
            self.state = 259
            self.match(BasicLangParser.T__1)
            self.state = 260
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
        self.enterRule(localctx, 50, self.RULE_link_app)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkAppEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 263
            self.match(BasicLangParser.T__25)
            self.state = 264
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
        self._predicates[12] = self.expr_sempred
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
         




