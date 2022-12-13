def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def EndTxnRequest():
'''public EndTxnRequest(final Struct struct, final short version)
'''
pass
def transactionalId():
'''public String transactionalId()
'''
pass
def producerId():
'''public long producerId()
'''
pass
def producerEpoch():
'''public short producerEpoch()
'''
pass
def command():
'''public TransactionResult command()
'''
pass
def getErrorResponse():
'''public EndTxnResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static EndTxnRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final String transactionalId, final long producerId, final short producerEpoch, final TransactionResult result)
'''
pass
def result():
'''public TransactionResult result()
'''
pass
def build():
'''public EndTxnRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
