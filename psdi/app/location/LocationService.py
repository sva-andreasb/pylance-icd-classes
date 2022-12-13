def LocationService():
'''public LocationService()
public LocationService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def restart():
'''public void restart()
'''
pass
def initCriteriaList():
'''public void initCriteriaList(final Hashtable criteriaTable)
'''
pass
def getStoreLocations():
'''public MboSetRemote getStoreLocations(final UserInfo userInfo)
'''
pass
def getDefaultStoreroom():
'''public String getDefaultStoreroom(final UserInfo userInfo)
'''
pass
def getDefaultStoreroomForSite():
'''public String getDefaultStoreroomForSite(final UserInfo userInfo, final String siteId)
'''
pass
def canAddItemsToStoreroom():
'''public void canAddItemsToStoreroom(final UserInfo userInfo)
'''
pass
def getKitComponentsNotYetInStore():
'''public MboSetRemote getKitComponentsNotYetInStore(final UserInfo userInfo, final ItemRemote item, final String storeroom, final Hashtable defaultBins)
public MboSetRemote getKitComponentsNotYetInStore(final UserInfo userInfo, final ItemRemote item, final String storeroom, final String siteId, final Hashtable defaultBins)
'''
pass
def addItemsToStoreroom():
'''public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final boolean addKitComponents, final MboRemote matrectrans)
public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final boolean addKitComponents)
public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final String siteId, final boolean addKitComponents)
public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final MboRemote location, final boolean addKitComponents, final MboRemote matrectrans)
'''
pass
def addAnItemToStoreroom():
'''public MboRemote addAnItemToStoreroom(final UserInfo userInfo, final String itemnum, final String itemsetid, final String storeroom, final String siteid, final boolean istool, final String orderunit, final String issueunit, final Number curbal, final String dfltbin, final String costtype, final Number unitcost, final Number stdcost, final Number avgcost, final String lotnum, final boolean savenow, final Number orderqty, final Number deliverytime, final Number minlevel, final Number reorder, final Number ccf)
'''
pass
def addItemsToStoreroomBulk():
'''public MboSetRemote addItemsToStoreroomBulk(final UserInfo userInfo, final MboSetRemote itemSet, final MboSetRemote locationSet, final boolean addKitComponents, final MboRemote matrectrans)
'''
pass
def getUnauthItemSet():
'''public Vector getUnauthItemSet()
'''
pass
def warningsFromAddItemsToStore():
'''public void warningsFromAddItemsToStore()
'''
pass
def warningsFromNonStockedOrgs():
'''public void warningsFromNonStockedOrgs()
'''
pass
def getTopLevelinPrimarySystem():
'''public MboRemote getTopLevelinPrimarySystem(final UserInfo userInfo, final String siteid)
'''
pass
def getPrimarySystem():
'''public String getPrimarySystem(final UserInfo userInfo)
public String getPrimarySystem(final UserInfo userInfo, String siteId)
'''
pass
def getPrimarySystemNoSite():
'''public String getPrimarySystemNoSite(final UserInfo userInfo)
'''
pass
def getAllSystemsNoSite():
'''public MboSetRemote getAllSystemsNoSite(final UserInfo userInfo)
'''
pass
def getTopLevelInSystem():
'''public MboRemote getTopLevelInSystem(final UserInfo userInfo, final String systemid, final String siteId)
'''
pass
def getAllSystems():
'''public MboSetRemote getAllSystems(final UserInfo userInfo, String siteId)
'''
pass
def getLocation():
'''public MboRemote getLocation(final UserInfo userInfo, final String attribute, final String key)
public MboRemote getLocation(final UserInfo userInfo, final String attribute, final String key, final String siteid)
'''
pass
def setIsTool():
'''public void setIsTool(final boolean tool)
'''
pass
def getSystemsForSite():
'''public MboSetRemote getSystemsForSite(final UserInfo userInfo, final String siteId)
'''
pass
def getPrimarySystemForSite():
'''public MboRemote getPrimarySystemForSite(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet)
public MboRemote getPrimarySystemForSite(final UserInfo userInfo, final String siteId)
'''
pass
def verifyLocSystemSiteHasOnePrimarySystem():
'''public boolean verifyLocSystemSiteHasOnePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet)
public boolean verifyLocSystemSiteHasOnePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet, final Vector<String> allowSetToPrimary, final boolean skipOtherSitesPrimarySysVerification)
'''
pass
def allowDeletionOfRedundantLocSystemSitePrimarySystem():
'''public boolean allowDeletionOfRedundantLocSystemSitePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet, final MboRemote locSystemToBeDeleted)
'''
pass
def verifyAllLocSystemSitesHaveOnePrimarySystem():
'''public boolean verifyAllLocSystemSitesHaveOnePrimarySystem(final UserInfo userInfo, final MboSetRemote workingSet)
public boolean verifyAllLocSystemSitesHaveOnePrimarySystem(final UserInfo userInfo, final MboSetRemote workingSet, final Vector<String> allowSetToPrimary, final boolean skipOtherSitesPrimarySysVerification)
'''
pass
def getNumberOfSystemsForSite():
'''public int getNumberOfSystemsForSite(final UserInfo userinfo, final String siteid, final MboSetRemote workingSet, final MboRemote locSystemToBeDeleted)
public int getNumberOfSystemsForSite(final UserInfo userinfo, final String siteid)
'''
pass
def createWorkorder():
'''public MboRemote createWorkorder(@WSMboKey("LOCATIONS") final MboRemote mbo, final String jpnum)
'''
pass
def createProblem():
'''public MboRemote createProblem(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)
'''
pass
def createIncident():
'''public MboRemote createIncident(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)
'''
pass
def createServiceRequest():
'''public MboRemote createServiceRequest(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)
'''
pass
def createChange():
'''public MboRemote createChange(@WSMboKey("LOCATIONS") final MboRemote mbo, final String jpnum)
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("LOCATIONS") final MboRemote mbo, final String status, final Date asOfDate, final String memo, final long accessModifier)
'''
pass
