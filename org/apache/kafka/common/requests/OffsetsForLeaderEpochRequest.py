def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def epochsByTopicPartition():
'''public Map<TopicPartition, Integer> epochsByTopicPartition()
'''
pass
def OffsetsForLeaderEpochRequest():
'''public OffsetsForLeaderEpochRequest(final Map<TopicPartition, Integer> epochsByPartition, final short version)
public OffsetsForLeaderEpochRequest(final Struct struct, final short version)
'''
pass
def parse():
'''public static OffsetsForLeaderEpochRequest parse(final ByteBuffer buffer, final short versionId)
public static OffsetsForLeaderEpochRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def Builder():
'''public Builder()
public Builder(final Map<TopicPartition, Integer> epochsByPartition)
'''
pass
def add():
'''public Builder add(final TopicPartition topicPartition, final Integer epoch)
'''
pass
def build():
'''public OffsetsForLeaderEpochRequest build(final short version)
'''
pass
def toString():
'''public String toString()
'''
pass
