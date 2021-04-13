%{
#include "parser.tab.h"
#include "storetokens.hh"
int lineno = 1;

%}

digit [0-9]
integer int
fl float
void void
return return
float (({digit}+\.{digit}*)|({digit}*[.]{digit}+))
letter [a-zA-Z_]
string [0-9a-zA-Z_]+
operator [-+*/]
line [\n]
assignop [=]
metachar [(){},;]
tab [\t]
whitespace [ ]
comments_multiline \/[*][{operator}{string}{line}{tab}]*[*]\/
comments_single \/[\/]+.*

%%
{line}    {lineno++;} 
{whitespace} {;}
{tab} {;}
{comments_single} {;}
{integer}    {store_token_name("INTEGER",yytext,lineno);return INTEGER;}
{fl}    {store_token_name("FLOAT",yytext,lineno);return FLOAT;} 
{void}    {store_token_name("VOID",yytext,lineno);return VOID;} 
{metachar} {store_token_name("META CHAR",yytext,lineno);return (int) yytext[0];}
{digit}+    {store_token_name("NUM",yytext,lineno);yylval.integer_value = atoi(yytext);return INTEGER_NUMBER;   }
{string}    {store_token_name("NAME",yytext,lineno);yylval.string_value = new std::string(yytext);return NAME;}
{float}    {store_token_name("FNUM",yytext,lineno);yylval.double_value = atof(yytext);return DOUBLE_NUMBER;}
{operator}  {store_token_name("ARITHOP",yytext,lineno);return (int) yytext[0];}
{assignop}  {store_token_name("ASSIGN_OP",yytext,lineno);return ASSIGN;}
. {printf("error: didn't match with defined regular expressions\n");}





