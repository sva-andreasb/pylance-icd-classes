def PMService():
'''public PMService()
public PMService(final MXServer mxServer)
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
def genPMsFromMasterAsset():
'''public PMSetRemote genPMsFromMasterAsset(final AssetRemote myAssetMbo)
'''
pass
def initCriteriaList():
'''public void initCriteriaList(final Hashtable criteriaTable)
'''
pass
def generateWork():
'''public PMSetRemote generateWork(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime)
'''
pass
def generateWorkNoPMSetReturn():
'''public void generateWorkNoPMSetReturn(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime)
public void generateWorkNoPMSetReturn(final UserInfo ui, final Enumeration enumit, final boolean useFreq, final int leadtime, final String repairFac, final String repSite, final boolean useAssetDef)
'''
pass
def meterBasedAutoWogen():
'''public void meterBasedAutoWogen(final MboRemote assetlocMbo, final MboRemote assetLocMeterMbo)
public void meterBasedAutoWogen(final MboRemote assetlocMbo)
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("PM") final PM pm, final String status, final boolean rollToAllChildren)
'''
pass
def BackGroundWogen():
'''public BackGroundWogen(final MboSetRemote mboset, final MboSetRemote warningSet, final UserInfo uInfo, final String assetnum)
public BackGroundWogen(final MboSetRemote mboset, final MboSetRemote warningSet, final UserInfo uInfo, final String assetnum, final MboRemote assetLocMeterMbo)
'''
pass
def run():
'''public void run()
'''
pass
