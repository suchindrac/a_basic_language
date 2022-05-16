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
        4,1,27,173,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,4,1,59,8,1,11,1,12,1,60,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,73,8,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,3,5,83,8,
        5,1,6,1,6,3,6,87,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,108,8,10,1,10,1,10,1,
        10,1,10,1,10,1,10,5,10,116,8,10,10,10,12,10,119,9,10,1,11,1,11,5,
        11,123,8,11,10,11,12,11,126,9,11,1,12,1,12,1,13,1,13,1,13,3,13,133,
        8,13,1,14,1,14,3,14,137,8,14,1,15,1,15,3,15,141,8,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,20,1,20,0,1,20,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,0,4,1,0,4,5,1,0,6,7,1,0,25,25,2,0,19,19,24,24,170,
        0,42,1,0,0,0,2,52,1,0,0,0,4,72,1,0,0,0,6,74,1,0,0,0,8,77,1,0,0,0,
        10,82,1,0,0,0,12,86,1,0,0,0,14,88,1,0,0,0,16,92,1,0,0,0,18,96,1,
        0,0,0,20,107,1,0,0,0,22,120,1,0,0,0,24,127,1,0,0,0,26,132,1,0,0,
        0,28,136,1,0,0,0,30,140,1,0,0,0,32,142,1,0,0,0,34,148,1,0,0,0,36,
        155,1,0,0,0,38,161,1,0,0,0,40,168,1,0,0,0,42,47,3,2,1,0,43,44,5,
        25,0,0,44,46,3,2,1,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,
        48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,0,0,1,51,1,1,0,0,
        0,52,53,5,22,0,0,53,54,5,17,0,0,54,58,5,25,0,0,55,56,3,4,2,0,56,
        57,5,25,0,0,57,59,1,0,0,0,58,55,1,0,0,0,59,60,1,0,0,0,60,58,1,0,
        0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,5,18,0,0,63,64,5,25,0,0,64,
        3,1,0,0,0,65,73,3,10,5,0,66,73,3,20,10,0,67,73,3,22,11,0,68,73,3,
        24,12,0,69,73,3,26,13,0,70,73,3,6,3,0,71,73,3,8,4,0,72,65,1,0,0,
        0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,72,70,
        1,0,0,0,72,71,1,0,0,0,73,5,1,0,0,0,74,75,5,1,0,0,75,76,5,22,0,0,
        76,7,1,0,0,0,77,78,5,2,0,0,78,79,5,19,0,0,79,9,1,0,0,0,80,83,3,12,
        6,0,81,83,3,18,9,0,82,80,1,0,0,0,82,81,1,0,0,0,83,11,1,0,0,0,84,
        87,3,14,7,0,85,87,3,16,8,0,86,84,1,0,0,0,86,85,1,0,0,0,87,13,1,0,
        0,0,88,89,5,19,0,0,89,90,5,3,0,0,90,91,5,19,0,0,91,15,1,0,0,0,92,
        93,5,19,0,0,93,94,5,3,0,0,94,95,5,24,0,0,95,17,1,0,0,0,96,97,5,19,
        0,0,97,98,5,3,0,0,98,99,3,20,10,0,99,19,1,0,0,0,100,101,6,10,-1,
        0,101,102,5,8,0,0,102,103,3,20,10,0,103,104,5,9,0,0,104,108,1,0,
        0,0,105,108,5,24,0,0,106,108,5,19,0,0,107,100,1,0,0,0,107,105,1,
        0,0,0,107,106,1,0,0,0,108,117,1,0,0,0,109,110,10,5,0,0,110,111,7,
        0,0,0,111,116,3,20,10,6,112,113,10,4,0,0,113,114,7,1,0,0,114,116,
        3,20,10,5,115,109,1,0,0,0,115,112,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,21,1,0,0,0,119,117,1,0,0,0,120,124,5,
        10,0,0,121,123,8,2,0,0,122,121,1,0,0,0,123,126,1,0,0,0,124,122,1,
        0,0,0,124,125,1,0,0,0,125,23,1,0,0,0,126,124,1,0,0,0,127,128,5,11,
        0,0,128,25,1,0,0,0,129,133,3,28,14,0,130,133,3,30,15,0,131,133,3,
        40,20,0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,1,0,0,0,133,27,1,
        0,0,0,134,137,3,32,16,0,135,137,3,36,18,0,136,134,1,0,0,0,136,135,
        1,0,0,0,137,29,1,0,0,0,138,141,3,34,17,0,139,141,3,38,19,0,140,138,
        1,0,0,0,140,139,1,0,0,0,141,31,1,0,0,0,142,143,5,19,0,0,143,144,
        5,12,0,0,144,145,7,3,0,0,145,146,5,13,0,0,146,147,7,3,0,0,147,33,
        1,0,0,0,148,149,5,19,0,0,149,150,5,14,0,0,150,151,7,3,0,0,151,152,
        5,15,0,0,152,153,5,3,0,0,153,154,7,3,0,0,154,35,1,0,0,0,155,156,
        5,19,0,0,156,157,5,12,0,0,157,158,7,3,0,0,158,159,5,13,0,0,159,160,
        3,20,10,0,160,37,1,0,0,0,161,162,5,19,0,0,162,163,5,14,0,0,163,164,
        7,3,0,0,164,165,5,15,0,0,165,166,5,3,0,0,166,167,3,20,10,0,167,39,
        1,0,0,0,168,169,5,19,0,0,169,170,5,16,0,0,170,171,7,3,0,0,171,41,
        1,0,0,0,12,47,60,72,82,86,107,115,117,124,132,136,140
    ]

