def GoogleIdTokenVerifier():
    '''public GoogleIdTokenVerifier(final HttpTransport transport, final JsonFactory jsonFactory)
    public GoogleIdTokenVerifier(final GooglePublicKeysManager publicKeys)
    '''
def getPublicKeysManager():
    '''public final GooglePublicKeysManager getPublicKeysManager()
    '''
def getTransport():
    '''public final HttpTransport getTransport()
    public final HttpTransport getTransport()
    '''
def getJsonFactory():
    '''public final JsonFactory getJsonFactory()
    public final JsonFactory getJsonFactory()
    '''
def getPublicCertsEncodedUrl():
    '''public final String getPublicCertsEncodedUrl()
    public final String getPublicCertsEncodedUrl()
    '''
def getPublicKeys():
    '''public final List<PublicKey> getPublicKeys()
    '''
def getExpirationTimeMilliseconds():
    '''public final long getExpirationTimeMilliseconds()
    '''
def verify():
    '''public boolean verify(final GoogleIdToken googleIdToken)
    public GoogleIdToken verify(final String idTokenString)
    '''
def loadPublicCerts():
    '''public GoogleIdTokenVerifier loadPublicCerts()
    '''
def Builder():
    '''public Builder(final HttpTransport transport, final JsonFactory jsonFactory)
    public Builder(final GooglePublicKeysManager publicKeys)
    '''
def build():
    '''public GoogleIdTokenVerifier build()
    '''
def getPublicCerts():
    '''public final GooglePublicKeysManager getPublicCerts()
    '''
def setPublicCertsEncodedUrl():
    '''public Builder setPublicCertsEncodedUrl(final String publicKeysEncodedUrl)
    '''
def setIssuer():
    '''public Builder setIssuer(final String issuer)
    '''
def setIssuers():
    '''public Builder setIssuers(final Collection<String> issuers)
    '''
def setAudience():
    '''public Builder setAudience(final Collection<String> audience)
    '''
def setAcceptableTimeSkewSeconds():
    '''public Builder setAcceptableTimeSkewSeconds(final long acceptableTimeSkewSeconds)
    '''
def setClock():
    '''public Builder setClock(final Clock clock)
    '''
