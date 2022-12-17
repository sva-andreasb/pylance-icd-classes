def ():
    '''returns SenderMetricsRegistry\n\n
    (final Metrics metrics)\n
    '''
def topicRecordSendRate():
    '''returns MetricName\n\n
    topicRecordSendRate(final Map<String, String> tags)\n
    '''
def topicRecordSendTotal():
    '''returns MetricName\n\n
    topicRecordSendTotal(final Map<String, String> tags)\n
    '''
def topicByteRate():
    '''returns MetricName\n\n
    topicByteRate(final Map<String, String> tags)\n
    '''
def topicByteTotal():
    '''returns MetricName\n\n
    topicByteTotal(final Map<String, String> tags)\n
    '''
def topicCompressionRate():
    '''returns MetricName\n\n
    topicCompressionRate(final Map<String, String> tags)\n
    '''
def topicRecordRetryRate():
    '''returns MetricName\n\n
    topicRecordRetryRate(final Map<String, String> tags)\n
    '''
def topicRecordRetryTotal():
    '''returns MetricName\n\n
    topicRecordRetryTotal(final Map<String, String> tags)\n
    '''
def topicRecordErrorRate():
    '''returns MetricName\n\n
    topicRecordErrorRate(final Map<String, String> tags)\n
    '''
def topicRecordErrorTotal():
    '''returns MetricName\n\n
    topicRecordErrorTotal(final Map<String, String> tags)\n
    '''
def allTemplates():
    '''returns List<MetricNameTemplate>\n\n
    allTemplates()\n
    '''
def sensor():
    '''returns Sensor\n\n
    sensor(final String name)\n
    '''
def addMetric():
    '''returns None\n\n
    addMetric(final MetricName m, final Measurable measurable)\n
    '''
def getSensor():
    '''returns Sensor\n\n
    getSensor(final String name)\n
    '''
