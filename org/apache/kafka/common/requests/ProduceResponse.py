INVALID_OFFSET = "long  -1L"
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def ProduceResponse():
    '''    public ProduceResponse(final Map<TopicPartition, PartitionResponse> responses)
    public ProduceResponse(final Map<TopicPartition, PartitionResponse> responses, final int throttleTime)
    public ProduceResponse(final Struct struct)
    '''
def responses():
    '''    public Map<TopicPartition, PartitionResponse> responses()
    '''
def getThrottleTime():
    '''    public int getThrottleTime()
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''    public static ProduceResponse parse(final ByteBuffer buffer, final short version)
    '''
def PartitionResponse():
    '''    public PartitionResponse(final Errors error)
    public PartitionResponse(final Errors error, final long baseOffset, final long logAppendTime, final long logStartOffset)
    '''
def toString():
    '''    public String toString()
    '''
