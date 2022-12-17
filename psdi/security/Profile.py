IGNORE_SITE = "String  \"Profile.IgnoreSite\""
def ():
    '''returns Profile\n\n
    (final MXServerRemote mxServer, final UserInfo systemUserInfo, final MboRemote maxUserMbo)\n
    (final MXServerRemote mxServer, final UserInfo systemUserInfo, final String userID, final MboSetRemote groupUserSet, final boolean loadAll)\n
    (final MXServerRemote mxServer, final UserInfo systemUserInfo, final UserInfo loginuserInfo, final boolean loadAll)\n
    (final MXServer mxServer, final MboSetRemote maxRoleSet)\n
    '''
def dumpSites():
    '''returns ArrayList<String>\n\n
    dumpSites()\n
    '''
def getPwDuration():
    '''returns int\n\n
    getPwDuration()\n
    '''
def getPwWarning():
    '''returns int\n\n
    getPwWarning()\n
    '''
def dumpPwDays():
    '''returns ArrayList<String>\n\n
    dumpPwDays()\n
    '''
def getApps():
    '''returns HashSet<String>\n\n
    getApps()\n
    getApps(final int sysFlag)\n
    '''
def getAppLevel():
    '''returns int\n\n
    getAppLevel(final String app)\n
    '''
def sysLevelApp():
    '''returns boolean\n\n
    sysLevelApp(final String app)\n
    '''
def orgLevelApp():
    '''returns boolean\n\n
    orgLevelApp(final String app)\n
    orgLevelApp(final String app, final boolean baseLevelOnly)\n
    '''
def siteLevelApp():
    '''returns boolean\n\n
    siteLevelApp(final String app)\n
    siteLevelApp(final String app, final boolean baseLevelOnly)\n
    '''
def getAppAuth():
    '''returns boolean\n\n
    getAppAuth(final String app)\n
    '''
def getAppOptionAuth():
    '''returns boolean\n\n
    getAppOptionAuth(String app, String optionname, final String siteorg)\n
    '''
def getPrerequisite():
    '''returns String\n\n
    getPrerequisite(final String app, final String optionname)\n
    '''
def getConditions():
    '''returns HashSet<String>\n\n
    getConditions(final String app, final String optionname, final String siteorg)\n
    '''
def getEveryoneCondition():
    '''returns String\n\n
    getEveryoneCondition(String app, String optionName)\n
    '''
def getAppOptions():
    '''returns HashSet<String>\n\n
    getAppOptions(String app)\n
    '''
def hasAppOption():
    '''returns boolean\n\n
    hasAppOption(String app, final String sigOption)\n
    '''
def getAppSiteOrgs():
    '''returns HashSet<String>\n\n
    getAppSiteOrgs(final String app)\n
    getAppSiteOrgs(String app, int forceLevel)\n
    '''
def getSiteCache():
    '''returns HashSet<String>\n\n
    getSiteCache(final UserInfo ui)\n
    '''
def getAppMenu():
    '''returns TreeMap\n\n
    getAppMenu(String app, final UserInfo userInfo)\n
    '''
def getAppTools():
    '''returns TreeMap\n\n
    getAppTools(String app, final UserInfo userInfo)\n
    '''
def getAppSearch():
    '''returns TreeMap\n\n
    getAppSearch(String app, final UserInfo userInfo)\n
    '''
def getSystemOptionMap():
    '''returns TreeMap\n\n
    getSystemOptionMap(final UserInfo userInfo)\n
    '''
def getModules():
    '''returns TreeMap\n\n
    getModules(final UserInfo userInfo)\n
    '''
def getQueryMap():
    '''returns TreeMap\n\n
    getQueryMap(String app, final UserInfo userInfo)\n
    '''
def setQueryMap():
    '''returns None\n\n
    setQueryMap(String app, final TreeMap newQueryMap, final UserInfo userInfo)\n
    '''
def addApp():
    '''returns None\n\n
    addApp(final String app, final UserInfo userInfo)\n
    '''
def updateAppMaps():
    '''returns None\n\n
    updateAppMaps(final String app, final UserInfo userInfo)\n
    '''
