def ():
    '''returns FilteringDirectoryNode\n\n
    (final DirectoryEntry directory, final Collection<String> excludes)\n
    '''
def createDirectory():
    '''returns DirectoryEntry\n\n
    createDirectory(final String name)\n
    '''
def createDocument():
    '''returns DocumentEntry\n\n
    createDocument(final String name, final InputStream stream)\n
    createDocument(final String name, final int size, final POIFSWriterListener writer)\n
    '''
def getEntries():
    '''returns Iterator<Entry>\n\n
    getEntries()\n
    '''
def iterator():
    '''returns Iterator<Entry>\n\n
    iterator()\n
    '''
def getEntryCount():
    '''returns int\n\n
    getEntryCount()\n
    '''
def getEntryNames():
    '''returns Set<String>\n\n
    getEntryNames()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def hasEntry():
    '''returns boolean\n\n
    hasEntry(final String name)\n
    '''
def getEntry():
    '''returns Entry\n\n
    getEntry(final String name)\n
    '''
def getStorageClsid():
    '''returns ClassID\n\n
    getStorageClsid()\n
    '''
def setStorageClsid():
    '''returns None\n\n
    setStorageClsid(final ClassID clsidStorage)\n
    '''
def delete():
    '''returns boolean\n\n
    delete()\n
    '''
def renameTo():
    '''returns boolean\n\n
    renameTo(final String newName)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getParent():
    '''returns DirectoryEntry\n\n
    getParent()\n
    '''
def isDirectoryEntry():
    '''returns boolean\n\n
    isDirectoryEntry()\n
    '''
def isDocumentEntry():
    '''returns boolean\n\n
    isDocumentEntry()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Entry\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
