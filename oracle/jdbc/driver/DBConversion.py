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
'''public DBConversion(final short n, final short n2, final short n3, final boolean isStrictASCIIConversion, final boolean isQuickASCIIConversion)
public DBConversion(final short n, final short n2, final short n3)
'''
pass
def getServerCharSetId():
'''public short getServerCharSetId()
'''
pass
def getNCharSetId():
'''public short getNCharSetId()
'''
pass
def IsNCharFixedWith():
'''public boolean IsNCharFixedWith()
'''
pass
def getClientCharSet():
'''public short getClientCharSet()
'''
pass
def getDbCharSetObj():
'''public CharacterSet getDbCharSetObj()
'''
pass
def getDriverCharSetObj():
'''public CharacterSet getDriverCharSetObj()
'''
pass
def getDriverNCharSetObj():
'''public CharacterSet getDriverNCharSetObj()
'''
pass
def findDriverCharSet():
'''public static final short findDriverCharSet(final short n, final short n2)
'''
pass
def stringToDriverCharBytes():
'''public static final byte[] stringToDriverCharBytes(final String s, final short n)
'''
pass
def StringToCharBytes():
'''public byte[] StringToCharBytes(final String s)
'''
pass
def CharBytesToString():
'''public String CharBytesToString(final byte[] array, final int n)
public String CharBytesToString(final byte[] ascii, final int count, final boolean b)
'''
pass
def NCharBytesToString():
'''public String NCharBytesToString(final byte[] ascii, final int count)
'''
pass
def javaCharsToCHARBytes():
'''public int javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2)
public int javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)
'''
pass
def javaCharsToNCHARBytes():
'''public int javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2)
public int javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)
'''
pass
def CHARBytesToJavaChars():
'''public int CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3, final boolean b)
public int CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3)
'''
pass
def NCHARBytesToJavaChars():
'''public int NCHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3)
'''
pass
def asciiBytesToCHARBytes():
'''public byte[] asciiBytesToCHARBytes(final byte[] array)
'''
pass
def javaCharsToDbCsBytes():
'''public int javaCharsToDbCsBytes(final char[] array, final int n, final byte[] array2)
public int javaCharsToDbCsBytes(final char[] value, final int offset, final byte[] array, final int n, final int count)
'''
pass
def javaCharsToUcs2Bytes():
'''public static final int javaCharsToUcs2Bytes(final char[] array, final int n, final byte[] array2)
public static final int javaCharsToUcs2Bytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)
'''
pass
def ucs2BytesToJavaChars():
'''public static final int ucs2BytesToJavaChars(final byte[] array, final int n, final char[] array2)
'''
pass
def stringToAsciiBytes():
'''public static final byte[] stringToAsciiBytes(final String s)
'''
pass
def asciiBytesToJavaChars():
'''public static final int asciiBytesToJavaChars(final byte[] array, final int n, final char[] array2)
'''
pass
def javaCharsToAsciiBytes():
'''public static final int javaCharsToAsciiBytes(final char[] array, final int n, final byte[] array2)
'''
pass
def isCharSetMultibyte():
'''public static final boolean isCharSetMultibyte(final short n)
'''
pass
def getMaxCharbyteSize():
'''public int getMaxCharbyteSize()
'''
pass
def getMaxNCharbyteSize():
'''public int getMaxNCharbyteSize()
'''
pass
def _getMaxCharbyteSize():
'''public int _getMaxCharbyteSize(final short n)
'''
pass
def isUcs2CharSet():
'''public boolean isUcs2CharSet()
'''
pass
def RAWBytesToHexChars():
'''public static final int RAWBytesToHexChars(final byte[] array, final int n, final char[] array2)
'''
pass
def hexDigit2Nibble():
'''public final int hexDigit2Nibble(final char c)
'''
pass
def hexString2Bytes():
'''public final byte[] hexString2Bytes(final String s)
'''
pass
def hexChars2Bytes():
'''public final byte[] hexChars2Bytes(final char[] array, final int n, final int n2)
'''
pass
def ConvertStream():
'''public InputStream ConvertStream(final InputStream inputStream, final int n)
public InputStream ConvertStream(final InputStream inputStream, final int n, final int n2)
public InputStream ConvertStream(final Reader reader, final int n, final int n2, final short n3)
'''
pass
def ConvertStreamInternal():
'''public InputStream ConvertStreamInternal(final InputStream inputStream, final int n, final int n2)
public InputStream ConvertStreamInternal(final Reader reader, final int n, final int n2, final short n3)
'''
pass
def ConvertCharacterStream():
'''public Reader ConvertCharacterStream(final InputStream inputStream, final int n)
public Reader ConvertCharacterStream(final InputStream inputStream, final int n, final short formOfUse)
'''
pass
def CharsToStream():
'''public InputStream CharsToStream(final char[] array, final int n, final int n2, final int n3)
'''
pass
def getUtfLen():
'''public static final int getUtfLen(final char c)
'''
pass
def needBytes():
'''public boolean needBytes()
public boolean needBytes(final int n)
public boolean needBytes()
public boolean needBytes(final int n)
'''
pass
