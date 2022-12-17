SYNC_STARTING = "int  100"
SYNC_USER = "int  200"
SYNC_GROUP = "int  300"
SYNC_GROUPMEMBERS = "int  500"
SYNC_ENDED = "int  600"
def ():
    '''returns VMMSyncEvent\n\n
    (final int eventId, final Connection con, final MXLogger logger, final MXLogger sqlLogger, final UserInfo userInfo)\n
    (final int eventId, final VMMDataMap dataMap, final VMMSyncData syncData)\n
    (final int eventId, final MemberDataMap memberDataMap, final VMMSyncData syncData, final Set members)\n
    '''
def getEventType():
    '''returns int\n\n
    getEventType()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def getLogger():
    '''returns MXLogger\n\n
    getLogger()\n
    '''
def getSqlLogger():
    '''returns MXLogger\n\n
    getSqlLogger()\n
    '''
def getUserSyncData():
    '''returns VMMSyncData\n\n
    getUserSyncData()\n
    '''
def getUserDataMap():
    '''returns VMMDataMap\n\n
    getUserDataMap()\n
    '''
def getGroupSyncData():
    '''returns VMMSyncData\n\n
    getGroupSyncData()\n
    '''
def getGroupDataMap():
    '''returns VMMDataMap\n\n
    getGroupDataMap()\n
    '''
def getGroupMemberDataMap():
    '''returns MemberDataMap\n\n
    getGroupMemberDataMap()\n
    '''
def getGroupMembers():
    '''returns Set\n\n
    getGroupMembers()\n
    '''
