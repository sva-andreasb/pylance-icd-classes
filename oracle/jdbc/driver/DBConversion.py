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
def ():
    '''returns DBConversion\n\n
    (final short n, final short n2, final short n3, final boolean isStrictASCIIConversion, final boolean isQuickASCIIConversion)\n
    (final short n, final short n2, final short n3)\n
    '''
def getServerCharSetId():
    '''returns short\n\n
    getServerCharSetId()\n
    '''
def getNCharSetId():
    '''returns short\n\n
    getNCharSetId()\n
    '''
def IsNCharFixedWith():
    '''returns boolean\n\n
    IsNCharFixedWith()\n
    '''
def getClientCharSet():
    '''returns short\n\n
    getClientCharSet()\n
    '''
def getDbCharSetObj():
    '''returns CharacterSet\n\n
    getDbCharSetObj()\n
    '''
def getDriverCharSetObj():
    '''returns CharacterSet\n\n
    getDriverCharSetObj()\n
    '''
def getDriverNCharSetObj():
    '''returns CharacterSet\n\n
    getDriverNCharSetObj()\n
    '''
def StringToCharBytes():
    '''returns byte[]\n\n
    StringToCharBytes(final String s)\n
    '''
def CharBytesToString():
    '''returns String\n\n
    CharBytesToString(final byte[] array, final int n)\n
    CharBytesToString(final byte[] ascii, final int count, final boolean b)\n
    '''
def NCharBytesToString():
    '''returns String\n\n
    NCharBytesToString(final byte[] ascii, final int count)\n
    '''
def javaCharsToCHARBytes():
    '''returns int\n\n
    javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2)\n
    javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)\n
    '''
def javaCharsToNCHARBytes():
    '''returns int\n\n
    javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2)\n
    javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2, final int n2, final int n3)\n
    '''
def CHARBytesToJavaChars():
    '''returns int\n\n
    CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3, final boolean b)\n
    CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3)\n
    '''
def NCHARBytesToJavaChars():
    '''returns int\n\n
    NCHARBytesToJavaChars(final byte[] array, final int n, final char[] array2, final int n2, final int[] array3, final int n3)\n
    '''
def asciiBytesToCHARBytes():
    '''returns byte[]\n\n
    asciiBytesToCHARBytes(final byte[] array)\n
    '''
def javaCharsToDbCsBytes():
    '''returns int\n\n
    javaCharsToDbCsBytes(final char[] array, final int n, final byte[] array2)\n
    javaCharsToDbCsBytes(final char[] value, final int offset, final byte[] array, final int n, final int count)\n
    '''
def getMaxCharbyteSize():
    '''returns int\n\n
    getMaxCharbyteSize()\n
    '''
def getMaxNCharbyteSize():
    '''returns int\n\n
    getMaxNCharbyteSize()\n
    '''
def _getMaxCharbyteSize():
    '''returns int\n\n
    _getMaxCharbyteSize(final short n)\n
    '''
def isUcs2CharSet():
    '''returns boolean\n\n
    isUcs2CharSet()\n
    '''
def ConvertStream():
    '''returns InputStream\n\n
    ConvertStream(final InputStream inputStream, final int n)\n
    ConvertStream(final InputStream inputStream, final int n, final int n2)\n
    ConvertStream(final Reader reader, final int n, final int n2, final short n3)\n
    '''
def ConvertStreamInternal():
    '''returns InputStream\n\n
    ConvertStreamInternal(final InputStream inputStream, final int n, final int n2)\n
    ConvertStreamInternal(final Reader reader, final int n, final int n2, final short n3)\n
    '''
def ConvertCharacterStream():
    '''returns Reader\n\n
    ConvertCharacterStream(final InputStream inputStream, final int n)\n
    ConvertCharacterStream(final InputStream inputStream, final int n, final short formOfUse)\n
    '''
def CharsToStream():
    '''returns InputStream\n\n
    CharsToStream(final char[] array, final int n, final int n2, final int n3)\n
    '''
def needBytes():
    '''returns boolean\n\n
    needBytes()\n
    needBytes(final int n)\n
    needBytes()\n
    needBytes(final int n)\n
    '''
