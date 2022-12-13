KEYPASSWORD_PROPERTY = "String  \"org.eclipse.jetty.ssl.keypassword\""
PASSWORD_PROPERTY = "String  \"org.eclipse.jetty.ssl.password\""
def SslContextFactory():
    '''public SslContextFactory()
    public SslContextFactory(final boolean trustAll)
    public SslContextFactory(final String keyStorePath)
    '''
def getExcludeProtocols():
    '''public String[] getExcludeProtocols()
    '''
def setExcludeProtocols():
    '''public void setExcludeProtocols(final String... protocols)
    '''
def addExcludeProtocols():
    '''public void addExcludeProtocols(final String... protocol)
    '''
def getIncludeProtocols():
    '''public String[] getIncludeProtocols()
    '''
def setIncludeProtocols():
    '''public void setIncludeProtocols(final String... protocols)
    '''
def getExcludeCipherSuites():
    '''public String[] getExcludeCipherSuites()
    '''
def setExcludeCipherSuites():
    '''public void setExcludeCipherSuites(final String... cipherSuites)
    '''
def addExcludeCipherSuites():
    '''public void addExcludeCipherSuites(final String... cipher)
    '''
def getIncludeCipherSuites():
    '''public String[] getIncludeCipherSuites()
    '''
def setIncludeCipherSuites():
    '''public void setIncludeCipherSuites(final String... cipherSuites)
    '''
def getKeyStorePath():
    '''public String getKeyStorePath()
    '''
def getKeyStore():
    '''public String getKeyStore()
    '''
def setKeyStorePath():
    '''public void setKeyStorePath(final String keyStorePath)
    '''
def setKeyStore():
    '''public void setKeyStore(final String keyStorePath)
    public void setKeyStore(final KeyStore keyStore)
    '''
def getKeyStoreProvider():
    '''public String getKeyStoreProvider()
    '''
def setKeyStoreProvider():
    '''public void setKeyStoreProvider(final String keyStoreProvider)
    '''
def getKeyStoreType():
    '''public String getKeyStoreType()
    '''
def setKeyStoreType():
    '''public void setKeyStoreType(final String keyStoreType)
    '''
def getKeyStoreInputStream():
    '''public InputStream getKeyStoreInputStream()
    '''
def setKeyStoreInputStream():
    '''public void setKeyStoreInputStream(final InputStream keyStoreInputStream)
    '''
def getCertAlias():
    '''public String getCertAlias()
    '''
def setCertAlias():
    '''public void setCertAlias(final String certAlias)
    '''
def getTrustStore():
    '''public String getTrustStore()
    '''
def setTrustStore():
    '''public void setTrustStore(final String trustStorePath)
    public void setTrustStore(final KeyStore trustStore)
    '''
def getTrustStoreProvider():
    '''public String getTrustStoreProvider()
    '''
def setTrustStoreProvider():
    '''public void setTrustStoreProvider(final String trustStoreProvider)
    '''
def getTrustStoreType():
    '''public String getTrustStoreType()
    '''
def setTrustStoreType():
    '''public void setTrustStoreType(final String trustStoreType)
    '''
def getTrustStoreInputStream():
    '''public InputStream getTrustStoreInputStream()
    '''
def setTrustStoreInputStream():
    '''public void setTrustStoreInputStream(final InputStream trustStoreInputStream)
    '''
def getNeedClientAuth():
    '''public boolean getNeedClientAuth()
    '''
def setNeedClientAuth():
    '''public void setNeedClientAuth(final boolean needClientAuth)
    '''
def getWantClientAuth():
    '''public boolean getWantClientAuth()
    '''
def setWantClientAuth():
    '''public void setWantClientAuth(final boolean wantClientAuth)
    '''
def getValidateCerts():
    '''public boolean getValidateCerts()
    '''
def isValidateCerts():
    '''public boolean isValidateCerts()
    '''
def setValidateCerts():
    '''public void setValidateCerts(final boolean validateCerts)
    '''
def isValidatePeerCerts():
    '''public boolean isValidatePeerCerts()
    '''
def setValidatePeerCerts():
    '''public void setValidatePeerCerts(final boolean validatePeerCerts)
    '''
def isAllowRenegotiate():
    '''public boolean isAllowRenegotiate()
    '''
def setAllowRenegotiate():
    '''public void setAllowRenegotiate(final boolean allowRenegotiate)
    '''
def setKeyStorePassword():
    '''public void setKeyStorePassword(final String password)
    '''
