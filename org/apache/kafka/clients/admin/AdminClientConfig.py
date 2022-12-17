BOOTSTRAP_SERVERS_CONFIG = "String  \"bootstrap.servers\""
RECONNECT_BACKOFF_MS_CONFIG = "String  \"reconnect.backoff.ms\""
RECONNECT_BACKOFF_MAX_MS_CONFIG = "String  \"reconnect.backoff.max.ms\""
RETRY_BACKOFF_MS_CONFIG = "String  \"retry.backoff.ms\""
CONNECTIONS_MAX_IDLE_MS_CONFIG = "String  \"connections.max.idle.ms\""
REQUEST_TIMEOUT_MS_CONFIG = "String  \"request.timeout.ms\""
CLIENT_ID_CONFIG = "String  \"client.id\""
METADATA_MAX_AGE_CONFIG = "String  \"metadata.max.age.ms\""
SEND_BUFFER_CONFIG = "String  \"send.buffer.bytes\""
RECEIVE_BUFFER_CONFIG = "String  \"receive.buffer.bytes\""
METRIC_REPORTER_CLASSES_CONFIG = "String  \"metric.reporters\""
METRICS_NUM_SAMPLES_CONFIG = "String  \"metrics.num.samples\""
METRICS_SAMPLE_WINDOW_MS_CONFIG = "String  \"metrics.sample.window.ms\""
METRICS_RECORDING_LEVEL_CONFIG = "String  \"metrics.recording.level\""
SECURITY_PROTOCOL_CONFIG = "String  \"security.protocol\""
DEFAULT_SECURITY_PROTOCOL = "String  \"PLAINTEXT\""
RETRIES_CONFIG = "String  \"retries\""
def ():
    '''returns AdminClientConfig\n\n
    (final Map<?, ?> props)\n
    '''
