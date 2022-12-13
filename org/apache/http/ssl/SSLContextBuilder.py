def create():
'''public static SSLContextBuilder create()
'''
pass
def SSLContextBuilder():
'''public SSLContextBuilder()
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
public SSLContextBuilder loadTrustMaterial(final TrustStrategy trustStrategy)
public SSLContextBuilder loadTrustMaterial(final File file, final char[] storePassword, final TrustStrategy trustStrategy)
public SSLContextBuilder loadTrustMaterial(final File file, final char[] storePassword)
public SSLContextBuilder loadTrustMaterial(final File file)
public SSLContextBuilder loadTrustMaterial(final URL url, final char[] storePassword, final TrustStrategy trustStrategy)
public SSLContextBuilder loadTrustMaterial(final URL url, final char[] storePassword)
'''
pass
def loadKeyMaterial():
'''public SSLContextBuilder loadKeyMaterial(final KeyStore keystore, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
public SSLContextBuilder loadKeyMaterial(final KeyStore keystore, final char[] keyPassword)
public SSLContextBuilder loadKeyMaterial(final File file, final char[] storePassword, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
public SSLContextBuilder loadKeyMaterial(final File file, final char[] storePassword, final char[] keyPassword)
public SSLContextBuilder loadKeyMaterial(final URL url, final char[] storePassword, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
public SSLContextBuilder loadKeyMaterial(final URL url, final char[] storePassword, final char[] keyPassword)
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
def getClientAliasMap():
'''public Map<String, PrivateKeyDetails> getClientAliasMap(final String[] keyTypes, final Principal[] issuers)
'''
pass
def getServerAliasMap():
'''public Map<String, PrivateKeyDetails> getServerAliasMap(final String keyType, final Principal[] issuers)
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
def chooseEngineClientAlias():
'''public String chooseEngineClientAlias(final String[] keyTypes, final Principal[] issuers, final SSLEngine sslEngine)
'''
pass
def chooseEngineServerAlias():
'''public String chooseEngineServerAlias(final String keyType, final Principal[] issuers, final SSLEngine sslEngine)
'''
pass
