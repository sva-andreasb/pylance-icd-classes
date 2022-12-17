DONE = "int  -1"
PARSE_VARIABLES = "int  1"
PARSE_ESCAPES = "int  2"
SKIP_WHITESPACE = "int  4"
def ():
    '''returns RuleCharacterIterator\n\n
    (final String text, final SymbolTable sym, final ParsePosition pos)\n
    '''
def atEnd():
    '''returns boolean\n\n
    atEnd()\n
    '''
def next():
    '''returns int\n\n
    next(final int options)\n
    '''
def isEscaped():
    '''returns boolean\n\n
    isEscaped()\n
    '''
def inVariable():
    '''returns boolean\n\n
    inVariable()\n
    '''
def getPos():
    '''returns Object\n\n
    getPos(final Object p)\n
    '''
def setPos():
    '''returns None\n\n
    setPos(final Object p)\n
    '''
def skipIgnored():
    '''returns None\n\n
    skipIgnored(final int options)\n
    '''
def lookahead():
    '''returns String\n\n
    lookahead()\n
    '''
def jumpahead():
    '''returns None\n\n
    jumpahead(final int count)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