def dumpAppAuth():
    '''returns ArrayList<String>\n\n
    dumpAppAuth()\n
    '''
def getGLAuth():
    '''returns boolean\n\n
    getGLAuth(final String glField, String siteorg)\n
    getGLAuth(final int glFieldPos, String siteorg)\n
    '''
def getGLAuthForUserApp():
    '''returns boolean\n\n
    getGLAuthForUserApp(final int glFieldPos)\n
    '''
def hasAllGLAuth():
    '''returns boolean\n\n
    hasAllGLAuth(String siteorg)\n
    '''
def hasAnyGLAuth():
    '''returns boolean\n\n
    hasAnyGLAuth(String siteorg)\n
    '''
def dumpGLAuth():
    '''returns ArrayList<String>\n\n
    dumpGLAuth()\n
    '''
def getTolerance():
    '''returns double\n\n
    getTolerance(final String attrName, final String siteorg)\n
    '''
def dumpTolerances():
    '''returns ArrayList<String>\n\n
    dumpTolerances()\n
    '''
def isLocAuthAll():
    '''returns boolean\n\n
    isLocAuthAll()\n
    isLocAuthAll(final String siteid)\n
    '''
def getStorerooms():
    '''returns String\n\n
    getStorerooms(final String siteid)\n
    '''
def getLocAuth():
    '''returns boolean\n\n
    getLocAuth(final String siteid, final String location)\n
    '''
def dumpLocAuth():
    '''returns ArrayList<String>\n\n
    dumpLocAuth()\n
    '''
def isAllCombineableGLSegments():
    '''returns boolean\n\n
    isAllCombineableGLSegments()\n
    '''
def isAllIndependentGLSegments():
    '''returns boolean\n\n
    isAllIndependentGLSegments()\n
    '''
def getGroupNames():
    '''returns HashSet\n\n
    getGroupNames()\n
    '''
def getGroupStartApps():
    '''returns HashSet\n\n
    getGroupStartApps()\n
    '''
def getGroupsString():
    '''returns String\n\n
    getGroupsString()\n
    '''
def getSite():
    '''returns boolean\n\n
    getSite(final String siteid)\n
    '''
def getOrg():
    '''returns boolean\n\n
    getOrg(final String orgid)\n
    '''
def getLeftNav():
    '''returns boolean\n\n
    getLeftNav()\n
    '''
def getSites():
    '''returns TreeSet<String>\n\n
    getSites()\n
    '''
def getSitesString():
    '''returns String\n\n
    getSitesString()\n
    '''
def oneGroupHasAllSites():
    '''returns boolean\n\n
    oneGroupHasAllSites()\n
    '''
def hasCombinableAllRepairFacilities():
    '''returns boolean\n\n
    hasCombinableAllRepairFacilities()\n
    '''
def getOrgs():
    '''returns TreeSet<String>\n\n
    getOrgs()\n
    '''
def getOrgsString():
    '''returns String\n\n
    getOrgsString()\n
    '''
def getReadableSites():
    '''returns TreeSet<String>\n\n
    getReadableSites(final String app)\n
    '''
def getReadableSitesString():
    '''returns String\n\n
    getReadableSitesString(final String app)\n
    '''
def getReadableOrgs():
    '''returns TreeSet<String>\n\n
    getReadableOrgs(final String app)\n
    '''
def getReadableOrgsString():
    '''returns String\n\n
    getReadableOrgsString(final String app)\n
    '''
def isLaborAuthAll():
    '''returns boolean\n\n
    isLaborAuthAll()\n
    '''
def isAuthLaborSelf():
    '''returns boolean\n\n
    isAuthLaborSelf(final String orgid, final String laborcode)\n
    '''
def isAuthLaborSuper():
    '''returns boolean\n\n
    isAuthLaborSuper(final String orgid, final String laborcode)\n
    '''
def isAuthLaborCrew():
    '''returns boolean\n\n
    isAuthLaborCrew(final String orgid, final String laborcode)\n
    '''
def isAuthLaborGroup():
    '''returns boolean\n\n
    isAuthLaborGroup(final String orgid, final String laborcode)\n
    '''
