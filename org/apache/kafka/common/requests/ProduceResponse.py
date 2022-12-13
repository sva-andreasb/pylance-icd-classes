INVALID_OFFSET = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def ProduceResponse():
'''public ProduceResponse(final Map<TopicPartition, PartitionResponse> responses)
public ProduceResponse(final Map<TopicPartition, PartitionResponse> responses, final int throttleTime)
public ProduceResponse(final Struct struct)
'''
pass
def responses():
'''public Map<TopicPartition, PartitionResponse> responses()
'''
pass
def getThrottleTime():
'''public int getThrottleTime()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static ProduceResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def PartitionResponse():
'''public PartitionResponse(final Errors error)
public PartitionResponse(final Errors error, final long baseOffset, final long logAppendTime, final long logStartOffset)
'''
pass
def toString():
'''public String toString()
'''
pass
