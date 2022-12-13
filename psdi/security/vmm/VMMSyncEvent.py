SYNC_STARTING = "int  100"
SYNC_USER = "int  200"
SYNC_GROUP = "int  300"
SYNC_GROUPMEMBERS = "int  500"
SYNC_ENDED = "int  600"
def VMMSyncEvent():
    '''    public VMMSyncEvent(final int eventId, final Connection con, final MXLogger logger, final MXLogger sqlLogger, final UserInfo userInfo)
    public VMMSyncEvent(final int eventId, final VMMDataMap dataMap, final VMMSyncData syncData)
    public VMMSyncEvent(final int eventId, final MemberDataMap memberDataMap, final VMMSyncData syncData, final Set members)
    '''
def getEventType():
    '''    public int getEventType()
    '''
def getConnection():
    '''    public Connection getConnection()
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo()
    '''
def getLogger():
    '''    public MXLogger getLogger()
    '''
def getSqlLogger():
    '''    public MXLogger getSqlLogger()
    '''
def getUserSyncData():
    '''    public VMMSyncData getUserSyncData()
    '''
def getUserDataMap():
    '''    public VMMDataMap getUserDataMap()
    '''
def getGroupSyncData():
    '''    public VMMSyncData getGroupSyncData()
    '''
def getGroupDataMap():
    '''    public VMMDataMap getGroupDataMap()
    '''
def getGroupMemberDataMap():
    '''    public MemberDataMap getGroupMemberDataMap()
    '''
def getGroupMembers():
    '''    public Set getGroupMembers()
    '''
