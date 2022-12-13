KEYPASSWORD_PROPERTY = "String  org.eclipse.jetty.ssl.keypassword""
PASSWORD_PROPERTY = "String  org.eclipse.jetty.ssl.password""
def SslContextFactory():
'''public SslContextFactory()
public SslContextFactory(final boolean trustAll)
public SslContextFactory(final String keyStorePath)
'''
pass
def getExcludeProtocols():
'''public String[] getExcludeProtocols()
'''
pass
def setExcludeProtocols():
'''public void setExcludeProtocols(final String... protocols)
'''
pass
def addExcludeProtocols():
'''public void addExcludeProtocols(final String... protocol)
'''
pass
def getIncludeProtocols():
'''public String[] getIncludeProtocols()
'''
pass
def setIncludeProtocols():
'''public void setIncludeProtocols(final String... protocols)
'''
pass
def getExcludeCipherSuites():
'''public String[] getExcludeCipherSuites()
'''
pass
def setExcludeCipherSuites():
'''public void setExcludeCipherSuites(final String... cipherSuites)
'''
pass
def addExcludeCipherSuites():
'''public void addExcludeCipherSuites(final String... cipher)
'''
pass
def getIncludeCipherSuites():
'''public String[] getIncludeCipherSuites()
'''
pass
def setIncludeCipherSuites():
'''public void setIncludeCipherSuites(final String... cipherSuites)
'''
pass
def getKeyStorePath():
'''public String getKeyStorePath()
'''
pass
def getKeyStore():
'''public String getKeyStore()
'''
pass
def setKeyStorePath():
'''public void setKeyStorePath(final String keyStorePath)
'''
pass
def setKeyStore():
'''public void setKeyStore(final String keyStorePath)
public void setKeyStore(final KeyStore keyStore)
'''
pass
def getKeyStoreProvider():
'''public String getKeyStoreProvider()
'''
pass
def setKeyStoreProvider():
'''public void setKeyStoreProvider(final String keyStoreProvider)
'''
pass
def getKeyStoreType():
'''public String getKeyStoreType()
'''
pass
def setKeyStoreType():
'''public void setKeyStoreType(final String keyStoreType)
'''
pass
def getKeyStoreInputStream():
'''public InputStream getKeyStoreInputStream()
'''
pass
def setKeyStoreInputStream():
'''public void setKeyStoreInputStream(final InputStream keyStoreInputStream)
'''
pass
def getCertAlias():
'''public String getCertAlias()
'''
pass
def setCertAlias():
'''public void setCertAlias(final String certAlias)
'''
pass
def getTrustStore():
'''public String getTrustStore()
'''
pass
def setTrustStore():
'''public void setTrustStore(final String trustStorePath)
public void setTrustStore(final KeyStore trustStore)
'''
pass
def getTrustStoreProvider():
'''public String getTrustStoreProvider()
'''
pass
def setTrustStoreProvider():
'''public void setTrustStoreProvider(final String trustStoreProvider)
'''
pass
def getTrustStoreType():
'''public String getTrustStoreType()
'''
pass
def setTrustStoreType():
'''public void setTrustStoreType(final String trustStoreType)
'''
pass
def getTrustStoreInputStream():
'''public InputStream getTrustStoreInputStream()
'''
pass
def setTrustStoreInputStream():
'''public void setTrustStoreInputStream(final InputStream trustStoreInputStream)
'''
pass
def getNeedClientAuth():
'''public boolean getNeedClientAuth()
'''
pass
def setNeedClientAuth():
'''public void setNeedClientAuth(final boolean needClientAuth)
'''
pass
def getWantClientAuth():
'''public boolean getWantClientAuth()
'''
pass
def setWantClientAuth():
'''public void setWantClientAuth(final boolean wantClientAuth)
'''
pass
def getValidateCerts():
'''public boolean getValidateCerts()
'''
pass
def isValidateCerts():
'''public boolean isValidateCerts()
'''
pass
def setValidateCerts():
'''public void setValidateCerts(final boolean validateCerts)
'''
pass
def isValidatePeerCerts():
'''public boolean isValidatePeerCerts()
'''
pass
def setValidatePeerCerts():
'''public void setValidatePeerCerts(final boolean validatePeerCerts)
'''
pass
def isAllowRenegotiate():
'''public boolean isAllowRenegotiate()
'''
pass
def setAllowRenegotiate():
'''public void setAllowRenegotiate(final boolean allowRenegotiate)
'''
pass
def setKeyStorePassword():
'''public void setKeyStorePassword(final String password)
'''
pass
def setKeyManagerPassword():
'''public void setKeyManagerPassword(final String password)
'''
pass
def setTrustStorePassword():
'''public void setTrustStorePassword(final String password)
'''
pass
def getProvider():
'''public String getProvider()
'''
pass
def setProvider():
'''public void setProvider(final String provider)
'''
pass
def getProtocol():
'''public String getProtocol()
'''
pass
def setProtocol():
'''public void setProtocol(final String protocol)
'''
pass
def getSecureRandomAlgorithm():
'''public String getSecureRandomAlgorithm()
'''
pass
def setSecureRandomAlgorithm():
'''public void setSecureRandomAlgorithm(final String algorithm)
'''
pass
def getSslKeyManagerFactoryAlgorithm():
'''public String getSslKeyManagerFactoryAlgorithm()
'''
pass
def setSslKeyManagerFactoryAlgorithm():
'''public void setSslKeyManagerFactoryAlgorithm(final String algorithm)
'''
pass
def getTrustManagerFactoryAlgorithm():
'''public String getTrustManagerFactoryAlgorithm()
'''
pass
def isTrustAll():
'''public boolean isTrustAll()
'''
pass
def setTrustAll():
'''public void setTrustAll(final boolean trustAll)
'''
pass
def setTrustManagerFactoryAlgorithm():
'''public void setTrustManagerFactoryAlgorithm(final String algorithm)
'''
pass
def getCrlPath():
'''public String getCrlPath()
'''
pass
def setCrlPath():
'''public void setCrlPath(final String crlPath)
'''
pass
def getMaxCertPathLength():
'''public int getMaxCertPathLength()
'''
pass
def setMaxCertPathLength():
'''public void setMaxCertPathLength(final int maxCertPathLength)
'''
pass
def getSslContext():
'''public SSLContext getSslContext()
'''
pass
def setSslContext():
'''public void setSslContext(final SSLContext sslContext)
'''
pass
def checkKeyStore():
'''public void checkKeyStore()
'''
pass
def selectProtocols():
'''public String[] selectProtocols(final String[] enabledProtocols, final String[] supportedProtocols)
'''
pass
def selectCipherSuites():
'''public String[] selectCipherSuites(final String[] enabledCipherSuites, final String[] supportedCipherSuites)
'''
pass
def isEnableCRLDP():
'''public boolean isEnableCRLDP()
'''
pass
def setEnableCRLDP():
'''public void setEnableCRLDP(final boolean enableCRLDP)
'''
pass
def isEnableOCSP():
'''public boolean isEnableOCSP()
'''
pass
def setEnableOCSP():
'''public void setEnableOCSP(final boolean enableOCSP)
'''
pass
def getOcspResponderURL():
'''public String getOcspResponderURL()
'''
pass
def setOcspResponderURL():
'''public void setOcspResponderURL(final String ocspResponderURL)
'''
pass
def setKeyStoreResource():
'''public void setKeyStoreResource(final Resource resource)
'''
pass
def setTrustStoreResource():
'''public void setTrustStoreResource(final Resource resource)
'''
pass
def isSessionCachingEnabled():
'''public boolean isSessionCachingEnabled()
'''
pass
def setSessionCachingEnabled():
'''public void setSessionCachingEnabled(final boolean enableSessionCaching)
'''
pass
def getSslSessionCacheSize():
'''public int getSslSessionCacheSize()
'''
pass
def setSslSessionCacheSize():
'''public void setSslSessionCacheSize(final int sslSessionCacheSize)
'''
pass
def getSslSessionTimeout():
'''public int getSslSessionTimeout()
'''
pass
def setSslSessionTimeout():
'''public void setSslSessionTimeout(final int sslSessionTimeout)
'''
pass
def newSslServerSocket():
'''public SSLServerSocket newSslServerSocket(final String host, final int port, final int backlog)
'''
pass
def newSslSocket():
'''public SSLSocket newSslSocket()
'''
pass
def newSslEngine():
'''public SSLEngine newSslEngine(final String host, final int port)
public SSLEngine newSslEngine()
'''
pass
def customize():
'''public void customize(final SSLEngine sslEngine)
'''
pass
def toString():
'''public String toString()
'''
pass
def getAcceptedIssuers():
'''public X509Certificate[] getAcceptedIssuers()
'''
pass
def checkClientTrusted():
'''public void checkClientTrusted(final X509Certificate[] certs, final String authType)
'''
pass
def checkServerTrusted():
'''public void checkServerTrusted(final X509Certificate[] certs, final String authType)
'''
pass
