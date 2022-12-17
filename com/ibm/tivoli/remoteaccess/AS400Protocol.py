def ():
    '''returns AS400Protocol\n\n
    (final String username, final byte[] password)\n
    (final String username, final byte[] password, final String hostname)\n
    (final ProfileTokenCredential profileToken)\n
    (final ProfileTokenCredential profileToken, final String hostname)\n
    '''
def getAS400System():
    '''returns AS400\n\n
    getAS400System()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getTempDir():
    '''returns String\n\n
    getTempDir()\n
    '''
def isForceSecure():
    '''returns boolean\n\n
    isForceSecure()\n
    '''
def setForceSecure():
    '''returns None\n\n
    setForceSecure(final boolean forceSecure)\n
    '''
def getRemoteCharset():
    '''returns Charset\n\n
    getRemoteCharset(final CharsetType t)\n
    getRemoteCharset()\n
    '''
def getFileWriter():
    '''returns ConvertingWriter\n\n
    getFileWriter(final String fileName, CharsetEncoder encoder, final String lineSeparator, final boolean append)\n
    '''
def getFileCharset():
    '''returns Charset\n\n
    getFileCharset(final String remoteFile)\n
    '''
def setFileCharset():
    '''returns None\n\n
    setFileCharset(final String remotePath, final Charset charSet)\n
    '''
def setServicePort():
    '''returns None\n\n
    setServicePort(final int service, final int port)\n
    '''
def setProxyServer():
    '''returns None\n\n
    setProxyServer(final String proxyServer)\n
    '''
def getServicePort():
    '''returns int\n\n
    getServicePort(final int service)\n
    '''
def getProxyServer():
    '''returns String\n\n
    getProxyServer()\n
    '''
def getGuiAvailable():
    '''returns boolean\n\n
    getGuiAvailable()\n
    '''
def setGuiAvailable():
    '''returns None\n\n
    setGuiAvailable(final boolean value)\n
    '''
