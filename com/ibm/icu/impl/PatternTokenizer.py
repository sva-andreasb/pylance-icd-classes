SINGLE_QUOTE = "char  '\''"
BACK_SLASH = "char  '\\'"
DONE = "int  0"
SYNTAX = "int  1"
LITERAL = "int  2"
BROKEN_QUOTE = "int  3"
BROKEN_ESCAPE = "int  4"
UNKNOWN = "int  5"
def PatternTokenizer():
    '''public PatternTokenizer()
    '''
def getIgnorableCharacters():
    '''public UnicodeSet getIgnorableCharacters()
    '''
def setIgnorableCharacters():
    '''public PatternTokenizer setIgnorableCharacters(final UnicodeSet ignorableCharacters)
    '''
def getSyntaxCharacters():
    '''public UnicodeSet getSyntaxCharacters()
    '''
def getExtraQuotingCharacters():
    '''public UnicodeSet getExtraQuotingCharacters()
    '''
def setSyntaxCharacters():
    '''public PatternTokenizer setSyntaxCharacters(final UnicodeSet syntaxCharacters)
    '''
def setExtraQuotingCharacters():
    '''public PatternTokenizer setExtraQuotingCharacters(final UnicodeSet syntaxCharacters)
    '''
def getEscapeCharacters():
    '''public UnicodeSet getEscapeCharacters()
    '''
def setEscapeCharacters():
    '''public PatternTokenizer setEscapeCharacters(final UnicodeSet escapeCharacters)
    '''
def isUsingQuote():
    '''public boolean isUsingQuote()
    '''
def setUsingQuote():
    '''public PatternTokenizer setUsingQuote(final boolean usingQuote)
    '''
def isUsingSlash():
    '''public boolean isUsingSlash()
    '''
def setUsingSlash():
    '''public PatternTokenizer setUsingSlash(final boolean usingSlash)
    '''
def getLimit():
    '''public int getLimit()
    '''
def setLimit():
    '''public PatternTokenizer setLimit(final int limit)
    '''
def getStart():
    '''public int getStart()
    '''
def setStart():
    '''public PatternTokenizer setStart(final int start)
    '''
def setPattern():
    '''public PatternTokenizer setPattern(final CharSequence pattern)
    public PatternTokenizer setPattern(final String pattern)
    '''
def quoteLiteral():
    '''public String quoteLiteral(final CharSequence string)
    public String quoteLiteral(final String string)
    '''
def normalize():
    '''public String normalize()
    '''
def next():
    '''public int next(final StringBuffer buffer)
    '''
