def ():
    '''returns MaxUser\n\n
    (final MboSet ms)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getDbIn():
    '''returns int\n\n
    getDbIn()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def deleteThisUser():
    '''returns boolean\n\n
    deleteThisUser()\n
    deleteThisUser(final long accessModifier)\n
    '''
def undeleteThisUser():
    '''returns None\n\n
    undeleteThisUser()\n
    '''
def maxUserCanDelete():
    '''returns None\n\n
    maxUserCanDelete()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def userWasDuplicated():
    '''returns boolean\n\n
    userWasDuplicated()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def resetNativeEsigKey():
    '''returns None\n\n
    resetNativeEsigKey()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def recheckPasswordAuthority():
    '''returns None\n\n
    recheckPasswordAuthority()\n
    '''
def encryptEsigPassword():
    '''returns String\n\n
    encryptEsigPassword(final String esigPass)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def isInactive():
    '''returns boolean\n\n
    isInactive()\n
    '''
def isBlocked():
    '''returns boolean\n\n
    isBlocked()\n
    '''
def setBlocked():
    '''returns None\n\n
    setBlocked(final String memo)\n
    '''
def isDeleted():
    '''returns boolean\n\n
    isDeleted()\n
    '''
def addLoginTracking():
    '''returns MboRemote\n\n
    addLoginTracking(final boolean attemptResult)\n
    addLoginTracking(final boolean attemptResult, final String app, final String reason, final String transid, final String[] keyvalue)\n
    addLoginTracking(final boolean attemptResult, final String app, final String reason, final String transid, final String[] keyvalue, final String ownerTable, final String ownerId)\n
    addLoginTracking(final String attemptResult)\n
    addLoginTracking(final String attemptResult, final boolean updateStatus)\n
    '''
def addMaxSession():
    '''returns MboRemote\n\n
    addMaxSession()\n
    '''
def addServerSession():
    '''returns None\n\n
    addServerSession()\n
    '''
def isPasswordValid():
    '''returns boolean\n\n
    isPasswordValid()\n
    '''
def isDBPasswordValid():
    '''returns None\n\n
    isDBPasswordValid()\n
    '''
def canChangePassword():
    '''returns boolean\n\n
    canChangePassword()\n
    '''
def addGroupUser():
    '''returns None\n\n
    addGroupUser()\n
    '''
def createPersonMbo():
    '''returns MboRemote\n\n
    createPersonMbo(final String personID, final MboSetRemote personSet)\n
    createPersonMbo(final String personID, final MboSetRemote personSet, final boolean doAutokey)\n
    '''
def openMainRecordDialog():
    '''returns None\n\n
    openMainRecordDialog(String id)\n
    '''
def cancelMainRecordDialog():
    '''returns None\n\n
    cancelMainRecordDialog(String id)\n
    '''
def clearUserProfileHierarchySet():
    '''returns None\n\n
    clearUserProfileHierarchySet()\n
    '''
def showProfileWarning():
    '''returns boolean\n\n
    showProfileWarning()\n
    '''
def setLoginIdDefault():
    '''returns None\n\n
    setLoginIdDefault()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(String attributeName, String val, final long accessModifier)\n
    '''
def authorizeGroups():
    '''returns None\n\n
    authorizeGroups(final MboSetRemote groupSet, final String relationship)\n
    '''
def clearGenPswdInfo():
    '''returns None\n\n
    clearGenPswdInfo()\n
    '''
def generatePassword():
    '''returns None\n\n
    generatePassword()\n
    '''
def addGrpReassignAuthForUserInsert():
    '''returns None\n\n
    addGrpReassignAuthForUserInsert()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def getOldLoginID():
    '''returns String\n\n
    getOldLoginID()\n
    '''
def setOldLoginID():
    '''returns None\n\n
    setOldLoginID(final String oldLoginID)\n
    '''
