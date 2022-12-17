def ():
    '''returns DelegationTokenCache\n\n
    (final Collection<String> scramMechanisms)\n
    '''
def credential():
    '''returns ScramCredential\n\n
    credential(final String mechanism, final String tokenId)\n
    '''
def owner():
    '''returns String\n\n
    owner(final String tokenId)\n
    '''
def updateCache():
    '''returns None\n\n
    updateCache(final DelegationToken token, final Map<String, ScramCredential> scramCredentialMap)\n
    '''
def removeCache():
    '''returns None\n\n
    removeCache(final String tokenId)\n
    '''
def tokenForHmac():
    '''returns TokenInformation\n\n
    tokenForHmac(final String base64hmac)\n
    '''
def addToken():
    '''returns TokenInformation\n\n
    addToken(final String tokenId, final TokenInformation tokenInfo)\n
    '''
def removeToken():
    '''returns None\n\n
    removeToken(final String tokenId)\n
    '''
def tokens():
    '''returns Collection<TokenInformation>\n\n
    tokens()\n
    '''
def token():
    '''returns TokenInformation\n\n
    token(final String tokenId)\n
    '''
