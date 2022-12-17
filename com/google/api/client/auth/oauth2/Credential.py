def ():
    '''returns Builder\n\n
    (final AccessMethod method)\n
    (final AccessMethod method)\n
    '''
def intercept():
    '''returns None\n\n
    intercept(final HttpRequest request)\n
    '''
def handleResponse():
    '''returns boolean\n\n
    handleResponse(final HttpRequest request, final HttpResponse response, final boolean supportsRetry)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final HttpRequest request)\n
    '''
def setAccessToken():
    '''returns Credential\n\n
    setAccessToken(final String accessToken)\n
    '''
def setRefreshToken():
    '''returns Credential\n\n
    setRefreshToken(final String refreshToken)\n
    '''
def setExpirationTimeMilliseconds():
    '''returns Credential\n\n
    setExpirationTimeMilliseconds(final Long expirationTimeMilliseconds)\n
    '''
def setExpiresInSeconds():
    '''returns Credential\n\n
    setExpiresInSeconds(final Long expiresIn)\n
    '''
def setFromTokenResponse():
    '''returns Credential\n\n
    setFromTokenResponse(final TokenResponse tokenResponse)\n
    '''
def build():
    '''returns Credential\n\n
    build()\n
    '''
def setTransport():
    '''returns Builder\n\n
    setTransport(final HttpTransport transport)\n
    '''
def setClock():
    '''returns Builder\n\n
    setClock(final Clock clock)\n
    '''
def setJsonFactory():
    '''returns Builder\n\n
    setJsonFactory(final JsonFactory jsonFactory)\n
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
