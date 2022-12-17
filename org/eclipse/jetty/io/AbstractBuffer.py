def ():
    '''returns AbstractBuffer\n\n
    (final int access, final boolean isVolatile)\n
    '''
def asArray():
    '''returns byte[]\n\n
    asArray()\n
    '''
def duplicate():
    '''returns ByteArrayBuffer\n\n
    duplicate(final int access)\n
    '''
def asNonVolatileBuffer():
    '''returns Buffer\n\n
    asNonVolatileBuffer()\n
    '''
def asImmutableBuffer():
    '''returns Buffer\n\n
    asImmutableBuffer()\n
    '''
def asReadOnlyBuffer():
    '''returns Buffer\n\n
    asReadOnlyBuffer()\n
    '''
def asMutableBuffer():
    '''returns Buffer\n\n
    asMutableBuffer()\n
    '''
def buffer():
    '''returns Buffer\n\n
    buffer()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def compact():
    '''returns None\n\n
    compact()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def equalsIgnoreCase():
    '''returns boolean\n\n
    equalsIgnoreCase(final Buffer b)\n
    '''
def get():
    '''returns Buffer\n\n
    get()\n
    get(final byte[] b, final int offset, int length)\n
    get(final int length)\n
    '''
def hasContent():
    '''returns boolean\n\n
    hasContent()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def isImmutable():
    '''returns boolean\n\n
    isImmutable()\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def isVolatile():
    '''returns boolean\n\n
    isVolatile()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def mark():
    '''returns None\n\n
    mark()\n
    mark(final int offset)\n
    '''
def markIndex():
    '''returns int\n\n
    markIndex()\n
    '''
def peek():
    '''returns Buffer\n\n
    peek()\n
    peek(final int index, final int length)\n
    '''
def poke():
    '''returns int\n\n
    poke(int index, final Buffer src)\n
    poke(int index, final byte[] b, final int offset, int length)\n
    '''
def put():
    '''returns int\n\n
    put(final Buffer src)\n
    put(final byte b)\n
    put(final byte[] b, final int offset, final int length)\n
    put(final byte[] b)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def rewind():
    '''returns None\n\n
    rewind()\n
    '''
def setGetIndex():
    '''returns None\n\n
    setGetIndex(final int getIndex)\n
    '''
def setMarkIndex():
    '''returns None\n\n
    setMarkIndex(final int index)\n
    '''
def setPutIndex():
    '''returns None\n\n
    setPutIndex(final int putIndex)\n
    '''
def skip():
    '''returns int\n\n
    skip(int n)\n
    '''
def slice():
    '''returns Buffer\n\n
    slice()\n
    '''
def sliceFromMark():
    '''returns Buffer\n\n
    sliceFromMark()\n
    sliceFromMark(final int length)\n
    '''
def space():
    '''returns int\n\n
    space()\n
    '''
def toDetailString():
    '''returns String\n\n
    toDetailString()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final String charset)\n
    '''
def toDebugString():
    '''returns String\n\n
    toDebugString()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream out)\n
    '''
def readFrom():
    '''returns int\n\n
    readFrom(final InputStream in, final int max)\n
    '''
