DEFAULT_VERSION = "int  1"
MINIMUM_COMPATIBLE_VERSION = "int  1"
def getMagicHeader():
    '''public static byte[] getMagicHeader()
    '''
def toString():
    '''public String toString()
    '''
def headerSize():
    '''public static int headerSize()
    '''
def writeHeader():
    '''public int writeHeader(final byte[] array, final int n)
    public int writeHeader(final OutputStream outputStream)
    '''
def isValidMagicHeader():
    '''public boolean isValidMagicHeader()
    '''
def hasMagicHeaderPrefix():
    '''public static boolean hasMagicHeaderPrefix(final byte[] array)
    '''
def readHeader():
    '''public static SnappyCodec readHeader(final InputStream in)
    '''
