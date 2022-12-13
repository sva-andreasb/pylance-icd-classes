def AuthorizationCodeFlow():
    '''public AuthorizationCodeFlow(final Credential.AccessMethod method, final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final HttpExecuteInterceptor clientAuthentication, final String clientId, final String authorizationServerEncodedUrl)
    '''
def newAuthorizationUrl():
    '''public AuthorizationCodeRequestUrl newAuthorizationUrl()
    '''
def newTokenRequest():
    '''public AuthorizationCodeTokenRequest newTokenRequest(final String authorizationCode)
    '''
def createAndStoreCredential():
    '''public Credential createAndStoreCredential(final TokenResponse response, final String userId)
    '''
def loadCredential():
    '''public Credential loadCredential(final String userId)
    '''
def getTransport():
    '''public final HttpTransport getTransport()
    public final HttpTransport getTransport()
    '''
def getJsonFactory():
    '''public final JsonFactory getJsonFactory()
    public final JsonFactory getJsonFactory()
    '''
def getTokenServerEncodedUrl():
    '''public final String getTokenServerEncodedUrl()
    '''
def getClientAuthentication():
    '''public final HttpExecuteInterceptor getClientAuthentication()
    public final HttpExecuteInterceptor getClientAuthentication()
    '''
def getClientId():
    '''public final String getClientId()
    public final String getClientId()
    '''
def getAuthorizationServerEncodedUrl():
    '''public final String getAuthorizationServerEncodedUrl()
    public final String getAuthorizationServerEncodedUrl()
    '''
def getCredentialStore():
    '''public final CredentialStore getCredentialStore()
    public final CredentialStore getCredentialStore()
    '''
def getCredentialDataStore():
    '''public final DataStore<StoredCredential> getCredentialDataStore()
    public final DataStore<StoredCredential> getCredentialDataStore()
    '''
def getRequestInitializer():
    '''public final HttpRequestInitializer getRequestInitializer()
    public final HttpRequestInitializer getRequestInitializer()
    '''
def getScopesAsString():
    '''public final String getScopesAsString()
    '''
def getScopes():
    '''public final Collection<String> getScopes()
    public final Collection<String> getScopes()
    '''
def getClock():
    '''public final Clock getClock()
    public final Clock getClock()
    '''
def getRefreshListeners():
    '''public final Collection<CredentialRefreshListener> getRefreshListeners()
    public final Collection<CredentialRefreshListener> getRefreshListeners()
    '''
def Builder():
    '''public Builder(final Credential.AccessMethod method, final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final HttpExecuteInterceptor clientAuthentication, final String clientId, final String authorizationServerEncodedUrl)
    '''
def build():
    '''public AuthorizationCodeFlow build()
    '''
def setMethod():
    '''public Builder setMethod(final Credential.AccessMethod method)
    '''
def setTransport():
    '''public Builder setTransport(final HttpTransport transport)
    '''
def setJsonFactory():
    '''public Builder setJsonFactory(final JsonFactory jsonFactory)
    '''
def getTokenServerUrl():
    '''public final GenericUrl getTokenServerUrl()
    '''
def setTokenServerUrl():
    '''public Builder setTokenServerUrl(final GenericUrl tokenServerUrl)
    '''
def setClientAuthentication():
    '''public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
    '''
def setClientId():
    '''public Builder setClientId(final String clientId)
    '''
def setAuthorizationServerEncodedUrl():
    '''public Builder setAuthorizationServerEncodedUrl(final String authorizationServerEncodedUrl)
    '''
def setClock():
    '''public Builder setClock(final Clock clock)
    '''
def setCredentialStore():
    '''public Builder setCredentialStore(final CredentialStore credentialStore)
    '''
def setDataStoreFactory():
    '''public Builder setDataStoreFactory(final DataStoreFactory dataStoreFactory)
    '''
def setCredentialDataStore():
    '''public Builder setCredentialDataStore(final DataStore<StoredCredential> credentialDataStore)
    '''
def setRequestInitializer():
    '''public Builder setRequestInitializer(final HttpRequestInitializer requestInitializer)
    '''
def setScopes():
    '''public Builder setScopes(final Collection<String> scopes)
    '''
def setCredentialCreatedListener():
    '''public Builder setCredentialCreatedListener(final CredentialCreatedListener credentialCreatedListener)
    '''
def addRefreshListener():
    '''public Builder addRefreshListener(final CredentialRefreshListener refreshListener)
    '''
def setRefreshListeners():
    '''public Builder setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)
    '''
def getCredentialCreatedListener():
    '''public final CredentialCreatedListener getCredentialCreatedListener()
    '''
