def SignatureService():
'''public SignatureService()
public SignatureService(final MXServer mxServer)
'''
pass
def getSigCache():
'''public SignatureCache getSigCache()
'''
pass
def getNewUserGroup():
'''public String getNewUserGroup(final UserInfo userInfo)
'''
pass
def getEveryoneGroup():
'''public String getEveryoneGroup(final UserInfo userInfo)
'''
pass
def isActive():
'''public boolean isActive(final String userID, final UserInfo userInfo)
'''
pass
def setActive():
'''public MboSetRemote setActive(final String userID, final String memo, final UserInfo userInfo)
'''
pass
def activateUser():
'''public void activateUser(final String userID, final String memo, final UserInfo userInfo)
'''
pass
def isBlocked():
'''public boolean isBlocked(final String userID, final UserInfo userInfo)
'''
pass
def setBlocked():
'''public MboSetRemote setBlocked(final String userID, final String memo, final UserInfo userInfo)
'''
pass
def addLoginTracking():
'''public void addLoginTracking(final String userID, final boolean attemptResult, final UserInfo userInfo)
public void addLoginTracking(final String userID, final boolean attemptResult, final UserInfo userInfo, final String app, final String reason, final String transid, final String[] keyvalue)
public void addLoginTracking(final String userID, final boolean attemptResult, final UserInfo userInfo, final String app, final String reason, final String transid, final String[] keyvalue, final String ownerTable, final String ownerId)
'''
pass
def generatePassword():
'''public String generatePassword(final String userID, final UserInfo userInfo)
public String generatePassword(final String userID, final UserInfo userInfo, final MboRemote mbo)
'''
pass
def validatePassword():
'''public void validatePassword(final String userID, final String checkString, final UserInfo userInfo)
public void validatePassword(final String userID, final String checkString, final UserInfo userInfo, final MboRemote mbo)
'''
pass
def canChangePassword():
'''public boolean canChangePassword(String userID, final UserInfo userInfo)
'''
pass
def showPasswordWarning():
'''public boolean showPasswordWarning(String loginID, final UserInfo userInfo)
'''
pass
def hasPasswordExpired():
'''public boolean hasPasswordExpired(String loginID, final UserInfo userInfo)
'''
pass
def testForcePasswordChange():
'''public boolean testForcePasswordChange(String userID, final UserInfo userInfo)
'''
pass
def passwordWillExpire():
'''public int passwordWillExpire(String loginID, final UserInfo userInfo)
'''
pass
def getQuerySql():
'''public String getQuerySql(final String clauseName, final String appName, final UserInfo userInfo)
'''
pass
def getUserPref():
'''public String getUserPref(final String varname, final UserInfo userInfo)
'''
pass
def setUserPref():
'''public void setUserPref(final String varname, final String varvalue, final UserInfo userInfo)
'''
pass
def deleteUserPref():
'''public void deleteUserPref(final String varname, final UserInfo userInfo)
'''
pass
def getQueriesForUser():
'''public MboSetRemote getQueriesForUser(final String appName, final UserInfo userInfo)
'''
pass
def getUserAuthForApp():
'''public TreeMap[] getUserAuthForApp(String appName, final UserInfo userInfo)
'''
pass
def getModuleMap():
'''public TreeMap getModuleMap(final UserInfo userInfo)
'''
pass
def getQueryMap():
'''public TreeMap<String, Hashtable<String, String>> getQueryMap(final MboSetRemote querySet)
'''
pass
def getAppsForModuleAndUser():
'''public MboSetRemote getAppsForModuleAndUser(final String module, final UserInfo userInfo)
'''
pass
def getLaborForUserAndSite():
'''public LaborRemote getLaborForUserAndSite(final String userID, final String siteid, final UserInfo userInfo)
'''
pass
def getLaborForUserAndOrg():
'''public LaborRemote getLaborForUserAndOrg(final String userID, final String orgid, final UserInfo userInfo)
'''
pass
def isValidSite():
'''public boolean isValidSite(final UserInfo userInfo, final String siteId)
'''
pass
def getSiteAdminWhere():
'''public String[] getSiteAdminWhere(final MboSetRemote mboSet, final String app)
'''
pass
def validateAuthorized():
'''public void validateAuthorized(final boolean authorized, final MboRemote mbo, final MboSetRemote sigoSet1, final MboSetRemote sigoSet2, final MboSetRemote sigoSet3)
'''
pass
def setAuthorized():
'''public void setAuthorized(final boolean authorized, final MboRemote mbo, final MboSetRemote sigoSet1, final MboSetRemote sigoSet2, final MboSetRemote sigoSet3)
'''
pass
def getAlsoSigoption():
'''public HashSet<String> getAlsoSigoption(final boolean alsoGrants, final MboRemote mbo, final MboSetRemote sigoSet1, final MboSetRemote sigoSet2, final MboSetRemote sigoSet3)
'''
pass
def allowedWithLDAP():
'''public boolean allowedWithLDAP(final String app, final String optionname)
'''
pass
def isActiveSite():
'''public boolean isActiveSite(final String siteID)
'''
pass
def applyDefaultTemplate():
'''public void applyDefaultTemplate(@WSMboKey("MAXGROUP") final MboRemote maxGroup, final String app)
'''
pass
def applyUserQueryList():
'''public void applyUserQueryList(final MboSetRemote msr, final String queryName, final String owner, final String app, final boolean complete)
'''
pass
def refreshUserConts():
'''public void refreshUserConts(@WSMboKey("USERQUERY") final MboRemote userQuery)
'''
pass
def refreshUserCont():
'''public void refreshUserCont(final UserInfo userInfo)
'''
pass
