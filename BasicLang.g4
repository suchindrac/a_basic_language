grammar BasicLang; 

statement: equation 
           | expr 
           | show 
           | quit
           | link ;

link: link_def | link_acc ;
link_def: name=ID ':' lid=(ID | INT) '<->' rid=(ID | INT) # LinkDefEqn ;
link_acc: name=ID '[' what=(ID | INT) ']' # LinkAccEqn ;
equation: normal_equation | exp_equation ;
normal_equation: var=ID '=' value=INT # Eqn ;
exp_equation: var=ID '=' value=expr # ExprEqn ;
expr: left=expr op=('*'|'/') right=expr        # InfixExpr
    | left=expr op=('+'|'-') right=expr        # InfixExpr
    | atom=INT                                 # NumberExpr
    | '(' expr ')'                             # ParenExpr
    | atom=ID                                  # IDExpr
    ;
show: 'print' (ID | INT)  # showIDExpr
    | 'print' name=ID '[' what=(ID | INT) ']' # showLinkExpr ;
quit: 'exit' ;

ID : [a-z]+ ; // match lower-case identifiers
INT: [0-9]+ ; // match integers
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
