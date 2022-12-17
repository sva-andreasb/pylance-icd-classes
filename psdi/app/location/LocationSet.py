def ():
    '''returns LocationSet\n\n
    (final MboServerInterface ms)\n
    '''
def findTopLevel():
    '''returns None\n\n
    findTopLevel()\n
    findTopLevel(final String locSiteId)\n
    '''
def getTop():
    '''returns MboValueData[][]\n\n
    getTop(final String[] attrs, final int maxRows)\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getSiblings():
    '''returns MboValueData[][]\n\n
    getSiblings(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getParent():
    '''returns MboValueData[]\n\n
    getParent(final String object, final String key, final String[] attrs)\n
    '''
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def setPathToTopCalledByControl():
    '''returns None\n\n
    setPathToTopCalledByControl(final boolean wasByControl)\n
    '''
def setHierarchy():
    '''returns None\n\n
    setHierarchy(final String hierarchy)\n
    setHierarchy(final String object, final String key, final String hierarchy)\n
    '''
def getUniqueIDValue():
    '''returns MboValueData\n\n
    getUniqueIDValue(final String object, final String[] attributes, final String[] values)\n
    '''
def getAllHierarchies():
    '''returns MboValueData[][]\n\n
    getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def findTopLocationsAtSystem():
    '''returns None\n\n
    findTopLocationsAtSystem(final String system)\n
    '''
def findLocation():
    '''returns None\n\n
    findLocation(final String location)\n
    '''
def getAllLocationTypes():
    '''returns Vector\n\n
    getAllLocationTypes(final boolean internalVals)\n
    '''
def findSelectedLocs():
    '''returns None\n\n
    findSelectedLocs(final String where)\n
    '''
def findStoreRooms():
    '''returns None\n\n
    findStoreRooms()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
    '''
def setStoreroom():
    '''returns None\n\n
    setStoreroom()\n
    '''
def setNonStoreroom():
    '''returns None\n\n
    setNonStoreroom()\n
    '''
def getDataList():
    '''returns String[][]\n\n
    getDataList(final String[] attributes, final int overFlowValue, final MboRemote parent)\n
    getDataList(final String[] attributes, final int overFlowValue, final MboRemote parent, final String locSiteId)\n
    '''
def filterLocSet():
    '''returns None\n\n
    filterLocSet(final String locSiteId)\n
    '''
def setDrilldownFlag():
    '''returns None\n\n
    setDrilldownFlag()\n
    '''
def applyLocationModifyDefaults():
    '''returns None\n\n
    applyLocationModifyDefaults(final AssetModifyDfltSetRemote assetModifyDfltSet)\n
    '''
def setItemForAddToStore():
    '''returns None\n\n
    setItemForAddToStore(final MboRemote item)\n
    '''
def getItemForAddToStore():
    '''returns MboRemote\n\n
    getItemForAddToStore()\n
    '''
def getSqlForAuthorizedStorerooms():
    '''returns String\n\n
    getSqlForAuthorizedStorerooms()\n
    '''
def authorizedStoreRoomSet():
    '''returns None\n\n
    authorizedStoreRoomSet()\n
    '''
def getMultiSiteWhere():
    '''returns String\n\n
    getMultiSiteWhere()\n
    '''
def getRoleRestrictionWhere():
    '''returns String\n\n
    getRoleRestrictionWhere()\n
    '''
def addAtIndex():
    '''returns MboRemote\n\n
    addAtIndex(final long accessModifier, final int ind)\n
    '''
def addLocationOpSKD():
    '''returns None\n\n
    addLocationOpSKD(final MboSetRemote npLocationOpSKDSet)\n
    '''
def addLocationMntSKD():
    '''returns None\n\n
    addLocationMntSKD(final MboSetRemote npLocationOpSKDSet)\n
    '''
def addWorkZones():
    '''returns None\n\n
    addWorkZones(final String workzone, final String type, final String orgid)\n
    '''
def addReorderStorelocUpdatedWarning():
    '''returns None\n\n
    addReorderStorelocUpdatedWarning()\n
    '''
