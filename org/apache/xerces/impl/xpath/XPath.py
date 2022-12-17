EXPRTOKEN_OPEN_PAREN = "int  0"
EXPRTOKEN_CLOSE_PAREN = "int  1"
EXPRTOKEN_OPEN_BRACKET = "int  2"
EXPRTOKEN_CLOSE_BRACKET = "int  3"
EXPRTOKEN_PERIOD = "int  4"
EXPRTOKEN_DOUBLE_PERIOD = "int  5"
EXPRTOKEN_ATSIGN = "int  6"
EXPRTOKEN_COMMA = "int  7"
EXPRTOKEN_DOUBLE_COLON = "int  8"
EXPRTOKEN_NAMETEST_ANY = "int  9"
EXPRTOKEN_NAMETEST_NAMESPACE = "int  10"
EXPRTOKEN_NAMETEST_QNAME = "int  11"
EXPRTOKEN_NODETYPE_COMMENT = "int  12"
EXPRTOKEN_NODETYPE_TEXT = "int  13"
EXPRTOKEN_NODETYPE_PI = "int  14"
EXPRTOKEN_NODETYPE_NODE = "int  15"
EXPRTOKEN_OPERATOR_AND = "int  16"
EXPRTOKEN_OPERATOR_OR = "int  17"
EXPRTOKEN_OPERATOR_MOD = "int  18"
EXPRTOKEN_OPERATOR_DIV = "int  19"
EXPRTOKEN_OPERATOR_MULT = "int  20"
EXPRTOKEN_OPERATOR_SLASH = "int  21"
EXPRTOKEN_OPERATOR_DOUBLE_SLASH = "int  22"
EXPRTOKEN_OPERATOR_UNION = "int  23"
EXPRTOKEN_OPERATOR_PLUS = "int  24"
EXPRTOKEN_OPERATOR_MINUS = "int  25"
EXPRTOKEN_OPERATOR_EQUAL = "int  26"
EXPRTOKEN_OPERATOR_NOT_EQUAL = "int  27"
EXPRTOKEN_OPERATOR_LESS = "int  28"
EXPRTOKEN_OPERATOR_LESS_EQUAL = "int  29"
EXPRTOKEN_OPERATOR_GREATER = "int  30"
EXPRTOKEN_OPERATOR_GREATER_EQUAL = "int  31"
EXPRTOKEN_FUNCTION_NAME = "int  32"
EXPRTOKEN_AXISNAME_ANCESTOR = "int  33"
EXPRTOKEN_AXISNAME_ANCESTOR_OR_SELF = "int  34"
EXPRTOKEN_AXISNAME_ATTRIBUTE = "int  35"
EXPRTOKEN_AXISNAME_CHILD = "int  36"
EXPRTOKEN_AXISNAME_DESCENDANT = "int  37"
EXPRTOKEN_AXISNAME_DESCENDANT_OR_SELF = "int  38"
EXPRTOKEN_AXISNAME_FOLLOWING = "int  39"
EXPRTOKEN_AXISNAME_FOLLOWING_SIBLING = "int  40"
EXPRTOKEN_AXISNAME_NAMESPACE = "int  41"
EXPRTOKEN_AXISNAME_PARENT = "int  42"
EXPRTOKEN_AXISNAME_PRECEDING = "int  43"
EXPRTOKEN_AXISNAME_PRECEDING_SIBLING = "int  44"
EXPRTOKEN_AXISNAME_SELF = "int  45"
EXPRTOKEN_LITERAL = "int  46"
EXPRTOKEN_NUMBER = "int  47"
EXPRTOKEN_VARIABLE_REFERENCE = "int  48"
QNAME = "short  1"
WILDCARD = "short  2"
NODE = "short  3"
NAMESPACE = "short  4"
CHILD = "short  1"
ATTRIBUTE = "short  2"
SELF = "short  3"
DESCENDANT = "short  4"
def ():
    '''returns LocationPath\n\n
    (final String fExpression, final SymbolTable fSymbolTable, final NamespaceContext namespaceContext)\n
    (final SymbolTable fSymbolTable)\n
    (final SymbolTable fSymbolTable)\n
    (final short type)\n
    (final QName values)\n
    (final String s, final String s2)\n
    (final NodeTest nodeTest)\n
    (final short type)\n
    (final Axis axis, final NodeTest nodeTest)\n
    (final Step[] steps)\n
    '''
def getLocationPaths():
    '''returns LocationPath[]\n\n
    getLocationPaths()\n
    '''
def getLocationPath():
    '''returns LocationPath\n\n
    getLocationPath()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def scanExpr():
    '''returns boolean\n\n
    scanExpr(final SymbolTable symbolTable, final Tokens tokens, final String s, int i, final int n)\n
    '''
def getTokenString():
    '''returns String\n\n
    getTokenString(final int value)\n
    '''
def addToken():
    '''returns None\n\n
    addToken(final String s)\n
    addToken(final int n)\n
    '''
def rewind():
    '''returns None\n\n
    rewind()\n
    '''
def hasMore():
    '''returns boolean\n\n
    hasMore()\n
    '''
def nextToken():
    '''returns int\n\n
    nextToken()\n
    '''
def peekToken():
    '''returns int\n\n
    peekToken()\n
    '''
def nextTokenAsString():
    '''returns String\n\n
    nextTokenAsString()\n
    '''
def dumpTokens():
    '''returns None\n\n
    dumpTokens()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    clone()\n
    clone()\n
    clone()\n
    '''
