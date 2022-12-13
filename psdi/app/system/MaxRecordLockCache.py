SCRIPT_LOGGER = "String  \"maximo.script\""
def getInstance():
    '''public static final MaxRecordLockCache getInstance()
    '''
def getName():
    '''public String getName()
    '''
def isRecordLocked():
    '''public boolean isRecordLocked(final long ownerID, final String ownerTable)
    '''
def getRecordLockedByUserId():
    '''public String getRecordLockedByUserId(final long ownerID, final String ownerTable)
    '''
def getRecordLockedByDisplayName():
    '''public String getRecordLockedByDisplayName(final long ownerID, final String ownerTable)
    '''
def isRecordLockedByMe():
    '''public boolean isRecordLockedByMe(final long lockedSessionID, final long ownerID, final String ownerTable)
    '''
def getLockedRecordsSet():
    '''public MboSetRemote getLockedRecordsSet()
    '''
def isLockingAllowed():
    '''public boolean isLockingAllowed()
    '''
