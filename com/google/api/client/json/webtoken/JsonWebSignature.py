def JsonWebSignature():
    '''public JsonWebSignature(final Header header, final Payload payload, final byte[] signatureBytes, final byte[] signedContentBytes)
    '''
def getHeader():
    '''public Header getHeader()
    '''
def verifySignature():
    '''public final boolean verifySignature(final PublicKey publicKey)
    public final X509Certificate verifySignature(final X509TrustManager trustManager)
    public final X509Certificate verifySignature()
    '''
def getSignatureBytes():
    '''public final byte[] getSignatureBytes()
    '''
def getSignedContentBytes():
    '''public final byte[] getSignedContentBytes()
    '''
def parse():
    '''public static JsonWebSignature parse(final JsonFactory jsonFactory, final String tokenString)
    public JsonWebSignature parse(final String tokenString)
    '''
def parser():
    '''public static Parser parser(final JsonFactory jsonFactory)
    '''
def signUsingRsaSha256():
    '''public static String signUsingRsaSha256(final PrivateKey privateKey, final JsonFactory jsonFactory, final Header header, final Payload payload)
    '''
def setType():
    '''public Header setType(final String type)
    '''
def getAlgorithm():
    '''public final String getAlgorithm()
    '''
def setAlgorithm():
    '''public Header setAlgorithm(final String algorithm)
    '''
def getJwkUrl():
    '''public final String getJwkUrl()
    '''
def setJwkUrl():
    '''public Header setJwkUrl(final String jwkUrl)
    '''
def getJwk():
    '''public final String getJwk()
    '''
def setJwk():
    '''public Header setJwk(final String jwk)
    '''
def getKeyId():
    '''public final String getKeyId()
    '''
def setKeyId():
    '''public Header setKeyId(final String keyId)
    '''
def getX509Url():
    '''public final String getX509Url()
    '''
def setX509Url():
    '''public Header setX509Url(final String x509Url)
    '''
def getX509Thumbprint():
    '''public final String getX509Thumbprint()
    '''
def setX509Thumbprint():
    '''public Header setX509Thumbprint(final String x509Thumbprint)
    '''
def getX509Certificate():
    '''public final String getX509Certificate()
    '''
def getX509Certificates():
    '''public final List<String> getX509Certificates()
    '''
def setX509Certificate():
    '''public Header setX509Certificate(final String x509Certificate)
    '''
def setX509Certificates():
    '''public Header setX509Certificates(final List<String> x509Certificates)
    '''
def getCritical():
    '''public final List<String> getCritical()
    '''
def setCritical():
    '''public Header setCritical(final List<String> critical)
    '''
def set():
    '''public Header set(final String fieldName, final Object value)
    '''
def clone():
    '''public Header clone()
    '''
def Parser():
    '''public Parser(final JsonFactory jsonFactory)
    '''
def setHeaderClass():
    '''public Parser setHeaderClass(final Class<? extends Header> headerClass)
    '''
def setPayloadClass():
    '''public Parser setPayloadClass(final Class<? extends Payload> payloadClass)
    '''
def getJsonFactory():
    '''public JsonFactory getJsonFactory()
    '''
