IGNORE_SITE = "String  \"Profile.IgnoreSite\""
def Profile():
    '''public Profile(final MXServerRemote mxServer, final UserInfo systemUserInfo, final MboRemote maxUserMbo)
    public Profile(final MXServerRemote mxServer, final UserInfo systemUserInfo, final String userID, final MboSetRemote groupUserSet, final boolean loadAll)
    public Profile(final MXServerRemote mxServer, final UserInfo systemUserInfo, final UserInfo loginuserInfo, final boolean loadAll)
    public Profile(final MXServer mxServer, final MboSetRemote maxRoleSet)
    '''
def dumpSites():
    '''public ArrayList<String> dumpSites()
    '''
def getPwDuration():
    '''public int getPwDuration()
    '''
def getPwWarning():
    '''public int getPwWarning()
    '''
def dumpPwDays():
    '''public ArrayList<String> dumpPwDays()
    '''
def getApps():
    '''public HashSet<String> getApps()
    public HashSet<String> getApps(final int sysFlag)
    '''
def getAppsStructure():
    '''public HashMap<String, HashMap<String, HashMap<String, HashSet<String>>>> getAppsStructure()
    '''
def getAppLevel():
    '''public int getAppLevel(final String app)
    '''
def sysLevelApp():
    '''public boolean sysLevelApp(final String app)
    '''
def orgLevelApp():
    '''public boolean orgLevelApp(final String app)
    public boolean orgLevelApp(final String app, final boolean baseLevelOnly)
    '''
def siteLevelApp():
    '''public boolean siteLevelApp(final String app)
    public boolean siteLevelApp(final String app, final boolean baseLevelOnly)
    '''
def getAppAuth():
    '''public boolean getAppAuth(final String app)
    '''
def getAppOptionAuth():
    '''public boolean getAppOptionAuth(String app, String optionname, final String siteorg)
    '''
def getPrerequisite():
    '''public String getPrerequisite(final String app, final String optionname)
    '''
def getConditions():
    '''public HashSet<String> getConditions(final String app, final String optionname, final String siteorg)
    '''
def getEveryoneCondition():
    '''public String getEveryoneCondition(String app, String optionName)
    '''
def getAppOptions():
    '''public HashSet<String> getAppOptions(String app)
    '''
def hasAppOption():
    '''public boolean hasAppOption(String app, final String sigOption)
    '''
def getAppSiteOrgs():
    '''public HashSet<String> getAppSiteOrgs(final String app)
    public HashSet<String> getAppSiteOrgs(String app, int forceLevel)
    '''
def getSiteCache():
    '''public HashSet<String> getSiteCache(final UserInfo ui)
    '''
def getAppMenu():
    '''public TreeMap getAppMenu(String app, final UserInfo userInfo)
    '''
def getAppTools():
    '''public TreeMap getAppTools(String app, final UserInfo userInfo)
    '''
def getAppSearch():
    '''public TreeMap getAppSearch(String app, final UserInfo userInfo)
    '''
def getSystemOptionMap():
    '''public TreeMap getSystemOptionMap(final UserInfo userInfo)
    '''
def getModules():
    '''public TreeMap getModules(final UserInfo userInfo)
    '''
def getQueryMap():
    '''public TreeMap getQueryMap(String app, final UserInfo userInfo)
    '''
def getAppInfo():
    '''public Hashtable<String, String> getAppInfo(String app, final UserInfo userInfo)
    '''
def setQueryMap():
    '''public void setQueryMap(String app, final TreeMap newQueryMap, final UserInfo userInfo)
    '''
def addApp():
    '''public void addApp(final String app, final UserInfo userInfo)
    '''
def updateAppMaps():
    '''public void updateAppMaps(final String app, final UserInfo userInfo)
    '''
def dumpAppAuth():
    '''public ArrayList<String> dumpAppAuth()
    '''
def getGLAuth():
    '''public boolean getGLAuth(final String glField, String siteorg)
    public boolean getGLAuth(final int glFieldPos, String siteorg)
    '''
def getGLAuthForUserApp():
    '''public boolean getGLAuthForUserApp(final int glFieldPos)
    '''
def hasAllGLAuth():
    '''public boolean hasAllGLAuth(String siteorg)
    '''
def hasAnyGLAuth():
    '''public boolean hasAnyGLAuth(String siteorg)
    '''
def dumpGLAuth():
    '''public ArrayList<String> dumpGLAuth()
    '''
def getTolerance():
    '''public double getTolerance(final String attrName, final String siteorg)
    '''
def dumpTolerances():
    '''public ArrayList<String> dumpTolerances()
    '''
def isLocAuthAll():
    '''public boolean isLocAuthAll()
    public boolean isLocAuthAll(final String siteid)
    '''
def getStorerooms():
    '''public String getStorerooms(final String siteid)
    '''
def getLocAuth():
    '''public boolean getLocAuth(final String siteid, final String location)
    '''
def dumpLocAuth():
    '''public ArrayList<String> dumpLocAuth()
    '''
def isAllCombineableGLSegments():
    '''public boolean isAllCombineableGLSegments()
    '''
def isAllIndependentGLSegments():
    '''public boolean isAllIndependentGLSegments()
    '''
def getGroupNames():
    '''public HashSet getGroupNames()
    '''
def getGroupStartApps():
    '''public HashSet getGroupStartApps()
    '''
def getGroupsString():
    '''public String getGroupsString()
    '''
def getSite():
    '''public boolean getSite(final String siteid)
    '''
