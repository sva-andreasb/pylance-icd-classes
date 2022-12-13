def BatchRequest():
'''public BatchRequest(final HttpTransport transport, final HttpRequestInitializer httpRequestInitializer)
'''
pass
def setBatchUrl():
'''public BatchRequest setBatchUrl(final GenericUrl batchUrl)
'''
pass
def getBatchUrl():
'''public GenericUrl getBatchUrl()
'''
pass
def getSleeper():
'''public Sleeper getSleeper()
'''
pass
def setSleeper():
'''public BatchRequest setSleeper(final Sleeper sleeper)
'''
pass
def queue():
'''public <T, E> BatchRequest queue(final HttpRequest httpRequest, final Class<T> dataClass, final Class<E> errorClass, final BatchCallback<T, E> callback)
'''
pass
def size():
'''public int size()
'''
pass
def execute():
'''public void execute()
'''
pass
def intercept():
'''public void intercept(final HttpRequest batchRequest)
'''
pass
