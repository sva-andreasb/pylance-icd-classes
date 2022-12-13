def AS400Protocol():
    '''    public AS400Protocol(final String username, final byte[] password)
    public AS400Protocol(final String username, final byte[] password, final String hostname)
    public AS400Protocol(final ProfileTokenCredential profileToken)
    public AS400Protocol(final ProfileTokenCredential profileToken, final String hostname)
    '''
def getAS400System():
    '''    public AS400 getAS400System()
    '''
def clone():
    '''    public Object clone()
    '''
def getOS():
    '''    public synchronized OSInfo getOS()
    '''
def getProcessor():
    '''    public synchronized Processor[] getProcessor()
    '''
def getProcessorFamily():
    '''    public synchronized ProcessorArchEnum getProcessorFamily()
    '''
def putFile():
    '''    public synchronized void putFile(final String localFilename, final String remotePath)
    public synchronized void putFile(final String localFilename, final String remotePath, final boolean append)
    public synchronized void putFile(final String localFilename, final String remotePath, final boolean append, final int CCSID)
    '''
def putTextFile():
    '''    public synchronized void putTextFile(final String localFilename, final String remotePath, final boolean append, final String inputFileCharsetName, final int CCSID)
    '''
def getFile():
    '''    public synchronized void getFile(final String remoteFile, final String localPath)
    '''
def getTextFile():
    '''    public synchronized void getTextFile(final String remoteFile, final String localPath, final String localCharsetName)
    '''
def getRXAInputStream():
    '''    public synchronized RXAInputStream getRXAInputStream(final String remoteFile)
    '''
def getRXAOutputStream():
    '''    public synchronized RXAOutputStream getRXAOutputStream(final String remoteFile, final boolean append)
    '''
def putZIPFile():
    '''    public synchronized void putZIPFile(final String localFile, final String remoteDirectory)
    '''
def run():
    '''    public synchronized ProgramOutput run(final String command)
    public synchronized ProgramOutput run(final String command, final int timeout)
    '''
def runProgram():
    '''    public synchronized ProgramOutput runProgram(final String program, final ProgramParameter[] ParameterList)
    '''
def listFiles():
    '''    public synchronized FileInfo[] listFiles(final String remotePath)
    '''
def exists():
    '''    public synchronized boolean exists(String remotePath)
    '''
def rm():
    '''    public synchronized void rm(final String remotePath, final boolean recursive, final boolean force)
    '''
def shutdown():
    '''    public synchronized void shutdown(final boolean reboot, final String msg, final int delay)
    '''
def getPhysicalMemory():
    '''    public synchronized int getPhysicalMemory()
    '''
def getProcessInfo():
    '''    public synchronized ProcessInfo[] getProcessInfo()
    public synchronized ProcessInfo[] getProcessInfo(final int processID)
    '''
def getTCPPortInfo():
    '''    public synchronized PortInfo[] getTCPPortInfo()
    public synchronized PortInfo[] getTCPPortInfo(final int port)
    '''
def getEnvValue():
    '''    public synchronized String getEnvValue(String varname)
    '''
def getCurrentDirectory():
    '''    public synchronized String getCurrentDirectory()
    '''
def setCurrentDirectory():
    '''    public synchronized String setCurrentDirectory(final String dir)
    '''
def getTempDir():
    '''    public String getTempDir()
    '''
def mkDir():
    '''    public synchronized void mkDir(final String remoteDirectory)
    '''
def mkDirs():
    '''    public synchronized void mkDirs(final String remoteDirectory)
    '''
def mkRandomDirectory():
    '''    public synchronized String mkRandomDirectory(final String remoteDirectory)
    '''
def getFreeSpace():
    '''    public synchronized long getFreeSpace(String remoteDir)
    '''
def chmod():
    '''    public synchronized void chmod(String remotePath, String mode)
    public synchronized void chmod(String remotePath, final Permission perm)
    '''
def isPrivilegedLogin():
    '''    public synchronized boolean isPrivilegedLogin(String login)
    '''
def isForceSecure():
    '''    public boolean isForceSecure()
    '''
def setForceSecure():
    '''    public void setForceSecure(final boolean forceSecure)
    '''
def getRemoteCharset():
    '''    public Charset getRemoteCharset(final CharsetType t)
    public Charset getRemoteCharset()
    '''
def getFileWriter():
    '''    public ConvertingWriter getFileWriter(final String fileName, CharsetEncoder encoder, final String lineSeparator, final boolean append)
    '''
def getFileCharset():
    '''    public Charset getFileCharset(final String remoteFile)
    '''
def setFileCharset():
    '''    public void setFileCharset(final String remotePath, final Charset charSet)
    '''
def setServicePort():
    '''    public void setServicePort(final int service, final int port)
    '''
def setProxyServer():
    '''    public void setProxyServer(final String proxyServer)
    '''
def getServicePort():
    '''    public int getServicePort(final int service)
    '''
def getProxyServer():
    '''    public String getProxyServer()
    '''
def getGuiAvailable():
    '''    public boolean getGuiAvailable()
    '''
def setGuiAvailable():
    '''    public void setGuiAvailable(final boolean value)
    '''
