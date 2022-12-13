def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def WriteTxnMarkersResponse():
'''public WriteTxnMarkersResponse(final Map<Long, Map<TopicPartition, Errors>> errors)
public WriteTxnMarkersResponse(final Struct struct)
'''
pass
def errors():
'''public Map<TopicPartition, Errors> errors(final long producerId)
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def parse():
'''public static WriteTxnMarkersResponse parse(final ByteBuffer buffer, final short version)
'''
pass
