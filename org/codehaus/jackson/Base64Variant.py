BASE64_VALUE_INVALID = "int  -1"
BASE64_VALUE_PADDING = "int  -2"
def ():
    '''returns Base64Variant\n\n
    (final String name, final String base64Alphabet, final boolean usesPadding, final char paddingChar, final int maxLineLength)\n
    (final Base64Variant base, final String name, final int maxLineLength)\n
    (final Base64Variant base, final String name, final boolean usesPadding, final char paddingChar, final int maxLineLength)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def usesPadding():
    '''returns boolean\n\n
    usesPadding()\n
    '''
def usesPaddingChar():
    '''returns boolean\n\n
    usesPaddingChar(final char c)\n
    usesPaddingChar(final int ch)\n
    '''
def getPaddingChar():
    '''returns char\n\n
    getPaddingChar()\n
    '''
def getPaddingByte():
    '''returns byte\n\n
    getPaddingByte()\n
    '''
def getMaxLineLength():
    '''returns int\n\n
    getMaxLineLength()\n
    '''
def decodeBase64Char():
    '''returns int\n\n
    decodeBase64Char(final char c)\n
    decodeBase64Char(final int ch)\n
    '''
def decodeBase64Byte():
    '''returns int\n\n
    decodeBase64Byte(final byte b)\n
    '''
def encodeBase64BitsAsChar():
    '''returns char\n\n
    encodeBase64BitsAsChar(final int value)\n
    '''
def encodeBase64Chunk():
    '''returns int\n\n
    encodeBase64Chunk(final int b24, final char[] buffer, int ptr)\n
    encodeBase64Chunk(final StringBuilder sb, final int b24)\n
    encodeBase64Chunk(final int b24, final byte[] buffer, int ptr)\n
    '''
def encodeBase64Partial():
    '''returns int\n\n
    encodeBase64Partial(final int bits, final int outputBytes, final char[] buffer, int outPtr)\n
    encodeBase64Partial(final StringBuilder sb, final int bits, final int outputBytes)\n
    encodeBase64Partial(final int bits, final int outputBytes, final byte[] buffer, int outPtr)\n
    '''
def encodeBase64BitsAsByte():
    '''returns byte\n\n
    encodeBase64BitsAsByte(final int value)\n
    '''
def encode():
    '''returns String\n\n
    encode(final byte[] input)\n
    encode(final byte[] input, final boolean addQuotes)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
