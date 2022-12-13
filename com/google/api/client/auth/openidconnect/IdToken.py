def IdToken():
    '''public IdToken(final JsonWebSignature.Header header, final Payload payload, final byte[] signatureBytes, final byte[] signedContentBytes)
    '''
def getPayload():
    '''public Payload getPayload()
    '''
def verifyIssuer():
    '''public final boolean verifyIssuer(final String expectedIssuer)
    public final boolean verifyIssuer(final Collection<String> expectedIssuer)
    '''
def verifyAudience():
    '''public final boolean verifyAudience(final Collection<String> trustedClientIds)
    '''
def verifyTime():
    '''public final boolean verifyTime(final long currentTimeMillis, final long acceptableTimeSkewSeconds)
    '''
def verifyExpirationTime():
    '''public final boolean verifyExpirationTime(final long currentTimeMillis, final long acceptableTimeSkewSeconds)
    '''
def verifyIssuedAtTime():
    '''public final boolean verifyIssuedAtTime(final long currentTimeMillis, final long acceptableTimeSkewSeconds)
    '''
def parse():
    '''public static IdToken parse(final JsonFactory jsonFactory, final String idTokenString)
    '''
def getAuthorizationTimeSeconds():
    '''public final Long getAuthorizationTimeSeconds()
    '''
def setAuthorizationTimeSeconds():
    '''public Payload setAuthorizationTimeSeconds(final Long authorizationTimeSeconds)
    '''
def getAuthorizedParty():
    '''public final String getAuthorizedParty()
    '''
def setAuthorizedParty():
    '''public Payload setAuthorizedParty(final String authorizedParty)
    '''
def getNonce():
    '''public final String getNonce()
    '''
def setNonce():
    '''public Payload setNonce(final String nonce)
    '''
def getAccessTokenHash():
    '''public final String getAccessTokenHash()
    '''
def setAccessTokenHash():
    '''public Payload setAccessTokenHash(final String accessTokenHash)
    '''
def getClassReference():
    '''public final String getClassReference()
    '''
def setClassReference():
    '''public Payload setClassReference(final String classReference)
    '''
def getMethodsReferences():
    '''public final List<String> getMethodsReferences()
    '''
def setMethodsReferences():
    '''public Payload setMethodsReferences(final List<String> methodsReferences)
    '''
def setExpirationTimeSeconds():
    '''public Payload setExpirationTimeSeconds(final Long expirationTimeSeconds)
    '''
def setNotBeforeTimeSeconds():
    '''public Payload setNotBeforeTimeSeconds(final Long notBeforeTimeSeconds)
    '''
def setIssuedAtTimeSeconds():
    '''public Payload setIssuedAtTimeSeconds(final Long issuedAtTimeSeconds)
    '''
def setIssuer():
    '''public Payload setIssuer(final String issuer)
    '''
def setAudience():
    '''public Payload setAudience(final Object audience)
    '''
def setJwtId():
    '''public Payload setJwtId(final String jwtId)
    '''
def setType():
    '''public Payload setType(final String type)
    '''
def setSubject():
    '''public Payload setSubject(final String subject)
    '''
def set():
    '''public Payload set(final String fieldName, final Object value)
    '''
def clone():
    '''public Payload clone()
    '''
