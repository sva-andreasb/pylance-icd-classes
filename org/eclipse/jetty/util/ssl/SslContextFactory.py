KEYPASSWORD_PROPERTY = "String  \"org.eclipse.jetty.ssl.keypassword\""
PASSWORD_PROPERTY = "String  \"org.eclipse.jetty.ssl.password\""
def ():
    '''returns SslContextFactory\n\n
    ()\n
    (final boolean trustAll)\n
    (final String keyStorePath)\n
    '''
def getExcludeProtocols():
    '''returns String[]\n\n
    getExcludeProtocols()\n
    '''
def setExcludeProtocols():
    '''returns None\n\n
    setExcludeProtocols(final String... protocols)\n
    '''
def addExcludeProtocols():
    '''returns None\n\n
    addExcludeProtocols(final String... protocol)\n
    '''
def getIncludeProtocols():
    '''returns String[]\n\n
    getIncludeProtocols()\n
    '''
def setIncludeProtocols():
    '''returns None\n\n
    setIncludeProtocols(final String... protocols)\n
    '''
def getExcludeCipherSuites():
    '''returns String[]\n\n
    getExcludeCipherSuites()\n
    '''
def setExcludeCipherSuites():
    '''returns None\n\n
    setExcludeCipherSuites(final String... cipherSuites)\n
    '''
def addExcludeCipherSuites():
    '''returns None\n\n
    addExcludeCipherSuites(final String... cipher)\n
    '''
def getIncludeCipherSuites():
    '''returns String[]\n\n
    getIncludeCipherSuites()\n
    '''
def setIncludeCipherSuites():
    '''returns None\n\n
    setIncludeCipherSuites(final String... cipherSuites)\n
    '''
def getKeyStorePath():
    '''returns String\n\n
    getKeyStorePath()\n
    '''
def getKeyStore():
    '''returns String\n\n
    getKeyStore()\n
    '''
def setKeyStorePath():
    '''returns None\n\n
    setKeyStorePath(final String keyStorePath)\n
    '''
def setKeyStore():
    '''returns None\n\n
    setKeyStore(final String keyStorePath)\n
    setKeyStore(final KeyStore keyStore)\n
    '''
def getKeyStoreProvider():
    '''returns String\n\n
    getKeyStoreProvider()\n
    '''
def setKeyStoreProvider():
    '''returns None\n\n
    setKeyStoreProvider(final String keyStoreProvider)\n
    '''
def getKeyStoreType():
    '''returns String\n\n
    getKeyStoreType()\n
    '''
def setKeyStoreType():
    '''returns None\n\n
    setKeyStoreType(final String keyStoreType)\n
    '''
def getKeyStoreInputStream():
    '''returns InputStream\n\n
    getKeyStoreInputStream()\n
    '''
def setKeyStoreInputStream():
    '''returns None\n\n
    setKeyStoreInputStream(final InputStream keyStoreInputStream)\n
    '''
def getCertAlias():
    '''returns String\n\n
    getCertAlias()\n
    '''
def setCertAlias():
    '''returns None\n\n
    setCertAlias(final String certAlias)\n
    '''
def getTrustStore():
    '''returns String\n\n
    getTrustStore()\n
    '''
def setTrustStore():
    '''returns None\n\n
    setTrustStore(final String trustStorePath)\n
    setTrustStore(final KeyStore trustStore)\n
    '''
def getTrustStoreProvider():
    '''returns String\n\n
    getTrustStoreProvider()\n
    '''
def setTrustStoreProvider():
    '''returns None\n\n
    setTrustStoreProvider(final String trustStoreProvider)\n
    '''
def getTrustStoreType():
    '''returns String\n\n
    getTrustStoreType()\n
    '''
def setTrustStoreType():
    '''returns None\n\n
    setTrustStoreType(final String trustStoreType)\n
    '''
def getTrustStoreInputStream():
    '''returns InputStream\n\n
    getTrustStoreInputStream()\n
    '''
def setTrustStoreInputStream():
    '''returns None\n\n
    setTrustStoreInputStream(final InputStream trustStoreInputStream)\n
    '''
def getNeedClientAuth():
    '''returns boolean\n\n
    getNeedClientAuth()\n
    '''
def setNeedClientAuth():
    '''returns None\n\n
    setNeedClientAuth(final boolean needClientAuth)\n
    '''
def getWantClientAuth():
    '''returns boolean\n\n
    getWantClientAuth()\n
    '''
def setWantClientAuth():
    '''returns None\n\n
    setWantClientAuth(final boolean wantClientAuth)\n
    '''
def getValidateCerts():
    '''returns boolean\n\n
    getValidateCerts()\n
    '''
def isValidateCerts():
    '''returns boolean\n\n
    isValidateCerts()\n
    '''
def setValidateCerts():
    '''returns None\n\n
    setValidateCerts(final boolean validateCerts)\n
    '''
def isValidatePeerCerts():
    '''returns boolean\n\n
    isValidatePeerCerts()\n
    '''
def setValidatePeerCerts():
    '''returns None\n\n
    setValidatePeerCerts(final boolean validatePeerCerts)\n
    '''
def isAllowRenegotiate():
    '''returns boolean\n\n
    isAllowRenegotiate()\n
    '''
def setAllowRenegotiate():
    '''returns None\n\n
    setAllowRenegotiate(final boolean allowRenegotiate)\n
    '''
