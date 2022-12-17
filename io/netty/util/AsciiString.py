INDEX_NOT_FOUND = "int  -1"
def ():
    '''returns AsciiString\n\n
    (final byte[] value)\n
    (final byte[] value, final boolean copy)\n
    (final byte[] value, final int start, final int length, final boolean copy)\n
    (final ByteBuffer value)\n
    (final ByteBuffer value, final boolean copy)\n
    (final ByteBuffer value, final int start, final int length, final boolean copy)\n
    (final char[] value)\n
    (final char[] value, final int start, final int length)\n
    (final char[] value, final Charset charset)\n
    (final char[] value, final Charset charset, final int start, final int length)\n
    (final CharSequence value)\n
    (final CharSequence value, final int start, final int length)\n
    (final CharSequence value, final Charset charset)\n
    (final CharSequence value, final Charset charset, final int start, final int length)\n
    '''
def forEachByte():
    '''returns int\n\n
    forEachByte(final ByteProcessor visitor)\n
    forEachByte(final int index, final int length, final ByteProcessor visitor)\n
    '''
def forEachByteDesc():
    '''returns int\n\n
    forEachByteDesc(final ByteProcessor visitor)\n
    forEachByteDesc(final int index, final int length, final ByteProcessor visitor)\n
    '''
def byteAt():
    '''returns byte\n\n
    byteAt(final int index)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def arrayChanged():
    '''returns None\n\n
    arrayChanged()\n
    '''
def array():
    '''returns byte[]\n\n
    array()\n
    '''
def arrayOffset():
    '''returns int\n\n
    arrayOffset()\n
    '''
def isEntireArrayUsed():
    '''returns boolean\n\n
    isEntireArrayUsed()\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray()\n
    toByteArray(final int start, final int end)\n
    '''
def copy():
    '''returns None\n\n
    copy(final int srcIdx, final byte[] dst, final int dstIdx, final int length)\n
    copy(final int srcIdx, final char[] dst, final int dstIdx, final int length)\n
    '''
def charAt():
    '''returns char\n\n
    charAt(final int index)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final CharSequence cs)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final CharSequence string)\n
    '''
def concat():
    '''returns AsciiString\n\n
    concat(final CharSequence string)\n
    '''
def endsWith():
    '''returns boolean\n\n
    endsWith(final CharSequence suffix)\n
    '''
def contentEqualsIgnoreCase():
    '''returns boolean\n\n
    contentEqualsIgnoreCase(final CharSequence string)\n
    '''
def toCharArray():
    '''returns char[]\n\n
    toCharArray()\n
    toCharArray(final int start, final int end)\n
    '''
def subSequence():
    '''returns AsciiString\n\n
    subSequence(final int start)\n
    subSequence(final int start, final int end)\n
    subSequence(final int start, final int end, final boolean copy)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final CharSequence string)\n
    indexOf(final CharSequence subString, int start)\n
    indexOf(final char ch, int start)\n
    '''
def lastIndexOf():
    '''returns int\n\n
    lastIndexOf(final CharSequence string)\n
    lastIndexOf(final CharSequence subString, int start)\n
    '''
def regionMatches():
    '''returns boolean\n\n
    regionMatches(final int thisStart, final CharSequence string, final int start, final int length)\n
    regionMatches(final boolean ignoreCase, int thisStart, final CharSequence string, int start, final int length)\n
    '''
def replace():
    '''returns AsciiString\n\n
    replace(final char oldChar, final char newChar)\n
    '''
def startsWith():
    '''returns boolean\n\n
    startsWith(final CharSequence prefix)\n
    startsWith(final CharSequence prefix, final int start)\n
    '''
def toLowerCase():
    '''returns AsciiString\n\n
    toLowerCase()\n
    '''
def toUpperCase():
    '''returns AsciiString\n\n
    toUpperCase()\n
    '''
def trim():
    '''returns AsciiString\n\n
    trim()\n
    '''
def contentEquals():
    '''returns boolean\n\n
    contentEquals(final CharSequence a)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final String expr)\n
    '''
def split():
    '''returns AsciiString[]\n\n
    split(final String expr, final int max)\n
    split(final char delim)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode(final CharSequence o)\n
    hashCode(final CharSequence o)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final CharSequence a, final CharSequence b)\n
    equals(final CharSequence a, final CharSequence b)\n
    equals(final char a, final char b)\n
    equals(final char a, final char b)\n
    equals(final char a, final char b)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final int start)\n
    toString(final int start, final int end)\n
    '''
def parseBoolean():
    '''returns boolean\n\n
    parseBoolean()\n
    '''
def parseChar():
    '''returns char\n\n
    parseChar()\n
    parseChar(final int start)\n
    '''
def parseShort():
    '''returns short\n\n
    parseShort()\n
    parseShort(final int radix)\n
    parseShort(final int start, final int end)\n
    parseShort(final int start, final int end, final int radix)\n
    '''
def parseInt():
    '''returns int\n\n
    parseInt()\n
    parseInt(final int radix)\n
    parseInt(final int start, final int end)\n
    parseInt(final int start, final int end, final int radix)\n
    '''
def parseLong():
    '''returns long\n\n
    parseLong()\n
    parseLong(final int radix)\n
    parseLong(final int start, final int end)\n
    parseLong(final int start, final int end, final int radix)\n
    '''
def parseFloat():
    '''returns float\n\n
    parseFloat()\n
    parseFloat(final int start, final int end)\n
    '''
def parseDouble():
    '''returns double\n\n
    parseDouble()\n
    parseDouble(final int start, final int end)\n
    '''
