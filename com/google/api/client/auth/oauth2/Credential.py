def Credential():
    '''    public Credential(final AccessMethod method)
    '''
def intercept():
    '''    public void intercept(final HttpRequest request)
    '''
def handleResponse():
    '''    public boolean handleResponse(final HttpRequest request, final HttpResponse response, final boolean supportsRetry)
    '''
def initialize():
    '''    public void initialize(final HttpRequest request)
    '''
def getAccessToken():
    '''    public final String getAccessToken()
    '''
def setAccessToken():
    '''    public Credential setAccessToken(final String accessToken)
    '''
def getMethod():
    '''    public final AccessMethod getMethod()
    public final AccessMethod getMethod()
    '''
def getClock():
    '''    public final Clock getClock()
    public final Clock getClock()
    '''
def getTransport():
    '''    public final HttpTransport getTransport()
    public final HttpTransport getTransport()
    '''
def getJsonFactory():
    '''    public final JsonFactory getJsonFactory()
    public final JsonFactory getJsonFactory()
    '''
def getTokenServerEncodedUrl():
    '''    public final String getTokenServerEncodedUrl()
    '''
def getRefreshToken():
    '''    public final String getRefreshToken()
    '''
def setRefreshToken():
    '''    public Credential setRefreshToken(final String refreshToken)
    '''
def getExpirationTimeMilliseconds():
    '''    public final Long getExpirationTimeMilliseconds()
    '''
def setExpirationTimeMilliseconds():
    '''    public Credential setExpirationTimeMilliseconds(final Long expirationTimeMilliseconds)
    '''
def getExpiresInSeconds():
    '''    public final Long getExpiresInSeconds()
    '''
def setExpiresInSeconds():
    '''    public Credential setExpiresInSeconds(final Long expiresIn)
    '''
def getClientAuthentication():
    '''    public final HttpExecuteInterceptor getClientAuthentication()
    public final HttpExecuteInterceptor getClientAuthentication()
    '''
def getRequestInitializer():
    '''    public final HttpRequestInitializer getRequestInitializer()
    public final HttpRequestInitializer getRequestInitializer()
    '''
def refreshToken():
    '''    public final boolean refreshToken()
    '''
def setFromTokenResponse():
    '''    public Credential setFromTokenResponse(final TokenResponse tokenResponse)
    '''
def getRefreshListeners():
    '''    public final Collection<CredentialRefreshListener> getRefreshListeners()
    public final Collection<CredentialRefreshListener> getRefreshListeners()
    '''
def Builder():
    '''    public Builder(final AccessMethod method)
    '''
def build():
    '''    public Credential build()
    '''
def setTransport():
    '''    public Builder setTransport(final HttpTransport transport)
    '''
def setClock():
    '''    public Builder setClock(final Clock clock)
    '''
def setJsonFactory():
    '''    public Builder setJsonFactory(final JsonFactory jsonFactory)
    '''
def getTokenServerUrl():
    '''    public final GenericUrl getTokenServerUrl()
    '''
def setTokenServerUrl():
    '''    public Builder setTokenServerUrl(final GenericUrl tokenServerUrl)
    '''
def setTokenServerEncodedUrl():
    '''    public Builder setTokenServerEncodedUrl(final String tokenServerEncodedUrl)
    '''
def setClientAuthentication():
    '''    public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
    '''
def setRequestInitializer():
    '''    public Builder setRequestInitializer(final HttpRequestInitializer requestInitializer)
    '''
def addRefreshListener():
    '''    public Builder addRefreshListener(final CredentialRefreshListener refreshListener)
    '''
def setRefreshListeners():
    '''    public Builder setRefreshListeners(final Collection<CredentialRefreshListener> refreshListeners)
    '''
