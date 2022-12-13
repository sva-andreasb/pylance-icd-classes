def GoogleAuthorizationCodeFlow():
    '''    public GoogleAuthorizationCodeFlow(final HttpTransport transport, final JsonFactory jsonFactory, final String clientId, final String clientSecret, final Collection<String> scopes)
    '''
def newTokenRequest():
    '''    public GoogleAuthorizationCodeTokenRequest newTokenRequest(final String authorizationCode)
    '''
def newAuthorizationUrl():
    '''    public GoogleAuthorizationCodeRequestUrl newAuthorizationUrl()
    '''
def getApprovalPrompt():
    '''    public final String getApprovalPrompt()
    public final String getApprovalPrompt()
    '''
def getAccessType():
    '''    public final String getAccessType()
    public final String getAccessType()
    '''
def Builder():
    '''    public Builder(final HttpTransport transport, final JsonFactory jsonFactory, final String clientId, final String clientSecret, final Collection<String> scopes)
    public Builder(final HttpTransport transport, final JsonFactory jsonFactory, final GoogleClientSecrets clientSecrets, final Collection<String> scopes)
    '''
def build():
    '''    public GoogleAuthorizationCodeFlow build()
    '''
def setDataStoreFactory():
    '''    public Builder setDataStoreFactory(final DataStoreFactory dataStore)
    '''
def setCredentialDataStore():
    '''    public Builder setCredentialDataStore(final DataStore<StoredCredential> typedDataStore)
    '''
def setCredentialCreatedListener():
    '''    public Builder setCredentialCreatedListener(final AuthorizationCodeFlow.CredentialCreatedListener credentialCreatedListener)
    '''
def setCredentialStore():
    '''    public Builder setCredentialStore(final CredentialStore credentialStore)
    '''
def setRequestInitializer():
    '''    public Builder setRequestInitializer(final HttpRequestInitializer requestInitializer)
    '''
def setScopes():
    '''    public Builder setScopes(final Collection<String> scopes)
    '''
def setMethod():
    '''    public Builder setMethod(final Credential.AccessMethod method)
    '''
def setTransport():
    '''    public Builder setTransport(final HttpTransport transport)
    '''
def setJsonFactory():
    '''    public Builder setJsonFactory(final JsonFactory jsonFactory)
    '''
def setTokenServerUrl():
    '''    public Builder setTokenServerUrl(final GenericUrl tokenServerUrl)
    '''
def setClientAuthentication():
    '''    public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
    '''
def setClientId():
    '''    public Builder setClientId(final String clientId)
    '''
def setAuthorizationServerEncodedUrl():
    '''    public Builder setAuthorizationServerEncodedUrl(final String authorizationServerEncodedUrl)
    '''
def setClock():
    '''    public Builder setClock(final Clock clock)
    '''
def addRefreshListener():
    '''    public Builder addRefreshListener(final CredentialRefreshListener refreshListener)
    '''
def setRefreshListeners():
    '''    public Builder setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)
    '''
def setApprovalPrompt():
    '''    public Builder setApprovalPrompt(final String approvalPrompt)
    '''
def setAccessType():
    '''    public Builder setAccessType(final String accessType)
    '''
