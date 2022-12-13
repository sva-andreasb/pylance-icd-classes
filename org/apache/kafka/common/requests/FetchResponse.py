INVALID_HIGHWATERMARK = "long  -1L"
INVALID_LAST_STABLE_OFFSET = "long  -1L"
INVALID_LOG_START_OFFSET = "long  -1L"
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def FetchResponse():
    '''public FetchResponse(final Errors error, final LinkedHashMap<TopicPartition, PartitionData> responseData, final int throttleTimeMs, final int sessionId)
    public FetchResponse(final Struct struct)
    '''
def toStruct():
    '''public Struct toStruct(final short version)
    '''
def error():
    '''public Errors error()
    '''
def responseData():
    '''public LinkedHashMap<TopicPartition, PartitionData> responseData()
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def sessionId():
    '''public int sessionId()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''public static FetchResponse parse(final ByteBuffer buffer, final short version)
    '''
def sizeOf():
    '''public static int sizeOf(final short version, final Iterator<Map.Entry<TopicPartition, PartitionData>> partIterator)
    '''
def AbortedTransaction():
    '''public AbortedTransaction(final long producerId, final long firstOffset)
    '''
def equals():
    '''public boolean equals(final Object o)
    public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    public int hashCode()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def PartitionData():
    '''public PartitionData(final Errors error, final long highWatermark, final long lastStableOffset, final long logStartOffset, final List<AbortedTransaction> abortedTransactions, final Records records)
    '''
