INVALID_OFFSET = "long  -1L"
NO_METADATA = "String  "
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def OffsetFetchResponse():
'''public OffsetFetchResponse(final Errors error, final Map<TopicPartition, PartitionData> responseData)
public OffsetFetchResponse(final int throttleTimeMs, final Errors error, final Map<TopicPartition, PartitionData> responseData)
public OffsetFetchResponse(final Struct struct)
'''
pass
def maybeThrowFirstPartitionError():
'''public void maybeThrowFirstPartitionError()
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def hasError():
'''public boolean hasError()
public boolean hasError()
'''
pass
def error():
'''public Errors error()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def responseData():
'''public Map<TopicPartition, PartitionData> responseData()
'''
pass
def parse():
'''public static OffsetFetchResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def PartitionData():
'''public PartitionData(final long offset, final String metadata, final Errors error)
'''
pass