def setKeyStorePassword():
    '''returns None\n\n
    setKeyStorePassword(final String password)\n
    '''
def setKeyManagerPassword():
    '''returns None\n\n
    setKeyManagerPassword(final String password)\n
    '''
def setTrustStorePassword():
    '''returns None\n\n
    setTrustStorePassword(final String password)\n
    '''
def getProvider():
    '''returns String\n\n
    getProvider()\n
    '''
def setProvider():
    '''returns None\n\n
    setProvider(final String provider)\n
    '''
def getProtocol():
    '''returns String\n\n
    getProtocol()\n
    '''
def setProtocol():
    '''returns None\n\n
    setProtocol(final String protocol)\n
    '''
def getSecureRandomAlgorithm():
    '''returns String\n\n
    getSecureRandomAlgorithm()\n
    '''
def setSecureRandomAlgorithm():
    '''returns None\n\n
    setSecureRandomAlgorithm(final String algorithm)\n
    '''
def getSslKeyManagerFactoryAlgorithm():
    '''returns String\n\n
    getSslKeyManagerFactoryAlgorithm()\n
    '''
def setSslKeyManagerFactoryAlgorithm():
    '''returns None\n\n
    setSslKeyManagerFactoryAlgorithm(final String algorithm)\n
    '''
def getTrustManagerFactoryAlgorithm():
    '''returns String\n\n
    getTrustManagerFactoryAlgorithm()\n
    '''
def isTrustAll():
    '''returns boolean\n\n
    isTrustAll()\n
    '''
def setTrustAll():
    '''returns None\n\n
    setTrustAll(final boolean trustAll)\n
    '''
def setTrustManagerFactoryAlgorithm():
    '''returns None\n\n
    setTrustManagerFactoryAlgorithm(final String algorithm)\n
    '''
def getCrlPath():
    '''returns String\n\n
    getCrlPath()\n
    '''
def setCrlPath():
    '''returns None\n\n
    setCrlPath(final String crlPath)\n
    '''
def getMaxCertPathLength():
    '''returns int\n\n
    getMaxCertPathLength()\n
    '''
def setMaxCertPathLength():
    '''returns None\n\n
    setMaxCertPathLength(final int maxCertPathLength)\n
    '''
def getSslContext():
    '''returns SSLContext\n\n
    getSslContext()\n
    '''
def setSslContext():
    '''returns None\n\n
    setSslContext(final SSLContext sslContext)\n
    '''
def checkKeyStore():
    '''returns None\n\n
    checkKeyStore()\n
    '''
def selectProtocols():
    '''returns String[]\n\n
    selectProtocols(final String[] enabledProtocols, final String[] supportedProtocols)\n
    '''
def selectCipherSuites():
    '''returns String[]\n\n
    selectCipherSuites(final String[] enabledCipherSuites, final String[] supportedCipherSuites)\n
    '''
def isEnableCRLDP():
    '''returns boolean\n\n
    isEnableCRLDP()\n
    '''
def setEnableCRLDP():
    '''returns None\n\n
    setEnableCRLDP(final boolean enableCRLDP)\n
    '''
def isEnableOCSP():
    '''returns boolean\n\n
    isEnableOCSP()\n
    '''
def setEnableOCSP():
    '''returns None\n\n
    setEnableOCSP(final boolean enableOCSP)\n
    '''
def getOcspResponderURL():
    '''returns String\n\n
    getOcspResponderURL()\n
    '''
def setOcspResponderURL():
    '''returns None\n\n
    setOcspResponderURL(final String ocspResponderURL)\n
    '''
def setKeyStoreResource():
    '''returns None\n\n
    setKeyStoreResource(final Resource resource)\n
    '''
def setTrustStoreResource():
    '''returns None\n\n
    setTrustStoreResource(final Resource resource)\n
    '''
def isSessionCachingEnabled():
    '''returns boolean\n\n
    isSessionCachingEnabled()\n
    '''
def setSessionCachingEnabled():
    '''returns None\n\n
    setSessionCachingEnabled(final boolean enableSessionCaching)\n
    '''
def getSslSessionCacheSize():
    '''returns int\n\n
    getSslSessionCacheSize()\n
    '''
def setSslSessionCacheSize():
    '''returns None\n\n
    setSslSessionCacheSize(final int sslSessionCacheSize)\n
    '''
def getSslSessionTimeout():
    '''returns int\n\n
    getSslSessionTimeout()\n
    '''
def setSslSessionTimeout():
    '''returns None\n\n
    setSslSessionTimeout(final int sslSessionTimeout)\n
    '''
def newSslServerSocket():
    '''returns SSLServerSocket\n\n
    newSslServerSocket(final String host, final int port, final int backlog)\n
    '''
def newSslSocket():
    '''returns SSLSocket\n\n
    newSslSocket()\n
    '''
def newSslEngine():
    '''returns SSLEngine\n\n
    newSslEngine(final String host, final int port)\n
    newSslEngine()\n
    '''
def customize():
    '''returns None\n\n
    customize(final SSLEngine sslEngine)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getAcceptedIssuers():
    '''returns X509Certificate[]\n\n
    getAcceptedIssuers()\n
    '''
def checkClientTrusted():
    '''returns None\n\n
    checkClientTrusted(final X509Certificate[] certs, final String authType)\n
    '''
def checkServerTrusted():
    '''returns None\n\n
    checkServerTrusted(final X509Certificate[] certs, final String authType)\n
    '''
