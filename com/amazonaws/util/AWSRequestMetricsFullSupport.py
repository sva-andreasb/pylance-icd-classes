def AWSRequestMetricsFullSupport():
    '''public AWSRequestMetricsFullSupport()
    '''
def startEvent():
    '''public void startEvent(final String eventName)
    public void startEvent(final MetricType f)
    '''
def endEvent():
    '''public void endEvent(final String eventName)
    public void endEvent(final MetricType f)
    '''
def incrementCounter():
    '''public void incrementCounter(final String event)
    public void incrementCounter(final MetricType f)
    '''
def setCounter():
    '''public void setCounter(final String counterName, final long count)
    public void setCounter(final MetricType f, final long count)
    '''
def addProperty():
    '''public void addProperty(final String propertyName, final Object value)
    public void addProperty(final MetricType f, final Object value)
    '''
def log():
    '''public void log()
    '''
def getProperty():
    '''public List<Object> getProperty(final String propertyName)
    public List<Object> getProperty(final MetricType f)
    '''
def isEnabled():
    '''public final boolean isEnabled()
    '''
