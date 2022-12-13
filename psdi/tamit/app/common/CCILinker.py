batchSize = "int  200"
CCILINKDISGUID = "String  CCIAssetCIDISGUID""
def getReconInfo():
'''public ReconInfo getReconInfo()
'''
pass
def setReconInfo():
'''public void setReconInfo(final ReconInfo reconInfo)
'''
pass
def CCILinker():
'''public CCILinker(final UserInfo userInfo)
'''
pass
def findAssetsForCIs():
'''public void findAssetsForCIs(final List<String> ciKeys)
public void findAssetsForCIs(final MboSet ciMbos)
public void findAssetsForCIs(final String filterCIs, final String filterAssets)
'''
pass
def findCIsForAssets():
'''public void findCIsForAssets(final List<String[]> assetKeys)
public void findCIsForAssets(final MboSet assetMbos)
public void findCIsForAssets(final String filterAssets, final String filterCIs)
'''
pass
def findAssetsForDeployedAssets():
'''public void findAssetsForDeployedAssets(final List<Long> dpaKeys)
public void findAssetsForDeployedAssets(final MboSet dpaMbos)
public void findAssetsForDeployedAssets(final String where)
'''
pass
def findCIsForActualCIs():
'''public void findCIsForActualCIs(final List<String> actCIKeys)
public void findCIsForActualCIs(final MboSet actCIMbos)
public void findCIsForActualCIs(final String where)
'''
pass
def findCIsForActualCIsByKey():
'''public void findCIsForActualCIsByKey(final String actCIKey)
'''
pass
def findCIsForAssetsViaRecon():
'''public void findCIsForAssetsViaRecon(final ReconInfo rInfo, final String ciFilter, final String assetFilter)
'''
pass
def getResults():
'''public List<LinkResult> getResults()
'''
pass
def getResultByCI():
'''public LinkResult getResultByCI(final String cinum)
'''
pass
def getResultByAsset():
'''public LinkResult getResultByAsset(final String assetnum, final String siteid)
'''
pass
def getResultByDPA():
'''public LinkResult getResultByDPA(final int nodeid)
'''
pass
def getResultByActCI():
'''public LinkResult getResultByActCI(final String actcinum)
'''
pass
def isSaveLinks():
'''public boolean isSaveLinks()
'''
pass
def setSaveLinks():
'''public void setSaveLinks(final boolean saveLinks)
'''
pass
def setTest():
'''public void setTest(final boolean test)
'''
pass
def getTestQueries():
'''public List<String> getTestQueries()
'''
pass
def gettestSaveWhere():
'''public List<String> gettestSaveWhere()
'''
pass
def LinkResult():
'''public LinkResult()
'''
pass
def getAssetnum():
'''public String getAssetnum()
'''
pass
def getOrgid():
'''public String getOrgid()
'''
pass
def getSiteid():
'''public String getSiteid()
'''
pass
def getCinum():
'''public String getCinum()
'''
pass
def getNodeid():
'''public String getNodeid()
'''
pass
def getActcinum():
'''public String getActcinum()
'''
pass
def getDisguid():
'''public String getDisguid()
'''
pass
def getLinkRule():
'''public String getLinkRule()
'''
pass
def getConflictAssetnum():
'''public String getConflictAssetnum()
'''
pass
def getConflictSiteid():
'''public String getConflictSiteid()
'''
pass
def getConflictCinum():
'''public String getConflictCinum()
'''
pass
def getConflictNodeid():
'''public String getConflictNodeid()
'''
pass
def isSaveFailed():
'''public boolean isSaveFailed()
'''
pass
def isMultiLink():
'''public boolean isMultiLink()
'''
pass
def setSaveFailed():
'''public void setSaveFailed(final boolean saveFailed)
'''
pass
