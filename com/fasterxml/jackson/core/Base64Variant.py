BASE64_VALUE_INVALID = "int  -1"
BASE64_VALUE_PADDING = "int  -2"
def Base64Variant():
'''public Base64Variant(final String name, final String base64Alphabet, final boolean usesPadding, final char paddingChar, final int maxLineLength)
public Base64Variant(final Base64Variant base, final String name, final int maxLineLength)
public Base64Variant(final Base64Variant base, final String name, final boolean usesPadding, final char paddingChar, final int maxLineLength)
'''
pass
def getName():
'''public String getName()
'''
pass
def usesPadding():
'''public boolean usesPadding()
'''
pass
def usesPaddingChar():
'''public boolean usesPaddingChar(final char c)
public boolean usesPaddingChar(final int ch)
'''
pass
def getPaddingChar():
'''public char getPaddingChar()
'''
pass
def getPaddingByte():
'''public byte getPaddingByte()
'''
pass
def getMaxLineLength():
'''public int getMaxLineLength()
'''
pass
def decodeBase64Char():
'''public int decodeBase64Char(final char c)
public int decodeBase64Char(final int ch)
'''
pass
def decodeBase64Byte():
'''public int decodeBase64Byte(final byte b)
'''
pass
def encodeBase64BitsAsChar():
'''public char encodeBase64BitsAsChar(final int value)
'''
pass
def encodeBase64Chunk():
'''public int encodeBase64Chunk(final int b24, final char[] buffer, int ptr)
public void encodeBase64Chunk(final StringBuilder sb, final int b24)
public int encodeBase64Chunk(final int b24, final byte[] buffer, int ptr)
'''
pass
def encodeBase64Partial():
'''public int encodeBase64Partial(final int bits, final int outputBytes, final char[] buffer, int outPtr)
public void encodeBase64Partial(final StringBuilder sb, final int bits, final int outputBytes)
public int encodeBase64Partial(final int bits, final int outputBytes, final byte[] buffer, int outPtr)
'''
pass
def encodeBase64BitsAsByte():
'''public byte encodeBase64BitsAsByte(final int value)
'''
pass
def encode():
'''public String encode(final byte[] input)
public String encode(final byte[] input, final boolean addQuotes)
'''
pass
def decode():
'''public byte[] decode(final String input)
public void decode(final String str, final ByteArrayBuilder builder)
'''
pass
def toString():
'''public String toString()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def missingPaddingMessage():
'''public String missingPaddingMessage()
'''
pass
