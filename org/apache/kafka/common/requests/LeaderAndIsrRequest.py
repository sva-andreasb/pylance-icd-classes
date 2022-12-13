def schemaVersions():
    '''public static Schema[] schemaVersions()
    '''
def LeaderAndIsrRequest():
    '''public LeaderAndIsrRequest(final Struct struct, final short version)
    '''
def getErrorResponse():
    '''public LeaderAndIsrResponse getErrorResponse(final int throttleTimeMs, final Throwable e)
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
def liveLeaders():
    '''public Set<Node> liveLeaders()
    '''
def parse():
    '''public static LeaderAndIsrRequest parse(final ByteBuffer buffer, final short version)
    '''
def Builder():
    '''public Builder(final short version, final int controllerId, final int controllerEpoch, final Map<TopicPartition, PartitionState> partitionStates, final Set<Node> liveLeaders)
    '''
def build():
    '''public LeaderAndIsrRequest build(final short version)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def PartitionState():
    '''public PartitionState(final int controllerEpoch, final int leader, final int leaderEpoch, final List<Integer> isr, final int zkVersion, final List<Integer> replicas, final boolean isNew)
    '''
