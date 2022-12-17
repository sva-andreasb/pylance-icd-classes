SINGLE_QUOTE = "char  '\''"
BACK_SLASH = "char  '\\'"
DONE = "int  0"
SYNTAX = "int  1"
LITERAL = "int  2"
BROKEN_QUOTE = "int  3"
BROKEN_ESCAPE = "int  4"
UNKNOWN = "int  5"
def ():
    '''returns PatternTokenizer\n\n
    ()\n
    '''
def getIgnorableCharacters():
    '''returns UnicodeSet\n\n
    getIgnorableCharacters()\n
    '''
def setIgnorableCharacters():
    '''returns PatternTokenizer\n\n
    setIgnorableCharacters(final UnicodeSet ignorableCharacters)\n
    '''
def getSyntaxCharacters():
    '''returns UnicodeSet\n\n
    getSyntaxCharacters()\n
    '''
def getExtraQuotingCharacters():
    '''returns UnicodeSet\n\n
    getExtraQuotingCharacters()\n
    '''
def setSyntaxCharacters():
    '''returns PatternTokenizer\n\n
    setSyntaxCharacters(final UnicodeSet syntaxCharacters)\n
    '''
def setExtraQuotingCharacters():
    '''returns PatternTokenizer\n\n
    setExtraQuotingCharacters(final UnicodeSet syntaxCharacters)\n
    '''
def getEscapeCharacters():
    '''returns UnicodeSet\n\n
    getEscapeCharacters()\n
    '''
def setEscapeCharacters():
    '''returns PatternTokenizer\n\n
    setEscapeCharacters(final UnicodeSet escapeCharacters)\n
    '''
def isUsingQuote():
    '''returns boolean\n\n
    isUsingQuote()\n
    '''
def setUsingQuote():
    '''returns PatternTokenizer\n\n
    setUsingQuote(final boolean usingQuote)\n
    '''
def isUsingSlash():
    '''returns boolean\n\n
    isUsingSlash()\n
    '''
def setUsingSlash():
    '''returns PatternTokenizer\n\n
    setUsingSlash(final boolean usingSlash)\n
    '''
def getLimit():
    '''returns int\n\n
    getLimit()\n
    '''
def setLimit():
    '''returns PatternTokenizer\n\n
    setLimit(final int limit)\n
    '''
def getStart():
    '''returns int\n\n
    getStart()\n
    '''
def setStart():
    '''returns PatternTokenizer\n\n
    setStart(final int start)\n
    '''
def setPattern():
    '''returns PatternTokenizer\n\n
    setPattern(final CharSequence pattern)\n
    setPattern(final String pattern)\n
    '''
def quoteLiteral():
    '''returns String\n\n
    quoteLiteral(final CharSequence string)\n
    quoteLiteral(final String string)\n
    '''
def normalize():
    '''returns String\n\n
    normalize()\n
    '''
def next():
    '''returns int\n\n
    next(final StringBuffer buffer)\n
    '''
