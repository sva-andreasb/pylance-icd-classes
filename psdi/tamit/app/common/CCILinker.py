batchSize = "int  200"
CCILINKDISGUID = "String  \"CCIAssetCIDISGUID\""
def getReconInfo():
    '''public ReconInfo getReconInfo()
    '''
def setReconInfo():
    '''public void setReconInfo(final ReconInfo reconInfo)
    '''
def CCILinker():
    '''public CCILinker(final UserInfo userInfo)
    '''
def findAssetsForCIs():
    '''public void findAssetsForCIs(final List<String> ciKeys)
    public void findAssetsForCIs(final MboSet ciMbos)
    public void findAssetsForCIs(final String filterCIs, final String filterAssets)
    '''
def findCIsForAssets():
    '''public void findCIsForAssets(final List<String[]> assetKeys)
    public void findCIsForAssets(final MboSet assetMbos)
    public void findCIsForAssets(final String filterAssets, final String filterCIs)
    '''
def findAssetsForDeployedAssets():
    '''public void findAssetsForDeployedAssets(final List<Long> dpaKeys)
    public void findAssetsForDeployedAssets(final MboSet dpaMbos)
    public void findAssetsForDeployedAssets(final String where)
    '''
def findCIsForActualCIs():
    '''public void findCIsForActualCIs(final List<String> actCIKeys)
    public void findCIsForActualCIs(final MboSet actCIMbos)
    public void findCIsForActualCIs(final String where)
    '''
def findCIsForActualCIsByKey():
    '''public void findCIsForActualCIsByKey(final String actCIKey)
    '''
def findCIsForAssetsViaRecon():
    '''public void findCIsForAssetsViaRecon(final ReconInfo rInfo, final String ciFilter, final String assetFilter)
    '''
def getResults():
    '''public List<LinkResult> getResults()
    '''
def getResultByCI():
    '''public LinkResult getResultByCI(final String cinum)
    '''
def getResultByAsset():
    '''public LinkResult getResultByAsset(final String assetnum, final String siteid)
    '''
def getResultByDPA():
    '''public LinkResult getResultByDPA(final int nodeid)
    '''
def getResultByActCI():
    '''public LinkResult getResultByActCI(final String actcinum)
    '''
def isSaveLinks():
    '''public boolean isSaveLinks()
    '''
def setSaveLinks():
    '''public void setSaveLinks(final boolean saveLinks)
    '''
def setTest():
    '''public void setTest(final boolean test)
    '''
def getTestQueries():
    '''public List<String> getTestQueries()
    '''
def gettestSaveWhere():
    '''public List<String> gettestSaveWhere()
    '''
def LinkResult():
    '''public LinkResult()
    '''
def getAssetnum():
    '''public String getAssetnum()
    '''
def getOrgid():
    '''public String getOrgid()
    '''
def getSiteid():
    '''public String getSiteid()
    '''
def getCinum():
    '''public String getCinum()
    '''
def getNodeid():
    '''public String getNodeid()
    '''
def getActcinum():
    '''public String getActcinum()
    '''
def getDisguid():
    '''public String getDisguid()
    '''
def getLinkRule():
    '''public String getLinkRule()
    '''
def getConflictAssetnum():
    '''public String getConflictAssetnum()
    '''
def getConflictSiteid():
    '''public String getConflictSiteid()
    '''
def getConflictCinum():
    '''public String getConflictCinum()
    '''
def getConflictNodeid():
    '''public String getConflictNodeid()
    '''
def isSaveFailed():
    '''public boolean isSaveFailed()
    '''
def isMultiLink():
    '''public boolean isMultiLink()
    '''
def setSaveFailed():
    '''public void setSaveFailed(final boolean saveFailed)
    '''
