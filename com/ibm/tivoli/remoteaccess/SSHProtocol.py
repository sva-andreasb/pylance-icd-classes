def SSHProtocol():
'''public SSHProtocol()
public SSHProtocol(final String username, final byte[] password)
public SSHProtocol(final String username, final byte[] password, final String hostname)
public SSHProtocol(final File privateKeyStore, final String username, final byte[] passPhrase)
public SSHProtocol(final File privateKeyStore, final String username, final byte[] passPhrase, final String hostname)
public SSHProtocol(final KeyPair keyPair, final String username)
public SSHProtocol(final KeyPair keyPair, final String username, final String hostname)
'''
pass
def clone():
'''public synchronized Object clone()
'''
pass
def exec():
'''public RemoteProcess exec(final String command)
'''
pass
def getServerVersion():
'''public String getServerVersion()
'''
pass
def getHostKey():
'''public HostKey getHostKey()
'''
pass
def installKey():
'''public void installKey(final PublicKey publicKey)
public void installKey(final File publicKeyFile)
'''
pass
def getSecureSession():
'''public SecureSession getSecureSession()
'''
pass
