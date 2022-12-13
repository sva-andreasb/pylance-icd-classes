def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def AddOffsetsToTxnRequest():
    '''public AddOffsetsToTxnRequest(final Struct struct, final short version)
    '''
def transactionalId():
    '''public String transactionalId()
    '''
def producerId():
    '''public long producerId()
    '''
def producerEpoch():
    '''public short producerEpoch()
    '''
def consumerGroupId():
    '''public String consumerGroupId()
    public String consumerGroupId()
    '''
def getErrorResponse():
    '''public AddOffsetsToTxnResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''public static AddOffsetsToTxnRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''public Builder(final String transactionalId, final long producerId, final short producerEpoch, final String consumerGroupId)
    '''
def build():
    '''public AddOffsetsToTxnRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