class BasicLangParser ( Parser ):

    grammarFileName = "BasicLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'exec'", "'import'", "'='", "'*'", "'/'", 
                     "'+'", "'-'", "'('", "')'", "'print'", "'exit'", "':'", 
                     "'<->'", "'['", "']'", "'+='", "'<#'", "'#>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BSTART", "BFIN", "ID", "DOT", "DASH", 
                      "CAPID", "ANY", "INT", "NL", "WS", "BRACES" ]

    RULE_script = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_exec = 3
    RULE_insert = 4
    RULE_equation = 5
    RULE_normal_equation = 6
    RULE_str_equation = 7
    RULE_num_equation = 8
    RULE_exp_equation = 9
    RULE_expr = 10
    RULE_show = 11
    RULE_quit = 12
    RULE_link = 13
    RULE_link_def = 14
    RULE_link_mod = 15
    RULE_link_def_n = 16
    RULE_link_mod_n = 17
    RULE_link_def_expr = 18
    RULE_link_mod_expr = 19
    RULE_link_app = 20

    ruleNames =  [ "script", "block", "statement", "exec", "insert", "equation", 
                   "normal_equation", "str_equation", "num_equation", "exp_equation", 
                   "expr", "show", "quit", "link", "link_def", "link_mod", 
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
    BSTART=17
    BFIN=18
    ID=19
    DOT=20
    DASH=21
    CAPID=22
    ANY=23
    INT=24
    NL=25
    WS=26
    BRACES=27

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
            self.state = 42
            self.block()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BasicLangParser.NL:
                self.state = 43
                self.match(BasicLangParser.NL)
                self.state = 44
                self.block()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
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
        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLangParser.NL)
            else:
                return self.getToken(BasicLangParser.NL, i)
        def BFIN(self):
            return self.getToken(BasicLangParser.BFIN, 0)
        def CAPID(self):
            return self.getToken(BasicLangParser.CAPID, 0)
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
            self.state = 52
            localctx.bid = self.match(BasicLangParser.CAPID)
            self.state = 53
            self.match(BasicLangParser.BSTART)
            self.state = 54
            self.match(BasicLangParser.NL)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.statement()
                self.state = 56
                self.match(BasicLangParser.NL)
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__0) | (1 << BasicLangParser.T__1) | (1 << BasicLangParser.T__7) | (1 << BasicLangParser.T__9) | (1 << BasicLangParser.T__10) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.INT))) != 0)):
                    break

            self.state = 62
            self.match(BasicLangParser.BFIN)
            self.state = 63
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
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.show()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.quit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.link()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.exec()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.insert()
                pass


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
            self.copyFrom(ctx)

        def CAPID(self):
            return self.getToken(BasicLangParser.CAPID, 0)

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
        self.enterRule(localctx, 6, self.RULE_exec)
        try:
            localctx = BasicLangParser.ExecBlockContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(BasicLangParser.T__0)
            self.state = 75
            localctx.blkid = self.match(BasicLangParser.CAPID)
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
        self.enterRule(localctx, 8, self.RULE_insert)
        try:
            localctx = BasicLangParser.InsertFileContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(BasicLangParser.T__1)
            self.state = 78
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
        self.enterRule(localctx, 10, self.RULE_equation)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.normal_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
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
        self.enterRule(localctx, 12, self.RULE_normal_equation)
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.str_equation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
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
        self.enterRule(localctx, 14, self.RULE_str_equation)
        try:
            localctx = BasicLangParser.StrEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 89
            self.match(BasicLangParser.T__2)
            self.state = 90
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
        self.enterRule(localctx, 16, self.RULE_num_equation)
        try:
            localctx = BasicLangParser.IntEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 93
            self.match(BasicLangParser.T__2)
            self.state = 94
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
        self.enterRule(localctx, 18, self.RULE_exp_equation)
        try:
            localctx = BasicLangParser.ExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            localctx.var = self.match(BasicLangParser.ID)
            self.state = 97
            self.match(BasicLangParser.T__2)
            self.state = 98
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BasicLangParser.T__7]:
                localctx = BasicLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 101
                self.match(BasicLangParser.T__7)
                self.state = 102
                self.expr(0)
                self.state = 103
                self.match(BasicLangParser.T__8)
                pass
            elif token in [BasicLangParser.INT]:
                localctx = BasicLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                localctx.atom = self.match(BasicLangParser.INT)
                pass
            elif token in [BasicLangParser.ID]:
                localctx = BasicLangParser.IDExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                localctx.atom = self.match(BasicLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 115
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 110
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__3 or _la==BasicLangParser.T__4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 111
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BasicLangParser.InfixExprContext(self, BasicLangParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 112
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 113
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==BasicLangParser.T__5 or _la==BasicLangParser.T__6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 114
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_show)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.ShowStrExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(BasicLangParser.T__9)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BasicLangParser.T__0) | (1 << BasicLangParser.T__1) | (1 << BasicLangParser.T__2) | (1 << BasicLangParser.T__3) | (1 << BasicLangParser.T__4) | (1 << BasicLangParser.T__5) | (1 << BasicLangParser.T__6) | (1 << BasicLangParser.T__7) | (1 << BasicLangParser.T__8) | (1 << BasicLangParser.T__9) | (1 << BasicLangParser.T__10) | (1 << BasicLangParser.T__11) | (1 << BasicLangParser.T__12) | (1 << BasicLangParser.T__13) | (1 << BasicLangParser.T__14) | (1 << BasicLangParser.T__15) | (1 << BasicLangParser.BSTART) | (1 << BasicLangParser.BFIN) | (1 << BasicLangParser.ID) | (1 << BasicLangParser.DOT) | (1 << BasicLangParser.DASH) | (1 << BasicLangParser.CAPID) | (1 << BasicLangParser.ANY) | (1 << BasicLangParser.INT) | (1 << BasicLangParser.WS) | (1 << BasicLangParser.BRACES))) != 0):
                self.state = 121
                localctx.text = self._input.LT(1)
                _la = self._input.LA(1)
                if _la <= 0 or _la==BasicLangParser.NL:
                    localctx.text = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 24, self.RULE_quit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(BasicLangParser.T__10)
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
        self.enterRule(localctx, 26, self.RULE_link)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.link_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.link_mod()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
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
        self.enterRule(localctx, 28, self.RULE_link_def)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.link_def_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
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
        self.enterRule(localctx, 30, self.RULE_link_mod)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                self.link_mod_n()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 139
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
        self.enterRule(localctx, 32, self.RULE_link_def_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 143
            self.match(BasicLangParser.T__11)
            self.state = 144
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 145
            self.match(BasicLangParser.T__12)
            self.state = 146
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
        self.enterRule(localctx, 34, self.RULE_link_mod_n)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 149
            self.match(BasicLangParser.T__13)
            self.state = 150
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.match(BasicLangParser.T__14)
            self.state = 152
            self.match(BasicLangParser.T__2)
            self.state = 153
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
        self.enterRule(localctx, 36, self.RULE_link_def_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkDefExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 156
            self.match(BasicLangParser.T__11)
            self.state = 157
            localctx.lid = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.lid = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 158
            self.match(BasicLangParser.T__12)
            self.state = 159
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
        self.enterRule(localctx, 38, self.RULE_link_mod_expr)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkModExprEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 162
            self.match(BasicLangParser.T__13)
            self.state = 163
            localctx.elem = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==BasicLangParser.ID or _la==BasicLangParser.INT):
                localctx.elem = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.match(BasicLangParser.T__14)
            self.state = 165
            self.match(BasicLangParser.T__2)
            self.state = 166
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
        self.enterRule(localctx, 40, self.RULE_link_app)
        self._la = 0 # Token type
        try:
            localctx = BasicLangParser.LinkAppEqnContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            localctx.name = self.match(BasicLangParser.ID)
            self.state = 169
            self.match(BasicLangParser.T__15)
            self.state = 170
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
        self._predicates[10] = self.expr_sempred
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
         




