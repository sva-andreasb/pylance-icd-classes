def AbstractHttpClientConnection():
'''public AbstractHttpClientConnection()
'''
pass
def isResponseAvailable():
'''public boolean isResponseAvailable(final int timeout)
'''
pass
def sendRequestHeader():
'''public void sendRequestHeader(final HttpRequest request)
'''
pass
def sendRequestEntity():
'''public void sendRequestEntity(final HttpEntityEnclosingRequest request)
'''
pass
def flush():
'''public void flush()
'''
pass
def receiveResponseHeader():
'''public HttpResponse receiveResponseHeader()
'''
pass
def receiveResponseEntity():
'''public void receiveResponseEntity(final HttpResponse response)
'''
pass
def isStale():
'''public boolean isStale()
'''
pass
def getMetrics():
'''public HttpConnectionMetrics getMetrics()
'''
pass
