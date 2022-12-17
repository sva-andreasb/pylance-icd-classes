PLUSCASSETSTATUS = "String  \"PLUSCASSETSTATUS\""
def ():
    '''returns AssetSet\n\n
    (final MboServerInterface ms)\n
    '''
def moveAsset():
    '''returns None\n\n
    moveAsset()\n
    '''
def moveSingleAsset():
    '''returns None\n\n
    moveSingleAsset(Asset asset)\n
    '''
def findTopLevel():
    '''returns None\n\n
    findTopLevel()\n
    '''
def findAssetsAtLocation():
    '''returns None\n\n
    findAssetsAtLocation(final String location)\n
    '''
def findAsset():
    '''returns None\n\n
    findAsset(final String asset)\n
    '''
def findSelectedAssets():
    '''returns None\n\n
    findSelectedAssets(final String where)\n
    '''
def findNotDecommissionedAssets():
    '''returns None\n\n
    findNotDecommissionedAssets()\n
    '''
def findNotMovedAssets():
    '''returns None\n\n
    findNotMovedAssets()\n
    '''
def setLocsystem():
    '''returns None\n\n
    setLocsystem(final String locationSystem)\n
    '''
def setLocgroup():
    '''returns None\n\n
    setLocgroup(final Vector locationGroup)\n
    '''
def getLocsystem():
    '''returns String\n\n
    getLocsystem()\n
    '''
def getLocgroup():
    '''returns String\n\n
    getLocgroup()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
    '''
def findAssetAtLocation():
    '''returns None\n\n
    findAssetAtLocation(final String location)\n
    '''
def setMoveAssetPageFlag():
    '''returns None\n\n
    setMoveAssetPageFlag(final boolean flag)\n
    '''
def getMoveAssetPageFlag():
    '''returns boolean\n\n
    getMoveAssetPageFlag()\n
    '''
def setSwapAssetPageFlag():
    '''returns None\n\n
    setSwapAssetPageFlag(final boolean flag)\n
    '''
def getSwapAssetPageFlag():
    '''returns boolean\n\n
    getSwapAssetPageFlag()\n
    '''
def setWoNumAssetSetMv():
    '''returns None\n\n
    setWoNumAssetSetMv(final String setWonum)\n
    '''
def setPoNumAssetSetMv():
    '''returns None\n\n
    setPoNumAssetSetMv(final String setPoNum)\n
    '''
def setPoSiteIdAssetSetMv():
    '''returns None\n\n
    setPoSiteIdAssetSetMv(final String setPoSiteId)\n
    '''
def applyAssetMoveDefaults():
    '''returns None\n\n
    applyAssetMoveDefaults(final AssetMoveDfltSetRemote assetMoveDfltSet, final String applytype)\n
    '''
def applyAssetUserCustDefaults():
    '''returns None\n\n
    applyAssetUserCustDefaults(final AssetUserCusDfltSetRemote assetUserCusDfltSet)\n
    '''
def applyAssetModifyDefaults():
    '''returns None\n\n
    applyAssetModifyDefaults(final AssetModifyDfltSetRemote assetModifyDfltSet)\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getParent():
    '''returns MboValueData[]\n\n
    getParent(final String object, final String key, final String[] attrs)\n
    '''
def getSiblings():
    '''returns MboValueData[][]\n\n
    getSiblings(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getTop():
    '''returns MboValueData[][]\n\n
    getTop(final String[] attrs, final int maxRows)\n
    '''
def getUniqueIDValue():
    '''returns MboValueData\n\n
    getUniqueIDValue(final String object, final String[] attributes, final String[] values)\n
    '''
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def zeroCosts():
    '''returns None\n\n
    zeroCosts(final boolean ytd, final boolean total)\n
    '''
def addAssetsToCollectDetails():
    '''returns None\n\n
    addAssetsToCollectDetails(final String collectionNum)\n
    '''
def setItemMbo():
    '''returns None\n\n
    setItemMbo(final MboRemote item)\n
    '''
def setItemOrgInfo():
    '''returns None\n\n
    setItemOrgInfo(final MboRemote itemOrgInfo)\n
    '''
def getItemMbo():
    '''returns MboRemote\n\n
    getItemMbo()\n
    '''
def getItemOrgInfo():
    '''returns MboRemote\n\n
    getItemOrgInfo()\n
    '''
def inventoryLocationHasChecked():
    '''returns None\n\n
    inventoryLocationHasChecked(final String location, final String siteid)\n
    '''
def toCheckInventoryLocation():
    '''returns boolean\n\n
    toCheckInventoryLocation()\n
    '''
def setAssetForSpecifications():
    '''returns None\n\n
    setAssetForSpecifications(final MboRemote asseet)\n
    '''
def getAssetForSpecifications():
    '''returns MboRemote\n\n
    getAssetForSpecifications()\n
    '''
def storeAssetsInMultiAssetLocCISet():
    '''returns None\n\n
    storeAssetsInMultiAssetLocCISet(final MboSetRemote malcSet)\n
    '''
def isInMassMoveLocation():
    '''returns boolean\n\n
    isInMassMoveLocation()\n
    '''
def inMassMoveNewLocationMbo():
    '''returns MboRemote\n\n
    inMassMoveNewLocationMbo()\n
    '''
def filterByLinearAsset():
    '''returns None\n\n
    filterByLinearAsset(final MboSetRemote fltrSet)\n
    '''
def getSqlForFiltering():
    '''returns String\n\n
    getSqlForFiltering(final MboSetRemote fltrSet)\n
    '''
def getOriginalAssetQbe():
    '''returns Hashtable\n\n
    getOriginalAssetQbe()\n
    '''
def getOriginalAssetUserWhere():
    '''returns String\n\n
    getOriginalAssetUserWhere()\n
    '''
def setOriginalAssetUserWhere():
    '''returns None\n\n
    setOriginalAssetUserWhere(final String inWhere)\n
    '''
def setOriginalAssetQbe():
    '''returns None\n\n
    setOriginalAssetQbe(final Hashtable inQbe)\n
    '''
def applyAssetPersonGroupDefaults():
    '''returns None\n\n
    applyAssetPersonGroupDefaults(final AssetGrpDfltSetRemote personGroupDefaults)\n
    '''
def addAssetOpSKD():
    '''returns None\n\n
    addAssetOpSKD(final MboSetRemote npAssetOpSKDSet)\n
    '''
def addAssetMntSKD():
    '''returns None\n\n
    addAssetMntSKD(final MboSetRemote npAssetOpSKDSet)\n
    '''
def addWorkZones():
    '''returns None\n\n
    addWorkZones(final String workzone, final String type, final String orgid)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)\n
    '''
def getMaxAppsWhere():
    '''returns String\n\n
    getMaxAppsWhere()\n
    '''
