def ():
    '''returns Metrics\n\n
    ()\n
    (final Time time)\n
    (final MetricConfig defaultConfig, final Time time)\n
    (final MetricConfig defaultConfig)\n
    (final MetricConfig defaultConfig, final List<MetricsReporter> reporters, final Time time)\n
    (final MetricConfig defaultConfig, final List<MetricsReporter> reporters, final Time time, final boolean enableExpiration)\n
    '''
def newThread():
    '''returns Thread\n\n
    newThread(final Runnable runnable)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def metricName():
    '''returns MetricName\n\n
    metricName(final String name, final String group, final String description, final Map<String, String> tags)\n
    metricName(final String name, final String group, final String description)\n
    metricName(final String name, final String group)\n
    metricName(final String name, final String group, final String description, final String... keyValue)\n
    metricName(final String name, final String group, final Map<String, String> tags)\n
    '''
def config():
    '''returns MetricConfig\n\n
    config()\n
    '''
def getSensor():
    '''returns Sensor\n\n
    getSensor(final String name)\n
    '''
def sensor():
    '''returns Sensor\n\n
    sensor(final String name)\n
    sensor(final String name, final Sensor.RecordingLevel recordingLevel)\n
    sensor(final String name, final Sensor... parents)\n
    sensor(final String name, final Sensor.RecordingLevel recordingLevel, final Sensor... parents)\n
    '''
def removeSensor():
    '''returns None\n\n
    removeSensor(final String name)\n
    '''
def addMetric():
    '''returns None\n\n
    addMetric(final MetricName metricName, final Measurable measurable)\n
    addMetric(final MetricName metricName, final MetricConfig config, final Measurable measurable)\n
    addMetric(final MetricName metricName, final MetricConfig config, final MetricValueProvider<?> metricValueProvider)\n
    addMetric(final MetricName metricName, final MetricValueProvider<?> metricValueProvider)\n
    '''
def reporters():
    '''returns List<MetricsReporter>\n\n
    reporters()\n
    '''
def metric():
    '''returns KafkaMetric\n\n
    metric(final MetricName metricName)\n
    '''
def metricInstance():
    '''returns MetricName\n\n
    metricInstance(final MetricNameTemplate template, final String... keyValue)\n
    metricInstance(final MetricNameTemplate template, final Map<String, String> tags)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
