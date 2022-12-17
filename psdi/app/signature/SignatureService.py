def ():
    '''returns SignatureService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getSigCache():
    '''returns SignatureCache\n\n
    getSigCache()\n
    '''
def getNewUserGroup():
    '''returns String\n\n
    getNewUserGroup(final UserInfo userInfo)\n
    '''
def getEveryoneGroup():
    '''returns String\n\n
    getEveryoneGroup(final UserInfo userInfo)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive(final String userID, final UserInfo userInfo)\n
    '''
def setActive():
    '''returns MboSetRemote\n\n
    setActive(final String userID, final String memo, final UserInfo userInfo)\n
    '''
def activateUser():
    '''returns None\n\n
    activateUser(final String userID, final String memo, final UserInfo userInfo)\n
    '''
def isBlocked():
    '''returns boolean\n\n
    isBlocked(final String userID, final UserInfo userInfo)\n
    '''
def setBlocked():
    '''returns MboSetRemote\n\n
    setBlocked(final String userID, final String memo, final UserInfo userInfo)\n
    '''
def addLoginTracking():
    '''returns None\n\n
    addLoginTracking(final String userID, final boolean attemptResult, final UserInfo userInfo)\n
    addLoginTracking(final String userID, final boolean attemptResult, final UserInfo userInfo, final String app, final String reason, final String transid, final String[] keyvalue)\n
    addLoginTracking(final String userID, final boolean attemptResult, final UserInfo userInfo, final String app, final String reason, final String transid, final String[] keyvalue, final String ownerTable, final String ownerId)\n
    '''
def generatePassword():
    '''returns String\n\n
    generatePassword(final String userID, final UserInfo userInfo)\n
    generatePassword(final String userID, final UserInfo userInfo, final MboRemote mbo)\n
    '''
def validatePassword():
    '''returns None\n\n
    validatePassword(final String userID, final String checkString, final UserInfo userInfo)\n
    validatePassword(final String userID, final String checkString, final UserInfo userInfo, final MboRemote mbo)\n
    '''
def canChangePassword():
    '''returns boolean\n\n
    canChangePassword(String userID, final UserInfo userInfo)\n
    '''
def showPasswordWarning():
    '''returns boolean\n\n
    showPasswordWarning(String loginID, final UserInfo userInfo)\n
    '''
def hasPasswordExpired():
    '''returns boolean\n\n
    hasPasswordExpired(String loginID, final UserInfo userInfo)\n
    '''
def testForcePasswordChange():
    '''returns boolean\n\n
    testForcePasswordChange(String userID, final UserInfo userInfo)\n
    '''
def passwordWillExpire():
    '''returns int\n\n
    passwordWillExpire(String loginID, final UserInfo userInfo)\n
    '''
def getQuerySql():
    '''returns String\n\n
    getQuerySql(final String clauseName, final String appName, final UserInfo userInfo)\n
    '''
def getUserPref():
    '''returns String\n\n
    getUserPref(final String varname, final UserInfo userInfo)\n
    '''
def setUserPref():
    '''returns None\n\n
    setUserPref(final String varname, final String varvalue, final UserInfo userInfo)\n
    '''
def deleteUserPref():
    '''returns None\n\n
    deleteUserPref(final String varname, final UserInfo userInfo)\n
    '''
def getQueriesForUser():
    '''returns MboSetRemote\n\n
    getQueriesForUser(final String appName, final UserInfo userInfo)\n
    '''
def getUserAuthForApp():
    '''returns TreeMap[]\n\n
    getUserAuthForApp(String appName, final UserInfo userInfo)\n
    '''
def getModuleMap():
    '''returns TreeMap\n\n
    getModuleMap(final UserInfo userInfo)\n
    '''
def getAppsForModuleAndUser():
    '''returns MboSetRemote\n\n
    getAppsForModuleAndUser(final String module, final UserInfo userInfo)\n
    '''
def getLaborForUserAndSite():
    '''returns LaborRemote\n\n
    getLaborForUserAndSite(final String userID, final String siteid, final UserInfo userInfo)\n
    '''
def getLaborForUserAndOrg():
    '''returns LaborRemote\n\n
    getLaborForUserAndOrg(final String userID, final String orgid, final UserInfo userInfo)\n
    '''
def isValidSite():
    '''returns boolean\n\n
    isValidSite(final UserInfo userInfo, final String siteId)\n
    '''
def getSiteAdminWhere():
    '''returns String[]\n\n
    getSiteAdminWhere(final MboSetRemote mboSet, final String app)\n
    '''
def validateAuthorized():
    '''returns None\n\n
    validateAuthorized(final boolean authorized, final MboRemote mbo, final MboSetRemote sigoSet1, final MboSetRemote sigoSet2, final MboSetRemote sigoSet3)\n
    '''
def setAuthorized():
    '''returns None\n\n
    setAuthorized(final boolean authorized, final MboRemote mbo, final MboSetRemote sigoSet1, final MboSetRemote sigoSet2, final MboSetRemote sigoSet3)\n
    '''
def getAlsoSigoption():
    '''returns HashSet<String>\n\n
    getAlsoSigoption(final boolean alsoGrants, final MboRemote mbo, final MboSetRemote sigoSet1, final MboSetRemote sigoSet2, final MboSetRemote sigoSet3)\n
    '''
def allowedWithLDAP():
    '''returns boolean\n\n
    allowedWithLDAP(final String app, final String optionname)\n
    '''
def isActiveSite():
    '''returns boolean\n\n
    isActiveSite(final String siteID)\n
    '''
def applyDefaultTemplate():
    '''returns None\n\n
    applyDefaultTemplate(@WSMboKey("MAXGROUP") final MboRemote maxGroup, final String app)\n
    '''
def applyUserQueryList():
    '''returns None\n\n
    applyUserQueryList(final MboSetRemote msr, final String queryName, final String owner, final String app, final boolean complete)\n
    '''
def refreshUserConts():
    '''returns None\n\n
    refreshUserConts(@WSMboKey("USERQUERY") final MboRemote userQuery)\n
    '''
def refreshUserCont():
    '''returns None\n\n
    refreshUserCont(final UserInfo userInfo)\n
    '''
