SSL = "String  \"SSL\""
TLS = "String  \"TLS\""
PROTO_SSL3 = "String  \"SSLv3\""
PROTO_TLSV1 = "String  \"TLSv1\""
PROTO_TLSV1_1 = "String  \"TLSv1.1\""
PROTO_TLSV1_2 = "String  \"TLSv1.2\""
def verify():
    '''returns boolean\n\n
    verify(final String hostname, final SSLSession session)\n
    '''
def checkClientTrusted():
    '''returns None\n\n
    checkClientTrusted(final X509Certificate[] arg0, final String arg1)\n
    '''
def checkServerTrusted():
    '''returns None\n\n
    checkServerTrusted(final X509Certificate[] arg0, final String arg1)\n
    '''
def getAcceptedIssuers():
    '''returns X509Certificate[]\n\n
    getAcceptedIssuers()\n
    '''