def getOrg():
    '''public boolean getOrg(final String orgid)
    '''
def getLeftNav():
    '''public boolean getLeftNav()
    '''
def getSites():
    '''public TreeSet<String> getSites()
    '''
def getSitesString():
    '''public String getSitesString()
    '''
def oneGroupHasAllSites():
    '''public boolean oneGroupHasAllSites()
    '''
def hasCombinableAllRepairFacilities():
    '''public boolean hasCombinableAllRepairFacilities()
    '''
def getOrgs():
    '''public TreeSet<String> getOrgs()
    '''
def getOrgsString():
    '''public String getOrgsString()
    '''
def getReadableSites():
    '''public TreeSet<String> getReadableSites(final String app)
    '''
def getReadableSitesString():
    '''public String getReadableSitesString(final String app)
    '''
def getReadableOrgs():
    '''public TreeSet<String> getReadableOrgs(final String app)
    '''
def getReadableOrgsString():
    '''public String getReadableOrgsString(final String app)
    '''
def isLaborAuthAll():
    '''public boolean isLaborAuthAll()
    '''
def isAuthLaborSelf():
    '''public boolean isAuthLaborSelf(final String orgid, final String laborcode)
    '''
def isAuthLaborSuper():
    '''public boolean isAuthLaborSuper(final String orgid, final String laborcode)
    '''
def isAuthLaborCrew():
    '''public boolean isAuthLaborCrew(final String orgid, final String laborcode)
    '''
def isAuthLaborGroup():
    '''public boolean isAuthLaborGroup(final String orgid, final String laborcode)
    '''
def getLaborAuthFlags():
    '''public HashMap<String, Boolean> getLaborAuthFlags(final String orgid)
    '''
def getLaborAuth():
    '''public boolean getLaborAuth(final String orgid, final String laborcode)
    '''
def getLaborAuthorities():
    '''public HashMap<String, HashSet<String>> getLaborAuthorities()
    '''
def getLaborCodes():
    '''public String getLaborCodes(final String orgid)
    '''
def getLaborCodeSubWhere():
    '''public static String getLaborCodeSubWhere(String laborcodes)
    '''
def dumpLaborAuth():
    '''public ArrayList<String> dumpLaborAuth(final String tempUserid)
    '''
def getRoleRestrictions():
    '''public String getRoleRestrictions(final String entityname)
    public HashMap getRoleRestrictions()
    '''
def dumpRoleRestrictions():
    '''public ArrayList dumpRoleRestrictions()
    '''
def getNonStandardSiteOrgs():
    '''public HashSet<String> getNonStandardSiteOrgs(final String app, final boolean getSites)
    '''
def getNonStandardApps():
    '''public HashMap getNonStandardApps()
    '''
def getNonStandardAppOptionAuth():
    '''public boolean getNonStandardAppOptionAuth(String app, String optionname, final String orgid, final String siteid)
    '''
def dumpNonStandardApps():
    '''public ArrayList<String> dumpNonStandardApps()
    '''
def getDefaultSite():
    '''public String getDefaultSite()
    '''
def setDefaultSite():
    '''public void setDefaultSite(final String site)
    '''
def getDefaultOrg():
    '''public String getDefaultOrg()
    '''
def setDefaultOrg():
    '''public void setDefaultOrg(final String org)
    '''
def getInsertSite():
    '''public String getInsertSite()
    '''
def getInsertOrg():
    '''public String getInsertOrg()
    '''
def setInsertOrg():
    '''public void setInsertOrg(String org)
    '''
def setInsertSite():
    '''public void setInsertSite(String site)
    '''
def getDefaultRepairFacility():
    '''public String getDefaultRepairFacility()
    '''
def getDefaultRepairFacilitySite():
    '''public String getDefaultRepairFacilitySite()
    '''
def setInsertItemSet():
    '''public void setInsertItemSet(final String setid)
    '''
def getInsertItemSet():
    '''public String getInsertItemSet()
    '''
def setInsertCompanySet():
    '''public void setInsertCompanySet(final String setid)
    '''
def getInsertCompanySet():
    '''public String getInsertCompanySet()
    '''
def getQueryWithSite():
    '''public boolean getQueryWithSite()
    '''
def getDefaultStoreroom():
    '''public String getDefaultStoreroom()
    '''
def getDefaultStoreroomSite():
    '''public String getDefaultStoreroomSite()
    '''
def setUserStatus():
    '''public void setUserStatus(final String newInternalStatus)
    '''
def getLogout():
    '''public boolean getLogout()
    '''
def getUserStatus():
    '''public String getUserStatus()
    '''
def useDataRestriction():
    '''public boolean useDataRestriction(final String groupname, final String app, final String siteorg)
    '''
def allCollectionsAllowed():
    '''public boolean allCollectionsAllowed()
    '''
def getCollections():
    '''public HashSet<String> getCollections()
    '''
def hasCombinableNullRepairFacilities():
    '''public boolean hasCombinableNullRepairFacilities()
    '''
def getDiscreteRepFacAuthSites():
    '''public HashMap<String, Boolean[]> getDiscreteRepFacAuthSites()
    '''
def getCombinableSites():
    '''public HashSet<String> getCombinableSites()
    '''
def setProxy():
    '''public void setProxy(final Remote proxy)
    '''
def getProxy():
    '''public Remote getProxy()
    '''
def getReportLimit():
    '''public Integer getReportLimit(final String attributeName)
    '''
