def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def TxnOffsetCommitRequest():
    '''    public TxnOffsetCommitRequest(final short version, final String transactionalId, final String consumerGroupId, final long producerId, final short producerEpoch, final Map<TopicPartition, CommittedOffset> offsets)
    public TxnOffsetCommitRequest(final Struct struct, final short version)
    '''
def transactionalId():
    '''    public String transactionalId()
    '''
def consumerGroupId():
    '''    public String consumerGroupId()
    public String consumerGroupId()
    '''
def producerId():
    '''    public long producerId()
    '''
def producerEpoch():
    '''    public short producerEpoch()
    '''
def offsets():
    '''    public Map<TopicPartition, CommittedOffset> offsets()
    public Map<TopicPartition, CommittedOffset> offsets()
    '''
def getErrorResponse():
    '''    public TxnOffsetCommitResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''    public static TxnOffsetCommitRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''    public Builder(final String transactionalId, final String consumerGroupId, final long producerId, final short producerEpoch, final Map<TopicPartition, CommittedOffset> offsets)
    '''
def build():
    '''    public TxnOffsetCommitRequest build(final short version)
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def CommittedOffset():
    '''    public CommittedOffset(final long offset, final String metadata)
    '''
def offset():
    '''    public long offset()
    '''
def metadata():
    '''    public String metadata()
    '''
