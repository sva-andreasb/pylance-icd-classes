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
pass
def run():
'''public Object run()
public Object run()
public Object run()
public void run()
'''
pass
def setDebugEnabled():
'''public void setDebugEnabled(final boolean debugEnabled, final Handler handler)
'''
pass
def connect():
'''public int connect(final InetAddress address, final AuthMethod authMethod)
public int connect(final InetSocketAddress inetSocketAddress, final int timeout, final AuthMethod authMethod, final Locale locale)
'''
pass
def retryAuth():
'''public int retryAuth(final AuthMethod authMethod)
'''
pass
def getClientVersion():
'''public String getClientVersion()
'''
pass
def getServerVersion():
'''public String getServerVersion()
'''
pass
def getClientKexList():
'''public String[] getClientKexList()
'''
pass
def getServerKexList():
'''public String[] getServerKexList()
'''
pass
def getDecidedKex():
'''public String getDecidedKex()
'''
pass
def getClientHostKeyList():
'''public String[] getClientHostKeyList()
'''
pass
def getServerHostKeyList():
'''public String[] getServerHostKeyList()
'''
pass
def getDecidedServerHostKey():
'''public String getDecidedServerHostKey()
'''
pass
def getClientEncryptionList():
'''public String[] getClientEncryptionList()
'''
pass
def getServerEncryptionLocalList():
'''public String[] getServerEncryptionLocalList()
'''
pass
def getDecidedLocalEncryption():
'''public String getDecidedLocalEncryption()
'''
pass
def getServerEncryptionRemoteList():
'''public String[] getServerEncryptionRemoteList()
'''
pass
def getDecidedRemoteEncryption():
'''public String getDecidedRemoteEncryption()
'''
pass
def getClientMacList():
'''public String[] getClientMacList()
'''
pass
def getServerMacLocalList():
'''public String[] getServerMacLocalList()
'''
pass
def getDecidedLocalMac():
'''public String getDecidedLocalMac()
'''
pass
def getServerMacRemoteList():
'''public String[] getServerMacRemoteList()
'''
pass
def getDecidedRemoteMac():
'''public String getDecidedRemoteMac()
'''
pass
def getClientCompressionList():
'''public String[] getClientCompressionList()
'''
pass
def getServerCompressionLocalList():
'''public String[] getServerCompressionLocalList()
'''
pass
def getDecidedLocalCompression():
'''public String getDecidedLocalCompression()
'''
pass
def getServerCompressionRemoteList():
'''public String[] getServerCompressionRemoteList()
'''
pass
def getDecidedRemoteCompression():
'''public String getDecidedRemoteCompression()
'''
pass
def getServerLanguageLocalList():
'''public String[] getServerLanguageLocalList()
'''
pass
def getServerLanguageRemoteList():
'''public String[] getServerLanguageRemoteList()
'''
pass
def getFingerprint():
'''public Fingerprint getFingerprint()
'''
pass
def executeCommand():
'''public SecureProcess executeCommand(final String command)
public SecureProcess executeCommand(final String command, final boolean usePty)
public SecureProcess executeCommand(final String command, final String terminal, final int rows, final int columns, final String[] environment)
'''
pass
def openShell():
'''public SecureShell openShell()
public SecureShell openShell(final String terminal, final int rows, final int columns, final String[] environment)
'''
pass
def openSFTP():
'''public SecureFTP openSFTP()
'''
pass
def forwardLocalPort():
'''public boolean forwardLocalPort(final InetSocketAddress originAddress, final InetSocketAddress hostAddress)
'''
pass
def openPublicKeyExchange():
'''public SecurePublicKeyExchange openPublicKeyExchange()
'''
pass
def disconnect():
'''public void disconnect()
public void disconnect(final int reasonCode, final String description)
'''
pass
def getConnectionStatus():
'''public int getConnectionStatus()
'''
pass
