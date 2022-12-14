OBSERVED_OBJECT_ERROR = "String  \"jmx.monitor.error.mbean\""
OBSERVED_ATTRIBUTE_ERROR = "String  \"jmx.monitor.error.attribute\""
OBSERVED_ATTRIBUTE_TYPE_ERROR = "String  \"jmx.monitor.error.type\""
THRESHOLD_ERROR = "String  \"jmx.monitor.error.threshold\""
RUNTIME_ERROR = "String  \"jmx.monitor.error.runtime\""
THRESHOLD_VALUE_EXCEEDED = "String  \"jmx.monitor.counter.threshold\""
THRESHOLD_HIGH_VALUE_EXCEEDED = "String  \"jmx.monitor.gauge.high\""
THRESHOLD_LOW_VALUE_EXCEEDED = "String  \"jmx.monitor.gauge.low\""
STRING_TO_COMPARE_VALUE_MATCHED = "String  \"jmx.monitor.string.matches\""
STRING_TO_COMPARE_VALUE_DIFFERED = "String  \"jmx.monitor.string.differs\""
def getDerivedGauge():
    '''returns Object\n\n
    getDerivedGauge()\n
    '''
def getTrigger():
    '''returns Object\n\n
    getTrigger()\n
    '''
def getObservedAttribute():
    '''returns String\n\n
    getObservedAttribute()\n
    '''
def getObservedObject():
    '''returns ObjectName\n\n
    getObservedObject()\n
    '''
