HIGH_WATERMARK = "long  -1L"
def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def DeleteRecordsRequest():
    '''    public DeleteRecordsRequest(final Struct struct, final short version)
    public DeleteRecordsRequest(final int timeout, final Map<TopicPartition, Long> partitionOffsets, final short version)
    '''
def getErrorResponse():
    '''    public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def timeout():
    '''    public int timeout()
    '''
def partitionOffsets():
    '''    public Map<TopicPartition, Long> partitionOffsets()
    '''
def parse():
    '''    public static DeleteRecordsRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''    public Builder(final int timeout, final Map<TopicPartition, Long> partitionOffsets)
    '''
def build():
    '''    public DeleteRecordsRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    '''
