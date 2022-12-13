INVALID_LOW_WATERMARK = "long  -1L"
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def DeleteRecordsResponse():
    '''    public DeleteRecordsResponse(final Struct struct)
    public DeleteRecordsResponse(final int throttleTimeMs, final Map<TopicPartition, PartitionResponse> responses)
    '''
def throttleTimeMs():
    '''    public int throttleTimeMs()
    '''
def responses():
    '''    public Map<TopicPartition, PartitionResponse> responses()
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''    public static DeleteRecordsResponse parse(final ByteBuffer buffer, final short version)
    '''
def PartitionResponse():
    '''    public PartitionResponse(final long lowWatermark, final Errors error)
    '''
def toString():
    '''    public String toString()
    '''
