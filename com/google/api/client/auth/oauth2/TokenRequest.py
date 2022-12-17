def ():
    '''returns TokenRequest\n\n
    (final HttpTransport transport, final JsonFactory jsonFactory, final GenericUrl tokenServerUrl, final String grantType)\n
    '''
def setRequestInitializer():
    '''returns TokenRequest\n\n
    setRequestInitializer(final HttpRequestInitializer requestInitializer)\n
    '''
def setClientAuthentication():
    '''returns TokenRequest\n\n
    setClientAuthentication(final HttpExecuteInterceptor clientAuthentication)\n
    '''
def setTokenServerUrl():
    '''returns TokenRequest\n\n
    setTokenServerUrl(final GenericUrl tokenServerUrl)\n
    '''
def setScopes():
    '''returns TokenRequest\n\n
    setScopes(final Collection<String> scopes)\n
    '''
def setGrantType():
    '''returns TokenRequest\n\n
    setGrantType(final String grantType)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final HttpRequest request)\n
    '''
def intercept():
    '''returns None\n\n
    intercept(final HttpRequest request)\n
    '''
def execute():
    '''returns TokenResponse\n\n
    execute()\n
    '''
def set():
    '''returns TokenRequest\n\n
    set(final String fieldName, final Object value)\n
    '''
