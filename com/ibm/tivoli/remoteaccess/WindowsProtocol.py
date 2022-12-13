def WindowsProtocol():
'''public WindowsProtocol()
public WindowsProtocol(final String username, final byte[] password)
public WindowsProtocol(final String username, final byte[] password, final String hostname)
'''
pass
def setTimeout():
'''public synchronized void setTimeout(final int time)
'''
pass
def setNetBIOSPort():
'''public synchronized void setNetBIOSPort(final int port)
'''
pass
def setSMBPort():
'''public synchronized void setSMBPort(final int port)
'''
pass
def setSMBTransportType():
'''public synchronized void setSMBTransportType(final SMBTransportType type)
'''
pass
def setNetBIOSNamePort():
'''public synchronized void setNetBIOSNamePort(final int port)
'''
pass
def setUsername():
'''public synchronized void setUsername(final String userName)
'''
pass
def getNetBIOSPort():
'''public synchronized int getNetBIOSPort()
'''
pass
def getSMBPort():
'''public synchronized int getSMBPort()
'''
pass
def getNetBIOSNamePort():
'''public synchronized int getNetBIOSNamePort()
'''
pass
def getSMBTransportType():
'''public synchronized SMBTransportType getSMBTransportType()
'''
pass
def getPhysicalMemory():
'''public synchronized int getPhysicalMemory()
'''
pass
def clone():
'''public synchronized Object clone()
'''
pass
def getOS():
'''public synchronized OSInfo getOS()
'''
pass
def getProcessorFamily():
'''public synchronized ProcessorArchEnum getProcessorFamily()
'''
pass
def getProcessor():
'''public synchronized Processor[] getProcessor()
'''
pass
def putFile():
'''public synchronized void putFile(final String localFilename, final String remotePath)
'''
pass
def getFile():
'''public synchronized void getFile(final String remoteFile, String localPath)
'''
pass
def putZIPFile():
'''public synchronized void putZIPFile(final String localFile, final String remoteDirectory)
'''
pass
def getRXAOutputStream():
'''public synchronized RXAOutputStream getRXAOutputStream(final String remoteFile, final boolean append)
'''
pass
def getRXAInputStream():
'''public synchronized RXAInputStream getRXAInputStream(final String remoteFile)
'''
pass
def run():
'''public synchronized ProgramOutput run(final String commandLine)
public synchronized ProgramOutput run(final String commandLine, final int timeout)
public synchronized ProgramOutput run(final String commandLine, final String workingDir, final int timeout, final boolean interactive)
public synchronized ProgramOutput run(final String commandLine, String workingDir, final int timeout, final boolean interactive, final boolean asSystem)
'''
pass
def listFiles():
'''public synchronized FileInfo[] listFiles(final String remotePath)
'''
pass
def exists():
'''public synchronized boolean exists(final String remotePath)
'''
pass
def rm():
'''public synchronized void rm(final String remotePath, final boolean recursive, final boolean force)
'''
pass
def getCurrentDirectory():
'''public synchronized String getCurrentDirectory()
'''
pass
def setCurrentDirectory():
'''public synchronized String setCurrentDirectory(final String remoteDirectory)
'''
pass
def getTempDir():
'''public synchronized String getTempDir()
'''
pass
def mkDir():
'''public synchronized void mkDir(final String remoteDirectory)
'''
pass
def mkDirs():
'''public synchronized void mkDirs(String remoteDirectory)
'''
pass
def mkRandomDirectory():
'''public synchronized String mkRandomDirectory(String remoteDirectory)
'''
pass
def getFreeSpace():
'''public synchronized long getFreeSpace(final String remoteDirectory)
'''
pass
def setShare():
'''public synchronized String setShare(final String shr)
'''
pass
def chmod():
'''public synchronized void chmod(String remotePath, String mode)
'''
pass
def getSystemRoot():
'''public synchronized String getSystemRoot()
'''
pass
def getProgramFilesPath():
'''public synchronized String getProgramFilesPath()
'''
pass
def getCommonFilesPath():
'''public synchronized String getCommonFilesPath()
'''
pass
def getShareList():
'''public synchronized String[] getShareList()
'''
pass
def getServiceList():
'''public synchronized WindowsService[] getServiceList()
'''
pass
def getRegistryKeyString():
'''public synchronized String getRegistryKeyString(final String keypath)
'''
pass
def getRegistryKeyDWORD():
'''public synchronized long getRegistryKeyDWORD(final String keypath)
'''
pass
def getRegistryKeyBin():
'''public synchronized byte[] getRegistryKeyBin(final String keypath)
'''
pass
def getRegistryValueType():
'''public synchronized RegistryValueType getRegistryValueType(final String keypath)
'''
pass
def listRegistryValueNames():
'''public synchronized String[] listRegistryValueNames(final String keypath)
'''
pass
def listRegistrySubkeys():
'''public synchronized String[] listRegistrySubkeys(final String keypath)
'''
pass
def setRegistryValue():
'''public synchronized void setRegistryValue(final String keypath, final String value)
public synchronized void setRegistryValue(final String keypath, final long value)
public synchronized void setRegistryValue(final String keypath, final byte[] value)
public synchronized void setRegistryValue(final String keypath, final String value, final RegistryValueType type)
public synchronized void setRegistryValue(final String keypath, final long value, final RegistryValueType type)
public synchronized void setRegistryValue(final String keypath, final byte[] value, final RegistryValueType type)
'''
pass
def createRegistryKey():
'''public synchronized void createRegistryKey(final String keypath)
'''
pass
def deleteRegistryKey():
'''public synchronized void deleteRegistryKey(final String keypath)
'''
pass
def getNodeName():
'''public synchronized String getNodeName()
'''
pass
def getMACAddress():
'''public synchronized byte[] getMACAddress()
'''
pass
def getWSUsername():
'''public synchronized String getWSUsername()
'''
pass
def getWSDomain():
'''public synchronized String getWSDomain()
'''
pass
def getRegisteredOwner():
'''public synchronized String getRegisteredOwner()
'''
pass
def isPrivilegedLogin():
'''public synchronized boolean isPrivilegedLogin(String login)
'''
pass
def shutdown():
'''public synchronized void shutdown(final boolean reboot, String msg, final int delay)
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
