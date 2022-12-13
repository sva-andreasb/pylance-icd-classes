def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def UpdateMetadataRequest():
    '''public UpdateMetadataRequest(final Struct struct, final short versionId)
    '''
def getErrorResponse():
    '''public AbstractResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
    '''
def controllerId():
    '''public int controllerId()
    '''
def controllerEpoch():
    '''public int controllerEpoch()
    '''
def partitionStates():
    '''public Map<TopicPartition, PartitionState> partitionStates()
    '''
def liveBrokers():
    '''public Set<Broker> liveBrokers()
    '''
def parse():
    '''public static UpdateMetadataRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''public Builder(final short version, final int controllerId, final int controllerEpoch, final Map<TopicPartition, PartitionState> partitionStates, final Set<Broker> liveBrokers)
    '''
def build():
    '''public UpdateMetadataRequest build(final short version)
    '''
def toString():
    '''public String toString()
    public String toString()
    public String toString()
    public String toString()
    '''
def PartitionState():
    '''public PartitionState(final int controllerEpoch, final int leader, final int leaderEpoch, final List<Integer> isr, final int zkVersion, final List<Integer> replicas, final List<Integer> offlineReplicas)
    '''
def Broker():
    '''public Broker(final int id, final List<EndPoint> endPoints, final String rack)
    '''
def EndPoint():
    '''public EndPoint(final String host, final int port, final SecurityProtocol securityProtocol, final ListenerName listenerName)
    '''
