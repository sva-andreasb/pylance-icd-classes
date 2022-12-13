DEFAULT_PORT = "int  22"
DEFAULT_TIMEOUT = "int  15000"
NO_CONNECTION = "int  0"
CONNECTION_SUCCESS = "int  1"
NO_SSH_SERVER = "int  2"
UNSUPPORTED_VERSION = "int  3"
CONNECTION_FAILED = "int  4"
AUTHENTICATION_FAILED = "int  5"
def SecureSession():
    '''public SecureSession()
    '''
def run():
    '''public Object run()
    public Object run()
    public Object run()
    public void run()
    '''
def setDebugEnabled():
    '''public void setDebugEnabled(final boolean debugEnabled, final Handler handler)
    '''
def connect():
    '''public int connect(final InetAddress address, final AuthMethod authMethod)
    public int connect(final InetSocketAddress inetSocketAddress, final int timeout, final AuthMethod authMethod, final Locale locale)
    '''
def retryAuth():
    '''public int retryAuth(final AuthMethod authMethod)
    '''
def getClientVersion():
    '''public String getClientVersion()
    '''
def getServerVersion():
    '''public String getServerVersion()
    '''
def getClientKexList():
    '''public String[] getClientKexList()
    '''
def getServerKexList():
    '''public String[] getServerKexList()
    '''
def getDecidedKex():
    '''public String getDecidedKex()
    '''
def getClientHostKeyList():
    '''public String[] getClientHostKeyList()
    '''
def getServerHostKeyList():
    '''public String[] getServerHostKeyList()
    '''
def getDecidedServerHostKey():
    '''public String getDecidedServerHostKey()
    '''
def getClientEncryptionList():
    '''public String[] getClientEncryptionList()
    '''
def getServerEncryptionLocalList():
    '''public String[] getServerEncryptionLocalList()
    '''
def getDecidedLocalEncryption():
    '''public String getDecidedLocalEncryption()
    '''
def getServerEncryptionRemoteList():
    '''public String[] getServerEncryptionRemoteList()
    '''
def getDecidedRemoteEncryption():
    '''public String getDecidedRemoteEncryption()
    '''
def getClientMacList():
    '''public String[] getClientMacList()
    '''
def getServerMacLocalList():
    '''public String[] getServerMacLocalList()
    '''
def getDecidedLocalMac():
    '''public String getDecidedLocalMac()
    '''
def getServerMacRemoteList():
    '''public String[] getServerMacRemoteList()
    '''
def getDecidedRemoteMac():
    '''public String getDecidedRemoteMac()
    '''
def getClientCompressionList():
    '''public String[] getClientCompressionList()
    '''
def getServerCompressionLocalList():
    '''public String[] getServerCompressionLocalList()
    '''
def getDecidedLocalCompression():
    '''public String getDecidedLocalCompression()
    '''
def getServerCompressionRemoteList():
    '''public String[] getServerCompressionRemoteList()
    '''
def getDecidedRemoteCompression():
    '''public String getDecidedRemoteCompression()
    '''
def getServerLanguageLocalList():
    '''public String[] getServerLanguageLocalList()
    '''
def getServerLanguageRemoteList():
    '''public String[] getServerLanguageRemoteList()
    '''
def getFingerprint():
    '''public Fingerprint getFingerprint()
    '''
def executeCommand():
    '''public SecureProcess executeCommand(final String command)
    public SecureProcess executeCommand(final String command, final boolean usePty)
    public SecureProcess executeCommand(final String command, final String terminal, final int rows, final int columns, final String[] environment)
    '''
def openShell():
    '''public SecureShell openShell()
    public SecureShell openShell(final String terminal, final int rows, final int columns, final String[] environment)
    '''
def openSFTP():
    '''public SecureFTP openSFTP()
    '''
def forwardLocalPort():
    '''public boolean forwardLocalPort(final InetSocketAddress originAddress, final InetSocketAddress hostAddress)
    '''
def openPublicKeyExchange():
    '''public SecurePublicKeyExchange openPublicKeyExchange()
    '''
def disconnect():
    '''public void disconnect()
    public void disconnect(final int reasonCode, final String description)
    '''
def getConnectionStatus():
    '''public int getConnectionStatus()
    '''
