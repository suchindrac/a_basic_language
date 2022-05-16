grammar BasicLang; 

script: block (NL block)* EOF # ExecScript ; 
block: bid=CAPID BSTART NL? (statement NL?)+ BFIN NL? # Blk ;

statement: equation 
           | expr 
           | show 
           | quit
           | link 
           | exec 
           | insert
           | setres
           | ifblock ;

ifblock: cond=CAPID act=CAPID # ifBlock ;
setres: 'setres' varint=INT? varid=ID? # setResult ;
exec: 'exec' blkid=CAPID COMMA? times=INT? # ExecBlock ; 
insert: 'import' fname=ID # InsertFile ;
equation: normal_equation | exp_equation ;
normal_equation: str_equation | num_equation ;
str_equation: var=ID  '='  value=ID # StrEqn ;
num_equation: var=ID  '='  value=INT # IntEqn ;
exp_equation: var=ID  '='  value=expr # ExprEqn ;


expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | '(' expr ')'                             # ParenExpr
    | atom=INT                                 # NumberExpr
    | atom=ID                                  # IDExpr
    ;

show: 'print' text=~NL* # ShowStrExpr ;

quit: 'exit' ;

link: link_def | link_mod | link_app;
link_def: link_def_n | link_def_expr;
link_mod: link_mod_n | link_mod_expr;
link_def_n: name=ID ':'  lid=(ID | INT)  '<->'  rid=(ID | INT) # LinkDefEqn ;
link_mod_n: name=ID '[' elem=(ID | INT) ']'  '='  value=(ID | INT) # LinkModEqn ;
link_def_expr: name=ID ':'  lid=(ID | INT)  '<->'  rid=expr # LinkDefExprEqn ;
link_mod_expr: name=ID '[' elem=(ID | INT) ']'  '='  value=expr # LinkModExprEqn ;
link_app: name=ID  '+='  value=(ID | INT) # LinkAppEqn ;

BSTART: '<#' ;
BFIN: '#>' ;
ID : [a-z]+ ; 
DOT : [.]+ ;
DASH : [-_]+ ;
CAPID: [A-Z]+ ;
COMMA: ',' ;
ANY: (ID | DOT | DASH) ;
INT: [0-9]+ ;
NL : '\r'? '\n' ;
WS : [ \t]+ -> skip;
BRACES: [{}]+ ;
