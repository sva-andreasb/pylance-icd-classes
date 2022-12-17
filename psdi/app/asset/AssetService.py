MAXPRIORITY = "int  999"
MAXMETERWEIGHTPRCNT = "int  100"
def ():
    '''returns AssetService\n\n
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
def getAssetForLocation():
    '''returns String\n\n
    getAssetForLocation(final UserInfo userInfo, final String loc)\n
    '''
def getRotatingAssetForItem():
    '''returns MboSetRemote\n\n
    getRotatingAssetForItem(final UserInfo userInfo, final String itemnum, final String itemsetid)\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def getAsset():
    '''returns MboRemote\n\n
    getAsset(final UserInfo userInfo, final String attribute, final String key)\n
    '''
def moveSingleAsset():
    '''returns None\n\n
    moveSingleAsset(@WSMboKey("ASSET") final MboRemote asset, final String newLocation, final String newSite, final String newParent)\n
    '''
def setLinearInfo():
    '''returns None\n\n
    setLinearInfo(final MboRemote linearMbo, final String altAttr)\n
    '''
def setOffsetInfo():
    '''returns None\n\n
    setOffsetInfo(final MboRemote linearMbo, final String altAttr)\n
    '''
def initLinearAttrs():
    '''returns None\n\n
    initLinearAttrs(final MboRemote linearMbo, final String altAttr)\n
    initLinearAttrs(final MboRemote linearMbo)\n
    '''
def initLinearEndMeasureAttrs():
    '''returns None\n\n
    initLinearEndMeasureAttrs(final MboRemote linearMbo, final String altAttr)\n
    initLinearEndMeasureAttrs(final MboRemote linearMbo)\n
    '''
def setLinearMeasureUnitIdInfo():
    '''returns None\n\n
    setLinearMeasureUnitIdInfo(final MboRemote linearMbo, String attr)\n
    '''
def initOffsetAttrs():
    '''returns None\n\n
    initOffsetAttrs(final MboRemote linearMbo, final String attr)\n
    '''
def initEndMeasureAttrs():
    '''returns None\n\n
    initEndMeasureAttrs(final MboRemote linearMbo)\n
    '''
def initStartOffsetAttrs():
    '''returns None\n\n
    initStartOffsetAttrs(final MboRemote linearMbo, final String attr)\n
    '''
def initEndOffsetAttrs():
    '''returns None\n\n
    initEndOffsetAttrs(final MboRemote linearMbo, final String attr)\n
    '''
def setStartOffsetInfo():
    '''returns None\n\n
    setStartOffsetInfo(final MboRemote linearMbo, final String attr)\n
    '''
def setEndOffsetInfo():
    '''returns None\n\n
    setEndOffsetInfo(final MboRemote linearMbo, final String attr)\n
    '''
def getAssetsBeingMovedFromMultiAssetLocCI():
    '''returns Hashtable\n\n
    getAssetsBeingMovedFromMultiAssetLocCI()\n
    '''
def storeAssetsBeingMovedFromMultiAssetLocCI():
    '''returns None\n\n
    storeAssetsBeingMovedFromMultiAssetLocCI(final MboRemote asset)\n
    '''
def clearAssetsBeingMovedFromMultiAssetLocCI():
    '''returns None\n\n
    clearAssetsBeingMovedFromMultiAssetLocCI()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("ASSET") final MboRemote mbo, final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)\n
    '''
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder(@WSMboKey("ASSET") final MboRemote mbo, final String jpnum)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest(@WSMboKey("ASSET") final MboRemote mbo, final String tickettemplateid)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange(@WSMboKey("ASSET") final MboRemote mbo, final String jpnum)\n
    '''
def hasActiveRoutes():
    '''returns boolean\n\n
    hasActiveRoutes(@WSMboKey("ASSET") final MboRemote mbo)\n
    '''
def hasActiveSP():
    '''returns boolean\n\n
    hasActiveSP(@WSMboKey("ASSET") final MboRemote mbo)\n
    '''
def hasActivePM():
    '''returns boolean\n\n
    hasActivePM(@WSMboKey("ASSET") final MboRemote mbo)\n
    '''
def uploadObservation():
    '''returns String\n\n
    uploadObservation(final OslcRequest request)\n
    '''
