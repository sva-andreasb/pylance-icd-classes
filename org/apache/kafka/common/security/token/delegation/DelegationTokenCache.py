def DelegationTokenCache():
    '''    public DelegationTokenCache(final Collection<String> scramMechanisms)
    '''
def credential():
    '''    public ScramCredential credential(final String mechanism, final String tokenId)
    '''
def owner():
    '''    public String owner(final String tokenId)
    '''
def updateCache():
    '''    public void updateCache(final DelegationToken token, final Map<String, ScramCredential> scramCredentialMap)
    '''
def removeCache():
    '''    public void removeCache(final String tokenId)
    '''
def tokenForHmac():
    '''    public TokenInformation tokenForHmac(final String base64hmac)
    '''
def addToken():
    '''    public TokenInformation addToken(final String tokenId, final TokenInformation tokenInfo)
    '''
def removeToken():
    '''    public void removeToken(final String tokenId)
    '''
def tokens():
    '''    public Collection<TokenInformation> tokens()
    '''
def token():
    '''    public TokenInformation token(final String tokenId)
    '''
