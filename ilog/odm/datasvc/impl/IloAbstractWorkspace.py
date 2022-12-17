COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
REPOSITORY_CHANGE_POLLING_TIMER = "String  \"ilog.edi.workspace.refreshtimer\""
WORKSPACE_DELETE = "String  \"Delete\""
WORKSPACE_READ = "String  \"Read\""
WORKSPACE_WRITE = "String  \"Write\""
WORKSPACE_LOCK = "String  \"Lock\""
def ():
    '''returns IloAbstractWorkspace\n\n
    (final IloAbstractDataManager data_manager, final IloPersistentRow wpo)\n
    '''
def getVersion():
    '''returns Long\n\n
    getVersion()\n
    '''
def call():
    '''returns Void\n\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    call()\n
    '''
def getLockVersion():
    '''returns Long\n\n
    getLockVersion()\n
    '''
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
def getPersistentID():
    '''returns String\n\n
    getPersistentID()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final IloWorkspaceListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final IloWorkspaceListener listener)\n
    '''
def checkInSync():
    '''returns boolean\n\n
    checkInSync()\n
    '''
def addRepositoryChangeListener():
    '''returns None\n\n
    addRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getSource():
    '''returns IloSharable\n\n
    getSource()\n
    '''
def removeRepositoryChangeListener():
    '''returns None\n\n
    removeRepositoryChangeListener(final IloRepositoryChangeListener listener)\n
    '''
def getLastModifier():
    '''returns IloUser\n\n
    getLastModifier()\n
    '''
def getLastModificationDate():
    '''returns Date\n\n
    getLastModificationDate()\n
    '''
def isInSync():
    '''returns boolean\n\n
    isInSync()\n
    '''
def areLocksInSync():
    '''returns boolean\n\n
    areLocksInSync()\n
    '''
def getLocks():
    '''returns Collection<IloLock>\n\n
    getLocks()\n
    '''
def transferLockOwnership():
    '''returns None\n\n
    transferLockOwnership(final ilog.odm.datasvc.internal.IloLock lock, final IloUser otherUser)\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
    '''
def refreshLocks():
    '''returns None\n\n
    refreshLocks()\n
    '''
def removeLock():
    '''returns None\n\n
    removeLock(final IloLock lock)\n
    '''
def getItemVersion():
    '''returns Long\n\n
    getItemVersion()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
