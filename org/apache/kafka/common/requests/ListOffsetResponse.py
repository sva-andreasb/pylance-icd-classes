UNKNOWN_TIMESTAMP = "long  -1L"
UNKNOWN_OFFSET = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def ListOffsetResponse():
'''public ListOffsetResponse(final Map<TopicPartition, PartitionData> responseData)
public ListOffsetResponse(final int throttleTimeMs, final Map<TopicPartition, PartitionData> responseData)
public ListOffsetResponse(final Struct struct)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def responseData():
'''public Map<TopicPartition, PartitionData> responseData()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static ListOffsetResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def PartitionData():
'''public PartitionData(final Errors error, final List<Long> offsets)
public PartitionData(final Errors error, final long timestamp, final long offset)
'''
pass
