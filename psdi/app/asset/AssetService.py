MAXPRIORITY = "int  999"
MAXMETERWEIGHTPRCNT = "int  100"
def AssetService():
'''public AssetService()
public AssetService(final MXServer mxServer)
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
def getAssetForLocation():
'''public String getAssetForLocation(final UserInfo userInfo, final String loc)
'''
pass
def getRotatingAssetForItem():
'''public MboSetRemote getRotatingAssetForItem(final UserInfo userInfo, final String itemnum, final String itemsetid)
'''
pass
def initCriteriaList():
'''public void initCriteriaList(final Hashtable criteriaTable)
'''
pass
def getAsset():
'''public MboRemote getAsset(final UserInfo userInfo, final String attribute, final String key)
'''
pass
def incrInvCost():
'''public synchronized void incrInvCost(final UserInfo userinfo, final String assetnum, final double invCost)
'''
pass
def moveSingleAsset():
'''public void moveSingleAsset(@WSMboKey("ASSET") final MboRemote asset, final String newLocation, final String newSite, final String newParent)
'''
pass
def setLinearInfo():
'''public void setLinearInfo(final MboRemote linearMbo, final String altAttr)
'''
pass
def setOffsetInfo():
'''public void setOffsetInfo(final MboRemote linearMbo, final String altAttr)
'''
pass
def initLinearAttrs():
'''public void initLinearAttrs(final MboRemote linearMbo, final String altAttr)
public void initLinearAttrs(final MboRemote linearMbo)
'''
pass
def initLinearEndMeasureAttrs():
'''public void initLinearEndMeasureAttrs(final MboRemote linearMbo, final String altAttr)
public void initLinearEndMeasureAttrs(final MboRemote linearMbo)
'''
pass
def setLinearMeasureUnitIdInfo():
'''public void setLinearMeasureUnitIdInfo(final MboRemote linearMbo, String attr)
'''
pass
def initOffsetAttrs():
'''public void initOffsetAttrs(final MboRemote linearMbo, final String attr)
'''
pass
def initEndMeasureAttrs():
'''public void initEndMeasureAttrs(final MboRemote linearMbo)
'''
pass
def initStartOffsetAttrs():
'''public void initStartOffsetAttrs(final MboRemote linearMbo, final String attr)
'''
pass
def initEndOffsetAttrs():
'''public void initEndOffsetAttrs(final MboRemote linearMbo, final String attr)
'''
pass
def setStartOffsetInfo():
'''public void setStartOffsetInfo(final MboRemote linearMbo, final String attr)
'''
pass
def setEndOffsetInfo():
'''public void setEndOffsetInfo(final MboRemote linearMbo, final String attr)
'''
pass
def getAssetsBeingMovedFromMultiAssetLocCI():
'''public Hashtable getAssetsBeingMovedFromMultiAssetLocCI()
'''
pass
def storeAssetsBeingMovedFromMultiAssetLocCI():
'''public void storeAssetsBeingMovedFromMultiAssetLocCI(final MboRemote asset)
'''
pass
def clearAssetsBeingMovedFromMultiAssetLocCI():
'''public void clearAssetsBeingMovedFromMultiAssetLocCI()
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("ASSET") final MboRemote mbo, final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)
'''
pass
def createWorkorder():
'''public MboRemote createWorkorder(@WSMboKey("ASSET") final MboRemote mbo, final String jpnum)
'''
pass
def createProblem():
'''public MboRemote createProblem(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)
'''
pass
def createIncident():
'''public MboRemote createIncident(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)
'''
pass
def createServiceRequest():
'''public MboRemote createServiceRequest(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)
'''
pass
def createChange():
'''public MboRemote createChange(@WSMboKey("ASSET") final MboRemote mbo, final String jpnum)
'''
pass
def hasActiveRoutes():
'''public boolean hasActiveRoutes(@WSMboKey("ASSET") final MboRemote mbo)
'''
pass
def hasActiveSP():
'''public boolean hasActiveSP(@WSMboKey("ASSET") final MboRemote mbo)
'''
pass
def hasActivePM():
'''public boolean hasActivePM(@WSMboKey("ASSET") final MboRemote mbo)
'''
pass
def uploadObservation():
'''public String uploadObservation(final OslcRequest request)
'''
pass
