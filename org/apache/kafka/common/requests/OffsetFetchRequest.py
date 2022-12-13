def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def forAllPartitions():
'''public static OffsetFetchRequest forAllPartitions(final String groupId)
'''
pass
def OffsetFetchRequest():
'''public OffsetFetchRequest(final Struct struct, final short version)
'''
pass
def getErrorResponse():
'''public OffsetFetchResponse getErrorResponse(final Errors error)
public OffsetFetchResponse getErrorResponse(final int throttleTimeMs, final Errors error)
public OffsetFetchResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def groupId():
'''public String groupId()
'''
pass
def partitions():
'''public List<TopicPartition> partitions()
'''
pass
def parse():
'''public static OffsetFetchRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def isAllPartitions():
'''public boolean isAllPartitions()
'''
pass
def Builder():
'''public Builder(final String groupId, final List<TopicPartition> partitions)
'''
pass
def allTopicPartitions():
'''public static Builder allTopicPartitions(final String groupId)
'''
pass
def isAllTopicPartitions():
'''public boolean isAllTopicPartitions()
'''
pass
def build():
'''public OffsetFetchRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
