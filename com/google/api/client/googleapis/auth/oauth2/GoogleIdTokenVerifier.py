def ():
    '''returns Builder\n\n
    (final HttpTransport transport, final JsonFactory jsonFactory)\n
    (final GooglePublicKeysManager publicKeys)\n
    (final HttpTransport transport, final JsonFactory jsonFactory)\n
    (final GooglePublicKeysManager publicKeys)\n
    '''
def verify():
    '''returns GoogleIdToken\n\n
    verify(final GoogleIdToken googleIdToken)\n
    verify(final String idTokenString)\n
    '''
def loadPublicCerts():
    '''returns GoogleIdTokenVerifier\n\n
    loadPublicCerts()\n
    '''
def build():
    '''returns GoogleIdTokenVerifier\n\n
    build()\n
    '''
def setPublicCertsEncodedUrl():
    '''returns Builder\n\n
    setPublicCertsEncodedUrl(final String publicKeysEncodedUrl)\n
    '''
def setIssuer():
    '''returns Builder\n\n
    setIssuer(final String issuer)\n
    '''
def setIssuers():
    '''returns Builder\n\n
    setIssuers(final Collection<String> issuers)\n
    '''
def setAudience():
    '''returns Builder\n\n
    setAudience(final Collection<String> audience)\n
    '''
def setAcceptableTimeSkewSeconds():
    '''returns Builder\n\n
    setAcceptableTimeSkewSeconds(final long acceptableTimeSkewSeconds)\n
    '''
def setClock():
    '''returns Builder\n\n
    setClock(final Clock clock)\n
    '''