def setKeyManagerPassword():
    '''public void setKeyManagerPassword(final String password)
    '''
def setTrustStorePassword():
    '''public void setTrustStorePassword(final String password)
    '''
def getProvider():
    '''public String getProvider()
    '''
def setProvider():
    '''public void setProvider(final String provider)
    '''
def getProtocol():
    '''public String getProtocol()
    '''
def setProtocol():
    '''public void setProtocol(final String protocol)
    '''
def getSecureRandomAlgorithm():
    '''public String getSecureRandomAlgorithm()
    '''
def setSecureRandomAlgorithm():
    '''public void setSecureRandomAlgorithm(final String algorithm)
    '''
def getSslKeyManagerFactoryAlgorithm():
    '''public String getSslKeyManagerFactoryAlgorithm()
    '''
def setSslKeyManagerFactoryAlgorithm():
    '''public void setSslKeyManagerFactoryAlgorithm(final String algorithm)
    '''
def getTrustManagerFactoryAlgorithm():
    '''public String getTrustManagerFactoryAlgorithm()
    '''
def isTrustAll():
    '''public boolean isTrustAll()
    '''
def setTrustAll():
    '''public void setTrustAll(final boolean trustAll)
    '''
def setTrustManagerFactoryAlgorithm():
    '''public void setTrustManagerFactoryAlgorithm(final String algorithm)
    '''
def getCrlPath():
    '''public String getCrlPath()
    '''
def setCrlPath():
    '''public void setCrlPath(final String crlPath)
    '''
def getMaxCertPathLength():
    '''public int getMaxCertPathLength()
    '''
def setMaxCertPathLength():
    '''public void setMaxCertPathLength(final int maxCertPathLength)
    '''
def getSslContext():
    '''public SSLContext getSslContext()
    '''
def setSslContext():
    '''public void setSslContext(final SSLContext sslContext)
    '''
def checkKeyStore():
    '''public void checkKeyStore()
    '''
def selectProtocols():
    '''public String[] selectProtocols(final String[] enabledProtocols, final String[] supportedProtocols)
    '''
def selectCipherSuites():
    '''public String[] selectCipherSuites(final String[] enabledCipherSuites, final String[] supportedCipherSuites)
    '''
def isEnableCRLDP():
    '''public boolean isEnableCRLDP()
    '''
def setEnableCRLDP():
    '''public void setEnableCRLDP(final boolean enableCRLDP)
    '''
def isEnableOCSP():
    '''public boolean isEnableOCSP()
    '''
def setEnableOCSP():
    '''public void setEnableOCSP(final boolean enableOCSP)
    '''
def getOcspResponderURL():
    '''public String getOcspResponderURL()
    '''
def setOcspResponderURL():
    '''public void setOcspResponderURL(final String ocspResponderURL)
    '''
def setKeyStoreResource():
    '''public void setKeyStoreResource(final Resource resource)
    '''
def setTrustStoreResource():
    '''public void setTrustStoreResource(final Resource resource)
    '''
def isSessionCachingEnabled():
    '''public boolean isSessionCachingEnabled()
    '''
def setSessionCachingEnabled():
    '''public void setSessionCachingEnabled(final boolean enableSessionCaching)
    '''
def getSslSessionCacheSize():
    '''public int getSslSessionCacheSize()
    '''
def setSslSessionCacheSize():
    '''public void setSslSessionCacheSize(final int sslSessionCacheSize)
    '''
def getSslSessionTimeout():
    '''public int getSslSessionTimeout()
    '''
def setSslSessionTimeout():
    '''public void setSslSessionTimeout(final int sslSessionTimeout)
    '''
def newSslServerSocket():
    '''public SSLServerSocket newSslServerSocket(final String host, final int port, final int backlog)
    '''
def newSslSocket():
    '''public SSLSocket newSslSocket()
    '''
def newSslEngine():
    '''public SSLEngine newSslEngine(final String host, final int port)
    public SSLEngine newSslEngine()
    '''
def customize():
    '''public void customize(final SSLEngine sslEngine)
    '''
def toString():
    '''public String toString()
    '''
def getAcceptedIssuers():
    '''public X509Certificate[] getAcceptedIssuers()
    '''
def checkClientTrusted():
    '''public void checkClientTrusted(final X509Certificate[] certs, final String authType)
    '''
def checkServerTrusted():
    '''public void checkServerTrusted(final X509Certificate[] certs, final String authType)
    '''
