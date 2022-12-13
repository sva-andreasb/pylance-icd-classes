def schemaVersions():
'''public static Schema[] schemaVersions()
'''
pass
def UpdateMetadataRequest():
'''public UpdateMetadataRequest(final Struct struct, final short versionId)
'''
pass
def getErrorResponse():
'''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
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
def liveBrokers():
'''public Set<Broker> liveBrokers()
'''
pass
def parse():
'''public static UpdateMetadataRequest parse(final ByteBuffer buffer, final short version)
'''
pass
def Builder():
'''public Builder(final short version, final int controllerId, final int controllerEpoch, final Map<TopicPartition, PartitionState> partitionStates, final Set<Broker> liveBrokers)
'''
pass
def build():
'''public UpdateMetadataRequest build(final short version)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
public String toString()
'''
pass
def PartitionState():
'''public PartitionState(final int controllerEpoch, final int leader, final int leaderEpoch, final List<Integer> isr, final int zkVersion, final List<Integer> replicas, final List<Integer> offlineReplicas)
'''
pass
def Broker():
'''public Broker(final int id, final List<EndPoint> endPoints, final String rack)
'''
pass
def EndPoint():
'''public EndPoint(final String host, final int port, final SecurityProtocol securityProtocol, final ListenerName listenerName)
'''
pass
