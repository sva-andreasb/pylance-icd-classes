def ():
    '''returns FrameInfo\n\n
    (final OutputStream out, final BLOCKSIZE blockSize, final FLG.Bits... bits)\n
    (final OutputStream out, final BLOCKSIZE blockSize, final long knownSize, final FLG.Bits... bits)\n
    (final OutputStream out, final BLOCKSIZE blockSize)\n
    (final OutputStream out)\n
    (final int version, final Bits... bits)\n
    (final FLG flg, final BD bd)\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] b, int off, int len)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getIndicator():
    '''returns int\n\n
    getIndicator()\n
    '''
def toByte():
    '''returns byte\n\n
    toByte()\n
    toByte()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Bits bit)\n
    isEnabled(final FLG.Bits bit)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getBlockMaximumSize():
    '''returns int\n\n
    getBlockMaximumSize()\n
    '''
def getFLG():
    '''returns FLG\n\n
    getFLG()\n
    '''
def getBD():
    '''returns BD\n\n
    getBD()\n
    '''
def updateStreamHash():
    '''returns None\n\n
    updateStreamHash(final byte[] buff, final int off, final int len)\n
    '''
def currentStreamHash():
    '''returns int\n\n
    currentStreamHash()\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def isFinished():
    '''returns boolean\n\n
    isFinished()\n
    '''
