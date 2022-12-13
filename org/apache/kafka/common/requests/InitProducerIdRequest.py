NO_TRANSACTION_TIMEOUT_MS = "int  Integer.MAX_VALUE"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def InitProducerIdRequest():
'''public InitProducerIdRequest(final Struct struct, final short version)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static InitProducerIdRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def transactionalId():
'''public String transactionalId()
'''
pass
def transactionTimeoutMs():
'''public int transactionTimeoutMs()
'''
pass
def Builder():
'''public Builder(final String transactionalId)
public Builder(final String transactionalId, final int transactionTimeoutMs)
'''
pass
def build():
'''public InitProducerIdRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
