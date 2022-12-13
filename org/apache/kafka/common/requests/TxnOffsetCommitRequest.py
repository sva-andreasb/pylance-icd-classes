def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def TxnOffsetCommitRequest():
'''public TxnOffsetCommitRequest(final short version, final String transactionalId, final String consumerGroupId, final long producerId, final short producerEpoch, final Map<TopicPartition, CommittedOffset> offsets)
public TxnOffsetCommitRequest(final Struct struct, final short version)
'''
pass
def transactionalId():
'''public String transactionalId()
'''
pass
def consumerGroupId():
'''public String consumerGroupId()
public String consumerGroupId()
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
def offsets():
'''public Map<TopicPartition, CommittedOffset> offsets()
public Map<TopicPartition, CommittedOffset> offsets()
'''
pass
def getErrorResponse():
'''public TxnOffsetCommitResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def parse():
'''public static TxnOffsetCommitRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final String transactionalId, final String consumerGroupId, final long producerId, final short producerEpoch, final Map<TopicPartition, CommittedOffset> offsets)
'''
pass
def build():
'''public TxnOffsetCommitRequest build(final short version)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def CommittedOffset():
'''public CommittedOffset(final long offset, final String metadata)
'''
pass
def offset():
'''public long offset()
'''
pass
def metadata():
'''public String metadata()
'''
pass
