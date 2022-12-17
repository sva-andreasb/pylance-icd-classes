def ():
    '''returns DataStoreCredentialRefreshListener\n\n
    (final String userId, final DataStoreFactory dataStoreFactory)\n
    (final String userId, final DataStore<StoredCredential> credentialDataStore)\n
    '''
def onTokenResponse():
    '''returns None\n\n
    onTokenResponse(final Credential credential, final TokenResponse tokenResponse)\n
    '''
def onTokenErrorResponse():
    '''returns None\n\n
    onTokenErrorResponse(final Credential credential, final TokenErrorResponse tokenErrorResponse)\n
    '''
def getCredentialDataStore():
    '''returns DataStore<StoredCredential>\n\n
    getCredentialDataStore()\n
    '''
def makePersistent():
    '''returns None\n\n
    makePersistent(final Credential credential)\n
    '''
