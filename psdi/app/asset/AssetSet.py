PLUSCASSETSTATUS = "String  \"PLUSCASSETSTATUS\""
def AssetSet():
    '''public AssetSet(final MboServerInterface ms)
    '''
def moveAsset():
    '''public void moveAsset()
    '''
def moveSingleAsset():
    '''public void moveSingleAsset(Asset asset)
    '''
def findTopLevel():
    '''public void findTopLevel()
    '''
def findAssetsAtLocation():
    '''public void findAssetsAtLocation(final String location)
    '''
def findAsset():
    '''public void findAsset(final String asset)
    '''
def findSelectedAssets():
    '''public void findSelectedAssets(final String where)
    '''
def findNotDecommissionedAssets():
    '''public void findNotDecommissionedAssets()
    '''
def findNotMovedAssets():
    '''public void findNotMovedAssets()
    '''
def setLocsystem():
    '''public void setLocsystem(final String locationSystem)
    '''
def setLocgroup():
    '''public void setLocgroup(final Vector locationGroup)
    '''
def getLocsystem():
    '''public String getLocsystem()
    '''
def getLocgroup():
    '''public String getLocgroup()
    '''
def getUserPrefWhere():
    '''public String getUserPrefWhere()
    '''
def findAssetAtLocation():
    '''public void findAssetAtLocation(final String location)
    '''
def setMoveAssetPageFlag():
    '''public void setMoveAssetPageFlag(final boolean flag)
    '''
def getMoveAssetPageFlag():
    '''public boolean getMoveAssetPageFlag()
    '''
def setSwapAssetPageFlag():
    '''public void setSwapAssetPageFlag(final boolean flag)
    '''
def getSwapAssetPageFlag():
    '''public boolean getSwapAssetPageFlag()
    '''
def setWoNumAssetSetMv():
    '''public void setWoNumAssetSetMv(final String setWonum)
    '''
def setPoNumAssetSetMv():
    '''public void setPoNumAssetSetMv(final String setPoNum)
    '''
def setPoSiteIdAssetSetMv():
    '''public void setPoSiteIdAssetSetMv(final String setPoSiteId)
    '''
def applyAssetMoveDefaults():
    '''public void applyAssetMoveDefaults(final AssetMoveDfltSetRemote assetMoveDfltSet, final String applytype)
    '''
def applyAssetUserCustDefaults():
    '''public void applyAssetUserCustDefaults(final AssetUserCusDfltSetRemote assetUserCusDfltSet)
    '''
def applyAssetModifyDefaults():
    '''public void applyAssetModifyDefaults(final AssetModifyDfltSetRemote assetModifyDfltSet)
    '''
def getChildren():
    '''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getParent():
    '''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    '''
def getSiblings():
    '''public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getTop():
    '''public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getUniqueIDValue():
    '''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
def getPathToTop():
    '''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def zeroCosts():
    '''public void zeroCosts(final boolean ytd, final boolean total)
    '''
def addAssetsToCollectDetails():
    '''public void addAssetsToCollectDetails(final String collectionNum)
    '''
def setItemMbo():
    '''public void setItemMbo(final MboRemote item)
    '''
def setItemOrgInfo():
    '''public void setItemOrgInfo(final MboRemote itemOrgInfo)
    '''
def getItemMbo():
    '''public MboRemote getItemMbo()
    '''
def getItemOrgInfo():
    '''public MboRemote getItemOrgInfo()
    '''
def inventoryLocationHasChecked():
    '''public void inventoryLocationHasChecked(final String location, final String siteid)
    '''
def toCheckInventoryLocation():
    '''public boolean toCheckInventoryLocation()
    '''
def setAssetForSpecifications():
    '''public void setAssetForSpecifications(final MboRemote asseet)
    '''
def getAssetForSpecifications():
    '''public MboRemote getAssetForSpecifications()
    '''
def storeAssetsInMultiAssetLocCISet():
    '''public void storeAssetsInMultiAssetLocCISet(final MboSetRemote malcSet)
    '''
def isInMassMoveLocation():
    '''public boolean isInMassMoveLocation()
    '''
def inMassMoveNewLocationMbo():
    '''public MboRemote inMassMoveNewLocationMbo()
    '''
def filterByLinearAsset():
    '''public void filterByLinearAsset(final MboSetRemote fltrSet)
    '''
def getSqlForFiltering():
    '''public String getSqlForFiltering(final MboSetRemote fltrSet)
    '''
def getOriginalAssetQbe():
    '''public Hashtable getOriginalAssetQbe()
    '''
def getOriginalAssetUserWhere():
    '''public String getOriginalAssetUserWhere()
    '''
def setOriginalAssetUserWhere():
    '''public void setOriginalAssetUserWhere(final String inWhere)
    '''
def setOriginalAssetQbe():
    '''public void setOriginalAssetQbe(final Hashtable inQbe)
    '''
def applyAssetPersonGroupDefaults():
    '''public void applyAssetPersonGroupDefaults(final AssetGrpDfltSetRemote personGroupDefaults)
    '''
def addAssetOpSKD():
    '''public void addAssetOpSKD(final MboSetRemote npAssetOpSKDSet)
    '''
def addAssetMntSKD():
    '''public void addAssetMntSKD(final MboSetRemote npAssetOpSKDSet)
    '''
def addWorkZones():
    '''public void addWorkZones(final String workzone, final String type, final String orgid)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)
    '''
def getMaxAppsWhere():
    '''public String getMaxAppsWhere()
    '''
