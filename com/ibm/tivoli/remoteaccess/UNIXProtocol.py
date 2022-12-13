def clone():
    '''public synchronized Object clone()
    '''
def getOS():
    '''public synchronized OSInfo getOS()
    '''
def getPhysicalMemory():
    '''public synchronized int getPhysicalMemory()
    '''
def getProcessorFamily():
    '''public synchronized ProcessorArchEnum getProcessorFamily()
    '''
def getProcessor():
    '''public synchronized Processor[] getProcessor()
    '''
def putFile():
    '''public synchronized void putFile(final String localFile, String remotePath)
    '''
def getFile():
    '''public synchronized void getFile(String remoteFile, String localPath)
    '''
def putZIPFile():
    '''public synchronized void putZIPFile(final String localFile, String remoteDir)
    '''
def getRXAOutputStream():
    '''public synchronized RXAOutputStream getRXAOutputStream(String remoteFile, final boolean append)
    '''
def getRXAInputStream():
    '''public synchronized RXAInputStream getRXAInputStream(String remoteFile)
    '''
def run():
    '''public synchronized ProgramOutput run(final String command)
    public synchronized ProgramOutput run(final String command, final int timeout)
    '''
def listFiles():
    '''public synchronized FileInfo[] listFiles(String remotePath)
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
    '''public synchronized String setCurrentDirectory(final String RemoteDir)
    '''
def getEnv():
    '''public synchronized String[] getEnv()
    '''
def setEnv():
    '''public synchronized void setEnv(final String var, final String value)
    '''
def getEnvValue():
    '''public synchronized String getEnvValue(String varname)
    '''
def getTempDir():
    '''public synchronized String getTempDir()
    '''
def mkDir():
    '''public synchronized void mkDir(final String remoteDir)
    '''
def mkDirs():
    '''public synchronized void mkDirs(final String remoteDir)
    '''
def mkRandomDirectory():
    '''public synchronized String mkRandomDirectory(String remoteDir)
    '''
def getFreeSpace():
    '''public synchronized long getFreeSpace(String remoteDir)
    '''
def chmod():
    '''public synchronized void chmod(String remotePath, final String mode)
    '''
def chown():
    '''public synchronized void chown(String remotePath, final String owner)
    '''
def chgrp():
    '''public synchronized void chgrp(String remotePath, final String group)
    '''
def isPrivilegedLogin():
    '''public synchronized boolean isPrivilegedLogin(String login)
    '''
def shutdown():
    '''public synchronized void shutdown(final boolean reboot, final String msg, int delay)
    '''
def getProcessInfo():
    '''public synchronized ProcessInfo[] getProcessInfo()
    public synchronized ProcessInfo[] getProcessInfo(final int processID)
    '''
def getTCPPortInfo():
    '''public synchronized PortInfo[] getTCPPortInfo()
    public synchronized PortInfo[] getTCPPortInfo(final int port)
    '''
def getPortNumber():
    '''public synchronized int getPortNumber()
    '''
def setPortNumber():
    '''public synchronized void setPortNumber(final int portnum)
    '''
