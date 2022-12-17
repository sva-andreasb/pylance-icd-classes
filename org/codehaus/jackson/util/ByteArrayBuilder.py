def ():
    '''returns ByteArrayBuilder\n\n
    ()\n
    (final BufferRecycler br)\n
    (final int firstBlockSize)\n
    (final BufferRecycler br, final int firstBlockSize)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def release():
    '''returns None\n\n
    release()\n
    '''
def append():
    '''returns None\n\n
    append(final int i)\n
    '''
def appendTwoBytes():
    '''returns None\n\n
    appendTwoBytes(final int b16)\n
    '''
def appendThreeBytes():
    '''returns None\n\n
    appendThreeBytes(final int b24)\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray()\n
    '''
def resetAndGetFirstSegment():
    '''returns byte[]\n\n
    resetAndGetFirstSegment()\n
    '''
def finishCurrentSegment():
    '''returns byte[]\n\n
    finishCurrentSegment()\n
    '''
def completeAndCoalesce():
    '''returns byte[]\n\n
    completeAndCoalesce(final int lastBlockLength)\n
    '''
def getCurrentSegment():
    '''returns byte[]\n\n
    getCurrentSegment()\n
    '''
def setCurrentSegmentLength():
    '''returns None\n\n
    setCurrentSegmentLength(final int len)\n
    '''
def getCurrentSegmentLength():
    '''returns int\n\n
    getCurrentSegmentLength()\n
    '''
def write():
    '''returns None\n\n
    write(final byte[] b)\n
    write(final byte[] b, int off, int len)\n
    write(final int b)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
