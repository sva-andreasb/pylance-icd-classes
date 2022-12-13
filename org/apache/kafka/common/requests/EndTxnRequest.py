def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def EndTxnRequest():
    '''public EndTxnRequest(final Struct struct, final short version)
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
def command():
    '''public TransactionResult command()
    '''
def getErrorResponse():
    '''public EndTxnResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''public static EndTxnRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''public Builder(final String transactionalId, final long producerId, final short producerEpoch, final TransactionResult result)
    '''
def result():
    '''public TransactionResult result()
    '''
def build():
    '''public EndTxnRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
