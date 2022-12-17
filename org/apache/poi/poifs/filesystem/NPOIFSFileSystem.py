def ():
    '''returns NPOIFSFileSystem\n\n
    ()\n
    (final File file)\n
    (final File file, final boolean readOnly)\n
    (final FileChannel channel)\n
    (final FileChannel channel, final boolean readOnly)\n
    (final InputStream stream)\n
    '''
def getMiniStore():
    '''returns NPOIFSMiniStore\n\n
    getMiniStore()\n
    '''
def createDocument():
    '''returns DocumentEntry\n\n
    createDocument(final InputStream stream, final String name)\n
    createDocument(final String name, final int size, final POIFSWriterListener writer)\n
    '''
def createDirectory():
    '''returns DirectoryEntry\n\n
    createDirectory(final String name)\n
    '''
def createOrUpdateDocument():
    '''returns DocumentEntry\n\n
    createOrUpdateDocument(final InputStream stream, final String name)\n
    '''
def isInPlaceWriteable():
    '''returns boolean\n\n
    isInPlaceWriteable()\n
    '''
def writeFilesystem():
    '''returns None\n\n
    writeFilesystem()\n
    writeFilesystem(final OutputStream stream)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getRoot():
    '''returns DirectoryNode\n\n
    getRoot()\n
    '''
def createDocumentInputStream():
    '''returns DocumentInputStream\n\n
    createDocumentInputStream(final String documentName)\n
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
def getBigBlockSize():
    '''returns int\n\n
    getBigBlockSize()\n
    '''
def getBigBlockSizeDetails():
    '''returns POIFSBigBlockSize\n\n
    getBigBlockSizeDetails()\n
    '''
def getPropertyTable():
    '''returns NPropertyTable\n\n
    getPropertyTable()\n
    '''
def getHeaderBlock():
    '''returns HeaderBlock\n\n
    getHeaderBlock()\n
    '''
