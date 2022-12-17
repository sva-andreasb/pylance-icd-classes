def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def isAppend():
    '''returns boolean\n\n
    isAppend()\n
    '''
def isCreateOnDemand():
    '''returns boolean\n\n
    isCreateOnDemand()\n
    '''
def isLocking():
    '''returns boolean\n\n
    isLocking()\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def getFilePermissions():
    '''returns Set<PosixFilePermission>\n\n
    getFilePermissions()\n
    '''
def getFileOwner():
    '''returns String\n\n
    getFileOwner()\n
    '''
def getFileGroup():
    '''returns String\n\n
    getFileGroup()\n
    '''
def isAttributeViewEnabled():
    '''returns boolean\n\n
    isAttributeViewEnabled()\n
    '''
def ():
    '''returns FactoryData\n\n
    (final boolean append, final boolean locking, final boolean bufferedIo, final int bufferSize, final boolean createOnDemand, final String advertiseURI, final Layout<? extends Serializable> layout, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)\n
    '''
def createManager():
    '''returns FileManager\n\n
    createManager(final String name, final FactoryData data)\n
    '''
