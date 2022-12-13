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
pass
def getIgnorableCharacters():
'''public UnicodeSet getIgnorableCharacters()
'''
pass
def setIgnorableCharacters():
'''public PatternTokenizer setIgnorableCharacters(final UnicodeSet ignorableCharacters)
'''
pass
def getSyntaxCharacters():
'''public UnicodeSet getSyntaxCharacters()
'''
pass
def getExtraQuotingCharacters():
'''public UnicodeSet getExtraQuotingCharacters()
'''
pass
def setSyntaxCharacters():
'''public PatternTokenizer setSyntaxCharacters(final UnicodeSet syntaxCharacters)
'''
pass
def setExtraQuotingCharacters():
'''public PatternTokenizer setExtraQuotingCharacters(final UnicodeSet syntaxCharacters)
'''
pass
def getEscapeCharacters():
'''public UnicodeSet getEscapeCharacters()
'''
pass
def setEscapeCharacters():
'''public PatternTokenizer setEscapeCharacters(final UnicodeSet escapeCharacters)
'''
pass
def isUsingQuote():
'''public boolean isUsingQuote()
'''
pass
def setUsingQuote():
'''public PatternTokenizer setUsingQuote(final boolean usingQuote)
'''
pass
def isUsingSlash():
'''public boolean isUsingSlash()
'''
pass
def setUsingSlash():
'''public PatternTokenizer setUsingSlash(final boolean usingSlash)
'''
pass
def getLimit():
'''public int getLimit()
'''
pass
def setLimit():
'''public PatternTokenizer setLimit(final int limit)
'''
pass
def getStart():
'''public int getStart()
'''
pass
def setStart():
'''public PatternTokenizer setStart(final int start)
'''
pass
def setPattern():
'''public PatternTokenizer setPattern(final CharSequence pattern)
public PatternTokenizer setPattern(final String pattern)
'''
pass
def quoteLiteral():
'''public String quoteLiteral(final CharSequence string)
public String quoteLiteral(final String string)
'''
pass
def normalize():
'''public String normalize()
'''
pass
def next():
'''public int next(final StringBuffer buffer)
'''
pass
