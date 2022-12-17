def ():
    '''returns LocationService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def getStoreLocations():
    '''returns MboSetRemote\n\n
    getStoreLocations(final UserInfo userInfo)\n
    '''
def getDefaultStoreroom():
    '''returns String\n\n
    getDefaultStoreroom(final UserInfo userInfo)\n
    '''
def getDefaultStoreroomForSite():
    '''returns String\n\n
    getDefaultStoreroomForSite(final UserInfo userInfo, final String siteId)\n
    '''
def canAddItemsToStoreroom():
    '''returns None\n\n
    canAddItemsToStoreroom(final UserInfo userInfo)\n
    '''
def getKitComponentsNotYetInStore():
    '''returns MboSetRemote\n\n
    getKitComponentsNotYetInStore(final UserInfo userInfo, final ItemRemote item, final String storeroom, final Hashtable defaultBins)\n
    getKitComponentsNotYetInStore(final UserInfo userInfo, final ItemRemote item, final String storeroom, final String siteId, final Hashtable defaultBins)\n
    '''
def addItemsToStoreroom():
    '''returns MboSetRemote\n\n
    addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final boolean addKitComponents, final MboRemote matrectrans)\n
    addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final boolean addKitComponents)\n
    addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final String siteId, final boolean addKitComponents)\n
    addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final MboRemote location, final boolean addKitComponents, final MboRemote matrectrans)\n
    '''
def addAnItemToStoreroom():
    '''returns MboRemote\n\n
    addAnItemToStoreroom(final UserInfo userInfo, final String itemnum, final String itemsetid, final String storeroom, final String siteid, final boolean istool, final String orderunit, final String issueunit, final Number curbal, final String dfltbin, final String costtype, final Number unitcost, final Number stdcost, final Number avgcost, final String lotnum, final boolean savenow, final Number orderqty, final Number deliverytime, final Number minlevel, final Number reorder, final Number ccf)\n
    '''
def addItemsToStoreroomBulk():
    '''returns MboSetRemote\n\n
    addItemsToStoreroomBulk(final UserInfo userInfo, final MboSetRemote itemSet, final MboSetRemote locationSet, final boolean addKitComponents, final MboRemote matrectrans)\n
    '''
def getUnauthItemSet():
    '''returns Vector\n\n
    getUnauthItemSet()\n
    '''
def warningsFromAddItemsToStore():
    '''returns None\n\n
    warningsFromAddItemsToStore()\n
    '''
def warningsFromNonStockedOrgs():
    '''returns None\n\n
    warningsFromNonStockedOrgs()\n
    '''
def getTopLevelinPrimarySystem():
    '''returns MboRemote\n\n
    getTopLevelinPrimarySystem(final UserInfo userInfo, final String siteid)\n
    '''
def getPrimarySystem():
    '''returns String\n\n
    getPrimarySystem(final UserInfo userInfo)\n
    getPrimarySystem(final UserInfo userInfo, String siteId)\n
    '''
def getPrimarySystemNoSite():
    '''returns String\n\n
    getPrimarySystemNoSite(final UserInfo userInfo)\n
    '''
def getAllSystemsNoSite():
    '''returns MboSetRemote\n\n
    getAllSystemsNoSite(final UserInfo userInfo)\n
    '''
def getTopLevelInSystem():
    '''returns MboRemote\n\n
    getTopLevelInSystem(final UserInfo userInfo, final String systemid, final String siteId)\n
    '''
def getAllSystems():
    '''returns MboSetRemote\n\n
    getAllSystems(final UserInfo userInfo, String siteId)\n
    '''
def getLocation():
    '''returns MboRemote\n\n
    getLocation(final UserInfo userInfo, final String attribute, final String key)\n
    getLocation(final UserInfo userInfo, final String attribute, final String key, final String siteid)\n
    '''
def setIsTool():
    '''returns None\n\n
    setIsTool(final boolean tool)\n
    '''
def getSystemsForSite():
    '''returns MboSetRemote\n\n
    getSystemsForSite(final UserInfo userInfo, final String siteId)\n
    '''
def getPrimarySystemForSite():
    '''returns MboRemote\n\n
    getPrimarySystemForSite(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet)\n
    getPrimarySystemForSite(final UserInfo userInfo, final String siteId)\n
    '''
def verifyLocSystemSiteHasOnePrimarySystem():
    '''returns boolean\n\n
    verifyLocSystemSiteHasOnePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet)\n
    verifyLocSystemSiteHasOnePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet, final Vector<String> allowSetToPrimary, final boolean skipOtherSitesPrimarySysVerification)\n
    '''
def allowDeletionOfRedundantLocSystemSitePrimarySystem():
    '''returns boolean\n\n
    allowDeletionOfRedundantLocSystemSitePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet, final MboRemote locSystemToBeDeleted)\n
    '''
def verifyAllLocSystemSitesHaveOnePrimarySystem():
    '''returns boolean\n\n
    verifyAllLocSystemSitesHaveOnePrimarySystem(final UserInfo userInfo, final MboSetRemote workingSet)\n
    verifyAllLocSystemSitesHaveOnePrimarySystem(final UserInfo userInfo, final MboSetRemote workingSet, final Vector<String> allowSetToPrimary, final boolean skipOtherSitesPrimarySysVerification)\n
    '''
def getNumberOfSystemsForSite():
    '''returns int\n\n
    getNumberOfSystemsForSite(final UserInfo userinfo, final String siteid, final MboSetRemote workingSet, final MboRemote locSystemToBeDeleted)\n
    getNumberOfSystemsForSite(final UserInfo userinfo, final String siteid)\n
    '''
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder(@WSMboKey("LOCATIONS") final MboRemote mbo, final String jpnum)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange(@WSMboKey("LOCATIONS") final MboRemote mbo, final String jpnum)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("LOCATIONS") final MboRemote mbo, final String status, final Date asOfDate, final String memo, final long accessModifier)\n
    '''
