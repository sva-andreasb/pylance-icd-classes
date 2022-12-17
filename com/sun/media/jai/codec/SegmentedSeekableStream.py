def ():
    '''returns SegmentedSeekableStream\n\n
    (final SeekableStream stream, final StreamSegmentMapper mapper, final boolean canSeekBackwards)\n
    (final SeekableStream stream, final long[] segmentPositions, final int[] segmentLengths, final boolean canSeekBackwards)\n
    (final SeekableStream stream, final long[] segmentPositions, final int segmentLength, final int totalLength, final boolean canSeekBackwards)\n
    '''
def getFilePointer():
    '''returns long\n\n
    getFilePointer()\n
    '''
def canSeekBackwards():
    '''returns boolean\n\n
    canSeekBackwards()\n
    '''
def seek():
    '''returns None\n\n
    seek(final long pos)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
