def ApacheHttpTransport():
    '''public ApacheHttpTransport()
    public ApacheHttpTransport(final HttpClient httpClient)
    '''
def newDefaultHttpClient():
    '''public static DefaultHttpClient newDefaultHttpClient()
    '''
def supportsMethod():
    '''public boolean supportsMethod(final String method)
    '''
def shutdown():
    '''public void shutdown()
    '''
def getHttpClient():
    '''public HttpClient getHttpClient()
    '''
def Builder():
    '''public Builder()
    '''
def setProxy():
    '''public Builder setProxy(final HttpHost proxy)
    '''
def setProxySelector():
    '''public Builder setProxySelector(final ProxySelector proxySelector)
    '''
def trustCertificatesFromJavaKeyStore():
    '''public Builder trustCertificatesFromJavaKeyStore(final InputStream keyStoreStream, final String storePass)
    '''
def trustCertificatesFromStream():
    '''public Builder trustCertificatesFromStream(final InputStream certificateStream)
    '''
def trustCertificates():
    '''public Builder trustCertificates(final KeyStore trustStore)
    '''
def doNotValidateCertificate():
    '''public Builder doNotValidateCertificate()
    '''
def setSocketFactory():
    '''public Builder setSocketFactory(final SSLSocketFactory socketFactory)
    '''
def getSSLSocketFactory():
    '''public SSLSocketFactory getSSLSocketFactory()
    '''
def getHttpParams():
    '''public HttpParams getHttpParams()
    '''
def build():
    '''public ApacheHttpTransport build()
    '''
