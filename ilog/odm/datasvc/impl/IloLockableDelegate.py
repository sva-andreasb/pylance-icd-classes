COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloLockableDelegate\n\n
    (final IloAbstractDataManager data_manager, final IloLockableManager lockable_manager, final IloPersistentRow sharablePo)\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted(final boolean deleted)\n
    isDeleted()\n
    '''
def getLocks():
    '''returns Collection<IloLock>\n\n
    getLocks()\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
    '''
def refreshLocks():
    '''returns None\n\n
    refreshLocks()\n
    refreshLocks(final Collection<IloRow> rows)\n
    '''
def transferLockOwnership():
    '''returns None\n\n
    transferLockOwnership(final IloLock lock, final IloUser other_user)\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final IloLock lock)\n
    '''
def getHighiestLockForCurrentUser():
    '''returns IloLock\n\n
    getHighiestLockForCurrentUser()\n
    '''
def getHighiestLockForOtherUsers():
    '''returns IloLock\n\n
    getHighiestLockForOtherUsers()\n
    '''
def checkInSync():
    '''returns None\n\n
    checkInSync()\n
    '''
def isInvalidatedLocks():
    '''returns boolean\n\n
    isInvalidatedLocks()\n
    '''
def checkLock():
    '''returns None\n\n
    checkLock(final int user_min_right, final int other_max_right)\n
    '''
def getSharableId():
    '''returns Long\n\n
    getSharableId()\n
    '''
def getLockVersion():
    '''returns Long\n\n
    getLockVersion()\n
    '''
