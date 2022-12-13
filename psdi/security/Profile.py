IGNORE_SITE = "String  Profile.IgnoreSite""
def Profile():
'''public Profile(final MXServerRemote mxServer, final UserInfo systemUserInfo, final MboRemote maxUserMbo)
public Profile(final MXServerRemote mxServer, final UserInfo systemUserInfo, final String userID, final MboSetRemote groupUserSet, final boolean loadAll)
public Profile(final MXServerRemote mxServer, final UserInfo systemUserInfo, final UserInfo loginuserInfo, final boolean loadAll)
public Profile(final MXServer mxServer, final MboSetRemote maxRoleSet)
'''
pass
def dumpSites():
'''public ArrayList<String> dumpSites()
'''
pass
def getPwDuration():
'''public int getPwDuration()
'''
pass
def getPwWarning():
'''public int getPwWarning()
'''
pass
def dumpPwDays():
'''public ArrayList<String> dumpPwDays()
'''
pass
def getApps():
'''public HashSet<String> getApps()
public HashSet<String> getApps(final int sysFlag)
'''
pass
def getAppsStructure():
'''public HashMap<String, HashMap<String, HashMap<String, HashSet<String>>>> getAppsStructure()
'''
pass
def getAppLevel():
'''public int getAppLevel(final String app)
'''
pass
def sysLevelApp():
'''public boolean sysLevelApp(final String app)
'''
pass
def orgLevelApp():
'''public boolean orgLevelApp(final String app)
public boolean orgLevelApp(final String app, final boolean baseLevelOnly)
'''
pass
def siteLevelApp():
'''public boolean siteLevelApp(final String app)
public boolean siteLevelApp(final String app, final boolean baseLevelOnly)
'''
pass
def getAppAuth():
'''public boolean getAppAuth(final String app)
'''
pass
def getAppOptionAuth():
'''public boolean getAppOptionAuth(String app, String optionname, final String siteorg)
'''
pass
def getPrerequisite():
'''public String getPrerequisite(final String app, final String optionname)
'''
pass
def getConditions():
'''public HashSet<String> getConditions(final String app, final String optionname, final String siteorg)
'''
pass
def getEveryoneCondition():
'''public String getEveryoneCondition(String app, String optionName)
'''
pass
def getAppOptions():
'''public HashSet<String> getAppOptions(String app)
'''
pass
def hasAppOption():
'''public boolean hasAppOption(String app, final String sigOption)
'''
pass
def getAppSiteOrgs():
'''public HashSet<String> getAppSiteOrgs(final String app)
public HashSet<String> getAppSiteOrgs(String app, int forceLevel)
'''
pass
def getSiteCache():
'''public HashSet<String> getSiteCache(final UserInfo ui)
'''
pass
def getAppMenu():
'''public TreeMap getAppMenu(String app, final UserInfo userInfo)
'''
pass
def getAppTools():
'''public TreeMap getAppTools(String app, final UserInfo userInfo)
'''
pass
def getAppSearch():
'''public TreeMap getAppSearch(String app, final UserInfo userInfo)
'''
pass
def getSystemOptionMap():
'''public TreeMap getSystemOptionMap(final UserInfo userInfo)
'''
pass
def getModules():
'''public TreeMap getModules(final UserInfo userInfo)
'''
pass
def getQueryMap():
'''public TreeMap getQueryMap(String app, final UserInfo userInfo)
'''
pass
def getAppInfo():
'''public Hashtable<String, String> getAppInfo(String app, final UserInfo userInfo)
'''
pass
def setQueryMap():
'''public void setQueryMap(String app, final TreeMap newQueryMap, final UserInfo userInfo)
'''
pass
def addApp():
'''public void addApp(final String app, final UserInfo userInfo)
'''
pass
def updateAppMaps():
'''public void updateAppMaps(final String app, final UserInfo userInfo)
'''
pass
def dumpAppAuth():
'''public ArrayList<String> dumpAppAuth()
'''
pass
def getGLAuth():
'''public boolean getGLAuth(final String glField, String siteorg)
public boolean getGLAuth(final int glFieldPos, String siteorg)
'''
pass
def getGLAuthForUserApp():
'''public boolean getGLAuthForUserApp(final int glFieldPos)
'''
pass
def hasAllGLAuth():
'''public boolean hasAllGLAuth(String siteorg)
'''
pass
def hasAnyGLAuth():
'''public boolean hasAnyGLAuth(String siteorg)
'''
pass
def dumpGLAuth():
'''public ArrayList<String> dumpGLAuth()
'''
pass
def getTolerance():
'''public double getTolerance(final String attrName, final String siteorg)
'''
pass
def dumpTolerances():
'''public ArrayList<String> dumpTolerances()
'''
pass
def isLocAuthAll():
'''public boolean isLocAuthAll()
public boolean isLocAuthAll(final String siteid)
'''
pass
def getStorerooms():
'''public String getStorerooms(final String siteid)
'''
pass
def getLocAuth():
'''public boolean getLocAuth(final String siteid, final String location)
'''
pass
def dumpLocAuth():
'''public ArrayList<String> dumpLocAuth()
'''
pass
def isAllCombineableGLSegments():
'''public boolean isAllCombineableGLSegments()
'''
pass
def isAllIndependentGLSegments():
'''public boolean isAllIndependentGLSegments()
'''
pass
def getGroupNames():
'''public HashSet getGroupNames()
'''
pass
def getGroupStartApps():
'''public HashSet getGroupStartApps()
'''
pass
def getGroupsString():
'''public String getGroupsString()
'''
pass
def getSite():
'''public boolean getSite(final String siteid)
'''
pass
def getOrg():
'''public boolean getOrg(final String orgid)
'''
pass
def getLeftNav():
'''public boolean getLeftNav()
'''
pass
def getSites():
'''public TreeSet<String> getSites()
'''
pass
def getSitesString():
'''public String getSitesString()
'''
pass
def oneGroupHasAllSites():
'''public boolean oneGroupHasAllSites()
'''
pass
def hasCombinableAllRepairFacilities():
'''public boolean hasCombinableAllRepairFacilities()
'''
pass
def getOrgs():
'''public TreeSet<String> getOrgs()
'''
pass
def getOrgsString():
'''public String getOrgsString()
'''
pass
def getReadableSites():
'''public TreeSet<String> getReadableSites(final String app)
'''
pass
def getReadableSitesString():
'''public String getReadableSitesString(final String app)
'''
pass
def getReadableOrgs():
'''public TreeSet<String> getReadableOrgs(final String app)
'''
pass
def getReadableOrgsString():
'''public String getReadableOrgsString(final String app)
'''
pass
def isLaborAuthAll():
'''public boolean isLaborAuthAll()
'''
pass
def isAuthLaborSelf():
'''public boolean isAuthLaborSelf(final String orgid, final String laborcode)
'''
pass
def isAuthLaborSuper():
'''public boolean isAuthLaborSuper(final String orgid, final String laborcode)
'''
pass
def isAuthLaborCrew():
'''public boolean isAuthLaborCrew(final String orgid, final String laborcode)
'''
pass
def isAuthLaborGroup():
'''public boolean isAuthLaborGroup(final String orgid, final String laborcode)
'''
pass
def getLaborAuthFlags():
'''public HashMap<String, Boolean> getLaborAuthFlags(final String orgid)
'''
pass
def getLaborAuth():
'''public boolean getLaborAuth(final String orgid, final String laborcode)
'''
pass
def getLaborAuthorities():
'''public HashMap<String, HashSet<String>> getLaborAuthorities()
'''
pass
def getLaborCodes():
'''public String getLaborCodes(final String orgid)
'''
pass
def getLaborCodeSubWhere():
'''public static String getLaborCodeSubWhere(String laborcodes)
'''
pass
def dumpLaborAuth():
'''public ArrayList<String> dumpLaborAuth(final String tempUserid)
'''
pass
def getRoleRestrictions():
'''public String getRoleRestrictions(final String entityname)
public HashMap getRoleRestrictions()
'''
pass
def dumpRoleRestrictions():
'''public ArrayList dumpRoleRestrictions()
'''
pass
def getNonStandardSiteOrgs():
'''public HashSet<String> getNonStandardSiteOrgs(final String app, final boolean getSites)
'''
pass
def getNonStandardApps():
'''public HashMap getNonStandardApps()
'''
pass
def getNonStandardAppOptionAuth():
'''public boolean getNonStandardAppOptionAuth(String app, String optionname, final String orgid, final String siteid)
'''
pass
def dumpNonStandardApps():
'''public ArrayList<String> dumpNonStandardApps()
'''
pass
def getDefaultSite():
'''public String getDefaultSite()
'''
pass
def setDefaultSite():
'''public void setDefaultSite(final String site)
'''
pass
def getDefaultOrg():
'''public String getDefaultOrg()
'''
pass
def setDefaultOrg():
'''public void setDefaultOrg(final String org)
'''
pass
def getInsertSite():
'''public String getInsertSite()
'''
pass
def getInsertOrg():
'''public String getInsertOrg()
'''
pass
def setInsertOrg():
'''public void setInsertOrg(String org)
'''
pass
def setInsertSite():
'''public void setInsertSite(String site)
'''
pass
def getDefaultRepairFacility():
'''public String getDefaultRepairFacility()
'''
pass
def getDefaultRepairFacilitySite():
'''public String getDefaultRepairFacilitySite()
'''
pass
def setInsertItemSet():
'''public void setInsertItemSet(final String setid)
'''
pass
def getInsertItemSet():
'''public String getInsertItemSet()
'''
pass
def setInsertCompanySet():
'''public void setInsertCompanySet(final String setid)
'''
pass
def getInsertCompanySet():
'''public String getInsertCompanySet()
'''
pass
def getQueryWithSite():
'''public boolean getQueryWithSite()
'''
pass
def getDefaultStoreroom():
'''public String getDefaultStoreroom()
'''
pass
def getDefaultStoreroomSite():
'''public String getDefaultStoreroomSite()
'''
pass
def setUserStatus():
'''public void setUserStatus(final String newInternalStatus)
'''
pass
def getLogout():
'''public boolean getLogout()
'''
pass
def getUserStatus():
'''public String getUserStatus()
'''
pass
def useDataRestriction():
'''public boolean useDataRestriction(final String groupname, final String app, final String siteorg)
'''
pass
def allCollectionsAllowed():
'''public boolean allCollectionsAllowed()
'''
pass
def getCollections():
'''public HashSet<String> getCollections()
'''
pass
def hasCombinableNullRepairFacilities():
'''public boolean hasCombinableNullRepairFacilities()
'''
pass
def getDiscreteRepFacAuthSites():
'''public HashMap<String, Boolean[]> getDiscreteRepFacAuthSites()
'''
pass
def getCombinableSites():
'''public HashSet<String> getCombinableSites()
'''
pass
def setProxy():
'''public void setProxy(final Remote proxy)
'''
pass
def getProxy():
'''public Remote getProxy()
'''
pass
def getReportLimit():
'''public Integer getReportLimit(final String attributeName)
'''
pass
