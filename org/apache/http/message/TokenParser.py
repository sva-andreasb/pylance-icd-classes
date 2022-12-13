CR = "char  '\r'"
LF = "char  '\n'"
SP = "char  ' '"
HT = "char  '\t'"
DQUOTE = "char  '\"'"
ESCAPE = "char  '\\'"
def INIT_BITSET():
'''public static BitSet INIT_BITSET(final int... b)
'''
pass
def isWhitespace():
'''public static boolean isWhitespace(final char ch)
'''
pass
def parseToken():
'''public String parseToken(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters)
'''
pass
def parseValue():
'''public String parseValue(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters)
'''
pass
def skipWhiteSpace():
'''public void skipWhiteSpace(final CharArrayBuffer buf, final ParserCursor cursor)
'''
pass
def copyContent():
'''public void copyContent(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters, final StringBuilder dst)
'''
pass
def copyUnquotedContent():
'''public void copyUnquotedContent(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters, final StringBuilder dst)
'''
pass
def copyQuotedContent():
'''public void copyQuotedContent(final CharArrayBuffer buf, final ParserCursor cursor, final StringBuilder dst)
'''
pass
