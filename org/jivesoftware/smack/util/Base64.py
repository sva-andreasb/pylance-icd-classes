NO_OPTIONS = "int  0"
ENCODE = "int  1"
DECODE = "int  0"
GZIP = "int  2"
DONT_BREAK_LINES = "int  8"
URL_SAFE = "int  16"
ORDERED = "int  32"
def main():
'''public static final void main(final String[] args)
'''
pass
def encodeObject():
'''public static String encodeObject(final Serializable serializableObject)
public static String encodeObject(final Serializable serializableObject, final int options)
'''
pass
def encodeBytes():
'''public static String encodeBytes(final byte[] source)
public static String encodeBytes(final byte[] source, final int options)
public static String encodeBytes(final byte[] source, final int off, final int len)
public static String encodeBytes(final byte[] source, final int off, final int len, final int options)
'''
pass
def decode():
'''public static byte[] decode(final byte[] source, final int off, final int len, final int options)
public static byte[] decode(final String s)
public static byte[] decode(final String s, final int options)
'''
pass
def decodeToObject():
'''public static Object decodeToObject(final String encodedObject)
'''
pass
def encodeToFile():
'''public static boolean encodeToFile(final byte[] dataToEncode, final String filename)
'''
pass
def decodeToFile():
'''public static boolean decodeToFile(final String dataToDecode, final String filename)
'''
pass
def decodeFromFile():
'''public static byte[] decodeFromFile(final String filename)
'''
pass
def encodeFromFile():
'''public static String encodeFromFile(final String filename)
'''
pass
def encodeFileToFile():
'''public static void encodeFileToFile(final String infile, final String outfile)
'''
pass
def decodeFileToFile():
'''public static void decodeFileToFile(final String infile, final String outfile)
'''
pass
def InputStream():
'''public InputStream(final java.io.InputStream in)
public InputStream(final java.io.InputStream in, final int options)
'''
pass
def read():
'''public int read()
public int read(final byte[] dest, final int off, final int len)
'''
pass
def OutputStream():
'''public OutputStream(final java.io.OutputStream out)
public OutputStream(final java.io.OutputStream out, final int options)
'''
pass
def write():
'''public void write(final int theByte)
public void write(final byte[] theBytes, final int off, final int len)
'''
pass
def flushBase64():
'''public void flushBase64()
'''
pass
def close():
'''public void close()
'''
pass
def suspendEncoding():
'''public void suspendEncoding()
'''
pass
def resumeEncoding():
'''public void resumeEncoding()
'''
pass
