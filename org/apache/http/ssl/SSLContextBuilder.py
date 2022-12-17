def ():
    '''returns SSLContextBuilder\n\n
    ()\n
    '''
def useProtocol():
    '''returns SSLContextBuilder\n\n
    useProtocol(final String protocol)\n
    '''
def setSecureRandom():
    '''returns SSLContextBuilder\n\n
    setSecureRandom(final SecureRandom secureRandom)\n
    '''
def loadTrustMaterial():
    '''returns SSLContextBuilder\n\n
    loadTrustMaterial(final KeyStore truststore, final TrustStrategy trustStrategy)\n
    loadTrustMaterial(final TrustStrategy trustStrategy)\n
    loadTrustMaterial(final File file, final char[] storePassword, final TrustStrategy trustStrategy)\n
    loadTrustMaterial(final File file, final char[] storePassword)\n
    loadTrustMaterial(final File file)\n
    loadTrustMaterial(final URL url, final char[] storePassword, final TrustStrategy trustStrategy)\n
    loadTrustMaterial(final URL url, final char[] storePassword)\n
    '''
def loadKeyMaterial():
    '''returns SSLContextBuilder\n\n
    loadKeyMaterial(final KeyStore keystore, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)\n
    loadKeyMaterial(final KeyStore keystore, final char[] keyPassword)\n
    loadKeyMaterial(final File file, final char[] storePassword, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)\n
    loadKeyMaterial(final File file, final char[] storePassword, final char[] keyPassword)\n
    loadKeyMaterial(final URL url, final char[] storePassword, final char[] keyPassword, final PrivateKeyStrategy aliasStrategy)\n
    loadKeyMaterial(final URL url, final char[] storePassword, final char[] keyPassword)\n
    '''
def build():
    '''returns SSLContext\n\n
    build()\n
    '''
def checkClientTrusted():
    '''returns None\n\n
    checkClientTrusted(final X509Certificate[] chain, final String authType)\n
    '''
def checkServerTrusted():
    '''returns None\n\n
    checkServerTrusted(final X509Certificate[] chain, final String authType)\n
    '''
def getAcceptedIssuers():
    '''returns X509Certificate[]\n\n
    getAcceptedIssuers()\n
    '''
def getClientAliases():
    '''returns String[]\n\n
    getClientAliases(final String keyType, final Principal[] issuers)\n
    '''
def chooseClientAlias():
    '''returns String\n\n
    chooseClientAlias(final String[] keyTypes, final Principal[] issuers, final Socket socket)\n
    '''
def getServerAliases():
    '''returns String[]\n\n
    getServerAliases(final String keyType, final Principal[] issuers)\n
    '''
def chooseServerAlias():
    '''returns String\n\n
    chooseServerAlias(final String keyType, final Principal[] issuers, final Socket socket)\n
    '''
def getCertificateChain():
    '''returns X509Certificate[]\n\n
    getCertificateChain(final String alias)\n
    '''
def getPrivateKey():
    '''returns PrivateKey\n\n
    getPrivateKey(final String alias)\n
    '''
def chooseEngineClientAlias():
    '''returns String\n\n
    chooseEngineClientAlias(final String[] keyTypes, final Principal[] issuers, final SSLEngine sslEngine)\n
    '''
def chooseEngineServerAlias():
    '''returns String\n\n
    chooseEngineServerAlias(final String keyType, final Principal[] issuers, final SSLEngine sslEngine)\n
    '''
