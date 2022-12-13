def WindowsProtocol():
    '''public WindowsProtocol()
    public WindowsProtocol(final String username, final byte[] password)
    public WindowsProtocol(final String username, final byte[] password, final String hostname)
    '''
def setTimeout():
    '''public synchronized void setTimeout(final int time)
    '''
def setNetBIOSPort():
    '''public synchronized void setNetBIOSPort(final int port)
    '''
def setSMBPort():
    '''public synchronized void setSMBPort(final int port)
    '''
def setSMBTransportType():
    '''public synchronized void setSMBTransportType(final SMBTransportType type)
    '''
def setNetBIOSNamePort():
    '''public synchronized void setNetBIOSNamePort(final int port)
    '''
def setUsername():
    '''public synchronized void setUsername(final String userName)
    '''
def getNetBIOSPort():
    '''public synchronized int getNetBIOSPort()
    '''
def getSMBPort():
    '''public synchronized int getSMBPort()
    '''
def getNetBIOSNamePort():
    '''public synchronized int getNetBIOSNamePort()
    '''
def getSMBTransportType():
    '''public synchronized SMBTransportType getSMBTransportType()
    '''
def getPhysicalMemory():
    '''public synchronized int getPhysicalMemory()
    '''
def clone():
    '''public synchronized Object clone()
    '''
def getOS():
    '''public synchronized OSInfo getOS()
    '''
def getProcessorFamily():
    '''public synchronized ProcessorArchEnum getProcessorFamily()
    '''
def getProcessor():
    '''public synchronized Processor[] getProcessor()
    '''
def putFile():
    '''public synchronized void putFile(final String localFilename, final String remotePath)
    '''
def getFile():
    '''public synchronized void getFile(final String remoteFile, String localPath)
    '''
def putZIPFile():
    '''public synchronized void putZIPFile(final String localFile, final String remoteDirectory)
    '''
def getRXAOutputStream():
    '''public synchronized RXAOutputStream getRXAOutputStream(final String remoteFile, final boolean append)
    '''
def getRXAInputStream():
    '''public synchronized RXAInputStream getRXAInputStream(final String remoteFile)
    '''
def run():
    '''public synchronized ProgramOutput run(final String commandLine)
    public synchronized ProgramOutput run(final String commandLine, final int timeout)
    public synchronized ProgramOutput run(final String commandLine, final String workingDir, final int timeout, final boolean interactive)
    public synchronized ProgramOutput run(final String commandLine, String workingDir, final int timeout, final boolean interactive, final boolean asSystem)
    '''
def listFiles():
    '''public synchronized FileInfo[] listFiles(final String remotePath)
    '''
def exists():
    '''public synchronized boolean exists(final String remotePath)
    '''
def rm():
    '''public synchronized void rm(final String remotePath, final boolean recursive, final boolean force)
    '''
def getCurrentDirectory():
    '''public synchronized String getCurrentDirectory()
    '''
def setCurrentDirectory():
    '''public synchronized String setCurrentDirectory(final String remoteDirectory)
    '''
def getTempDir():
    '''public synchronized String getTempDir()
    '''
def mkDir():
    '''public synchronized void mkDir(final String remoteDirectory)
    '''
def mkDirs():
    '''public synchronized void mkDirs(String remoteDirectory)
    '''
def mkRandomDirectory():
    '''public synchronized String mkRandomDirectory(String remoteDirectory)
    '''
def getFreeSpace():
    '''public synchronized long getFreeSpace(final String remoteDirectory)
    '''
def setShare():
    '''public synchronized String setShare(final String shr)
    '''
def chmod():
    '''public synchronized void chmod(String remotePath, String mode)
    '''
def getSystemRoot():
    '''public synchronized String getSystemRoot()
    '''
def getProgramFilesPath():
    '''public synchronized String getProgramFilesPath()
    '''
def getCommonFilesPath():
    '''public synchronized String getCommonFilesPath()
    '''
def getShareList():
    '''public synchronized String[] getShareList()
    '''
def getServiceList():
    '''public synchronized WindowsService[] getServiceList()
    '''
def getRegistryKeyString():
    '''public synchronized String getRegistryKeyString(final String keypath)
    '''
def getRegistryKeyDWORD():
    '''public synchronized long getRegistryKeyDWORD(final String keypath)
    '''
def getRegistryKeyBin():
    '''public synchronized byte[] getRegistryKeyBin(final String keypath)
    '''
def getRegistryValueType():
    '''public synchronized RegistryValueType getRegistryValueType(final String keypath)
    '''
def listRegistryValueNames():
    '''public synchronized String[] listRegistryValueNames(final String keypath)
    '''
def listRegistrySubkeys():
    '''public synchronized String[] listRegistrySubkeys(final String keypath)
    '''
def setRegistryValue():
    '''public synchronized void setRegistryValue(final String keypath, final String value)
    public synchronized void setRegistryValue(final String keypath, final long value)
    public synchronized void setRegistryValue(final String keypath, final byte[] value)
    public synchronized void setRegistryValue(final String keypath, final String value, final RegistryValueType type)
    public synchronized void setRegistryValue(final String keypath, final long value, final RegistryValueType type)
    public synchronized void setRegistryValue(final String keypath, final byte[] value, final RegistryValueType type)
    '''
def createRegistryKey():
    '''public synchronized void createRegistryKey(final String keypath)
    '''
def deleteRegistryKey():
    '''public synchronized void deleteRegistryKey(final String keypath)
    '''
def getNodeName():
    '''public synchronized String getNodeName()
    '''
def getMACAddress():
    '''public synchronized byte[] getMACAddress()
    '''
def getWSUsername():
    '''public synchronized String getWSUsername()
    '''
def getWSDomain():
    '''public synchronized String getWSDomain()
    '''
def getRegisteredOwner():
    '''public synchronized String getRegisteredOwner()
    '''
def isPrivilegedLogin():
    '''public synchronized boolean isPrivilegedLogin(String login)
    '''
def shutdown():
    '''public synchronized void shutdown(final boolean reboot, String msg, final int delay)
    '''
def getProcessInfo():
    '''public synchronized ProcessInfo[] getProcessInfo()
    public synchronized ProcessInfo[] getProcessInfo(final int processID)
    '''
def getTCPPortInfo():
    '''public synchronized PortInfo[] getTCPPortInfo()
    public synchronized PortInfo[] getTCPPortInfo(final int port)
    '''
def getEnvValue():
    '''public synchronized String getEnvValue(String varname)
    '''
