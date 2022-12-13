def getSslContext():
    '''public static SSLContext getSslContext()
    '''
def getTlsSslContext():
    '''public static SSLContext getTlsSslContext()
    '''
def getDefaultTrustManagerFactory():
    '''public static TrustManagerFactory getDefaultTrustManagerFactory()
    '''
def getPkixTrustManagerFactory():
    '''public static TrustManagerFactory getPkixTrustManagerFactory()
    '''
def getDefaultKeyManagerFactory():
    '''public static KeyManagerFactory getDefaultKeyManagerFactory()
    '''
def getPkixKeyManagerFactory():
    '''public static KeyManagerFactory getPkixKeyManagerFactory()
    '''
def initSslContext():
    '''public static SSLContext initSslContext(final SSLContext sslContext, final KeyStore trustStore, final TrustManagerFactory trustManagerFactory)
    '''
def trustAllSSLContext():
    '''public static SSLContext trustAllSSLContext()
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
def trustAllHostnameVerifier():
    '''public static HostnameVerifier trustAllHostnameVerifier()
    '''
def verify():
    '''public boolean verify(final String arg0, final SSLSession arg1)
    '''
