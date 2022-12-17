def ():
    '''returns MaxRecordLockCacheImpl\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def isLockingAllowed():
    '''returns boolean\n\n
    isLockingAllowed()\n
    '''
def getLockedRecordsSet():
    '''returns MboSetRemote\n\n
    getLockedRecordsSet()\n
    '''
def isRecordLockedByMe():
    '''returns boolean\n\n
    isRecordLockedByMe(final long lockedSessionID, final long ownerID, final String ownerTable)\n
    '''
def getRecordLockedByDisplayName():
    '''returns String\n\n
    getRecordLockedByDisplayName(final long ownerID, final String ownerTable)\n
    '''
def getRecordLockedByUserId():
    '''returns String\n\n
    getRecordLockedByUserId(final long ownerID, final String ownerTable)\n
    '''
def isRecordLocked():
    '''returns boolean\n\n
    isRecordLocked(final long ownerID, final String ownerTable)\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
