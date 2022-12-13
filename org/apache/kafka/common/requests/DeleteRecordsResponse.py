INVALID_LOW_WATERMARK = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DeleteRecordsResponse():
'''public DeleteRecordsResponse(final Struct struct)
public DeleteRecordsResponse(final int throttleTimeMs, final Map<TopicPartition, PartitionResponse> responses)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def responses():
'''public Map<TopicPartition, PartitionResponse> responses()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static DeleteRecordsResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def PartitionResponse():
'''public PartitionResponse(final long lowWatermark, final Errors error)
'''
pass
def toString():
'''public String toString()
'''
pass
