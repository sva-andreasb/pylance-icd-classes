def create():
    '''public static SSLContextBuilder create()
    '''
def SSLContextBuilder():
    '''public SSLContextBuilder()
    '''
def useProtocol():
    '''public SSLContextBuilder useProtocol(final String protocol)
    '''
def setSecureRandom():
    '''public SSLContextBuilder setSecureRandom(final SecureRandom secureRandom)
    '''
def loadTrustMaterial():
    '''public SSLContextBuilder loadTrustMaterial(final KeyStore truststore, final TrustStrategy trustStrategy)
    public SSLContextBuilder loadTrustMaterial(final TrustStrategy trustStrategy)
    public SSLContextBuilder loadTrustMaterial(final File file, final char[] storePassword, final TrustStrategy trustStrategy)
    public SSLContextBuilder loadTrustMaterial(final File file, final char[] storePassword)
    public SSLContextBuilder loadTrustMaterial(final File file)
    public SSLContextBuilder loadTrustMaterial(final URL url, final char[] storePassword, final TrustStrategy trustStrategy)
    public SSLContextBuilder loadTrustMaterial(final URL url, final char[] storePassword)
    '''
def loadKeyMaterial():
    '''public SSLContextBuilder loadKeyMaterial(final KeyStore keystore, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
    public SSLContextBuilder loadKeyMaterial(final KeyStore keystore, final char[] keyPassword)
    public SSLContextBuilder loadKeyMaterial(final File file, final char[] storePassword, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
    public SSLContextBuilder loadKeyMaterial(final File file, final char[] storePassword, final char[] keyPassword)
    public SSLContextBuilder loadKeyMaterial(final URL url, final char[] storePassword, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)
    public SSLContextBuilder loadKeyMaterial(final URL url, final char[] storePassword, final char[] keyPassword)
    '''
def build():
    '''public SSLContext build()
    '''
def checkClientTrusted():
    '''public void checkClientTrusted(final X509Certificate[] chain, final String authType)
    '''
def checkServerTrusted():
    '''public void checkServerTrusted(final X509Certificate[] chain, final String authType)
    '''
def getAcceptedIssuers():
    '''public X509Certificate[] getAcceptedIssuers()
    '''
def getClientAliases():
    '''public String[] getClientAliases(final String keyType, final Principal[] issuers)
    '''
def getClientAliasMap():
    '''public Map<String, PrivateKeyDetails> getClientAliasMap(final String[] keyTypes, final Principal[] issuers)
    '''
def getServerAliasMap():
    '''public Map<String, PrivateKeyDetails> getServerAliasMap(final String keyType, final Principal[] issuers)
    '''
def chooseClientAlias():
    '''public String chooseClientAlias(final String[] keyTypes, final Principal[] issuers, final Socket socket)
    '''
def getServerAliases():
    '''public String[] getServerAliases(final String keyType, final Principal[] issuers)
    '''
def chooseServerAlias():
    '''public String chooseServerAlias(final String keyType, final Principal[] issuers, final Socket socket)
    '''
def getCertificateChain():
    '''public X509Certificate[] getCertificateChain(final String alias)
    '''
def getPrivateKey():
    '''public PrivateKey getPrivateKey(final String alias)
    '''
def chooseEngineClientAlias():
    '''public String chooseEngineClientAlias(final String[] keyTypes, final Principal[] issuers, final SSLEngine sslEngine)
    '''
def chooseEngineServerAlias():
    '''public String chooseEngineServerAlias(final String keyType, final Principal[] issuers, final SSLEngine sslEngine)
    '''
