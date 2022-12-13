def JsonWebSignature():
'''public JsonWebSignature(final Header header, final Payload payload, final byte[] signatureBytes, final byte[] signedContentBytes)
'''
pass
def getHeader():
'''public Header getHeader()
'''
pass
def verifySignature():
'''public final boolean verifySignature(final PublicKey publicKey)
public final X509Certificate verifySignature(final X509TrustManager trustManager)
public final X509Certificate verifySignature()
'''
pass
def getSignatureBytes():
'''public final byte[] getSignatureBytes()
'''
pass
def getSignedContentBytes():
'''public final byte[] getSignedContentBytes()
'''
pass
def parse():
'''public static JsonWebSignature parse(final JsonFactory jsonFactory, final String tokenString)
public JsonWebSignature parse(final String tokenString)
'''
pass
def parser():
'''public static Parser parser(final JsonFactory jsonFactory)
'''
pass
def signUsingRsaSha256():
'''public static String signUsingRsaSha256(final PrivateKey privateKey, final JsonFactory jsonFactory, final Header header, final Payload payload)
'''
pass
def setType():
'''public Header setType(final String type)
'''
pass
def getAlgorithm():
'''public final String getAlgorithm()
'''
pass
def setAlgorithm():
'''public Header setAlgorithm(final String algorithm)
'''
pass
def getJwkUrl():
'''public final String getJwkUrl()
'''
pass
def setJwkUrl():
'''public Header setJwkUrl(final String jwkUrl)
'''
pass
def getJwk():
'''public final String getJwk()
'''
pass
def setJwk():
'''public Header setJwk(final String jwk)
'''
pass
def getKeyId():
'''public final String getKeyId()
'''
pass
def setKeyId():
'''public Header setKeyId(final String keyId)
'''
pass
def getX509Url():
'''public final String getX509Url()
'''
pass
def setX509Url():
'''public Header setX509Url(final String x509Url)
'''
pass
def getX509Thumbprint():
'''public final String getX509Thumbprint()
'''
pass
def setX509Thumbprint():
'''public Header setX509Thumbprint(final String x509Thumbprint)
'''
pass
def getX509Certificate():
'''public final String getX509Certificate()
'''
pass
def getX509Certificates():
'''public final List<String> getX509Certificates()
'''
pass
def setX509Certificate():
'''public Header setX509Certificate(final String x509Certificate)
'''
pass
def setX509Certificates():
'''public Header setX509Certificates(final List<String> x509Certificates)
'''
pass
def getCritical():
'''public final List<String> getCritical()
'''
pass
def setCritical():
'''public Header setCritical(final List<String> critical)
'''
pass
def set():
'''public Header set(final String fieldName, final Object value)
'''
pass
def clone():
'''public Header clone()
'''
pass
def Parser():
'''public Parser(final JsonFactory jsonFactory)
'''
pass
def setHeaderClass():
'''public Parser setHeaderClass(final Class<? extends Header> headerClass)
'''
pass
def setPayloadClass():
'''public Parser setPayloadClass(final Class<? extends Payload> payloadClass)
'''
pass
def getJsonFactory():
'''public JsonFactory getJsonFactory()
'''
pass
