def ():
    '''returns Builder\n\n
    (final HttpTransport transport, final JsonFactory jsonFactory, final String clientId, final String clientSecret, final Collection<String> scopes)\n
    (final HttpTransport transport, final JsonFactory jsonFactory, final String clientId, final String clientSecret, final Collection<String> scopes)\n
    (final HttpTransport transport, final JsonFactory jsonFactory, final GoogleClientSecrets clientSecrets, final Collection<String> scopes)\n
    '''
def newTokenRequest():
    '''returns GoogleAuthorizationCodeTokenRequest\n\n
    newTokenRequest(final String authorizationCode)\n
    '''
def newAuthorizationUrl():
    '''returns GoogleAuthorizationCodeRequestUrl\n\n
    newAuthorizationUrl()\n
    '''
def build():
    '''returns GoogleAuthorizationCodeFlow\n\n
    build()\n
    '''
def setDataStoreFactory():
    '''returns Builder\n\n
    setDataStoreFactory(final DataStoreFactory dataStore)\n
    '''
def setCredentialDataStore():
    '''returns Builder\n\n
    setCredentialDataStore(final DataStore<StoredCredential> typedDataStore)\n
    '''
def setCredentialCreatedListener():
    '''returns Builder\n\n
    setCredentialCreatedListener(final AuthorizationCodeFlow.CredentialCreatedListener credentialCreatedListener)\n
    '''
def setCredentialStore():
    '''returns Builder\n\n
    setCredentialStore(final CredentialStore credentialStore)\n
    '''
def setRequestInitializer():
    '''returns Builder\n\n
    setRequestInitializer(final HttpRequestInitializer requestInitializer)\n
    '''
def setScopes():
    '''returns Builder\n\n
    setScopes(final Collection<String> scopes)\n
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
def addRefreshListener():
    '''returns Builder\n\n
    addRefreshListener(final CredentialRefreshListener refreshListener)\n
    '''
def setRefreshListeners():
    '''returns Builder\n\n
    setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)\n
    '''
def setApprovalPrompt():
    '''returns Builder\n\n
    setApprovalPrompt(final String approvalPrompt)\n
    '''
def setAccessType():
    '''returns Builder\n\n
    setAccessType(final String accessType)\n
    '''
