SYNC_STARTING = "int  100"
SYNC_USER = "int  200"
SYNC_GROUP = "int  300"
SYNC_GROUPMEMBERS = "int  500"
SYNC_ENDED = "int  600"
def LdapSyncEvent():
    '''    public LdapSyncEvent(final int eventId, final Connection con, final MXLogger logger, final MXLogger sqlLogger, final UserInfo userInfo)
    public LdapSyncEvent(final int eventId, final DataMap dataMap, final SyncData syncData)
    public LdapSyncEvent(final int eventId, final MemberDataMap memberDataMap, final SyncData syncData, final Set members)
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
    '''    public SyncData getUserSyncData()
    '''
def getUserDataMap():
    '''    public DataMap getUserDataMap()
    '''
def getGroupSyncData():
    '''    public SyncData getGroupSyncData()
    '''
def getGroupDataMap():
    '''    public DataMap getGroupDataMap()
    '''
def getGroupMemberDataMap():
    '''    public MemberDataMap getGroupMemberDataMap()
    '''
def getGroupMembers():
    '''    public Set getGroupMembers()
    '''
