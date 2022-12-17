CR = "char  '\r'"
LF = "char  '\n'"
SP = "char  ' '"
HT = "char  '\t'"
DQUOTE = "char  '\\"'"
ESCAPE = "char  '\\'"
def parseToken():
    '''returns String\n\n
    parseToken(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters)\n
    '''
def parseValue():
    '''returns String\n\n
    parseValue(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters)\n
    '''
def skipWhiteSpace():
    '''returns None\n\n
    skipWhiteSpace(final CharArrayBuffer buf, final ParserCursor cursor)\n
    '''
def copyContent():
    '''returns None\n\n
    copyContent(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters, final StringBuilder dst)\n
    '''
def copyUnquotedContent():
    '''returns None\n\n
    copyUnquotedContent(final CharArrayBuffer buf, final ParserCursor cursor, final BitSet delimiters, final StringBuilder dst)\n
    '''
def copyQuotedContent():
    '''returns None\n\n
    copyQuotedContent(final CharArrayBuffer buf, final ParserCursor cursor, final StringBuilder dst)\n
    '''
