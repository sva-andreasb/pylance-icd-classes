def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def OffsetCommitResponse():
'''public OffsetCommitResponse(final Map<TopicPartition, Errors> responseData)
public OffsetCommitResponse(final int throttleTimeMs, final Map<TopicPartition, Errors> responseData)
public OffsetCommitResponse(final Struct struct)
'''
pass
def toStruct():
'''public Struct toStruct(final short version)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def responseData():
'''public Map<TopicPartition, Errors> responseData()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static OffsetCommitResponse parse(final ByteBuffer buffer, final short version)
'''
pass
