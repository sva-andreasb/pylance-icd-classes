def DelegationTokenCache():
'''public DelegationTokenCache(final Collection<String> scramMechanisms)
'''
pass
def credential():
'''public ScramCredential credential(final String mechanism, final String tokenId)
'''
pass
def owner():
'''public String owner(final String tokenId)
'''
pass
def updateCache():
'''public void updateCache(final DelegationToken token, final Map<String, ScramCredential> scramCredentialMap)
'''
pass
def removeCache():
'''public void removeCache(final String tokenId)
'''
pass
def tokenForHmac():
'''public TokenInformation tokenForHmac(final String base64hmac)
'''
pass
def addToken():
'''public TokenInformation addToken(final String tokenId, final TokenInformation tokenInfo)
'''
pass
def removeToken():
'''public void removeToken(final String tokenId)
'''
pass
def tokens():
'''public Collection<TokenInformation> tokens()
'''
pass
def token():
'''public TokenInformation token(final String tokenId)
'''
pass
