def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def AddPartitionsToTxnRequest():
    '''    public AddPartitionsToTxnRequest(final Struct struct, final short version)
    '''
def transactionalId():
    '''    public String transactionalId()
    '''
def producerId():
    '''    public long producerId()
    '''
def producerEpoch():
    '''    public short producerEpoch()
    '''
def partitions():
    '''    public List<TopicPartition> partitions()
    public List<TopicPartition> partitions()
    '''
def getErrorResponse():
    '''    public AddPartitionsToTxnResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''    public static AddPartitionsToTxnRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''    public Builder(final String transactionalId, final long producerId, final short producerEpoch, final List<TopicPartition> partitions)
    '''
def build():
    '''    public AddPartitionsToTxnRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    '''
