def ():
    '''returns SSHProtocol\n\n
    ()\n
    (final String username, final byte[] password)\n
    (final String username, final byte[] password, final String hostname)\n
    (final File privateKeyStore, final String username, final byte[] passPhrase)\n
    (final File privateKeyStore, final String username, final byte[] passPhrase, final String hostname)\n
    (final KeyPair keyPair, final String username)\n
    (final KeyPair keyPair, final String username, final String hostname)\n
    '''
def exec():
    '''returns RemoteProcess\n\n
    exec(final String command)\n
    '''
def getServerVersion():
    '''returns String\n\n
    getServerVersion()\n
    '''
def getHostKey():
    '''returns HostKey\n\n
    getHostKey()\n
    '''
def installKey():
    '''returns None\n\n
    installKey(final PublicKey publicKey)\n
    installKey(final File publicKeyFile)\n
    '''
def getSecureSession():
    '''returns SecureSession\n\n
    getSecureSession()\n
    '''
