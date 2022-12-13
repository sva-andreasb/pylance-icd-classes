def SSLContextBuilder():
'''public SSLContextBuilder()
'''
pass
def useTLS():
'''public SSLContextBuilder useTLS()
'''
pass
def useSSL():
'''public SSLContextBuilder useSSL()
'''
pass
def useProtocol():
'''public SSLContextBuilder useProtocol(final String protocol)
'''
pass
def setSecureRandom():
'''public SSLContextBuilder setSecureRandom(final SecureRandom secureRandom)
'''
pass
def loadTrustMaterial():
'''public SSLContextBuilder loadTrustMaterial(final KeyStore truststore, final TrustStrategy trustStrategy)
public SSLContextBuilder loadTrustMaterial(final KeyStore truststore)
'''
pass
def loadKeyMaterial():
'''public SSLContextBuilder loadKeyMaterial(final KeyStore keystore, final char[] keyPassword)
public SSLContextBuilder loadKeyMaterial(final KeyStore keystore, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
'''
pass
def build():
'''public SSLContext build()
'''
pass
def checkClientTrusted():
'''public void checkClientTrusted(final X509Certificate[] chain, final String authType)
'''
pass
def checkServerTrusted():
'''public void checkServerTrusted(final X509Certificate[] chain, final String authType)
'''
pass
def getAcceptedIssuers():
'''public X509Certificate[] getAcceptedIssuers()
'''
pass
def getClientAliases():
'''public String[] getClientAliases(final String keyType, final Principal[] issuers)
'''
pass
def chooseClientAlias():
'''public String chooseClientAlias(final String[] keyTypes, final Principal[] issuers, final Socket socket)
'''
pass
def getServerAliases():
'''public String[] getServerAliases(final String keyType, final Principal[] issuers)
'''
pass
def chooseServerAlias():
'''public String chooseServerAlias(final String keyType, final Principal[] issuers, final Socket socket)
'''
pass
def getCertificateChain():
'''public X509Certificate[] getCertificateChain(final String alias)
'''
pass
def getPrivateKey():
'''public PrivateKey getPrivateKey(final String alias)
'''
pass
