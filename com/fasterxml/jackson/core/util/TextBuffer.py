def ():
    '''returns TextBuffer\n\n
    (final BufferRecycler allocator)\n
    '''
def releaseBuffers():
    '''returns None\n\n
    releaseBuffers()\n
    '''
def resetWithEmpty():
    '''returns None\n\n
    resetWithEmpty()\n
    '''
def resetWith():
    '''returns None\n\n
    resetWith(final char ch)\n
    '''
def resetWithShared():
    '''returns None\n\n
    resetWithShared(final char[] buf, final int start, final int len)\n
    '''
def resetWithCopy():
    '''returns None\n\n
    resetWithCopy(final char[] buf, final int start, final int len)\n
    resetWithCopy(final String text, final int start, final int len)\n
    '''
def resetWithString():
    '''returns None\n\n
    resetWithString(final String value)\n
    '''
def getBufferWithoutReset():
    '''returns char[]\n\n
    getBufferWithoutReset()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getTextOffset():
    '''returns int\n\n
    getTextOffset()\n
    '''
def hasTextAsCharacters():
    '''returns boolean\n\n
    hasTextAsCharacters()\n
    '''
def getTextBuffer():
    '''returns char[]\n\n
    getTextBuffer()\n
    '''
def contentsAsString():
    '''returns String\n\n
    contentsAsString()\n
    '''
def contentsAsArray():
    '''returns char[]\n\n
    contentsAsArray()\n
    '''
def contentsAsDecimal():
    '''returns BigDecimal\n\n
    contentsAsDecimal()\n
    '''
def contentsAsDouble():
    '''returns double\n\n
    contentsAsDouble()\n
    '''
def contentsAsInt():
    '''returns int\n\n
    contentsAsInt(final boolean neg)\n
    '''
def contentsAsLong():
    '''returns long\n\n
    contentsAsLong(final boolean neg)\n
    '''
def contentsToWriter():
    '''returns int\n\n
    contentsToWriter(final Writer w)\n
    '''
def ensureNotShared():
    '''returns None\n\n
    ensureNotShared()\n
    '''
def append():
    '''returns None\n\n
    append(final char c)\n
    append(final char[] c, int start, int len)\n
    append(final String str, int offset, int len)\n
    '''
def getCurrentSegment():
    '''returns char[]\n\n
    getCurrentSegment()\n
    '''
def emptyAndGetCurrentSegment():
    '''returns char[]\n\n
    emptyAndGetCurrentSegment()\n
    '''
def getCurrentSegmentSize():
    '''returns int\n\n
    getCurrentSegmentSize()\n
    '''
def setCurrentLength():
    '''returns None\n\n
    setCurrentLength(final int len)\n
    '''
def setCurrentAndReturn():
    '''returns String\n\n
    setCurrentAndReturn(final int len)\n
    '''
def finishCurrentSegment():
    '''returns char[]\n\n
    finishCurrentSegment()\n
    '''
def expandCurrentSegment():
    '''returns char[]\n\n
    expandCurrentSegment()\n
    expandCurrentSegment(final int minSize)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
