def MaxUser():
    '''public MaxUser(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def getDbIn():
    '''public int getDbIn()
    '''
def add():
    '''public void add()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def undelete():
    '''public void undelete()
    '''
def deleteThisUser():
    '''public boolean deleteThisUser()
    public boolean deleteThisUser(final long accessModifier)
    '''
def undeleteThisUser():
    '''public void undeleteThisUser()
    '''
def maxUserCanDelete():
    '''public void maxUserCanDelete()
    '''
def canDelete():
    '''public void canDelete()
    '''
def toBeSaved():
    '''public boolean toBeSaved()
    '''
def userWasDuplicated():
    '''public boolean userWasDuplicated()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def resetNativeEsigKey():
    '''public void resetNativeEsigKey()
    '''
def appValidate():
    '''public void appValidate()
    '''
def recheckPasswordAuthority():
    '''public void recheckPasswordAuthority()
    '''
def encryptEsigPassword():
    '''public String encryptEsigPassword(final String esigPass)
    '''
def save():
    '''public void save()
    '''
def isActive():
    '''public boolean isActive()
    '''
def isInactive():
    '''public boolean isInactive()
    '''
def isBlocked():
    '''public boolean isBlocked()
    '''
def setBlocked():
    '''public void setBlocked(final String memo)
    '''
def isDeleted():
    '''public boolean isDeleted()
    '''
def addLoginTracking():
    '''public void addLoginTracking(final boolean attemptResult)
    public void addLoginTracking(final boolean attemptResult, final String app, final String reason, final String transid, final String[] keyvalue)
    public void addLoginTracking(final boolean attemptResult, final String app, final String reason, final String transid, final String[] keyvalue, final String ownerTable, final String ownerId)
    public MboRemote addLoginTracking(final String attemptResult)
    public MboRemote addLoginTracking(final String attemptResult, final boolean updateStatus)
    '''
def addMaxSession():
    '''public MboRemote addMaxSession()
    '''
def addServerSession():
    '''public void addServerSession()
    '''
def isPasswordValid():
    '''public boolean isPasswordValid()
    '''
def isDBPasswordValid():
    '''public void isDBPasswordValid()
    '''
def addDBUser():
    '''public final void addDBUser(final String dbuserid)
    '''
def deleteDBUser():
    '''public final void deleteDBUser(final String deleteID)
    '''
def canChangePassword():
    '''public boolean canChangePassword()
    '''
def changeDBPassword():
    '''public final void changeDBPassword()
    '''
def userExistsOnDB():
    '''public final boolean userExistsOnDB(Connection con, final String checkID)
    '''
def addGroupUser():
    '''public void addGroupUser()
    '''
def createPersonMbo():
    '''public MboRemote createPersonMbo(final String personID, final MboSetRemote personSet)
    public MboRemote createPersonMbo(final String personID, final MboSetRemote personSet, final boolean doAutokey)
    '''
def openMainRecordDialog():
    '''public void openMainRecordDialog(String id)
    '''
def cancelMainRecordDialog():
    '''public void cancelMainRecordDialog(String id)
    '''
def clearUserProfileHierarchySet():
    '''public void clearUserProfileHierarchySet()
    '''
def showProfileWarning():
    '''public boolean showProfileWarning()
    '''
def setLoginIdDefault():
    '''public void setLoginIdDefault()
    '''
def setValue():
    '''public void setValue(String attributeName, String val, final long accessModifier)
    '''
def authorizeGroups():
    '''public void authorizeGroups(final MboSetRemote groupSet, final String relationship)
    '''
def clearGenPswdInfo():
    '''public void clearGenPswdInfo()
    '''
def generatePassword():
    '''public void generatePassword()
    '''
def addGrpReassignAuthForUserInsert():
    '''public void addGrpReassignAuthForUserInsert()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def getOldLoginID():
    '''public String getOldLoginID()
    '''
def setOldLoginID():
    '''public void setOldLoginID(final String oldLoginID)
    '''
