def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def AddPartitionsToTxnRequest():
'''public AddPartitionsToTxnRequest(final Struct struct, final short version)
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
def partitions():
'''public List<TopicPartition> partitions()
public List<TopicPartition> partitions()
'''
pass
def getErrorResponse():
'''public AddPartitionsToTxnResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static AddPartitionsToTxnRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final String transactionalId, final long producerId, final short producerEpoch, final List<TopicPartition> partitions)
'''
pass
def build():
'''public AddPartitionsToTxnRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
