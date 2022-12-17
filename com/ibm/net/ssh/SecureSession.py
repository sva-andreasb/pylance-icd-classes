DEFAULT_PORT = "int  22"
DEFAULT_TIMEOUT = "int  15000"
NO_CONNECTION = "int  0"
CONNECTION_SUCCESS = "int  1"
NO_SSH_SERVER = "int  2"
UNSUPPORTED_VERSION = "int  3"
CONNECTION_FAILED = "int  4"
AUTHENTICATION_FAILED = "int  5"
def ():
    '''returns SecureSession\n\n
    ()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def setDebugEnabled():
    '''returns None\n\n
    setDebugEnabled(final boolean debugEnabled, final Handler handler)\n
    '''
def connect():
    '''returns int\n\n
    connect(final InetAddress address, final AuthMethod authMethod)\n
    connect(final InetSocketAddress inetSocketAddress, final int timeout, final AuthMethod authMethod, final Locale locale)\n
    '''
def retryAuth():
    '''returns int\n\n
    retryAuth(final AuthMethod authMethod)\n
    '''
def getClientVersion():
    '''returns String\n\n
    getClientVersion()\n
    '''
def getServerVersion():
    '''returns String\n\n
    getServerVersion()\n
    '''
def getClientKexList():
    '''returns String[]\n\n
    getClientKexList()\n
    '''
def getServerKexList():
    '''returns String[]\n\n
    getServerKexList()\n
    '''
def getDecidedKex():
    '''returns String\n\n
    getDecidedKex()\n
    '''
def getClientHostKeyList():
    '''returns String[]\n\n
    getClientHostKeyList()\n
    '''
def getServerHostKeyList():
    '''returns String[]\n\n
    getServerHostKeyList()\n
    '''
def getDecidedServerHostKey():
    '''returns String\n\n
    getDecidedServerHostKey()\n
    '''
def getClientEncryptionList():
    '''returns String[]\n\n
    getClientEncryptionList()\n
    '''
def getServerEncryptionLocalList():
    '''returns String[]\n\n
    getServerEncryptionLocalList()\n
    '''
def getDecidedLocalEncryption():
    '''returns String\n\n
    getDecidedLocalEncryption()\n
    '''
def getServerEncryptionRemoteList():
    '''returns String[]\n\n
    getServerEncryptionRemoteList()\n
    '''
def getDecidedRemoteEncryption():
    '''returns String\n\n
    getDecidedRemoteEncryption()\n
    '''
def getClientMacList():
    '''returns String[]\n\n
    getClientMacList()\n
    '''
def getServerMacLocalList():
    '''returns String[]\n\n
    getServerMacLocalList()\n
    '''
def getDecidedLocalMac():
    '''returns String\n\n
    getDecidedLocalMac()\n
    '''
def getServerMacRemoteList():
    '''returns String[]\n\n
    getServerMacRemoteList()\n
    '''
def getDecidedRemoteMac():
    '''returns String\n\n
    getDecidedRemoteMac()\n
    '''
def getClientCompressionList():
    '''returns String[]\n\n
    getClientCompressionList()\n
    '''
def getServerCompressionLocalList():
    '''returns String[]\n\n
    getServerCompressionLocalList()\n
    '''
def getDecidedLocalCompression():
    '''returns String\n\n
    getDecidedLocalCompression()\n
    '''
def getServerCompressionRemoteList():
    '''returns String[]\n\n
    getServerCompressionRemoteList()\n
    '''
def getDecidedRemoteCompression():
    '''returns String\n\n
    getDecidedRemoteCompression()\n
    '''
def getServerLanguageLocalList():
    '''returns String[]\n\n
    getServerLanguageLocalList()\n
    '''
def getServerLanguageRemoteList():
    '''returns String[]\n\n
    getServerLanguageRemoteList()\n
    '''
def getFingerprint():
    '''returns Fingerprint\n\n
    getFingerprint()\n
    '''
def executeCommand():
    '''returns SecureProcess\n\n
    executeCommand(final String command)\n
    executeCommand(final String command, final boolean usePty)\n
    executeCommand(final String command, final String terminal, final int rows, final int columns, final String[] environment)\n
    '''
def openShell():
    '''returns SecureShell\n\n
    openShell()\n
    openShell(final String terminal, final int rows, final int columns, final String[] environment)\n
    '''
def openSFTP():
    '''returns SecureFTP\n\n
    openSFTP()\n
    '''
def forwardLocalPort():
    '''returns boolean\n\n
    forwardLocalPort(final InetSocketAddress originAddress, final InetSocketAddress hostAddress)\n
    '''
def openPublicKeyExchange():
    '''returns SecurePublicKeyExchange\n\n
    openPublicKeyExchange()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    disconnect(final int reasonCode, final String description)\n
    '''
def getConnectionStatus():
    '''returns int\n\n
    getConnectionStatus()\n
    '''
