SEPARATORS = "String  \" ;,:@()<>\\\\"/[]?={}\t\""
UNSAFE_CHARS = "String  \"\\"\\\""
def formatElements():
    '''public static String formatElements(final HeaderElement[] elems, final boolean quote, final HeaderValueFormatter formatter)
    public CharArrayBuffer formatElements(final CharArrayBuffer charBuffer, final HeaderElement[] elems, final boolean quote)
    '''
def formatHeaderElement():
    '''public static String formatHeaderElement(final HeaderElement elem, final boolean quote, final HeaderValueFormatter formatter)
    public CharArrayBuffer formatHeaderElement(final CharArrayBuffer charBuffer, final HeaderElement elem, final boolean quote)
    '''
def formatParameters():
    '''public static String formatParameters(final NameValuePair[] nvps, final boolean quote, final HeaderValueFormatter formatter)
    public CharArrayBuffer formatParameters(final CharArrayBuffer charBuffer, final NameValuePair[] nvps, final boolean quote)
    '''
def formatNameValuePair():
    '''public static String formatNameValuePair(final NameValuePair nvp, final boolean quote, final HeaderValueFormatter formatter)
    public CharArrayBuffer formatNameValuePair(final CharArrayBuffer charBuffer, final NameValuePair nvp, final boolean quote)
    '''
