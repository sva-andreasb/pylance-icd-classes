batchSize = "int  200"
CCILINKDISGUID = "String  \"CCIAssetCIDISGUID\""
def getReconInfo():
    '''returns ReconInfo\n\n
    getReconInfo()\n
    '''
def setReconInfo():
    '''returns None\n\n
    setReconInfo(final ReconInfo reconInfo)\n
    '''
def ():
    '''returns LinkResult\n\n
    (final UserInfo userInfo)\n
    ()\n
    '''
def findAssetsForCIs():
    '''returns None\n\n
    findAssetsForCIs(final List<String> ciKeys)\n
    findAssetsForCIs(final MboSet ciMbos)\n
    findAssetsForCIs(final String filterCIs, final String filterAssets)\n
    '''
def findCIsForAssets():
    '''returns None\n\n
    findCIsForAssets(final List<String[]> assetKeys)\n
    findCIsForAssets(final MboSet assetMbos)\n
    findCIsForAssets(final String filterAssets, final String filterCIs)\n
    '''
def findAssetsForDeployedAssets():
    '''returns None\n\n
    findAssetsForDeployedAssets(final List<Long> dpaKeys)\n
    findAssetsForDeployedAssets(final MboSet dpaMbos)\n
    findAssetsForDeployedAssets(final String where)\n
    '''
def findCIsForActualCIs():
    '''returns None\n\n
    findCIsForActualCIs(final List<String> actCIKeys)\n
    findCIsForActualCIs(final MboSet actCIMbos)\n
    findCIsForActualCIs(final String where)\n
    '''
def findCIsForActualCIsByKey():
    '''returns None\n\n
    findCIsForActualCIsByKey(final String actCIKey)\n
    '''
def findCIsForAssetsViaRecon():
    '''returns None\n\n
    findCIsForAssetsViaRecon(final ReconInfo rInfo, final String ciFilter, final String assetFilter)\n
    '''
def getResults():
    '''returns List<LinkResult>\n\n
    getResults()\n
    '''
def getResultByCI():
    '''returns LinkResult\n\n
    getResultByCI(final String cinum)\n
    '''
def getResultByAsset():
    '''returns LinkResult\n\n
    getResultByAsset(final String assetnum, final String siteid)\n
    '''
def getResultByDPA():
    '''returns LinkResult\n\n
    getResultByDPA(final int nodeid)\n
    '''
def getResultByActCI():
    '''returns LinkResult\n\n
    getResultByActCI(final String actcinum)\n
    '''
def isSaveLinks():
    '''returns boolean\n\n
    isSaveLinks()\n
    '''
def setSaveLinks():
    '''returns None\n\n
    setSaveLinks(final boolean saveLinks)\n
    '''
def setTest():
    '''returns None\n\n
    setTest(final boolean test)\n
    '''
def getTestQueries():
    '''returns List<String>\n\n
    getTestQueries()\n
    '''
def gettestSaveWhere():
    '''returns List<String>\n\n
    gettestSaveWhere()\n
    '''
def getAssetnum():
    '''returns String\n\n
    getAssetnum()\n
    '''
def getOrgid():
    '''returns String\n\n
    getOrgid()\n
    '''
def getSiteid():
    '''returns String\n\n
    getSiteid()\n
    '''
def getCinum():
    '''returns String\n\n
    getCinum()\n
    '''
def getNodeid():
    '''returns String\n\n
    getNodeid()\n
    '''
def getActcinum():
    '''returns String\n\n
    getActcinum()\n
    '''
def getDisguid():
    '''returns String\n\n
    getDisguid()\n
    '''
def getLinkRule():
    '''returns String\n\n
    getLinkRule()\n
    '''
def getConflictAssetnum():
    '''returns String\n\n
    getConflictAssetnum()\n
    '''
def getConflictSiteid():
    '''returns String\n\n
    getConflictSiteid()\n
    '''
def getConflictCinum():
    '''returns String\n\n
    getConflictCinum()\n
    '''
def getConflictNodeid():
    '''returns String\n\n
    getConflictNodeid()\n
    '''
def isSaveFailed():
    '''returns boolean\n\n
    isSaveFailed()\n
    '''
def isMultiLink():
    '''returns boolean\n\n
    isMultiLink()\n
    '''
def setSaveFailed():
    '''returns None\n\n
    setSaveFailed(final boolean saveFailed)\n
    '''
