ACTIVE_LOCAL_DATA_CONNECTION_MODE = "int  0"
ACTIVE_REMOTE_DATA_CONNECTION_MODE = "int  1"
PASSIVE_LOCAL_DATA_CONNECTION_MODE = "int  2"
PASSIVE_REMOTE_DATA_CONNECTION_MODE = "int  3"
def FTPClient():
    '''    public FTPClient()
    '''
def setDataTimeout():
    '''    public void setDataTimeout(final int timeout)
    '''
def setParserFactory():
    '''    public void setParserFactory(final FTPFileEntryParserFactory parserFactory)
    '''
def disconnect():
    '''    public void disconnect()
    '''
def setRemoteVerificationEnabled():
    '''    public void setRemoteVerificationEnabled(final boolean enable)
    '''
def isRemoteVerificationEnabled():
    '''    public boolean isRemoteVerificationEnabled()
    '''
def login():
    '''    public boolean login(final String username, final String password)
    public boolean login(final String username, final String password, final String account)
    '''
def logout():
    '''    public boolean logout()
    '''
def changeWorkingDirectory():
    '''    public boolean changeWorkingDirectory(final String pathname)
    '''
def changeToParentDirectory():
    '''    public boolean changeToParentDirectory()
    '''
def structureMount():
    '''    public boolean structureMount(final String pathname)
    '''
def enterLocalActiveMode():
    '''    public void enterLocalActiveMode()
    '''
def enterLocalPassiveMode():
    '''    public void enterLocalPassiveMode()
    '''
def enterRemoteActiveMode():
    '''    public boolean enterRemoteActiveMode(final InetAddress host, final int port)
    '''
def enterRemotePassiveMode():
    '''    public boolean enterRemotePassiveMode()
    '''
def getPassiveHost():
    '''    public String getPassiveHost()
    '''
def getPassivePort():
    '''    public int getPassivePort()
    '''
def getDataConnectionMode():
    '''    public int getDataConnectionMode()
    '''
def setFileType():
    '''    public boolean setFileType(final int fileType)
    public boolean setFileType(final int fileType, final int formatOrByteSize)
    '''
def setFileStructure():
    '''    public boolean setFileStructure(final int structure)
    '''
def setFileTransferMode():
    '''    public boolean setFileTransferMode(final int mode)
    '''
def remoteRetrieve():
    '''    public boolean remoteRetrieve(final String filename)
    '''
def remoteStore():
    '''    public boolean remoteStore(final String filename)
    '''
def remoteStoreUnique():
    '''    public boolean remoteStoreUnique(final String filename)
    public boolean remoteStoreUnique()
    '''
def remoteAppend():
    '''    public boolean remoteAppend(final String filename)
    '''
def completePendingCommand():
    '''    public boolean completePendingCommand()
    '''
def retrieveFile():
    '''    public boolean retrieveFile(final String remote, final OutputStream local)
    '''
def retrieveFileStream():
    '''    public InputStream retrieveFileStream(final String remote)
    '''
def storeFile():
    '''    public boolean storeFile(final String remote, final InputStream local)
    '''
def storeFileStream():
    '''    public OutputStream storeFileStream(final String remote)
    '''
def appendFile():
    '''    public boolean appendFile(final String remote, final InputStream local)
    '''
def appendFileStream():
    '''    public OutputStream appendFileStream(final String remote)
    '''
def storeUniqueFile():
    '''    public boolean storeUniqueFile(final String remote, final InputStream local)
    public boolean storeUniqueFile(final InputStream local)
    '''
def storeUniqueFileStream():
    '''    public OutputStream storeUniqueFileStream(final String remote)
    public OutputStream storeUniqueFileStream()
    '''
def allocate():
    '''    public boolean allocate(final int bytes)
    public boolean allocate(final int bytes, final int recordSize)
    '''
def setRestartOffset():
    '''    public void setRestartOffset(final long offset)
    '''
def getRestartOffset():
    '''    public long getRestartOffset()
    '''
def rename():
    '''    public boolean rename(final String from, final String to)
    '''
def abort():
    '''    public boolean abort()
    '''
def deleteFile():
    '''    public boolean deleteFile(final String pathname)
    '''
def removeDirectory():
    '''    public boolean removeDirectory(final String pathname)
    '''
def makeDirectory():
    '''    public boolean makeDirectory(final String pathname)
    '''
def printWorkingDirectory():
    '''    public String printWorkingDirectory()
    '''
def sendSiteCommand():
    '''    public boolean sendSiteCommand(final String arguments)
    '''
def getSystemName():
    '''    public String getSystemName()
    '''
def listHelp():
    '''    public String listHelp()
    public String listHelp(final String command)
    '''
def sendNoOp():
    '''    public boolean sendNoOp()
    '''
def listNames():
    '''    public String[] listNames(final String pathname)
    public String[] listNames()
    '''
def listFiles():
    '''    public FTPFile[] listFiles(final String parserKey, final String pathname)
    public FTPFile[] listFiles(final String pathname)
    public FTPFile[] listFiles()
    public FTPFile[] listFiles(final FTPFileListParser parser, final String pathname)
    public FTPFile[] listFiles(final FTPFileListParser parser)
    '''
def initiateListParsing():
    '''    public FTPListParseEngine initiateListParsing()
    public FTPListParseEngine initiateListParsing(final String pathname)
    public FTPListParseEngine initiateListParsing(final String parserKey, final String pathname)
    '''
def getStatus():
    '''    public String getStatus()
    public String getStatus(final String pathname)
    '''
def createFileList():
    '''    public FTPFileList createFileList(final FTPFileEntryParser parser)
    public FTPFileList createFileList(final String pathname, final FTPFileEntryParser parser)
    '''
def setBufferSize():
    '''    public void setBufferSize(final int bufSize)
    '''
def getBufferSize():
    '''    public int getBufferSize()
    '''
def configure():
    '''    public void configure(final FTPClientConfig config)
    '''
