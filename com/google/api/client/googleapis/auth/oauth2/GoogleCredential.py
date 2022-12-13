def getApplicationDefault():
'''public static GoogleCredential getApplicationDefault()
public static GoogleCredential getApplicationDefault(final HttpTransport transport, final JsonFactory jsonFactory)
'''
pass
def fromStream():
'''public static GoogleCredential fromStream(final InputStream credentialStream)
public static GoogleCredential fromStream(final InputStream credentialStream, final HttpTransport transport, final JsonFactory jsonFactory)
'''
pass
def GoogleCredential():
'''public GoogleCredential()
'''
pass
def setAccessToken():
'''public GoogleCredential setAccessToken(final String accessToken)
'''
pass
def setRefreshToken():
'''public GoogleCredential setRefreshToken(final String refreshToken)
'''
pass
def setExpirationTimeMilliseconds():
'''public GoogleCredential setExpirationTimeMilliseconds(final Long expirationTimeMilliseconds)
'''
pass
def setExpiresInSeconds():
'''public GoogleCredential setExpiresInSeconds(final Long expiresIn)
'''
pass
def setFromTokenResponse():
'''public GoogleCredential setFromTokenResponse(final TokenResponse tokenResponse)
'''
pass
def getServiceAccountId():
'''public final String getServiceAccountId()
public final String getServiceAccountId()
'''
pass
def getServiceAccountProjectId():
'''public final String getServiceAccountProjectId()
public final String getServiceAccountProjectId()
'''
pass
def getServiceAccountScopes():
'''public final Collection<String> getServiceAccountScopes()
public final Collection<String> getServiceAccountScopes()
'''
pass
def getServiceAccountScopesAsString():
'''public final String getServiceAccountScopesAsString()
'''
pass
def getServiceAccountPrivateKey():
'''public final PrivateKey getServiceAccountPrivateKey()
public final PrivateKey getServiceAccountPrivateKey()
'''
pass
def getServiceAccountPrivateKeyId():
'''public final String getServiceAccountPrivateKeyId()
public final String getServiceAccountPrivateKeyId()
'''
pass
def getServiceAccountUser():
'''public final String getServiceAccountUser()
public final String getServiceAccountUser()
'''
pass
def createScopedRequired():
'''public boolean createScopedRequired()
'''
pass
def createScoped():
'''public GoogleCredential createScoped(final Collection<String> scopes)
'''
pass
def Builder():
'''public Builder()
'''
pass
def build():
'''public GoogleCredential build()
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
def setClock():
'''public Builder setClock(final Clock clock)
'''
pass
def setClientSecrets():
'''public Builder setClientSecrets(final String clientId, final String clientSecret)
public Builder setClientSecrets(final GoogleClientSecrets clientSecrets)
'''
pass
def setServiceAccountId():
'''public Builder setServiceAccountId(final String serviceAccountId)
'''
pass
def setServiceAccountProjectId():
'''public Builder setServiceAccountProjectId(final String serviceAccountProjectId)
'''
pass
def setServiceAccountScopes():
'''public Builder setServiceAccountScopes(final Collection<String> serviceAccountScopes)
'''
pass
def setServiceAccountPrivateKey():
'''public Builder setServiceAccountPrivateKey(final PrivateKey serviceAccountPrivateKey)
'''
pass
def setServiceAccountPrivateKeyId():
'''public Builder setServiceAccountPrivateKeyId(final String serviceAccountPrivateKeyId)
'''
pass
def setServiceAccountPrivateKeyFromP12File():
'''public Builder setServiceAccountPrivateKeyFromP12File(final File p12File)
'''
pass
def setServiceAccountPrivateKeyFromPemFile():
'''public Builder setServiceAccountPrivateKeyFromPemFile(final File pemFile)
'''
pass
def setServiceAccountUser():
'''public Builder setServiceAccountUser(final String serviceAccountUser)
'''
pass
def setRequestInitializer():
'''public Builder setRequestInitializer(final HttpRequestInitializer requestInitializer)
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
def setTokenServerUrl():
'''public Builder setTokenServerUrl(final GenericUrl tokenServerUrl)
'''
pass
def setTokenServerEncodedUrl():
'''public Builder setTokenServerEncodedUrl(final String tokenServerEncodedUrl)
'''
pass
def setClientAuthentication():
'''public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
'''
pass
