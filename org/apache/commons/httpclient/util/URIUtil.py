def getName():
    '''    public static String getName(final String uri)
    '''
def getQuery():
    '''    public static String getQuery(final String uri)
    '''
def getPath():
    '''    public static String getPath(final String uri)
    '''
def getPathQuery():
    '''    public static String getPathQuery(final String uri)
    '''
def getFromPath():
    '''    public static String getFromPath(final String uri)
    '''
def encodeAll():
    '''    public static String encodeAll(final String unescaped)
    public static String encodeAll(final String unescaped, final String charset)
    '''
def encodeWithinAuthority():
    '''    public static String encodeWithinAuthority(final String unescaped)
    public static String encodeWithinAuthority(final String unescaped, final String charset)
    '''
def encodePathQuery():
    '''    public static String encodePathQuery(final String unescaped)
    public static String encodePathQuery(final String unescaped, final String charset)
    '''
def encodeWithinPath():
    '''    public static String encodeWithinPath(final String unescaped)
    public static String encodeWithinPath(final String unescaped, final String charset)
    '''
def encodePath():
    '''    public static String encodePath(final String unescaped)
    public static String encodePath(final String unescaped, final String charset)
    '''
def encodeWithinQuery():
    '''    public static String encodeWithinQuery(final String unescaped)
    public static String encodeWithinQuery(final String unescaped, final String charset)
    '''
def encodeQuery():
    '''    public static String encodeQuery(final String unescaped)
    public static String encodeQuery(final String unescaped, final String charset)
    '''
def encode():
    '''    public static String encode(final String unescaped, final BitSet allowed)
    public static String encode(final String unescaped, final BitSet allowed, final String charset)
    public static char[] encode(final String unescapedComponent, final BitSet allowed, final String charset)
    '''
def decode():
    '''    public static String decode(final String escaped)
    public static String decode(final String escaped, final String charset)
    public static String decode(final char[] escapedComponent, final String charset)
    '''
def verifyEscaped():
    '''    public static boolean verifyEscaped(final char[] original)
    '''
def replace():
    '''    public static String replace(String original, final char[] from, final char[] to)
    public static String replace(final String original, final char from, final char to)
    '''
