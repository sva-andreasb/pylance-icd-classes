def IdToken():
'''public IdToken(final JsonWebSignature.Header header, final Payload payload, final byte[] signatureBytes, final byte[] signedContentBytes)
'''
pass
def getPayload():
'''public Payload getPayload()
'''
pass
def verifyIssuer():
'''public final boolean verifyIssuer(final String expectedIssuer)
public final boolean verifyIssuer(final Collection<String> expectedIssuer)
'''
pass
def verifyAudience():
'''public final boolean verifyAudience(final Collection<String> trustedClientIds)
'''
pass
def verifyTime():
'''public final boolean verifyTime(final long currentTimeMillis, final long acceptableTimeSkewSeconds)
'''
pass
def verifyExpirationTime():
'''public final boolean verifyExpirationTime(final long currentTimeMillis, final long acceptableTimeSkewSeconds)
'''
pass
def verifyIssuedAtTime():
'''public final boolean verifyIssuedAtTime(final long currentTimeMillis, final long acceptableTimeSkewSeconds)
'''
pass
def parse():
'''public static IdToken parse(final JsonFactory jsonFactory, final String idTokenString)
'''
pass
def getAuthorizationTimeSeconds():
'''public final Long getAuthorizationTimeSeconds()
'''
pass
def setAuthorizationTimeSeconds():
'''public Payload setAuthorizationTimeSeconds(final Long authorizationTimeSeconds)
'''
pass
def getAuthorizedParty():
'''public final String getAuthorizedParty()
'''
pass
def setAuthorizedParty():
'''public Payload setAuthorizedParty(final String authorizedParty)
'''
pass
def getNonce():
'''public final String getNonce()
'''
pass
def setNonce():
'''public Payload setNonce(final String nonce)
'''
pass
def getAccessTokenHash():
'''public final String getAccessTokenHash()
'''
pass
def setAccessTokenHash():
'''public Payload setAccessTokenHash(final String accessTokenHash)
'''
pass
def getClassReference():
'''public final String getClassReference()
'''
pass
def setClassReference():
'''public Payload setClassReference(final String classReference)
'''
pass
def getMethodsReferences():
'''public final List<String> getMethodsReferences()
'''
pass
def setMethodsReferences():
'''public Payload setMethodsReferences(final List<String> methodsReferences)
'''
pass
def setExpirationTimeSeconds():
'''public Payload setExpirationTimeSeconds(final Long expirationTimeSeconds)
'''
pass
def setNotBeforeTimeSeconds():
'''public Payload setNotBeforeTimeSeconds(final Long notBeforeTimeSeconds)
'''
pass
def setIssuedAtTimeSeconds():
'''public Payload setIssuedAtTimeSeconds(final Long issuedAtTimeSeconds)
'''
pass
def setIssuer():
'''public Payload setIssuer(final String issuer)
'''
pass
def setAudience():
'''public Payload setAudience(final Object audience)
'''
pass
def setJwtId():
'''public Payload setJwtId(final String jwtId)
'''
pass
def setType():
'''public Payload setType(final String type)
'''
pass
def setSubject():
'''public Payload setSubject(final String subject)
'''
pass
def set():
'''public Payload set(final String fieldName, final Object value)
'''
pass
def clone():
'''public Payload clone()
'''
pass
