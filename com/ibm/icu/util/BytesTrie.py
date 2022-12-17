def ():
    '''returns BytesTrie\n\n
    (final byte[] trieBytes, final int offset)\n
    (final BytesTrie other)\n
    '''
def clone():
    '''returns BytesTrie\n\n
    clone()\n
    '''
def reset():
    '''returns Iterator\n\n
    reset()\n
    reset()\n
    '''
def getState64():
    '''returns long\n\n
    getState64()\n
    '''
def resetToState64():
    '''returns BytesTrie\n\n
    resetToState64(final long state)\n
    '''
def saveState():
    '''returns BytesTrie\n\n
    saveState(final State state)\n
    '''
def resetToState():
    '''returns BytesTrie\n\n
    resetToState(final State state)\n
    '''
def current():
    '''returns Result\n\n
    current()\n
    '''
def first():
    '''returns Result\n\n
    first(int inByte)\n
    '''
def next():
    '''returns Entry\n\n
    next(int inByte)\n
    next(final byte[] s, int sIndex, final int sLimit)\n
    next()\n
    '''
def getValue():
    '''returns int\n\n
    getValue()\n
    '''
def getUniqueValue():
    '''returns long\n\n
    getUniqueValue()\n
    '''
def getNextBytes():
    '''returns int\n\n
    getNextBytes(final Appendable out)\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    iterator(final int maxStringLength)\n
    '''
def matches():
    '''returns boolean\n\n
    matches()\n
    '''
def hasValue():
    '''returns boolean\n\n
    hasValue()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def bytesLength():
    '''returns int\n\n
    bytesLength()\n
    '''
def byteAt():
    '''returns byte\n\n
    byteAt(final int index)\n
    '''
def copyBytesTo():
    '''returns None\n\n
    copyBytesTo(final byte[] dest, final int destOffset)\n
    '''
def bytesAsByteBuffer():
    '''returns ByteBuffer\n\n
    bytesAsByteBuffer()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
