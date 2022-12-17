def mkdirs():
    '''returns boolean\n\n
    mkdirs(final String directory)\n
    '''
def getCurrentDir():
    '''returns String\n\n
    getCurrentDir()\n
    '''
def putZIPFile():
    '''returns None\n\n
    putZIPFile(final String localFile, String remoteDir)\n
    '''
def runScript():
    '''returns String[]\n\n
    runScript(final String commandScript, final String argumentString, final String remoteDir)\n
    runScript(String commandScript, final String argumentString, final String remoteDir, final int timeout)\n
    runScript(final String commandScript, final String argumentString)\n
    runScript(final String commandScript, final String argumentString, final int timeout)\n
    '''
def whatServicePackLevel():
    '''returns String\n\n
    whatServicePackLevel()\n
    '''
def is64Bit():
    '''returns boolean\n\n
    is64Bit()\n
    '''
def whatKindOfOS():
    '''returns String\n\n
    whatKindOfOS()\n
    '''
def whatTypeOfOS():
    '''returns String\n\n
    whatTypeOfOS()\n
    '''
def isWindows():
    '''returns boolean\n\n
    isWindows()\n
    '''
def isUnix():
    '''returns boolean\n\n
    isUnix()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def chmodFile():
    '''returns None\n\n
    chmodFile(final String remotePath, final String permissions)\n
    '''
def directoryExists():
    '''returns boolean\n\n
    directoryExists(final String remotePath)\n
    '''
def fileExists():
    '''returns boolean\n\n
    fileExists(final String remotePath)\n
    '''
def getFilePermission():
    '''returns String\n\n
    getFilePermission(final String remotePath)\n
    '''
def getFreeSpace():
    '''returns long\n\n
    getFreeSpace(final String remotePath)\n
    '''
def copyFile():
    '''returns None\n\n
    copyFile(final String remotePath, final String localPath)\n
    '''
def putFile():
    '''returns String\n\n
    putFile(String remotePath, final String localPath)\n
    '''
def rmFile():
    '''returns None\n\n
    rmFile(final String remoteFilePath, final boolean force)\n
    '''
def rmDir():
    '''returns None\n\n
    rmDir(final String remoteDirPath, final boolean recursive, final boolean force)\n
    '''
def setCurrentDir():
    '''returns None\n\n
    setCurrentDir(final String remotePath)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getRemoteHost():
    '''returns String\n\n
    getRemoteHost()\n
    '''
def isAIX():
    '''returns boolean\n\n
    isAIX()\n
    '''
def isSolaris():
    '''returns boolean\n\n
    isSolaris()\n
    '''
def isHPUX():
    '''returns boolean\n\n
    isHPUX()\n
    '''
def isWinXP():
    '''returns boolean\n\n
    isWinXP()\n
    '''
def setEnv():
    '''returns None\n\n
    setEnv(final String var, final String value)\n
    '''
def isWin2003():
    '''returns boolean\n\n
    isWin2003()\n
    '''
def getTempDir():
    '''returns String\n\n
    getTempDir()\n
    '''
def isWritable():
    '''returns boolean\n\n
    isWritable(String fileName)\n
    '''
