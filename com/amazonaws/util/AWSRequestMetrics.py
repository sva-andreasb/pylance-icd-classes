def AWSRequestMetrics():
'''public AWSRequestMetrics()
'''
pass
def getTimingInfo():
'''public final TimingInfo getTimingInfo()
'''
pass
def isEnabled():
'''public boolean isEnabled()
'''
pass
def startEvent():
'''public void startEvent(final String eventName)
public void startEvent(final MetricType f)
'''
pass
def endEvent():
'''public void endEvent(final String eventName)
public void endEvent(final MetricType f)
'''
pass
def incrementCounter():
'''public void incrementCounter(final String event)
public void incrementCounter(final MetricType f)
'''
pass
def incrementCounterWith():
'''public final AWSRequestMetrics incrementCounterWith(final String event)
public final AWSRequestMetrics incrementCounterWith(final MetricType f)
'''
pass
def setCounter():
'''public void setCounter(final String counterName, final long count)
public void setCounter(final MetricType f, final long count)
'''
pass
def withCounter():
'''public final AWSRequestMetrics withCounter(final String counterName, final long count)
public final AWSRequestMetrics withCounter(final MetricType f, final long count)
'''
pass
def addProperty():
'''public void addProperty(final String propertyName, final Object value)
public void addProperty(final MetricType f, final Object value)
'''
pass
def addPropertyWith():
'''public final AWSRequestMetrics addPropertyWith(final String propertyName, final Object value)
public final AWSRequestMetrics addPropertyWith(final MetricType f, final Object value)
'''
pass
def log():
'''public void log()
'''
pass
def getProperty():
'''public List<Object> getProperty(final String propertyName)
public List<Object> getProperty(final MetricType f)
'''
pass
