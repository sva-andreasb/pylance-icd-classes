DATA_CONTAINER_PROPERTY = "String  \"DataContainer\""
NODE_DOCUMENTS_ATTACHED_PROPERTY = "String  \"NodeDocumentAttached\""
def ():
    '''returns IlvDataContainerDocument\n\n
    ()\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
def initializeDocument():
    '''returns boolean\n\n
    initializeDocument(final Object o)\n
    '''
def getDataContainer():
    '''returns IlvDataContainer\n\n
    getDataContainer()\n
    '''
def setDataContainer():
    '''returns None\n\n
    setDataContainer(final IlvDataContainer ilvDataContainer)\n
    '''
def readDocument():
    '''returns boolean\n\n
    readDocument(final URL b, final IlvFileFilter ilvFileFilter)\n
    '''
def writeDocument():
    '''returns boolean\n\n
    writeDocument(final URL b, final IlvFileFilter ilvFileFilter)\n
    writeDocument(final Writer writer, final IlvFileFilter ilvFileFilter)\n
    '''
def openDocument():
    '''returns IlvDocument\n\n
    openDocument(final Object key)\n
    '''
def canOpenDocument():
    '''returns boolean\n\n
    canOpenDocument(final Object o)\n
    '''
def areNodeDocumentsAttached():
    '''returns boolean\n\n
    areNodeDocumentsAttached()\n
    '''
def attachNodeDocuments():
    '''returns None\n\n
    attachNodeDocuments(final boolean b)\n
    '''
def getOpenDocument():
    '''returns IlvDocument\n\n
    getOpenDocument(final Object key)\n
    '''
def getNodeTitle():
    '''returns String\n\n
    getNodeTitle(final Object o)\n
    '''
def setNodeTitle():
    '''returns None\n\n
    setNodeTitle(final Object o, final String s)\n
    '''
