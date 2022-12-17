SEPARATORS = "String  \" ;,:@()<>\\\\"/[]?={}\t\""
UNSAFE_CHARS = "String  \"\\"\\\""
def formatElements():
    '''returns CharArrayBuffer\n\n
    formatElements(final CharArrayBuffer charBuffer, final HeaderElement[] elems, final boolean quote)\n
    '''
def formatHeaderElement():
    '''returns CharArrayBuffer\n\n
    formatHeaderElement(final CharArrayBuffer charBuffer, final HeaderElement elem, final boolean quote)\n
    '''
def formatParameters():
    '''returns CharArrayBuffer\n\n
    formatParameters(final CharArrayBuffer charBuffer, final NameValuePair[] nvps, final boolean quote)\n
    '''
def formatNameValuePair():
    '''returns CharArrayBuffer\n\n
    formatNameValuePair(final CharArrayBuffer charBuffer, final NameValuePair nvp, final boolean quote)\n
    '''
