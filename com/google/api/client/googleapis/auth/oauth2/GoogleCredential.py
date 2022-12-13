def getApplicationDefault():
    '''public static GoogleCredential getApplicationDefault()
    public static GoogleCredential getApplicationDefault(final HttpTransport transport, final JsonFactory jsonFactory)
    '''
def fromStream():
    '''public static GoogleCredential fromStream(final InputStream credentialStream)
    public static GoogleCredential fromStream(final InputStream credentialStream, final HttpTransport transport, final JsonFactory jsonFactory)
    '''
def GoogleCredential():
    '''public GoogleCredential()
    '''
def setAccessToken():
    '''public GoogleCredential setAccessToken(final String accessToken)
    '''
def setRefreshToken():
    '''public GoogleCredential setRefreshToken(final String refreshToken)
    '''
def setExpirationTimeMilliseconds():
    '''public GoogleCredential setExpirationTimeMilliseconds(final Long expirationTimeMilliseconds)
    '''
def setExpiresInSeconds():
    '''public GoogleCredential setExpiresInSeconds(final Long expiresIn)
    '''
def setFromTokenResponse():
    '''public GoogleCredential setFromTokenResponse(final TokenResponse tokenResponse)
    '''
def getServiceAccountId():
    '''public final String getServiceAccountId()
    public final String getServiceAccountId()
    '''
def getServiceAccountProjectId():
    '''public final String getServiceAccountProjectId()
    public final String getServiceAccountProjectId()
    '''
def getServiceAccountScopes():
    '''public final Collection<String> getServiceAccountScopes()
    public final Collection<String> getServiceAccountScopes()
    '''
def getServiceAccountScopesAsString():
    '''public final String getServiceAccountScopesAsString()
    '''
def getServiceAccountPrivateKey():
    '''public final PrivateKey getServiceAccountPrivateKey()
    public final PrivateKey getServiceAccountPrivateKey()
    '''
def getServiceAccountPrivateKeyId():
    '''public final String getServiceAccountPrivateKeyId()
    public final String getServiceAccountPrivateKeyId()
    '''
def getServiceAccountUser():
    '''public final String getServiceAccountUser()
    public final String getServiceAccountUser()
    '''
def createScopedRequired():
    '''public boolean createScopedRequired()
    '''
def createScoped():
    '''public GoogleCredential createScoped(final Collection<String> scopes)
    '''
def Builder():
    '''public Builder()
    '''
def build():
    '''public GoogleCredential build()
    '''
def setTransport():
    '''public Builder setTransport(final HttpTransport transport)
    '''
def setJsonFactory():
    '''public Builder setJsonFactory(final JsonFactory jsonFactory)
    '''
def setClock():
    '''public Builder setClock(final Clock clock)
    '''
def setClientSecrets():
    '''public Builder setClientSecrets(final String clientId, final String clientSecret)
    public Builder setClientSecrets(final GoogleClientSecrets clientSecrets)
    '''
def setServiceAccountId():
    '''public Builder setServiceAccountId(final String serviceAccountId)
    '''
def setServiceAccountProjectId():
    '''public Builder setServiceAccountProjectId(final String serviceAccountProjectId)
    '''
def setServiceAccountScopes():
    '''public Builder setServiceAccountScopes(final Collection<String> serviceAccountScopes)
    '''
def setServiceAccountPrivateKey():
    '''public Builder setServiceAccountPrivateKey(final PrivateKey serviceAccountPrivateKey)
    '''
def setServiceAccountPrivateKeyId():
    '''public Builder setServiceAccountPrivateKeyId(final String serviceAccountPrivateKeyId)
    '''
def setServiceAccountPrivateKeyFromP12File():
    '''public Builder setServiceAccountPrivateKeyFromP12File(final File p12File)
    '''
def setServiceAccountPrivateKeyFromPemFile():
    '''public Builder setServiceAccountPrivateKeyFromPemFile(final File pemFile)
    '''
def setServiceAccountUser():
    '''public Builder setServiceAccountUser(final String serviceAccountUser)
    '''
def setRequestInitializer():
    '''public Builder setRequestInitializer(final HttpRequestInitializer requestInitializer)
    '''
def addRefreshListener():
    '''public Builder addRefreshListener(final CredentialRefreshListener refreshListener)
    '''
def setRefreshListeners():
    '''public Builder setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)
    '''
def setTokenServerUrl():
    '''public Builder setTokenServerUrl(final GenericUrl tokenServerUrl)
    '''
def setTokenServerEncodedUrl():
    '''public Builder setTokenServerEncodedUrl(final String tokenServerEncodedUrl)
    '''
def setClientAuthentication():
    '''public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
    '''
