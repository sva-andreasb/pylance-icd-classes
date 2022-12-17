TT_EOF = "int  -1"
TT_EOL = "int  10"
TT_NUMBER = "int  -2"
TT_WORD = "int  -3"
def ():
    '''returns IlvStreamTokenizer\n\n
    ()\n
    (final InputStream inStream)\n
    (final Reader inReader)\n
    '''
def commentChar():
    '''returns None\n\n
    commentChar(final int n)\n
    '''
def eolIsSignificant():
    '''returns None\n\n
    eolIsSignificant(final boolean isEOLSignificant)\n
    '''
def lineno():
    '''returns int\n\n
    lineno()\n
    '''
def lowerCaseMode():
    '''returns None\n\n
    lowerCaseMode(final boolean forceLowercase)\n
    '''
def nextToken():
    '''returns int\n\n
    nextToken()\n
    '''
def ordinaryChar():
    '''returns None\n\n
    ordinaryChar(final int n)\n
    '''
def ordinaryChars():
    '''returns None\n\n
    ordinaryChars(int n, int n2)\n
    '''
def parseNumbers():
    '''returns None\n\n
    parseNumbers()\n
    '''
def pushBack():
    '''returns None\n\n
    pushBack()\n
    '''
def quoteChar():
    '''returns None\n\n
    quoteChar(final int n)\n
    '''
def resetSyntax():
    '''returns None\n\n
    resetSyntax()\n
    '''
def slashSlashComments():
    '''returns None\n\n
    slashSlashComments(final boolean slashSlashComments)\n
    '''
def slashStarComments():
    '''returns None\n\n
    slashStarComments(final boolean slashStarComments)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def whitespaceChars():
    '''returns None\n\n
    whitespaceChars(int n, int n2)\n
    '''
def wordChars():
    '''returns None\n\n
    wordChars(int n, int n2)\n
    '''
