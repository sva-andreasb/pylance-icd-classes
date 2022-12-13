DO_CONVERSION_WITH_REPLACEMENT = "boolean  true"
ORACLE8_PROD_VERSION = "short  8030"
DBCS_CHARSET = "short  -1"
UCS2_CHARSET = "short  -5"
ASCII_CHARSET = "short  1"
ISO_LATIN_1_CHARSET = "short  31"
WE8ISO8859P15_CHARSET = "short  46"
AL24UTFFSS_CHARSET = "short  870"
UTF8_CHARSET = "short  871"
AL32UTF8_CHARSET = "short  873"
AL16UTF16_CHARSET = "short  2000"
def DBConversion():
    '''    public DBConversion(final short n, final short n2, final short n3, final boolean isStrictASCIIConversion, final boolean isQuickASCIIConversion)
    public DBConversion(final short n, final short n2, final short n3)
    '''
def getServerCharSetId():
    '''    public short getServerCharSetId()
    '''
def getNCharSetId():
    '''    public short getNCharSetId()
    '''
def IsNCharFixedWith():
    '''    public boolean IsNCharFixedWith()
    '''
def getClientCharSet():
    '''    public short getClientCharSet()
    '''
def getDbCharSetObj():
    '''    public CharacterSet getDbCharSetObj()
    '''
def getDriverCharSetObj():
    '''    public CharacterSet getDriverCharSetObj()
    '''
def getDriverNCharSetObj():
    '''    public CharacterSet getDriverNCharSetObj()
    '''
def findDriverCharSet():
    '''    public static final short findDriverCharSet(final short n, final short n2)
    '''
def stringToDriverCharBytes():
    '''    public static final byte[] stringToDriverCharBytes(final String s, final short n)
    '''
def StringToCharBytes():
    '''    public byte[] StringToCharBytes(final String s)
    '''
def CharBytesToString():
    '''    public String CharBytesToString(final byte[] array, final int n)
    public String CharBytesToString(final byte[] ascii, final int count, final boolean b)
    '''
def NCharBytesToString():
    '''    public String NCharBytesToString(final byte[] ascii, final int count)
    '''
def javaCharsToCHARBytes():
    '''    public int javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2)
    public int javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)
    '''
def javaCharsToNCHARBytes():
    '''    public int javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2)
    public int javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)
    '''
def CHARBytesToJavaChars():
    '''    public int CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3, final boolean b)
    public int CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3)
    '''
def NCHARBytesToJavaChars():
    '''    public int NCHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3)
    '''
def asciiBytesToCHARBytes():
    '''    public byte[] asciiBytesToCHARBytes(final byte[] array)
    '''
def javaCharsToDbCsBytes():
    '''    public int javaCharsToDbCsBytes(final char[] array, final int n, final byte[] array2)
    public int javaCharsToDbCsBytes(final char[] value, final int offset, final byte[] array, final int n, final int count)
    '''
def javaCharsToUcs2Bytes():
    '''    public static final int javaCharsToUcs2Bytes(final char[] array, final int n, final byte[] array2)
    public static final int javaCharsToUcs2Bytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)
    '''
def ucs2BytesToJavaChars():
    '''    public static final int ucs2BytesToJavaChars(final byte[] array, final int n, final char[] array2)
    '''
def stringToAsciiBytes():
    '''    public static final byte[] stringToAsciiBytes(final String s)
    '''
def asciiBytesToJavaChars():
    '''    public static final int asciiBytesToJavaChars(final byte[] array, final int n, final char[] array2)
    '''
def javaCharsToAsciiBytes():
    '''    public static final int javaCharsToAsciiBytes(final char[] array, final int n, final byte[] array2)
    '''
def isCharSetMultibyte():
    '''    public static final boolean isCharSetMultibyte(final short n)
    '''
def getMaxCharbyteSize():
    '''    public int getMaxCharbyteSize()
    '''
def getMaxNCharbyteSize():
    '''    public int getMaxNCharbyteSize()
    '''
def _getMaxCharbyteSize():
    '''    public int _getMaxCharbyteSize(final short n)
    '''
def isUcs2CharSet():
    '''    public boolean isUcs2CharSet()
    '''
def RAWBytesToHexChars():
    '''    public static final int RAWBytesToHexChars(final byte[] array, final int n, final char[] array2)
    '''
def hexDigit2Nibble():
    '''    public final int hexDigit2Nibble(final char c)
    '''
def hexString2Bytes():
    '''    public final byte[] hexString2Bytes(final String s)
    '''
def hexChars2Bytes():
    '''    public final byte[] hexChars2Bytes(final char[] array, final int n, final int n2)
    '''
def ConvertStream():
    '''    public InputStream ConvertStream(final InputStream inputStream, final int n)
    public InputStream ConvertStream(final InputStream inputStream, final int n, final int n2)
    public InputStream ConvertStream(final Reader reader, final int n, final int n2, final short n3)
    '''
def ConvertStreamInternal():
    '''    public InputStream ConvertStreamInternal(final InputStream inputStream, final int n, final int n2)
    public InputStream ConvertStreamInternal(final Reader reader, final int n, final int n2, final short n3)
    '''
def ConvertCharacterStream():
    '''    public Reader ConvertCharacterStream(final InputStream inputStream, final int n)
    public Reader ConvertCharacterStream(final InputStream inputStream, final int n, final short formOfUse)
    '''
def CharsToStream():
    '''    public InputStream CharsToStream(final char[] array, final int n, final int n2, final int n3)
    '''
def getUtfLen():
    '''    public static final int getUtfLen(final char c)
    '''
def needBytes():
    '''    public boolean needBytes()
    public boolean needBytes(final int n)
    public boolean needBytes()
    public boolean needBytes(final int n)
    '''
