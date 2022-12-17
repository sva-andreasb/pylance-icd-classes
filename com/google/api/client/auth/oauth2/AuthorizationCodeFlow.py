def ():
    '''returns Builder\n\n
    (final Credential.AccessMethod method, final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final HttpExecuteInterceptor clientAuthentication, final String clientId, final String authorizationServerEncodedUrl)\n
    (final Credential.AccessMethod method, final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final HttpExecuteInterceptor clientAuthentication, final String clientId, final String authorizationServerEncodedUrl)\n
    '''
def newAuthorizationUrl():
    '''returns AuthorizationCodeRequestUrl\n\n
    newAuthorizationUrl()\n
    '''
def newTokenRequest():
    '''returns AuthorizationCodeTokenRequest\n\n
    newTokenRequest(final String authorizationCode)\n
    '''
def createAndStoreCredential():
    '''returns Credential\n\n
    createAndStoreCredential(final TokenResponse response, final String userId)\n
    '''
def loadCredential():
    '''returns Credential\n\n
    loadCredential(final String userId)\n
    '''
def build():
    '''returns AuthorizationCodeFlow\n\n
    build()\n
    '''
def setMethod():
    '''returns Builder\n\n
    setMethod(final Credential.AccessMethod method)\n
    '''
def setTransport():
    '''returns Builder\n\n
    setTransport(final HttpTransport transport)\n
    '''
def setJsonFactory():
    '''returns Builder\n\n
    setJsonFactory(final JsonFactory jsonFactory)\n
    '''
def setTokenServerUrl():
    '''returns Builder\n\n
    setTokenServerUrl(final GenericUrl tokenServerUrl)\n
    '''
def setClientAuthentication():
    '''returns Builder\n\n
    setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)\n
    '''
def setClientId():
    '''returns Builder\n\n
    setClientId(final String clientId)\n
    '''
def setAuthorizationServerEncodedUrl():
    '''returns Builder\n\n
    setAuthorizationServerEncodedUrl(final String authorizationServerEncodedUrl)\n
    '''
def setClock():
    '''returns Builder\n\n
    setClock(final Clock clock)\n
    '''
def setCredentialStore():
    '''returns Builder\n\n
    setCredentialStore(final CredentialStore credentialStore)\n
    '''
def setDataStoreFactory():
    '''returns Builder\n\n
    setDataStoreFactory(final DataStoreFactory dataStoreFactory)\n
    '''
def setCredentialDataStore():
    '''returns Builder\n\n
    setCredentialDataStore(final DataStore<StoredCredential> credentialDataStore)\n
    '''
def setRequestInitializer():
    '''returns Builder\n\n
    setRequestInitializer(final HttpRequestInitializer requestInitializer)\n
    '''
def setScopes():
    '''returns Builder\n\n
    setScopes(final Collection<String> scopes)\n
    '''
def setCredentialCreatedListener():
    '''returns Builder\n\n
    setCredentialCreatedListener(final CredentialCreatedListener credentialCreatedListener)\n
    '''
def addRefreshListener():
    '''returns Builder\n\n
    addRefreshListener(final CredentialRefreshListener refreshListener)\n
    '''
def setRefreshListeners():
    '''returns Builder\n\n
    setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)\n
    '''
