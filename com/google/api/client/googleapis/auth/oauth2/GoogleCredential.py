def ():
    '''returns Builder\n\n
    ()\n
    ()\n
    '''
def setAccessToken():
    '''returns GoogleCredential\n\n
    setAccessToken(final String accessToken)\n
    '''
def setRefreshToken():
    '''returns GoogleCredential\n\n
    setRefreshToken(final String refreshToken)\n
    '''
def setExpirationTimeMilliseconds():
    '''returns GoogleCredential\n\n
    setExpirationTimeMilliseconds(final Long expirationTimeMilliseconds)\n
    '''
def setExpiresInSeconds():
    '''returns GoogleCredential\n\n
    setExpiresInSeconds(final Long expiresIn)\n
    '''
def setFromTokenResponse():
    '''returns GoogleCredential\n\n
    setFromTokenResponse(final TokenResponse tokenResponse)\n
    '''
def createScopedRequired():
    '''returns boolean\n\n
    createScopedRequired()\n
    '''
def createScoped():
    '''returns GoogleCredential\n\n
    createScoped(final Collection<String> scopes)\n
    '''
def build():
    '''returns GoogleCredential\n\n
    build()\n
    '''
def setTransport():
    '''returns Builder\n\n
    setTransport(final HttpTransport transport)\n
    '''
def setJsonFactory():
    '''returns Builder\n\n
    setJsonFactory(final JsonFactory jsonFactory)\n
    '''
def setClock():
    '''returns Builder\n\n
    setClock(final Clock clock)\n
    '''
def setClientSecrets():
    '''returns Builder\n\n
    setClientSecrets(final String clientId, final String clientSecret)\n
    setClientSecrets(final GoogleClientSecrets clientSecrets)\n
    '''
def setServiceAccountId():
    '''returns Builder\n\n
    setServiceAccountId(final String serviceAccountId)\n
    '''
def setServiceAccountProjectId():
    '''returns Builder\n\n
    setServiceAccountProjectId(final String serviceAccountProjectId)\n
    '''
def setServiceAccountScopes():
    '''returns Builder\n\n
    setServiceAccountScopes(final Collection<String> serviceAccountScopes)\n
    '''
def setServiceAccountPrivateKey():
    '''returns Builder\n\n
    setServiceAccountPrivateKey(final PrivateKey serviceAccountPrivateKey)\n
    '''
def setServiceAccountPrivateKeyId():
    '''returns Builder\n\n
    setServiceAccountPrivateKeyId(final String serviceAccountPrivateKeyId)\n
    '''
def setServiceAccountPrivateKeyFromP12File():
    '''returns Builder\n\n
    setServiceAccountPrivateKeyFromP12File(final File p12File)\n
    '''
def setServiceAccountPrivateKeyFromPemFile():
    '''returns Builder\n\n
    setServiceAccountPrivateKeyFromPemFile(final File pemFile)\n
    '''
def setServiceAccountUser():
    '''returns Builder\n\n
    setServiceAccountUser(final String serviceAccountUser)\n
    '''
def setRequestInitializer():
    '''returns Builder\n\n
    setRequestInitializer(final HttpRequestInitializer requestInitializer)\n
    '''
def addRefreshListener():
    '''returns Builder\n\n
    addRefreshListener(final CredentialRefreshListener refreshListener)\n
    '''
def setRefreshListeners():
    '''returns Builder\n\n
    setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)\n
    '''
def setTokenServerUrl():
    '''returns Builder\n\n
    setTokenServerUrl(final GenericUrl tokenServerUrl)\n
    '''
def setTokenServerEncodedUrl():
    '''returns Builder\n\n
    setTokenServerEncodedUrl(final String tokenServerEncodedUrl)\n
    '''
def setClientAuthentication():
    '''returns Builder\n\n
    setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)\n
    '''
