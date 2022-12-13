def GoogleIdTokenVerifier():
'''public GoogleIdTokenVerifier(final HttpTransport transport, final JsonFactory jsonFactory)
public GoogleIdTokenVerifier(final GooglePublicKeysManager publicKeys)
'''
pass
def getPublicKeysManager():
'''public final GooglePublicKeysManager getPublicKeysManager()
'''
pass
def getTransport():
'''public final HttpTransport getTransport()
public final HttpTransport getTransport()
'''
pass
def getJsonFactory():
'''public final JsonFactory getJsonFactory()
public final JsonFactory getJsonFactory()
'''
pass
def getPublicCertsEncodedUrl():
'''public final String getPublicCertsEncodedUrl()
public final String getPublicCertsEncodedUrl()
'''
pass
def getPublicKeys():
'''public final List<PublicKey> getPublicKeys()
'''
pass
def getExpirationTimeMilliseconds():
'''public final long getExpirationTimeMilliseconds()
'''
pass
def verify():
'''public boolean verify(final GoogleIdToken googleIdToken)
public GoogleIdToken verify(final String idTokenString)
'''
pass
def loadPublicCerts():
'''public GoogleIdTokenVerifier loadPublicCerts()
'''
pass
def Builder():
'''public Builder(final HttpTransport transport, final JsonFactory jsonFactory)
public Builder(final GooglePublicKeysManager publicKeys)
'''
pass
def build():
'''public GoogleIdTokenVerifier build()
'''
pass
def getPublicCerts():
'''public final GooglePublicKeysManager getPublicCerts()
'''
pass
def setPublicCertsEncodedUrl():
'''public Builder setPublicCertsEncodedUrl(final String publicKeysEncodedUrl)
'''
pass
def setIssuer():
'''public Builder setIssuer(final String issuer)
'''
pass
def setIssuers():
'''public Builder setIssuers(final Collection<String> issuers)
'''
pass
def setAudience():
'''public Builder setAudience(final Collection<String> audience)
'''
pass
def setAcceptableTimeSkewSeconds():
'''public Builder setAcceptableTimeSkewSeconds(final long acceptableTimeSkewSeconds)
'''
pass
def setClock():
'''public Builder setClock(final Clock clock)
'''
pass
