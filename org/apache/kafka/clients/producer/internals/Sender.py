def ():
    '''returns SenderMetrics\n\n
    (final LogContext logContext, final KafkaClient client, final Metadata metadata, final RecordAccumulator accumulator, final boolean guaranteeMessageOrder, final int maxRequestSize, final short acks, final int retries, final SenderMetricsRegistry metricsRegistry, final Time time, final int requestTimeout, final long retryBackoffMs, final TransactionManager transactionManager, final ApiVersions apiVersions)\n
    (final SenderMetricsRegistry metrics)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def initiateClose():
    '''returns None\n\n
    initiateClose()\n
    '''
def forceClose():
    '''returns None\n\n
    forceClose()\n
    '''
def onComplete():
    '''returns None\n\n
    onComplete(final ClientResponse response)\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    measure(final MetricConfig config, final long now)\n
    '''
def updateProduceRequestMetrics():
    '''returns None\n\n
    updateProduceRequestMetrics(final Map<Integer, List<ProducerBatch>> batches)\n
    '''
def recordRetries():
    '''returns None\n\n
    recordRetries(final String topic, final int count)\n
    '''
def recordErrors():
    '''returns None\n\n
    recordErrors(final String topic, final int count)\n
    '''
def recordLatency():
    '''returns None\n\n
    recordLatency(final String node, final long latency)\n
    '''
