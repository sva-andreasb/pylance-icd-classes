def GoogleAuthorizationCodeFlow():
'''public GoogleAuthorizationCodeFlow(final HttpTransport transport, final JsonFactory jsonFactory, final String clientId, final String clientSecret, final Collection<String> scopes)
'''
pass
def newTokenRequest():
'''public GoogleAuthorizationCodeTokenRequest newTokenRequest(final String authorizationCode)
'''
pass
def newAuthorizationUrl():
'''public GoogleAuthorizationCodeRequestUrl newAuthorizationUrl()
'''
pass
def getApprovalPrompt():
'''public final String getApprovalPrompt()
public final String getApprovalPrompt()
'''
pass
def getAccessType():
'''public final String getAccessType()
public final String getAccessType()
'''
pass
def Builder():
'''public Builder(final HttpTransport transport, final JsonFactory jsonFactory, final String clientId, final String clientSecret, final Collection<String> scopes)
public Builder(final HttpTransport transport, final JsonFactory jsonFactory, final GoogleClientSecrets clientSecrets, final Collection<String> scopes)
'''
pass
def build():
'''public GoogleAuthorizationCodeFlow build()
'''
pass
def setDataStoreFactory():
'''public Builder setDataStoreFactory(final DataStoreFactory dataStore)
'''
pass
def setCredentialDataStore():
'''public Builder setCredentialDataStore(final DataStore<StoredCredential> typedDataStore)
'''
pass
def setCredentialCreatedListener():
'''public Builder setCredentialCreatedListener(final AuthorizationCodeFlow.CredentialCreatedListener credentialCreatedListener)
'''
pass
def setCredentialStore():
'''public Builder setCredentialStore(final CredentialStore credentialStore)
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
def addRefreshListener():
'''public Builder addRefreshListener(final CredentialRefreshListener refreshListener)
'''
pass
def setRefreshListeners():
'''public Builder setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)
'''
pass
def setApprovalPrompt():
'''public Builder setApprovalPrompt(final String approvalPrompt)
'''
pass
def setAccessType():
'''public Builder setAccessType(final String accessType)
'''
pass
