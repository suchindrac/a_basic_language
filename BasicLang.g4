grammar BasicLang; 

statement: equation 
           | expr 
           | show 
           | quit
           | link ;

equation: normal_equation | exp_equation ;
normal_equation: str_equation | num_equation ;
str_equation: var=ID '=' value=ID # StrEqn ;
num_equation: var=ID '=' value=INT # IntEqn ;
exp_equation: var=ID '=' value=expr # ExprEqn ;

expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | '(' expr ')'                             # ParenExpr
    | atom=INT                                 # NumberExpr
    | atom=ID                                  # IDExpr
    ;

show: 'print' text=~EOF* EOF # ShowStrExpr ;

quit: 'exit' ;

link: link_def;
link_def: name=ID ':' lid=(ID | INT) '<->' rid=(ID | INT) # LinkDefEqn ;

ID : [a-z]+ ; 
CAPID: [A-Z]+ ;
ANY: (ID | CAPID) ;
INT: [0-9]+ ;
NL : [\r\n]+ ;
WS : [ \t]+ -> skip ;
VALUE_OF_VAR: '{' ID '}' ;
VALUE_OF_LINK: ID '[' (ID | INT) ']' ;