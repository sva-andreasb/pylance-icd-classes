NO_TRANSACTION_TIMEOUT_MS = "int  Integer.MAX_VALUE"
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def InitProducerIdRequest():
    '''public InitProducerIdRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def parse():
    '''public static InitProducerIdRequest parse(final ByteBuffer buffer, final short version)
    '''
def transactionalId():
    '''public String transactionalId()
    '''
def transactionTimeoutMs():
    '''public int transactionTimeoutMs()
    '''
def Builder():
    '''public Builder(final String transactionalId)
    public Builder(final String transactionalId, final int transactionTimeoutMs)
    '''
def build():
    '''public InitProducerIdRequest build(final short version)
    '''
def toString():
    '''public String toString()
    '''
