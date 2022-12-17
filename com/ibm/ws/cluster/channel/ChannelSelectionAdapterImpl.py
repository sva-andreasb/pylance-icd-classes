def ():
    '''returns ChannelSelectionAdapterImpl\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Object config)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def select():
    '''returns ChannelTarget\n\n
    select(final Identity clusterIdentity, final CFEndPointCriteria criteria)\n
    select(final ChannelSelectionCriteria selectCriteria)\n
    select(final Identity clusterIdentity, final ChannelSelectionCriteria selectCriteria)\n
    '''
def getCriteria():
    '''returns ChannelSelectionCriteria\n\n
    getCriteria(final Identity clusterIdentity, Map context, final CFEndPointCriteria cfCriteria)\n
    getCriteria(final Identity clusterIdentity, final Map context, final String chainName, final Class channelAccessor, final Class[] optionalChannelFactories, final boolean sslRequired)\n
    '''
def getChannelTargetFromIdentity():
    '''returns ChannelTarget\n\n
    getChannelTargetFromIdentity(final Identity clusterIdentity, final ClusterMemberDescription clusterMemberDescription, final ChannelSelectionCriteria selectCriteria)\n
    '''
def callback():
    '''returns None\n\n
    callback(final Collection<Target> targets)\n
    '''
