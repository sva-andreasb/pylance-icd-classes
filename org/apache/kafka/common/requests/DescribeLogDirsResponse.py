INVALID_OFFSET_LAG = "long  -1L"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def DescribeLogDirsResponse():
'''public DescribeLogDirsResponse(final Struct struct)
public DescribeLogDirsResponse(final int throttleTimeMs, final Map<String, LogDirInfo> logDirInfos)
'''
pass
def throttleTimeMs():
'''public int throttleTimeMs()
'''
pass
def errorCounts():
'''public Map<Errors, Integer> errorCounts()
'''
pass
def logDirInfos():
'''public Map<String, LogDirInfo> logDirInfos()
'''
pass
def parse():
'''public static DescribeLogDirsResponse parse(final ByteBuffer buffer, final short version)
'''
pass
def LogDirInfo():
'''public LogDirInfo(final Errors error, final Map<TopicPartition, ReplicaInfo> replicaInfos)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def ReplicaInfo():
'''public ReplicaInfo(final long size, final long offsetLag, final boolean isFuture)
'''
pass
