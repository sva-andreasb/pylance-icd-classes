HIGH_WATERMARK = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DeleteRecordsRequest():
'''public DeleteRecordsRequest(final Struct struct, final short version)
public DeleteRecordsRequest(final int timeout, final Map<TopicPartition, Long> partitionOffsets, final short version)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def timeout():
'''public int timeout()
'''
pass
def partitionOffsets():
'''public Map<TopicPartition, Long> partitionOffsets()
'''
pass
def parse():
'''public static DeleteRecordsRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final int timeout, final Map<TopicPartition, Long> partitionOffsets)
'''
pass
def build():
'''public DeleteRecordsRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
