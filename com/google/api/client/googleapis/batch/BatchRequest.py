def BatchRequest():
    '''public BatchRequest(final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)
    '''
def setBatchUrl():
    '''public BatchRequest setBatchUrl(final GenericUrl batchUrl)
    '''
def getBatchUrl():
    '''public GenericUrl getBatchUrl()
    '''
def getSleeper():
    '''public Sleeper getSleeper()
    '''
def setSleeper():
    '''public BatchRequest setSleeper(final Sleeper sleeper)
    '''
def queue():
    '''public <T, E> BatchRequest queue(final HttpRequest httpRequest, final Class<T> dataClass, final Class<E> errorClass, final BatchCallback<T, E> callback)
    '''
def size():
    '''public int size()
    '''
def execute():
    '''public void execute()
    '''
def intercept():
    '''public void intercept(final HttpRequest batchRequest)
    '''
