SYNC_STARTING = "int  100"
SYNC_USER = "int  200"
SYNC_GROUP = "int  300"
SYNC_GROUPMEMBERS = "int  500"
SYNC_ENDED = "int  600"
def LdapSyncEvent():
'''public LdapSyncEvent(final int eventId, final Connection con, final MXLogger logger, final MXLogger sqlLogger, final UserInfo userInfo)
public LdapSyncEvent(final int eventId, final DataMap dataMap, final SyncData syncData)
public LdapSyncEvent(final int eventId, final MemberDataMap memberDataMap, final SyncData syncData, final Set members)
'''
pass
def getEventType():
'''public int getEventType()
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def getLogger():
'''public MXLogger getLogger()
'''
pass
def getSqlLogger():
'''public MXLogger getSqlLogger()
'''
pass
def getUserSyncData():
'''public SyncData getUserSyncData()
'''
pass
def getUserDataMap():
'''public DataMap getUserDataMap()
'''
pass
def getGroupSyncData():
'''public SyncData getGroupSyncData()
'''
pass
def getGroupDataMap():
'''public DataMap getGroupDataMap()
'''
pass
def getGroupMemberDataMap():
'''public MemberDataMap getGroupMemberDataMap()
'''
pass
def getGroupMembers():
'''public Set getGroupMembers()
'''
pass
