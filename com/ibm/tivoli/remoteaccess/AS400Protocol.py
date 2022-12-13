def AS400Protocol():
'''public AS400Protocol(final String username, final byte[] password)
public AS400Protocol(final String username, final byte[] password, final String hostname)
public AS400Protocol(final ProfileTokenCredential profileToken)
public AS400Protocol(final ProfileTokenCredential profileToken, final String hostname)
'''
pass
def getAS400System():
'''public AS400 getAS400System()
'''
pass
def clone():
'''public Object clone()
'''
pass
def getOS():
'''public synchronized OSInfo getOS()
'''
pass
def getProcessor():
'''public synchronized Processor[] getProcessor()
'''
pass
def getProcessorFamily():
'''public synchronized ProcessorArchEnum getProcessorFamily()
'''
pass
def putFile():
'''public synchronized void putFile(final String localFilename, final String remotePath)
public synchronized void putFile(final String localFilename, final String remotePath, final boolean append)
public synchronized void putFile(final String localFilename, final String remotePath, final boolean append, final int CCSID)
'''
pass
def putTextFile():
'''public synchronized void putTextFile(final String localFilename, final String remotePath, final boolean append, final String inputFileCharsetName, final int CCSID)
'''
pass
def getFile():
'''public synchronized void getFile(final String remoteFile, final String localPath)
'''
pass
def getTextFile():
'''public synchronized void getTextFile(final String remoteFile, final String localPath, final String localCharsetName)
'''
pass
def getRXAInputStream():
'''public synchronized RXAInputStream getRXAInputStream(final String remoteFile)
'''
pass
def getRXAOutputStream():
'''public synchronized RXAOutputStream getRXAOutputStream(final String remoteFile, final boolean append)
'''
pass
def putZIPFile():
'''public synchronized void putZIPFile(final String localFile, final String remoteDirectory)
'''
pass
def run():
'''public synchronized ProgramOutput run(final String command)
public synchronized ProgramOutput run(final String command, final int timeout)
'''
pass
def runProgram():
'''public synchronized ProgramOutput runProgram(final String program, final ProgramParameter[] ParameterList)
'''
pass
def listFiles():
'''public synchronized FileInfo[] listFiles(final String remotePath)
'''
pass
def exists():
'''public synchronized boolean exists(String remotePath)
'''
pass
def rm():
'''public synchronized void rm(final String remotePath, final boolean recursive, final boolean force)
'''
pass
def shutdown():
'''public synchronized void shutdown(final boolean reboot, final String msg, final int delay)
'''
pass
def getPhysicalMemory():
'''public synchronized int getPhysicalMemory()
'''
pass
def getProcessInfo():
'''public synchronized ProcessInfo[] getProcessInfo()
public synchronized ProcessInfo[] getProcessInfo(final int processID)
'''
pass
def getTCPPortInfo():
'''public synchronized PortInfo[] getTCPPortInfo()
public synchronized PortInfo[] getTCPPortInfo(final int port)
'''
pass
def getEnvValue():
'''public synchronized String getEnvValue(String varname)
'''
pass
def getCurrentDirectory():
'''public synchronized String getCurrentDirectory()
'''
pass
def setCurrentDirectory():
'''public synchronized String setCurrentDirectory(final String dir)
'''
pass
def getTempDir():
'''public String getTempDir()
'''
pass
def mkDir():
'''public synchronized void mkDir(final String remoteDirectory)
'''
pass
def mkDirs():
'''public synchronized void mkDirs(final String remoteDirectory)
'''
pass
def mkRandomDirectory():
'''public synchronized String mkRandomDirectory(final String remoteDirectory)
'''
pass
def getFreeSpace():
'''public synchronized long getFreeSpace(String remoteDir)
'''
pass
def chmod():
'''public synchronized void chmod(String remotePath, String mode)
public synchronized void chmod(String remotePath, final Permission perm)
'''
pass
def isPrivilegedLogin():
'''public synchronized boolean isPrivilegedLogin(String login)
'''
pass
def isForceSecure():
'''public boolean isForceSecure()
'''
pass
def setForceSecure():
'''public void setForceSecure(final boolean forceSecure)
'''
pass
def getRemoteCharset():
'''public Charset getRemoteCharset(final CharsetType t)
public Charset getRemoteCharset()
'''
pass
def getFileWriter():
'''public ConvertingWriter getFileWriter(final String fileName, CharsetEncoder encoder, final String lineSeparator, final boolean append)
'''
pass
def getFileCharset():
'''public Charset getFileCharset(final String remoteFile)
'''
pass
def setFileCharset():
'''public void setFileCharset(final String remotePath, final Charset charSet)
'''
pass
def setServicePort():
'''public void setServicePort(final int service, final int port)
'''
pass
def setProxyServer():
'''public void setProxyServer(final String proxyServer)
'''
pass
def getServicePort():
'''public int getServicePort(final int service)
'''
pass
def getProxyServer():
'''public String getProxyServer()
'''
pass
def getGuiAvailable():
'''public boolean getGuiAvailable()
'''
pass
def setGuiAvailable():
'''public void setGuiAvailable(final boolean value)
'''
pass
