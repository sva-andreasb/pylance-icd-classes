def LocationSet():
    '''public LocationSet(final MboServerInterface ms)
    '''
def findTopLevel():
    '''public void findTopLevel()
    public void findTopLevel(final String locSiteId)
    '''
def getTop():
    '''public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getChildren():
    '''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getSiblings():
    '''public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getParent():
    '''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    '''
def getPathToTop():
    '''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def setPathToTopCalledByControl():
    '''public void setPathToTopCalledByControl(final boolean wasByControl)
    '''
def setHierarchy():
    '''public void setHierarchy(final String hierarchy)
    public void setHierarchy(final String object, final String key, final String hierarchy)
    '''
def getUniqueIDValue():
    '''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
def getAllHierarchies():
    '''public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def findTopLocationsAtSystem():
    '''public void findTopLocationsAtSystem(final String system)
    '''
def findLocation():
    '''public void findLocation(final String location)
    '''
def getAllLocationTypes():
    '''public Vector getAllLocationTypes(final boolean internalVals)
    '''
def findSelectedLocs():
    '''public void findSelectedLocs(final String where)
    '''
def findStoreRooms():
    '''public void findStoreRooms()
    '''
def getUserPrefWhere():
    '''public String getUserPrefWhere()
    '''
def setStoreroom():
    '''public void setStoreroom()
    '''
def setNonStoreroom():
    '''public void setNonStoreroom()
    '''
def getDataList():
    '''public String[][] getDataList(final String[] attributes, final int overFlowValue, final MboRemote parent)
    public String[][] getDataList(final String[] attributes, final int overFlowValue, final MboRemote parent, final String locSiteId)
    '''
def filterLocSet():
    '''public void filterLocSet(final String locSiteId)
    '''
def setDrilldownFlag():
    '''public void setDrilldownFlag()
    '''
def applyLocationModifyDefaults():
    '''public void applyLocationModifyDefaults(final AssetModifyDfltSetRemote assetModifyDfltSet)
    '''
def setItemForAddToStore():
    '''public void setItemForAddToStore(final MboRemote item)
    '''
def getItemForAddToStore():
    '''public MboRemote getItemForAddToStore()
    '''
def getSqlForAuthorizedStorerooms():
    '''public String getSqlForAuthorizedStorerooms()
    '''
def authorizedStoreRoomSet():
    '''public void authorizedStoreRoomSet()
    '''
def getMultiSiteWhere():
    '''public String getMultiSiteWhere()
    '''
def getRoleRestrictionWhere():
    '''public String getRoleRestrictionWhere()
    '''
def addAtIndex():
    '''public MboRemote addAtIndex(final long accessModifier, final int ind)
    '''
def addLocationOpSKD():
    '''public void addLocationOpSKD(final MboSetRemote npLocationOpSKDSet)
    '''
def addLocationMntSKD():
    '''public void addLocationMntSKD(final MboSetRemote npLocationOpSKDSet)
    '''
def addWorkZones():
    '''public void addWorkZones(final String workzone, final String type, final String orgid)
    '''
def addReorderStorelocUpdatedWarning():
    '''public void addReorderStorelocUpdatedWarning()
    '''
