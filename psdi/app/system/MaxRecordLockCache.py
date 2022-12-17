SCRIPT_LOGGER = "String  \"maximo.script\""
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isRecordLocked():
    '''returns boolean\n\n
    isRecordLocked(final long ownerID, final String ownerTable)\n
    '''
def getRecordLockedByUserId():
    '''returns String\n\n
    getRecordLockedByUserId(final long ownerID, final String ownerTable)\n
    '''
def getRecordLockedByDisplayName():
    '''returns String\n\n
    getRecordLockedByDisplayName(final long ownerID, final String ownerTable)\n
    '''
def isRecordLockedByMe():
    '''returns boolean\n\n
    isRecordLockedByMe(final long lockedSessionID, final long ownerID, final String ownerTable)\n
    '''
def getLockedRecordsSet():
    '''returns MboSetRemote\n\n
    getLockedRecordsSet()\n
    '''
def isLockingAllowed():
    '''returns boolean\n\n
    isLockingAllowed()\n
    '''
