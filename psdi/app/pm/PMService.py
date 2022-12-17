def ():
    '''returns BackGroundWogen\n\n
    ()\n
    (final MXServer mxServer)\n
    (final MboSetRemote mboset, final MboSetRemote warningSet, final UserInfo uInfo, final String assetnum)\n
    (final MboSetRemote mboset, final MboSetRemote warningSet, final UserInfo uInfo, final String assetnum, final MboRemote assetLocMeterMbo)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def genPMsFromMasterAsset():
    '''returns PMSetRemote\n\n
    genPMsFromMasterAsset(final AssetRemote myAssetMbo)\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def generateWork():
    '''returns PMSetRemote\n\n
    generateWork(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime)\n
    '''
def generateWorkNoPMSetReturn():
    '''returns None\n\n
    generateWorkNoPMSetReturn(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime)\n
    generateWorkNoPMSetReturn(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime, final String repairFac, final String repSite, final boolean useAssetDef)\n
    '''
def meterBasedAutoWogen():
    '''returns None\n\n
    meterBasedAutoWogen(final MboRemote assetlocMbo, final MboRemote assetLocMeterMbo)\n
    meterBasedAutoWogen(final MboRemote assetlocMbo)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("PM") final PM pm, final String status, final boolean rollToAllChildren)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
