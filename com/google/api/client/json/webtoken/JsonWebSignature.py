def ():
    '''returns Parser\n\n
    (final Header header, final Payload payload, final byte[] signatureBytes, final byte[] signedContentBytes)\n
    (final JsonFactory jsonFactory)\n
    '''
def getHeader():
    '''returns Header\n\n
    getHeader()\n
    '''
def setType():
    '''returns Header\n\n
    setType(final String type)\n
    '''
def setAlgorithm():
    '''returns Header\n\n
    setAlgorithm(final String algorithm)\n
    '''
def setJwkUrl():
    '''returns Header\n\n
    setJwkUrl(final String jwkUrl)\n
    '''
def setJwk():
    '''returns Header\n\n
    setJwk(final String jwk)\n
    '''
def setKeyId():
    '''returns Header\n\n
    setKeyId(final String keyId)\n
    '''
def setX509Url():
    '''returns Header\n\n
    setX509Url(final String x509Url)\n
    '''
def setX509Thumbprint():
    '''returns Header\n\n
    setX509Thumbprint(final String x509Thumbprint)\n
    '''
def setX509Certificate():
    '''returns Header\n\n
    setX509Certificate(final String x509Certificate)\n
    '''
def setX509Certificates():
    '''returns Header\n\n
    setX509Certificates(final List<String> x509Certificates)\n
    '''
def setCritical():
    '''returns Header\n\n
    setCritical(final List<String> critical)\n
    '''
def set():
    '''returns Header\n\n
    set(final String fieldName, final Object value)\n
    '''
def clone():
    '''returns Header\n\n
    clone()\n
    '''
def setHeaderClass():
    '''returns Parser\n\n
    setHeaderClass(final Class<? extends Header> headerClass)\n
    '''
def setPayloadClass():
    '''returns Parser\n\n
    setPayloadClass(final Class<? extends Payload> payloadClass)\n
    '''
def getJsonFactory():
    '''returns JsonFactory\n\n
    getJsonFactory()\n
    '''
def parse():
    '''returns JsonWebSignature\n\n
    parse(final String tokenString)\n
    '''
