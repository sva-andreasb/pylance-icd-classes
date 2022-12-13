def PMService():
    '''    public PMService()
    public PMService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def genPMsFromMasterAsset():
    '''    public PMSetRemote genPMsFromMasterAsset(final AssetRemote myAssetMbo)
    '''
def initCriteriaList():
    '''    public void initCriteriaList(final Hashtable criteriaTable)
    '''
def generateWork():
    '''    public PMSetRemote generateWork(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime)
    '''
def generateWorkNoPMSetReturn():
    '''    public void generateWorkNoPMSetReturn(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime)
    public void generateWorkNoPMSetReturn(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime, final String repairFac, final String repSite, final boolean useAssetDef)
    '''
def meterBasedAutoWogen():
    '''    public void meterBasedAutoWogen(final MboRemote assetlocMbo, final MboRemote assetLocMeterMbo)
    public void meterBasedAutoWogen(final MboRemote assetlocMbo)
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("PM") final PM pm, final String status, final boolean rollToAllChildren)
    '''
def BackGroundWogen():
    '''    public BackGroundWogen(final MboSetRemote mboset, final MboSetRemote warningSet, final UserInfo uInfo, final String assetnum)
    public BackGroundWogen(final MboSetRemote mboset, final MboSetRemote warningSet, final UserInfo uInfo, final String assetnum, final MboRemote assetLocMeterMbo)
    '''
def run():
    '''    public void run()
    '''
