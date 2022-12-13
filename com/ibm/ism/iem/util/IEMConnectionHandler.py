def getAcceptedIssuers():
'''public X509Certificate[] getAcceptedIssuers()
'''
pass
def checkClientTrusted():
'''public void checkClientTrusted(final X509Certificate[] arg0, final String arg1)
'''
pass
def checkServerTrusted():
'''public void checkServerTrusted(final X509Certificate[] arg0, final String arg1)
'''
pass
def verify():
'''public boolean verify(final String hostname, final SSLSession session)
'''
pass
def testSSLConnection():
'''public static CONNECTION_RESULT testSSLConnection(final String server, final int port, final String username, final String password)
'''
pass
def executeGET():
'''public static BESAPI executeGET(final String baseUrl, final String username, final String password, final String url, final Unmarshaller uMarhaller)
'''
pass
def executePOST():
'''public static BESAPI executePOST(final String baseUrl, final String username, final String password, final String url, final String body, final Unmarshaller uMarhaller)
'''
pass
def pingServer():
'''public static CONNECTION_RESULT pingServer(final String ipAddress)
'''
pass
def stripResponseLayers():
'''public static List<Object> stripResponseLayers(final BESAPI besapi)
'''
pass