def getLaborAuth():
    '''returns boolean\n\n
    getLaborAuth(final String orgid, final String laborcode)\n
    '''
def getLaborCodes():
    '''returns String\n\n
    getLaborCodes(final String orgid)\n
    '''
def dumpLaborAuth():
    '''returns ArrayList<String>\n\n
    dumpLaborAuth(final String tempUserid)\n
    '''
def getRoleRestrictions():
    '''returns HashMap\n\n
    getRoleRestrictions(final String entityname)\n
    getRoleRestrictions()\n
    '''
def dumpRoleRestrictions():
    '''returns ArrayList\n\n
    dumpRoleRestrictions()\n
    '''
def getNonStandardSiteOrgs():
    '''returns HashSet<String>\n\n
    getNonStandardSiteOrgs(final String app, final boolean getSites)\n
    '''
def getNonStandardApps():
    '''returns HashMap\n\n
    getNonStandardApps()\n
    '''
def getNonStandardAppOptionAuth():
    '''returns boolean\n\n
    getNonStandardAppOptionAuth(String app, String optionname, final String orgid, final String siteid)\n
    '''
def dumpNonStandardApps():
    '''returns ArrayList<String>\n\n
    dumpNonStandardApps()\n
    '''
def getDefaultSite():
    '''returns String\n\n
    getDefaultSite()\n
    '''
def setDefaultSite():
    '''returns None\n\n
    setDefaultSite(final String site)\n
    '''
def getDefaultOrg():
    '''returns String\n\n
    getDefaultOrg()\n
    '''
def setDefaultOrg():
    '''returns None\n\n
    setDefaultOrg(final String org)\n
    '''
def getInsertSite():
    '''returns String\n\n
    getInsertSite()\n
    '''
def getInsertOrg():
    '''returns String\n\n
    getInsertOrg()\n
    '''
def setInsertOrg():
    '''returns None\n\n
    setInsertOrg(String org)\n
    '''
def setInsertSite():
    '''returns None\n\n
    setInsertSite(String site)\n
    '''
def getDefaultRepairFacility():
    '''returns String\n\n
    getDefaultRepairFacility()\n
    '''
def getDefaultRepairFacilitySite():
    '''returns String\n\n
    getDefaultRepairFacilitySite()\n
    '''
def setInsertItemSet():
    '''returns None\n\n
    setInsertItemSet(final String setid)\n
    '''
def getInsertItemSet():
    '''returns String\n\n
    getInsertItemSet()\n
    '''
def setInsertCompanySet():
    '''returns None\n\n
    setInsertCompanySet(final String setid)\n
    '''
def getInsertCompanySet():
    '''returns String\n\n
    getInsertCompanySet()\n
    '''
def getQueryWithSite():
    '''returns boolean\n\n
    getQueryWithSite()\n
    '''
def getDefaultStoreroom():
    '''returns String\n\n
    getDefaultStoreroom()\n
    '''
def getDefaultStoreroomSite():
    '''returns String\n\n
    getDefaultStoreroomSite()\n
    '''
def setUserStatus():
    '''returns None\n\n
    setUserStatus(final String newInternalStatus)\n
    '''
def getLogout():
    '''returns boolean\n\n
    getLogout()\n
    '''
def getUserStatus():
    '''returns String\n\n
    getUserStatus()\n
    '''
def useDataRestriction():
    '''returns boolean\n\n
    useDataRestriction(final String groupname, final String app, final String siteorg)\n
    '''
def allCollectionsAllowed():
    '''returns boolean\n\n
    allCollectionsAllowed()\n
    '''
def getCollections():
    '''returns HashSet<String>\n\n
    getCollections()\n
    '''
def hasCombinableNullRepairFacilities():
    '''returns boolean\n\n
    hasCombinableNullRepairFacilities()\n
    '''
def getCombinableSites():
    '''returns HashSet<String>\n\n
    getCombinableSites()\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Remote proxy)\n
    '''
def getProxy():
    '''returns Remote\n\n
    getProxy()\n
    '''
def getReportLimit():
    '''returns Integer\n\n
    getReportLimit(final String attributeName)\n
    '''
