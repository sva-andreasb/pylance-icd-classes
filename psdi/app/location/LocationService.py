def LocationService():
    '''public LocationService()
    public LocationService(final MXServer mxServer)
    '''
def init():
    '''public void init()
    '''
def destroy():
    '''public void destroy()
    '''
def restart():
    '''public void restart()
    '''
def initCriteriaList():
    '''public void initCriteriaList(final Hashtable criteriaTable)
    '''
def getStoreLocations():
    '''public MboSetRemote getStoreLocations(final UserInfo userInfo)
    '''
def getDefaultStoreroom():
    '''public String getDefaultStoreroom(final UserInfo userInfo)
    '''
def getDefaultStoreroomForSite():
    '''public String getDefaultStoreroomForSite(final UserInfo userInfo, final String siteId)
    '''
def canAddItemsToStoreroom():
    '''public void canAddItemsToStoreroom(final UserInfo userInfo)
    '''
def getKitComponentsNotYetInStore():
    '''public MboSetRemote getKitComponentsNotYetInStore(final UserInfo userInfo, final ItemRemote item, final String storeroom, final Hashtable defaultBins)
    public MboSetRemote getKitComponentsNotYetInStore(final UserInfo userInfo, final ItemRemote item, final String storeroom, final String siteId, final Hashtable defaultBins)
    '''
def addItemsToStoreroom():
    '''public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final boolean addKitComponents, final MboRemote matrectrans)
    public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final boolean addKitComponents)
    public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final String storeroom, final String siteId, final boolean addKitComponents)
    public MboSetRemote addItemsToStoreroom(final UserInfo userInfo, final MboSetRemote itemSet, final MboRemote location, final boolean addKitComponents, final MboRemote matrectrans)
    '''
def addAnItemToStoreroom():
    '''public MboRemote addAnItemToStoreroom(final UserInfo userInfo, final String itemnum, final String itemsetid, final String storeroom, final String siteid, final boolean istool, final String orderunit, final String issueunit, final Number curbal, final String dfltbin, final String costtype, final Number unitcost, final Number stdcost, final Number avgcost, final String lotnum, final boolean savenow, final Number orderqty, final Number deliverytime, final Number minlevel, final Number reorder, final Number ccf)
    '''
def addItemsToStoreroomBulk():
    '''public MboSetRemote addItemsToStoreroomBulk(final UserInfo userInfo, final MboSetRemote itemSet, final MboSetRemote locationSet, final boolean addKitComponents, final MboRemote matrectrans)
    '''
def getUnauthItemSet():
    '''public Vector getUnauthItemSet()
    '''
def warningsFromAddItemsToStore():
    '''public void warningsFromAddItemsToStore()
    '''
def warningsFromNonStockedOrgs():
    '''public void warningsFromNonStockedOrgs()
    '''
def getTopLevelinPrimarySystem():
    '''public MboRemote getTopLevelinPrimarySystem(final UserInfo userInfo, final String siteid)
    '''
def getPrimarySystem():
    '''public String getPrimarySystem(final UserInfo userInfo)
    public String getPrimarySystem(final UserInfo userInfo, String siteId)
    '''
def getPrimarySystemNoSite():
    '''public String getPrimarySystemNoSite(final UserInfo userInfo)
    '''
def getAllSystemsNoSite():
    '''public MboSetRemote getAllSystemsNoSite(final UserInfo userInfo)
    '''
def getTopLevelInSystem():
    '''public MboRemote getTopLevelInSystem(final UserInfo userInfo, final String systemid, final String siteId)
    '''
def getAllSystems():
    '''public MboSetRemote getAllSystems(final UserInfo userInfo, String siteId)
    '''
def getLocation():
    '''public MboRemote getLocation(final UserInfo userInfo, final String attribute, final String key)
    public MboRemote getLocation(final UserInfo userInfo, final String attribute, final String key, final String siteid)
    '''
def setIsTool():
    '''public void setIsTool(final boolean tool)
    '''
def getSystemsForSite():
    '''public MboSetRemote getSystemsForSite(final UserInfo userInfo, final String siteId)
    '''
def getPrimarySystemForSite():
    '''public MboRemote getPrimarySystemForSite(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet)
    public MboRemote getPrimarySystemForSite(final UserInfo userInfo, final String siteId)
    '''
def verifyLocSystemSiteHasOnePrimarySystem():
    '''public boolean verifyLocSystemSiteHasOnePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet)
    public boolean verifyLocSystemSiteHasOnePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet, final Vector<String> allowSetToPrimary, final boolean skipOtherSitesPrimarySysVerification)
    '''
def allowDeletionOfRedundantLocSystemSitePrimarySystem():
    '''public boolean allowDeletionOfRedundantLocSystemSitePrimarySystem(final UserInfo userInfo, final String siteId, final MboSetRemote workingSet, final MboRemote locSystemToBeDeleted)
    '''
def verifyAllLocSystemSitesHaveOnePrimarySystem():
    '''public boolean verifyAllLocSystemSitesHaveOnePrimarySystem(final UserInfo userInfo, final MboSetRemote workingSet)
    public boolean verifyAllLocSystemSitesHaveOnePrimarySystem(final UserInfo userInfo, final MboSetRemote workingSet, final Vector<String> allowSetToPrimary, final boolean skipOtherSitesPrimarySysVerification)
    '''
def getNumberOfSystemsForSite():
    '''public int getNumberOfSystemsForSite(final UserInfo userinfo, final String siteid, final MboSetRemote workingSet, final MboRemote locSystemToBeDeleted)
    public int getNumberOfSystemsForSite(final UserInfo userinfo, final String siteid)
    '''
def createWorkorder():
    '''public MboRemote createWorkorder(@WSMboKey("LOCATIONS") final MboRemote mbo, final String jpnum)
    '''
def createProblem():
    '''public MboRemote createProblem(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)
    '''
def createIncident():
    '''public MboRemote createIncident(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)
    '''
def createServiceRequest():
    '''public MboRemote createServiceRequest(@WSMboKey("LOCATIONS") final MboRemote mbo, final String tickettemplateid)
    '''
def createChange():
    '''public MboRemote createChange(@WSMboKey("LOCATIONS") final MboRemote mbo, final String jpnum)
    '''
def changeStatus():
    '''public void changeStatus(@WSMboKey("LOCATIONS") final MboRemote mbo, final String status, final Date asOfDate, final String memo, final long accessModifier)
    '''
