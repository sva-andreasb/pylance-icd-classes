def ():
    '''returns ChunkedCipherOutputStream\n\n
    (final DirectoryNode dir, final int chunkSize)\n
    (final OutputStream stream, final int chunkSize)\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] b)\n
    write(final byte[] b, final int off, final int len)\n
    '''
def writePlain():
    '''returns None\n\n
    writePlain(final byte[] b, final int off, final int len)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setNextRecordSize():
    '''returns None\n\n
    setNextRecordSize(final int recordSize, final boolean isPlain)\n
    '''
def processPOIFSWriterEvent():
    '''returns None\n\n
    processPOIFSWriterEvent(final POIFSWriterEvent event)\n
    '''
