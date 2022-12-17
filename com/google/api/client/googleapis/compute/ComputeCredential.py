def ():
    '''returns Builder\n\n
    (final HttpTransport transport, final JsonFactory jsonFactory)\n
    (final HttpTransport transport, final JsonFactory jsonFactory)\n
    '''
def build():
    '''returns ComputeCredential\n\n
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
