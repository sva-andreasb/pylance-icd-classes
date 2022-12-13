def getAcceptedIssuers():
    '''    public X509Certificate[] getAcceptedIssuers()
    '''
def checkClientTrusted():
    '''    public void checkClientTrusted(final X509Certificate[] arg0, final String arg1)
    '''
def checkServerTrusted():
    '''    public void checkServerTrusted(final X509Certificate[] arg0, final String arg1)
    '''
def verify():
    '''    public boolean verify(final String hostname, final SSLSession session)
    '''
def testSSLConnection():
    '''    public static CONNECTION_RESULT testSSLConnection(final String server, final int port, final String username, final String password)
    '''
def executeGET():
    '''    public static BESAPI executeGET(final String baseUrl, final String username, final String password, final String url, final Unmarshaller uMarhaller)
    '''
def executePOST():
    '''    public static BESAPI executePOST(final String baseUrl, final String username, final String password, final String url, final String body, final Unmarshaller uMarhaller)
    '''
def pingServer():
    '''    public static CONNECTION_RESULT pingServer(final String ipAddress)
    '''
def stripResponseLayers():
    '''    public static List<Object> stripResponseLayers(final BESAPI besapi)
    '''
