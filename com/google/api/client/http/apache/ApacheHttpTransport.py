def ():
    '''returns Builder\n\n
    ()\n
    (final HttpClient httpClient)\n
    ()\n
    '''
def supportsMethod():
    '''returns boolean\n\n
    supportsMethod(final String method)\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def getHttpClient():
    '''returns HttpClient\n\n
    getHttpClient()\n
    '''
def setProxy():
    '''returns Builder\n\n
    setProxy(final HttpHost proxy)\n
    '''
def setProxySelector():
    '''returns Builder\n\n
    setProxySelector(final ProxySelector proxySelector)\n
    '''
def trustCertificatesFromJavaKeyStore():
    '''returns Builder\n\n
    trustCertificatesFromJavaKeyStore(final InputStream keyStoreStream, final String storePass)\n
    '''
def trustCertificatesFromStream():
    '''returns Builder\n\n
    trustCertificatesFromStream(final InputStream certificateStream)\n
    '''
def trustCertificates():
    '''returns Builder\n\n
    trustCertificates(final KeyStore trustStore)\n
    '''
def doNotValidateCertificate():
    '''returns Builder\n\n
    doNotValidateCertificate()\n
    '''
def setSocketFactory():
    '''returns Builder\n\n
    setSocketFactory(final SSLSocketFactory socketFactory)\n
    '''
def getSSLSocketFactory():
    '''returns SSLSocketFactory\n\n
    getSSLSocketFactory()\n
    '''
def getHttpParams():
    '''returns HttpParams\n\n
    getHttpParams()\n
    '''
def build():
    '''returns ApacheHttpTransport\n\n
    build()\n
    '''
