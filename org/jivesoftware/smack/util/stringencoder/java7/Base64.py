NO_OPTIONS = "int  0"
ENCODE = "int  1"
DECODE = "int  0"
GZIP = "int  2"
DONT_BREAK_LINES = "int  8"
URL_SAFE = "int  16"
ORDERED = "int  32"
def encodeObject():
    '''    public static String encodeObject(final Serializable serializableObject)
    public static String encodeObject(final Serializable serializableObject, final int options)
    '''
def encodeBytes():
    '''    public static String encodeBytes(final byte[] source)
    public static String encodeBytes(final byte[] source, final int options)
    public static String encodeBytes(final byte[] source, final int off, final int len)
    public static String encodeBytes(final byte[] source, final int off, final int len, final int options)
    '''
def decode():
    '''    public static byte[] decode(final byte[] source, final int off, final int len, final int options)
    public static byte[] decode(final String s)
    public static byte[] decode(final String s, final int options)
    '''
def decodeToObject():
    '''    public static Object decodeToObject(final String encodedObject)
    '''
def encodeToFile():
    '''    public static boolean encodeToFile(final byte[] dataToEncode, final String filename)
    '''
def decodeToFile():
    '''    public static boolean decodeToFile(final String dataToDecode, final String filename)
    '''
def decodeFromFile():
    '''    public static byte[] decodeFromFile(final String filename)
    '''
def encodeFromFile():
    '''    public static String encodeFromFile(final String filename)
    '''
def encodeFileToFile():
    '''    public static void encodeFileToFile(final String infile, final String outfile)
    '''
def decodeFileToFile():
    '''    public static void decodeFileToFile(final String infile, final String outfile)
    '''
def InputStream():
    '''    public InputStream(final java.io.InputStream in)
    public InputStream(final java.io.InputStream in, final int options)
    '''
def read():
    '''    public int read()
    public int read(final byte[] dest, final int off, final int len)
    '''
def OutputStream():
    '''    public OutputStream(final java.io.OutputStream out)
    public OutputStream(final java.io.OutputStream out, final int options)
    '''
def write():
    '''    public void write(final int theByte)
    public void write(final byte[] theBytes, final int off, final int len)
    '''
def flushBase64():
    '''    public void flushBase64()
    '''
def close():
    '''    public void close()
    '''
def suspendEncoding():
    '''    public void suspendEncoding()
    '''
def resumeEncoding():
    '''    public void resumeEncoding()
    '''
