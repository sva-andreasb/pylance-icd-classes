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
def resetWithShared():
    '''returns None\n\n
    resetWithShared(final char[] buf, final int start, final int len)\n
    '''
def resetWithCopy():
    '''returns None\n\n
    resetWithCopy(final char[] buf, final int start, final int len)\n
    '''
def resetWithString():
    '''returns None\n\n
    resetWithString(final String value)\n
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
def getCurrentSegmentSize():
    '''returns int\n\n
    getCurrentSegmentSize()\n
    '''
def setCurrentLength():
    '''returns None\n\n
    setCurrentLength(final int len)\n
    '''
def finishCurrentSegment():
    '''returns char[]\n\n
    finishCurrentSegment()\n
    '''
def expandCurrentSegment():
    '''returns char[]\n\n
    expandCurrentSegment()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
