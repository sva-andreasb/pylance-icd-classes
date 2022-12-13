INVALID_OFFSET_LAG = "long  -1L"
def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def DescribeLogDirsResponse():
    '''public DescribeLogDirsResponse(final Struct struct)
    public DescribeLogDirsResponse(final int throttleTimeMs, final Map<String, LogDirInfo> logDirInfos)
    '''
def throttleTimeMs():
    '''public int throttleTimeMs()
    '''
def errorCounts():
    '''public Map<Errors, Integer> errorCounts()
    '''
def logDirInfos():
    '''public Map<String, LogDirInfo> logDirInfos()
    '''
def parse():
    '''public static DescribeLogDirsResponse parse(final ByteBuffer buffer, final short version)
    '''
def LogDirInfo():
    '''public LogDirInfo(final Errors error, final Map<TopicPartition, ReplicaInfo> replicaInfos)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def ReplicaInfo():
    '''public ReplicaInfo(final long size, final long offsetLag, final boolean isFuture)
    '''
