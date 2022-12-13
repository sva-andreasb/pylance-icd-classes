MAXPRIORITY = "int  999"
MAXMETERWEIGHTPRCNT = "int  100"
def AssetService():
    '''    public AssetService()
    public AssetService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def getAssetForLocation():
    '''    public String getAssetForLocation(final UserInfo userInfo, final String loc)
    '''
def getRotatingAssetForItem():
    '''    public MboSetRemote getRotatingAssetForItem(final UserInfo userInfo, final String itemnum, final String itemsetid)
    '''
def initCriteriaList():
    '''    public void initCriteriaList(final Hashtable criteriaTable)
    '''
def getAsset():
    '''    public MboRemote getAsset(final UserInfo userInfo, final String attribute, final String key)
    '''
def incrInvCost():
    '''    public synchronized void incrInvCost(final UserInfo userinfo, final String assetnum, final double invCost)
    '''
def moveSingleAsset():
    '''    public void moveSingleAsset(@WSMboKey("ASSET") final MboRemote asset, final String newLocation, final String newSite, final String newParent)
    '''
def setLinearInfo():
    '''    public void setLinearInfo(final MboRemote linearMbo, final String altAttr)
    '''
def setOffsetInfo():
    '''    public void setOffsetInfo(final MboRemote linearMbo, final String altAttr)
    '''
def initLinearAttrs():
    '''    public void initLinearAttrs(final MboRemote linearMbo, final String altAttr)
    public void initLinearAttrs(final MboRemote linearMbo)
    '''
def initLinearEndMeasureAttrs():
    '''    public void initLinearEndMeasureAttrs(final MboRemote linearMbo, final String altAttr)
    public void initLinearEndMeasureAttrs(final MboRemote linearMbo)
    '''
def setLinearMeasureUnitIdInfo():
    '''    public void setLinearMeasureUnitIdInfo(final MboRemote linearMbo, String attr)
    '''
def initOffsetAttrs():
    '''    public void initOffsetAttrs(final MboRemote linearMbo, final String attr)
    '''
def initEndMeasureAttrs():
    '''    public void initEndMeasureAttrs(final MboRemote linearMbo)
    '''
def initStartOffsetAttrs():
    '''    public void initStartOffsetAttrs(final MboRemote linearMbo, final String attr)
    '''
def initEndOffsetAttrs():
    '''    public void initEndOffsetAttrs(final MboRemote linearMbo, final String attr)
    '''
def setStartOffsetInfo():
    '''    public void setStartOffsetInfo(final MboRemote linearMbo, final String attr)
    '''
def setEndOffsetInfo():
    '''    public void setEndOffsetInfo(final MboRemote linearMbo, final String attr)
    '''
def getAssetsBeingMovedFromMultiAssetLocCI():
    '''    public Hashtable getAssetsBeingMovedFromMultiAssetLocCI()
    '''
def storeAssetsBeingMovedFromMultiAssetLocCI():
    '''    public void storeAssetsBeingMovedFromMultiAssetLocCI(final MboRemote asset)
    '''
def clearAssetsBeingMovedFromMultiAssetLocCI():
    '''    public void clearAssetsBeingMovedFromMultiAssetLocCI()
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("ASSET") final MboRemote mbo, final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)
    '''
def createWorkorder():
    '''    public MboRemote createWorkorder(@WSMboKey("ASSET") final MboRemote mbo, final String jpnum)
    '''
def createProblem():
    '''    public MboRemote createProblem(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)
    '''
def createIncident():
    '''    public MboRemote createIncident(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)
    '''
def createServiceRequest():
    '''    public MboRemote createServiceRequest(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)
    '''
def createChange():
    '''    public MboRemote createChange(@WSMboKey("ASSET") final MboRemote mbo, final String jpnum)
    '''
def hasActiveRoutes():
    '''    public boolean hasActiveRoutes(@WSMboKey("ASSET") final MboRemote mbo)
    '''
def hasActiveSP():
    '''    public boolean hasActiveSP(@WSMboKey("ASSET") final MboRemote mbo)
    '''
def hasActivePM():
    '''    public boolean hasActivePM(@WSMboKey("ASSET") final MboRemote mbo)
    '''
def uploadObservation():
    '''    public String uploadObservation(final OslcRequest request)
    '''
