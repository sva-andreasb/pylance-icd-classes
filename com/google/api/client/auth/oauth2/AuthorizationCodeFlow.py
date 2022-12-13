def AuthorizationCodeFlow():
'''public AuthorizationCodeFlow(final Credential.AccessMethod method, final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final HttpExecuteInterceptor clientAuthentication, final String clientId, final String authorizationServerEncodedUrl)
'''
pass
def newAuthorizationUrl():
'''public AuthorizationCodeRequestUrl newAuthorizationUrl()
'''
pass
def newTokenRequest():
'''public AuthorizationCodeTokenRequest newTokenRequest(final String authorizationCode)
'''
pass
def createAndStoreCredential():
'''public Credential createAndStoreCredential(final TokenResponse response, final String userId)
'''
pass
def loadCredential():
'''public Credential loadCredential(final String userId)
'''
pass
def getTransport():
'''public final HttpTransport getTransport()
public final HttpTransport getTransport()
'''
pass
def getJsonFactory():
'''public final JsonFactory getJsonFactory()
public final JsonFactory getJsonFactory()
'''
pass
def getTokenServerEncodedUrl():
'''public final String getTokenServerEncodedUrl()
'''
pass
def getClientAuthentication():
'''public final HttpExecuteInterceptor getClientAuthentication()
public final HttpExecuteInterceptor getClientAuthentication()
'''
pass
def getClientId():
'''public final String getClientId()
public final String getClientId()
'''
pass
def getAuthorizationServerEncodedUrl():
'''public final String getAuthorizationServerEncodedUrl()
public final String getAuthorizationServerEncodedUrl()
'''
pass
def getCredentialStore():
'''public final CredentialStore getCredentialStore()
public final CredentialStore getCredentialStore()
'''
pass
def getCredentialDataStore():
'''public final DataStore<StoredCredential> getCredentialDataStore()
public final DataStore<StoredCredential> getCredentialDataStore()
'''
pass
def getRequestInitializer():
'''public final HttpRequestInitializer getRequestInitializer()
public final HttpRequestInitializer getRequestInitializer()
'''
pass
def getScopesAsString():
'''public final String getScopesAsString()
'''
pass
def getScopes():
'''public final Collection<String> getScopes()
public final Collection<String> getScopes()
'''
pass
def getClock():
'''public final Clock getClock()
public final Clock getClock()
'''
pass
def getRefreshListeners():
'''public final Collection<CredentialRefreshListener> getRefreshListeners()
public final Collection<CredentialRefreshListener> getRefreshListeners()
'''
pass
def Builder():
'''public Builder(final Credential.AccessMethod method, final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final HttpExecuteInterceptor clientAuthentication, final String clientId, final String authorizationServerEncodedUrl)
'''
pass
def build():
'''public AuthorizationCodeFlow build()
'''
pass
def setMethod():
'''public Builder setMethod(final Credential.AccessMethod method)
'''
pass
def setTransport():
'''public Builder setTransport(final HttpTransport transport)
'''
pass
def setJsonFactory():
'''public Builder setJsonFactory(final JsonFactory jsonFactory)
'''
pass
def getTokenServerUrl():
'''public final GenericUrl getTokenServerUrl()
'''
pass
def setTokenServerUrl():
'''public Builder setTokenServerUrl(final GenericUrl tokenServerUrl)
'''
pass
def setClientAuthentication():
'''public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
'''
pass
def setClientId():
'''public Builder setClientId(final String clientId)
'''
pass
def setAuthorizationServerEncodedUrl():
'''public Builder setAuthorizationServerEncodedUrl(final String authorizationServerEncodedUrl)
'''
pass
def setClock():
'''public Builder setClock(final Clock clock)
'''
pass
def setCredentialStore():
'''public Builder setCredentialStore(final CredentialStore credentialStore)
'''
pass
def setDataStoreFactory():
'''public Builder setDataStoreFactory(final DataStoreFactory dataStoreFactory)
'''
pass
def setCredentialDataStore():
'''public Builder setCredentialDataStore(final DataStore<StoredCredential> credentialDataStore)
'''
pass
def setRequestInitializer():
'''public Builder setRequestInitializer(final HttpRequestInitializer requestInitializer)
'''
pass
def setScopes():
'''public Builder setScopes(final Collection<String> scopes)
'''
pass
def setCredentialCreatedListener():
'''public Builder setCredentialCreatedListener(final CredentialCreatedListener credentialCreatedListener)
'''
pass
def addRefreshListener():
'''public Builder addRefreshListener(final CredentialRefreshListener refreshListener)
'''
pass
def setRefreshListeners():
'''public Builder setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)
'''
pass
def getCredentialCreatedListener():
'''public final CredentialCreatedListener getCredentialCreatedListener()
'''
pass
