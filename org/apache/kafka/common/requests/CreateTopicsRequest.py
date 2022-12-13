NO_NUM_PARTITIONS = "int  -1"
NO_REPLICATION_FACTOR = "short  -1"
def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def CreateTopicsRequest():
'''public CreateTopicsRequest(final Struct struct, final short version)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def topics():
'''public Map<String, TopicDetails> topics()
'''
pass
def timeout():
'''public int timeout()
'''
pass
def validateOnly():
'''public boolean validateOnly()
'''
pass
def duplicateTopics():
'''public Set<String> duplicateTopics()
'''
pass
def parse():
'''public static CreateTopicsRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def toStruct():
'''public Struct toStruct()
'''
pass
def TopicDetails():
'''public TopicDetails(final int partitions, final short replicationFactor, final Map<String, String> configs)
public TopicDetails(final int partitions, final short replicationFactor)
public TopicDetails(final Map<Integer, List<Integer>> replicasAssignments, final Map<String, String> configs)
public TopicDetails(final Map<Integer, List<Integer>> replicasAssignments)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def Builder():
'''public Builder(final Map<String, TopicDetails> topics, final int timeout)
public Builder(final Map<String, TopicDetails> topics, final int timeout, final boolean validateOnly)
'''
pass
def build():
'''public CreateTopicsRequest build(final short version)
'''
pass
