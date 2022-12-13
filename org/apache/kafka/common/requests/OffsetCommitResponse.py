def schemaVersions():
    '''    public static Schema[] schemaVersions()
    '''
def OffsetCommitResponse():
    '''    public OffsetCommitResponse(final Map<TopicPartition, Errors> responseData)
    public OffsetCommitResponse(final int throttleTimeMs, final Map<TopicPartition, Errors> responseData)
    public OffsetCommitResponse(final Struct struct)
    '''
def toStruct():
    '''    public Struct toStruct(final short version)
    '''
def throttleTimeMs():
    '''    public int throttleTimeMs()
    '''
def responseData():
    '''    public Map<TopicPartition, Errors> responseData()
    '''
def errorCounts():
    '''    public Map<Errors, Integer> errorCounts()
    '''
def parse():
    '''    public static OffsetCommitResponse parse(final ByteBuffer buffer, final short version)
    '''
