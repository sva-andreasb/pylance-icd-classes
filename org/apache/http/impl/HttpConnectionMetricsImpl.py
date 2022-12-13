REQUEST_COUNT = "String  \"http.request-count\""
RESPONSE_COUNT = "String  \"http.response-count\""
SENT_BYTES_COUNT = "String  \"http.sent-bytes-count\""
RECEIVED_BYTES_COUNT = "String  \"http.received-bytes-count\""
def HttpConnectionMetricsImpl():
    '''public HttpConnectionMetricsImpl(final HttpTransportMetrics inTransportMetric, final HttpTransportMetrics outTransportMetric)
    '''
def getReceivedBytesCount():
    '''public long getReceivedBytesCount()
    '''
def getSentBytesCount():
    '''public long getSentBytesCount()
    '''
def getRequestCount():
    '''public long getRequestCount()
    '''
def incrementRequestCount():
    '''public void incrementRequestCount()
    '''
def getResponseCount():
    '''public long getResponseCount()
    '''
def incrementResponseCount():
    '''public void incrementResponseCount()
    '''
def getMetric():
    '''public Object getMetric(final String metricName)
    '''
def setMetric():
    '''public void setMetric(final String metricName, final Object obj)
    '''
def reset():
    '''public void reset()
    '''
