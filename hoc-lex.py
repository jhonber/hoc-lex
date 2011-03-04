#  This Python file uses the following encoding: utf-8
#  ---------------------------------------------------------------
#  hoc-lex.py
#
#  Jhon Jimenez
#  Lexical Analyzer
#  --------------------

import sys
import ply.lex as lex

reserved = (
	'CATALAN','DEG','E','GAMMA','INF','INFINITY','MAXNORMAL',
	'MINNORMAL','MINSUBNORMAL','MINSUBNORMAL','PHI','PI','PREC',
	'QNAN','SNAN','__BANNER__','__DATE__','__FILE__','__IEEE_754__',
	'__LINENO__','__PACKAGE_BUGREPORT__','__PACKAGE_DATE__',
	'__PACKAGE_NAME__','__PACKAGE_STRING__','__PACKAGE_VERSION__',
	'__PROMPT__','__VERBOSE__','PRINT','PRINTLN'
	"SIN","COS","TAN","ATAN","ASIN","ACOS","SINH","COSH","TANH",
	"LOG","LOG10","EXP","SQRT","INT","ABS",
	'PROC','FUNC','RETURNIF','WHILE','FOR',
)

reserved_map = { }
for r in reserved:
	reserved_map[r] = r

tokens = reserved + (
	'COMMA','LPAREN','RPAREN','LBRACKET','RBRACKET','LBRACE','RBRACE','ASSIGN','GREATER','LESS',
	'EQ','NOT_EQ','GREATER_EQ','LESS_EQ','PLUS','MINUS','DIV','ELSE','IF','ELSE IF','ID','NUMI','NUMF',"STRING",
)










