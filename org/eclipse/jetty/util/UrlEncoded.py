def UrlEncoded():
    '''    public UrlEncoded(final UrlEncoded url)
    public UrlEncoded()
    public UrlEncoded(final String s)
    public UrlEncoded(final String s, final String charset)
    '''
def decode():
    '''    public void decode(final String query)
    public void decode(final String query, final String charset)
    '''
def encode():
    '''    public String encode()
    public String encode(final String charset)
    public synchronized String encode(final String charset, final boolean equalsForNullValue)
    public static String encode(final MultiMap map, String charset, final boolean equalsForNullValue)
    '''
def decodeTo():
    '''    public static void decodeTo(final String content, final MultiMap map, final String charset)
    public static void decodeTo(final String content, final MultiMap map, String charset, final int maxKeys)
    public static void decodeTo(final InputStream in, final MultiMap map, String charset, final int maxLength, final int maxKeys)
    '''
def decodeUtf8To():
    '''    public static void decodeUtf8To(final byte[] raw, final int offset, final int length, final MultiMap map)
    public static void decodeUtf8To(final byte[] raw, final int offset, final int length, final MultiMap map, final Utf8StringBuilder buffer)
    public static void decodeUtf8To(final InputStream in, final MultiMap map, final int maxLength, final int maxKeys)
    '''
def decode88591To():
    '''    public static void decode88591To(final InputStream in, final MultiMap map, final int maxLength, final int maxKeys)
    '''
def decodeUtf16To():
    '''    public static void decodeUtf16To(final InputStream in, final MultiMap map, final int maxLength, final int maxKeys)
    '''
def decodeString():
    '''    public static String decodeString(final String encoded, final int offset, final int length, final String charset)
    '''
def encodeString():
    '''    public static String encodeString(final String string)
    public static String encodeString(final String string, String charset)
    '''
def clone():
    '''    public Object clone()
    '''
