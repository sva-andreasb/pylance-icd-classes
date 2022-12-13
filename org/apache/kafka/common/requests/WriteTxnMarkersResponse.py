def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def WriteTxnMarkersResponse():
    '''public WriteTxnMarkersResponse(final Map<Long, Map<TopicPartition, Errors>> errors)
    public WriteTxnMarkersResponse(final Struct struct)
    '''
def errors():
    '''public Map<TopicPartition, Errors> errors(final long producerId)
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''public static WriteTxnMarkersResponse parse(final ByteBuffer buffer, final short version)
    '''
