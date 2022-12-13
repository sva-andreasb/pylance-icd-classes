ACTIVE_LOCAL_DATA_CONNECTION_MODE = "int  0"
ACTIVE_REMOTE_DATA_CONNECTION_MODE = "int  1"
PASSIVE_LOCAL_DATA_CONNECTION_MODE = "int  2"
PASSIVE_REMOTE_DATA_CONNECTION_MODE = "int  3"
def FTPClient():
'''public FTPClient()
'''
pass
def setDataTimeout():
'''public void setDataTimeout(final int timeout)
'''
pass
def setParserFactory():
'''public void setParserFactory(final FTPFileEntryParserFactory parserFactory)
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def setRemoteVerificationEnabled():
'''public void setRemoteVerificationEnabled(final boolean enable)
'''
pass
def isRemoteVerificationEnabled():
'''public boolean isRemoteVerificationEnabled()
'''
pass
def login():
'''public boolean login(final String username, final String password)
public boolean login(final String username, final String password, final String account)
'''
pass
def logout():
'''public boolean logout()
'''
pass
def changeWorkingDirectory():
'''public boolean changeWorkingDirectory(final String pathname)
'''
pass
def changeToParentDirectory():
'''public boolean changeToParentDirectory()
'''
pass
def structureMount():
'''public boolean structureMount(final String pathname)
'''
pass
def enterLocalActiveMode():
'''public void enterLocalActiveMode()
'''
pass
def enterLocalPassiveMode():
'''public void enterLocalPassiveMode()
'''
pass
def enterRemoteActiveMode():
'''public boolean enterRemoteActiveMode(final InetAddress host, final int port)
'''
pass
def enterRemotePassiveMode():
'''public boolean enterRemotePassiveMode()
'''
pass
def getPassiveHost():
'''public String getPassiveHost()
'''
pass
def getPassivePort():
'''public int getPassivePort()
'''
pass
def getDataConnectionMode():
'''public int getDataConnectionMode()
'''
pass
def setFileType():
'''public boolean setFileType(final int fileType)
public boolean setFileType(final int fileType, final int formatOrByteSize)
'''
pass
def setFileStructure():
'''public boolean setFileStructure(final int structure)
'''
pass
def setFileTransferMode():
'''public boolean setFileTransferMode(final int mode)
'''
pass
def remoteRetrieve():
'''public boolean remoteRetrieve(final String filename)
'''
pass
def remoteStore():
'''public boolean remoteStore(final String filename)
'''
pass
def remoteStoreUnique():
'''public boolean remoteStoreUnique(final String filename)
public boolean remoteStoreUnique()
'''
pass
def remoteAppend():
'''public boolean remoteAppend(final String filename)
'''
pass
def completePendingCommand():
'''public boolean completePendingCommand()
'''
pass
def retrieveFile():
'''public boolean retrieveFile(final String remote, final OutputStream local)
'''
pass
def retrieveFileStream():
'''public InputStream retrieveFileStream(final String remote)
'''
pass
def storeFile():
'''public boolean storeFile(final String remote, final InputStream local)
'''
pass
def storeFileStream():
'''public OutputStream storeFileStream(final String remote)
'''
pass
def appendFile():
'''public boolean appendFile(final String remote, final InputStream local)
'''
pass
def appendFileStream():
'''public OutputStream appendFileStream(final String remote)
'''
pass
def storeUniqueFile():
'''public boolean storeUniqueFile(final String remote, final InputStream local)
public boolean storeUniqueFile(final InputStream local)
'''
pass
def storeUniqueFileStream():
'''public OutputStream storeUniqueFileStream(final String remote)
public OutputStream storeUniqueFileStream()
'''
pass
def allocate():
'''public boolean allocate(final int bytes)
public boolean allocate(final int bytes, final int recordSize)
'''
pass
def setRestartOffset():
'''public void setRestartOffset(final long offset)
'''
pass
def getRestartOffset():
'''public long getRestartOffset()
'''
pass
def rename():
'''public boolean rename(final String from, final String to)
'''
pass
def abort():
'''public boolean abort()
'''
pass
def deleteFile():
'''public boolean deleteFile(final String pathname)
'''
pass
def removeDirectory():
'''public boolean removeDirectory(final String pathname)
'''
pass
def makeDirectory():
'''public boolean makeDirectory(final String pathname)
'''
pass
def printWorkingDirectory():
'''public String printWorkingDirectory()
'''
pass
def sendSiteCommand():
'''public boolean sendSiteCommand(final String arguments)
'''
pass
def getSystemName():
'''public String getSystemName()
'''
pass
def listHelp():
'''public String listHelp()
public String listHelp(final String command)
'''
pass
def sendNoOp():
'''public boolean sendNoOp()
'''
pass
def listNames():
'''public String[] listNames(final String pathname)
public String[] listNames()
'''
pass
def listFiles():
'''public FTPFile[] listFiles(final String parserKey, final String pathname)
public FTPFile[] listFiles(final String pathname)
public FTPFile[] listFiles()
public FTPFile[] listFiles(final FTPFileListParser parser, final String pathname)
public FTPFile[] listFiles(final FTPFileListParser parser)
'''
pass
def initiateListParsing():
'''public FTPListParseEngine initiateListParsing()
public FTPListParseEngine initiateListParsing(final String pathname)
public FTPListParseEngine initiateListParsing(final String parserKey, final String pathname)
'''
pass
def getStatus():
'''public String getStatus()
public String getStatus(final String pathname)
'''
pass
def createFileList():
'''public FTPFileList createFileList(final FTPFileEntryParser parser)
public FTPFileList createFileList(final String pathname, final FTPFileEntryParser parser)
'''
pass
def setBufferSize():
'''public void setBufferSize(final int bufSize)
'''
pass
def getBufferSize():
'''public int getBufferSize()
'''
pass
def configure():
'''public void configure(final FTPClientConfig config)
'''
pass
