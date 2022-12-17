def ():
    '''returns AWSRequestMetricsFullSupport\n\n
    ()\n
    '''
def startEvent():
    '''returns None\n\n
    startEvent(final String eventName)\n
    startEvent(final MetricType f)\n
    '''
def endEvent():
    '''returns None\n\n
    endEvent(final String eventName)\n
    endEvent(final MetricType f)\n
    '''
def incrementCounter():
    '''returns None\n\n
    incrementCounter(final String event)\n
    incrementCounter(final MetricType f)\n
    '''
def setCounter():
    '''returns None\n\n
    setCounter(final String counterName, final long count)\n
    setCounter(final MetricType f, final long count)\n
    '''
def addProperty():
    '''returns None\n\n
    addProperty(final String propertyName, final Object value)\n
    addProperty(final MetricType f, final Object value)\n
    '''
def log():
    '''returns None\n\n
    log()\n
    '''
def getProperty():
    '''returns List<Object>\n\n
    getProperty(final String propertyName)\n
    getProperty(final MetricType f)\n
    '''
