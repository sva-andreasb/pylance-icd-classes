REQUEST_COUNT = "String  \"http.request-count\""
RESPONSE_COUNT = "String  \"http.response-count\""
SENT_BYTES_COUNT = "String  \"http.sent-bytes-count\""
RECEIVED_BYTES_COUNT = "String  \"http.received-bytes-count\""
def ():
    '''returns HttpConnectionMetricsImpl\n\n
    (final HttpTransportMetrics inTransportMetric, final HttpTransportMetrics outTransportMetric)\n
    '''
def getReceivedBytesCount():
    '''returns long\n\n
    getReceivedBytesCount()\n
    '''
def getSentBytesCount():
    '''returns long\n\n
    getSentBytesCount()\n
    '''
def getRequestCount():
    '''returns long\n\n
    getRequestCount()\n
    '''
def incrementRequestCount():
    '''returns None\n\n
    incrementRequestCount()\n
    '''
def getResponseCount():
    '''returns long\n\n
    getResponseCount()\n
    '''
def incrementResponseCount():
    '''returns None\n\n
    incrementResponseCount()\n
    '''
def getMetric():
    '''returns Object\n\n
    getMetric(final String metricName)\n
    '''
def setMetric():
    '''returns None\n\n
    setMetric(final String metricName, final Object obj)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
