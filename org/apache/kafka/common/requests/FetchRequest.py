CONSUMER_REPLICA_ID = "int  -1"
DEFAULT_RESPONSE_MAX_BYTES = "int  Integer.MAX_VALUE"
INVALID_LOG_START_OFFSET = "long  -1L"
def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final long fetchOffset, final long logStartOffset, final int maxBytes)\n
    (final String topic)\n
    (final short minVersion, final short maxVersion, final int replicaId, final int maxWait, final int minBytes, final Map<TopicPartition, PartitionData> fetchData)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def replicaId():
    '''returns int\n\n
    replicaId()\n
    '''
def maxWait():
    '''returns int\n\n
    maxWait()\n
    '''
def minBytes():
    '''returns int\n\n
    minBytes()\n
    '''
def maxBytes():
    '''returns int\n\n
    maxBytes()\n
    '''
def toForget():
    '''returns Builder\n\n
    toForget()\n
    toForget()\n
    toForget(final List<TopicPartition> toForget)\n
    '''
def isFromFollower():
    '''returns boolean\n\n
    isFromFollower()\n
    '''
def isolationLevel():
    '''returns Builder\n\n
    isolationLevel()\n
    isolationLevel(final IsolationLevel isolationLevel)\n
    '''
def metadata():
    '''returns Builder\n\n
    metadata()\n
    metadata(final FetchMetadata metadata)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def setMaxBytes():
    '''returns Builder\n\n
    setMaxBytes(final int maxBytes)\n
    '''
def build():
    '''returns FetchRequest\n\n
    build(final short version)\n
    '''
