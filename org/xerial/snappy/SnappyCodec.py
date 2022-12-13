DEFAULT_VERSION = "int  1"
MINIMUM_COMPATIBLE_VERSION = "int  1"
def getMagicHeader():
'''public static byte[] getMagicHeader()
'''
pass
def toString():
'''public String toString()
'''
pass
def headerSize():
'''public static int headerSize()
'''
pass
def writeHeader():
'''public int writeHeader(final byte[] array, final int n)
public int writeHeader(final OutputStream outputStream)
'''
pass
def isValidMagicHeader():
'''public boolean isValidMagicHeader()
'''
pass
def hasMagicHeaderPrefix():
'''public static boolean hasMagicHeaderPrefix(final byte[] array)
'''
pass
def readHeader():
'''public static SnappyCodec readHeader(final InputStream in)
'''
pass
