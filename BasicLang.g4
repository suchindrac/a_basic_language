grammar BasicLang; 

script: block (NL block)* EOF # ExecScript ; 
block: bid=ID BSTART NL? (statement NL?)+ BFIN NL? # Blk ;

statement: equation 
           | expr 
           | show
           | quit
           | link 
           | exec 
           | insert
           | setres
           | getres
           | ifblock
           | ifcond
           | block ;

setres: 'setres' varint=INT? varid=ID? # setResult ;
getres: var=ID '=' 'getres' # getResult ;
exec: 'exec' blkid=ID COMMA? times=INT? times='max'? times=ID? # ExecBlock ; 
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

cond: left=(ID|INT) op=('eq' | 'gt' | 'lt' | 'ge' | 'le') right=(ID|INT) # CondExpr 
    | '(' cond ')'                                                       # CondParenExpr
    | atom=INT                                                           # NumberCondExpr
    | atom=ID                                                            # IDCondExpr
    ;                                      

ifblock: ifblk=ID op='?' acttrueid=ID? acttrueeqn=equation? acttrueval='none'? sep=':' actfalseid=ID? actfalseval='none'? actfalseeqn=equation? # ifBlock ;
ifcond: leftcond=cond op='?' iftrueid=ID? iftrueeqn=equation? iftrueval='none'? sep=':' iffalseid=ID? iffalseval='none'? iffalseeqn=equation? # ifCondition ;

      
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
ID : [a-zA-Z.]+ ; 
DOT : [.]+ ;
DASH : [-_]+ ;
COMMA: ',' ;
ANY: (ID | DOT | DASH) ;
INT: [0-9]+ ;
NL : '\r'? '\n' ;
WS : [ \t]+ -> skip;
BRACES: [{}]+ ;
