def clone():
'''public synchronized Object clone()
'''
pass
def getOS():
'''public synchronized OSInfo getOS()
'''
pass
def getPhysicalMemory():
'''public synchronized int getPhysicalMemory()
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
'''public synchronized void putFile(final String localFile, String remotePath)
'''
pass
def getFile():
'''public synchronized void getFile(String remoteFile, String localPath)
'''
pass
def putZIPFile():
'''public synchronized void putZIPFile(final String localFile, String remoteDir)
'''
pass
def getRXAOutputStream():
'''public synchronized RXAOutputStream getRXAOutputStream(String remoteFile, final boolean append)
'''
pass
def getRXAInputStream():
'''public synchronized RXAInputStream getRXAInputStream(String remoteFile)
'''
pass
def run():
'''public synchronized ProgramOutput run(final String command)
public synchronized ProgramOutput run(final String command, final int timeout)
'''
pass
def listFiles():
'''public synchronized FileInfo[] listFiles(String remotePath)
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
'''public synchronized String setCurrentDirectory(final String RemoteDir)
'''
pass
def getEnv():
'''public synchronized String[] getEnv()
'''
pass
def setEnv():
'''public synchronized void setEnv(final String var, final String value)
'''
pass
def getEnvValue():
'''public synchronized String getEnvValue(String varname)
'''
pass
def getTempDir():
'''public synchronized String getTempDir()
'''
pass
def mkDir():
'''public synchronized void mkDir(final String remoteDir)
'''
pass
def mkDirs():
'''public synchronized void mkDirs(final String remoteDir)
'''
pass
def mkRandomDirectory():
'''public synchronized String mkRandomDirectory(String remoteDir)
'''
pass
def getFreeSpace():
'''public synchronized long getFreeSpace(String remoteDir)
'''
pass
def chmod():
'''public synchronized void chmod(String remotePath, final String mode)
'''
pass
def chown():
'''public synchronized void chown(String remotePath, final String owner)
'''
pass
def chgrp():
'''public synchronized void chgrp(String remotePath, final String group)
'''
pass
def isPrivilegedLogin():
'''public synchronized boolean isPrivilegedLogin(String login)
'''
pass
def shutdown():
'''public synchronized void shutdown(final boolean reboot, final String msg, int delay)
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
def getPortNumber():
'''public synchronized int getPortNumber()
'''
pass
def setPortNumber():
'''public synchronized void setPortNumber(final int portnum)
'''
pass
