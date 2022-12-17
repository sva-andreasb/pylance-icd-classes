ACTIVE_LOCAL_DATA_CONNECTION_MODE = "int  0"
ACTIVE_REMOTE_DATA_CONNECTION_MODE = "int  1"
PASSIVE_LOCAL_DATA_CONNECTION_MODE = "int  2"
PASSIVE_REMOTE_DATA_CONNECTION_MODE = "int  3"
def ():
    '''returns FTPClient\n\n
    ()\n
    '''
def setDataTimeout():
    '''returns None\n\n
    setDataTimeout(final int timeout)\n
    '''
def setParserFactory():
    '''returns None\n\n
    setParserFactory(final FTPFileEntryParserFactory parserFactory)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def setRemoteVerificationEnabled():
    '''returns None\n\n
    setRemoteVerificationEnabled(final boolean enable)\n
    '''
def isRemoteVerificationEnabled():
    '''returns boolean\n\n
    isRemoteVerificationEnabled()\n
    '''
def login():
    '''returns boolean\n\n
    login(final String username, final String password)\n
    login(final String username, final String password, final String account)\n
    '''
def logout():
    '''returns boolean\n\n
    logout()\n
    '''
def changeWorkingDirectory():
    '''returns boolean\n\n
    changeWorkingDirectory(final String pathname)\n
    '''
def changeToParentDirectory():
    '''returns boolean\n\n
    changeToParentDirectory()\n
    '''
def structureMount():
    '''returns boolean\n\n
    structureMount(final String pathname)\n
    '''
def enterLocalActiveMode():
    '''returns None\n\n
    enterLocalActiveMode()\n
    '''
def enterLocalPassiveMode():
    '''returns None\n\n
    enterLocalPassiveMode()\n
    '''
def enterRemoteActiveMode():
    '''returns boolean\n\n
    enterRemoteActiveMode(final InetAddress host, final int port)\n
    '''
def enterRemotePassiveMode():
    '''returns boolean\n\n
    enterRemotePassiveMode()\n
    '''
def getPassiveHost():
    '''returns String\n\n
    getPassiveHost()\n
    '''
def getPassivePort():
    '''returns int\n\n
    getPassivePort()\n
    '''
def getDataConnectionMode():
    '''returns int\n\n
    getDataConnectionMode()\n
    '''
def setFileType():
    '''returns boolean\n\n
    setFileType(final int fileType)\n
    setFileType(final int fileType, final int formatOrByteSize)\n
    '''
def setFileStructure():
    '''returns boolean\n\n
    setFileStructure(final int structure)\n
    '''
def setFileTransferMode():
    '''returns boolean\n\n
    setFileTransferMode(final int mode)\n
    '''
def remoteRetrieve():
    '''returns boolean\n\n
    remoteRetrieve(final String filename)\n
    '''
def remoteStore():
    '''returns boolean\n\n
    remoteStore(final String filename)\n
    '''
def remoteStoreUnique():
    '''returns boolean\n\n
    remoteStoreUnique(final String filename)\n
    remoteStoreUnique()\n
    '''
def remoteAppend():
    '''returns boolean\n\n
    remoteAppend(final String filename)\n
    '''
def completePendingCommand():
    '''returns boolean\n\n
    completePendingCommand()\n
    '''
def retrieveFile():
    '''returns boolean\n\n
    retrieveFile(final String remote, final OutputStream local)\n
    '''
def retrieveFileStream():
    '''returns InputStream\n\n
    retrieveFileStream(final String remote)\n
    '''
def storeFile():
    '''returns boolean\n\n
    storeFile(final String remote, final InputStream local)\n
    '''
def storeFileStream():
    '''returns OutputStream\n\n
    storeFileStream(final String remote)\n
    '''
def appendFile():
    '''returns boolean\n\n
    appendFile(final String remote, final InputStream local)\n
    '''
def appendFileStream():
    '''returns OutputStream\n\n
    appendFileStream(final String remote)\n
    '''
def storeUniqueFile():
    '''returns boolean\n\n
    storeUniqueFile(final String remote, final InputStream local)\n
    storeUniqueFile(final InputStream local)\n
    '''
def storeUniqueFileStream():
    '''returns OutputStream\n\n
    storeUniqueFileStream(final String remote)\n
    storeUniqueFileStream()\n
    '''
def allocate():
    '''returns boolean\n\n
    allocate(final int bytes)\n
    allocate(final int bytes, final int recordSize)\n
    '''
def setRestartOffset():
    '''returns None\n\n
    setRestartOffset(final long offset)\n
    '''
def getRestartOffset():
    '''returns long\n\n
    getRestartOffset()\n
    '''
def rename():
    '''returns boolean\n\n
    rename(final String from, final String to)\n
    '''
def abort():
    '''returns boolean\n\n
    abort()\n
    '''
def deleteFile():
    '''returns boolean\n\n
    deleteFile(final String pathname)\n
    '''
def removeDirectory():
    '''returns boolean\n\n
    removeDirectory(final String pathname)\n
    '''
def makeDirectory():
    '''returns boolean\n\n
    makeDirectory(final String pathname)\n
    '''
def printWorkingDirectory():
    '''returns String\n\n
    printWorkingDirectory()\n
    '''
def sendSiteCommand():
    '''returns boolean\n\n
    sendSiteCommand(final String arguments)\n
    '''
def getSystemName():
    '''returns String\n\n
    getSystemName()\n
    '''
def listHelp():
    '''returns String\n\n
    listHelp()\n
    listHelp(final String command)\n
    '''
def sendNoOp():
    '''returns boolean\n\n
    sendNoOp()\n
    '''
def listNames():
    '''returns String[]\n\n
    listNames(final String pathname)\n
    listNames()\n
    '''
def listFiles():
    '''returns FTPFile[]\n\n
    listFiles(final String parserKey, final String pathname)\n
    listFiles(final String pathname)\n
    listFiles()\n
    listFiles(final FTPFileListParser parser, final String pathname)\n
    listFiles(final FTPFileListParser parser)\n
    '''
def initiateListParsing():
    '''returns FTPListParseEngine\n\n
    initiateListParsing()\n
    initiateListParsing(final String pathname)\n
    initiateListParsing(final String parserKey, final String pathname)\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    getStatus(final String pathname)\n
    '''
def createFileList():
    '''returns FTPFileList\n\n
    createFileList(final FTPFileEntryParser parser)\n
    createFileList(final String pathname, final FTPFileEntryParser parser)\n
    '''
def setBufferSize():
    '''returns None\n\n
    setBufferSize(final int bufSize)\n
    '''
def getBufferSize():
    '''returns int\n\n
    getBufferSize()\n
    '''
def configure():
    '''returns None\n\n
    configure(final FTPClientConfig config)\n
    '''
