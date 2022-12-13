CR = "char  '\r'"
LF = "char  '\n'"
SP = "char  ' '"
HT = "char  '\t'"
DQUOTE = "char  '\\"'"
ESCAPE = "char  '\\'"
def INIT_BITSET():
    '''    public static BitSet INIT_BITSET(final int... b)
    '''
def isWhitespace():
    '''    public static boolean isWhitespace(final char ch)
    '''
def parseToken():
    '''    public String parseToken(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters)
    '''
def parseValue():
    '''    public String parseValue(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters)
    '''
def skipWhiteSpace():
    '''    public void skipWhiteSpace(final CharArrayBuffer buf, final ParserCursor cursor)
    '''
def copyContent():
    '''    public void copyContent(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters, final StringBuilder dst)
    '''
def copyUnquotedContent():
    '''    public void copyUnquotedContent(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters, final StringBuilder dst)
    '''
def copyQuotedContent():
    '''    public void copyQuotedContent(final CharArrayBuffer buf, final ParserCursor cursor, final StringBuilder dst)
    '''
