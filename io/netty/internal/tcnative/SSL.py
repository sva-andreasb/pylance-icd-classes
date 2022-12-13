SSL_PROTOCOL_NONE = "int  0"
SSL_PROTOCOL_SSLV2 = "int  1"
SSL_PROTOCOL_SSLV3 = "int  2"
SSL_PROTOCOL_TLSV1 = "int  4"
SSL_PROTOCOL_TLSV1_1 = "int  8"
SSL_PROTOCOL_TLSV1_2 = "int  16"
SSL_PROTOCOL_TLSV1_3 = "int  32"
SSL_PROTOCOL_TLS = "int  62"
SSL_PROTOCOL_ALL = "int  63"
SSL_CVERIFY_IGNORED = "int  -1"
SSL_CVERIFY_NONE = "int  0"
SSL_CVERIFY_OPTIONAL = "int  1"
SSL_CVERIFY_REQUIRED = "int  2"
SSL_MODE_CLIENT = "int  0"
SSL_MODE_SERVER = "int  1"
SSL_MODE_COMBINED = "int  2"
SSL_SELECTOR_FAILURE_NO_ADVERTISE = "int  0"
SSL_SELECTOR_FAILURE_CHOOSE_MY_LAST_PROTOCOL = "int  1"
def setCipherSuites():
'''public static boolean setCipherSuites(final long ssl, final String ciphers)
'''
pass
def setTlsExtHostName():
'''public static void setTlsExtHostName(final long ssl, String hostname)
'''
pass
def setKeyMaterialServerSide():
'''public static void setKeyMaterialServerSide(final long ssl, final long chain, final long key)
'''
pass
