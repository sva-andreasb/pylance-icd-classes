INVALID_OFFSET = "long  -1L"
NO_METADATA = "String  \"\""
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def OffsetFetchResponse():
    '''public OffsetFetchResponse(final Errors error, final Map<TopicPartition, PartitionData> responseData)
    public OffsetFetchResponse(final int throttleTimeMs, final Errors error, final Map<TopicPartition, PartitionData> responseData)
    public OffsetFetchResponse(final Struct struct)
    '''
def maybeThrowFirstPartitionError():
    '''public void maybeThrowFirstPartitionError()
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def hasError():
    '''public boolean hasError()
    public boolean hasError()
    '''
def error():
    '''public Errors error()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def responseData():
    '''public Map<TopicPartition, PartitionData> responseData()
    '''
def parse():
    '''public static OffsetFetchResponse parse(final ByteBuffer buffer, final short version)
    '''
def PartitionData():
    '''public PartitionData(final long offset, final String metadata, final Errors error)
    '''
