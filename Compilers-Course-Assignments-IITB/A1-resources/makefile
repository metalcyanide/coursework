res: lex.yy.c
	g++ lex.yy.c -include allheaders.h -L. -Wl,-rpath=.  -o res -lsclpshared -lfl -ly 
lex.yy.c: scanner.l 
	lex scanner.l
