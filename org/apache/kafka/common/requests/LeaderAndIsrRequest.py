def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def LeaderAndIsrRequest():
'''public LeaderAndIsrRequest(final Struct struct, final short version)
'''
pass
def getErrorResponse():
'''public LeaderAndIsrResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
'''
pass
def controllerId():
'''public int controllerId()
'''
pass
def controllerEpoch():
'''public int controllerEpoch()
'''
pass
def partitionStates():
'''public Map<TopicPartition, PartitionState> partitionStates()
'''
pass
def liveLeaders():
'''public Set<Node> liveLeaders()
'''
pass
def parse():
'''public static LeaderAndIsrRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final short version, final int controllerId, final int controllerEpoch, final Map<TopicPartition, PartitionState> partitionStates, final Set<Node> liveLeaders)
'''
pass
def build():
'''public LeaderAndIsrRequest build(final short version)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def PartitionState():
'''public PartitionState(final int controllerEpoch, final int leader, final int leaderEpoch, final List<Integer> isr, final int zkVersion, final List<Integer> replicas, final boolean isNew)
'''
pass
