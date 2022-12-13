def Credential():
'''public Credential(final AccessMethod method)
'''
pass
def intercept():
'''public void intercept(final HttpRequest request)
'''
pass
def handleResponse():
'''public boolean handleResponse(final HttpRequest request, final HttpResponse response, final boolean supportsRetry)
'''
pass
def initialize():
'''public void initialize(final HttpRequest request)
'''
pass
def getAccessToken():
'''public final String getAccessToken()
'''
pass
def setAccessToken():
'''public Credential setAccessToken(final String accessToken)
'''
pass
def getMethod():
'''public final AccessMethod getMethod()
public final AccessMethod getMethod()
'''
pass
def getClock():
'''public final Clock getClock()
public final Clock getClock()
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
def getRefreshToken():
'''public final String getRefreshToken()
'''
pass
def setRefreshToken():
'''public Credential setRefreshToken(final String refreshToken)
'''
pass
def getExpirationTimeMilliseconds():
'''public final Long getExpirationTimeMilliseconds()
'''
pass
def setExpirationTimeMilliseconds():
'''public Credential setExpirationTimeMilliseconds(final Long expirationTimeMilliseconds)
'''
pass
def getExpiresInSeconds():
'''public final Long getExpiresInSeconds()
'''
pass
def setExpiresInSeconds():
'''public Credential setExpiresInSeconds(final Long expiresIn)
'''
pass
def getClientAuthentication():
'''public final HttpExecuteInterceptor getClientAuthentication()
public final HttpExecuteInterceptor getClientAuthentication()
'''
pass
def getRequestInitializer():
'''public final HttpRequestInitializer getRequestInitializer()
public final HttpRequestInitializer getRequestInitializer()
'''
pass
def refreshToken():
'''public final boolean refreshToken()
'''
pass
def setFromTokenResponse():
'''public Credential setFromTokenResponse(final TokenResponse tokenResponse)
'''
pass
def getRefreshListeners():
'''public final Collection<CredentialRefreshListener> getRefreshListeners()
public final Collection<CredentialRefreshListener> getRefreshListeners()
'''
pass
def Builder():
'''public Builder(final AccessMethod method)
'''
pass
def build():
'''public Credential build()
'''
pass
def setTransport():
'''public Builder setTransport(final HttpTransport transport)
'''
pass
def setClock():
'''public Builder setClock(final Clock clock)
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
def setTokenServerEncodedUrl():
'''public Builder setTokenServerEncodedUrl(final String tokenServerEncodedUrl)
'''
pass
def setClientAuthentication():
'''public Builder setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)
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
