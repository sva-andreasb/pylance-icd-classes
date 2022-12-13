def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def ProduceRequest():
'''public ProduceRequest(final Struct struct, final short version)
'''
pass
def toStruct():
'''public Struct toStruct()
'''
pass
def toString():
'''public String toString(final boolean verbose)
public String toString()
'''
pass
def getErrorResponse():
'''public ProduceResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts(final Throwable e)
'''
pass
def acks():
'''public short acks()
'''
pass
def timeout():
'''public int timeout()
'''
pass
def transactionalId():
'''public String transactionalId()
'''
pass
def isTransactional():
'''public boolean isTransactional()
'''
pass
def isIdempotent():
'''public boolean isIdempotent()
'''
pass
def partitionRecordsOrFail():
'''public Map<TopicPartition, MemoryRecords> partitionRecordsOrFail()
'''
pass
def clearPartitionRecords():
'''public void clearPartitionRecords()
'''
pass
def parse():
'''public static ProduceRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def requiredMagicForVersion():
'''public static byte requiredMagicForVersion(final short produceRequestVersion)
'''
pass
def forCurrentMagic():
'''public static Builder forCurrentMagic(final short acks, final int timeout, final Map<TopicPartition, MemoryRecords> partitionRecords)
'''
pass
def forMagic():
'''public static Builder forMagic(final byte magic, final short acks, final int timeout, final Map<TopicPartition, MemoryRecords> partitionRecords, final String transactionalId)
'''
pass
def build():
'''public ProduceRequest build(final short version)
'''
pass
