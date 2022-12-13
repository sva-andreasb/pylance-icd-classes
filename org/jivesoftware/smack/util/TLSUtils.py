SSL = "String  SSL""
TLS = "String  TLS""
PROTO_SSL3 = "String  SSLv3""
PROTO_TLSV1 = "String  TLSv1""
PROTO_TLSV1_1 = "String  TLSv1.1""
PROTO_TLSV1_2 = "String  TLSv1.2""
def setEnabledProtocolsAndCiphers():
'''public static void setEnabledProtocolsAndCiphers(final SSLSocket sslSocket, String[] enabledProtocols, String[] enabledCiphers)
'''
pass
def getChannelBindingTlsServerEndPoint():
'''public static byte[] getChannelBindingTlsServerEndPoint(final SSLSession sslSession)
'''
pass
def verify():
'''public boolean verify(final String hostname, final SSLSession session)
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
def getAcceptedIssuers():
'''public X509Certificate[] getAcceptedIssuers()
'''
pass
