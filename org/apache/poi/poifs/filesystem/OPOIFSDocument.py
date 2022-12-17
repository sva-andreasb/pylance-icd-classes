def ():
    '''returns OPOIFSDocument\n\n
    (final String name, final RawDataBlock[] blocks, final int length)\n
    (final String name, final SmallDocumentBlock[] blocks, final int length)\n
    (final String name, final POIFSBigBlockSize bigBlockSize, final ListManagedBlock[] blocks, final int length)\n
    (final String name, final ListManagedBlock[] blocks, final int length)\n
    (final String name, final POIFSBigBlockSize bigBlockSize, final InputStream stream)\n
    (final String name, final InputStream stream)\n
    (final String name, final int size, final POIFSBigBlockSize bigBlockSize, final POIFSDocumentPath path, final POIFSWriterListener writer)\n
    (final String name, final int size, final POIFSDocumentPath path, final POIFSWriterListener writer)\n
    '''
def getSmallBlocks():
    '''returns SmallDocumentBlock[]\n\n
    getSmallBlocks()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def writeBlocks():
    '''returns None\n\n
    writeBlocks(final OutputStream stream)\n
    '''
def countBlocks():
    '''returns int\n\n
    countBlocks()\n
    '''
def setStartBlock():
    '''returns None\n\n
    setStartBlock(final int index)\n
    '''
def getViewableArray():
    '''returns Object[]\n\n
    getViewableArray()\n
    '''
def getViewableIterator():
    '''returns Iterator<Object>\n\n
    getViewableIterator()\n
    '''
def preferArray():
    '''returns boolean\n\n
    preferArray()\n
    '''
def getShortDescription():
    '''returns String\n\n
    getShortDescription()\n
    '''
