def LocationSet():
'''public LocationSet(final MboServerInterface ms)
'''
pass
def findTopLevel():
'''public void findTopLevel()
public void findTopLevel(final String locSiteId)
'''
pass
def getTop():
'''public MboValueData[][] getTop(final String[] attrs, final int maxRows)
'''
pass
def getChildren():
'''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def getSiblings():
'''public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def getParent():
'''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
'''
pass
def getPathToTop():
'''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def setPathToTopCalledByControl():
'''public void setPathToTopCalledByControl(final boolean wasByControl)
'''
pass
def setHierarchy():
'''public void setHierarchy(final String hierarchy)
public void setHierarchy(final String object, final String key, final String hierarchy)
'''
pass
def getUniqueIDValue():
'''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
'''
pass
def getAllHierarchies():
'''public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def findTopLocationsAtSystem():
'''public void findTopLocationsAtSystem(final String system)
'''
pass
def findLocation():
'''public void findLocation(final String location)
'''
pass
def getAllLocationTypes():
'''public Vector getAllLocationTypes(final boolean internalVals)
'''
pass
def findSelectedLocs():
'''public void findSelectedLocs(final String where)
'''
pass
def findStoreRooms():
'''public void findStoreRooms()
'''
pass
def getUserPrefWhere():
'''public String getUserPrefWhere()
'''
pass
def setStoreroom():
'''public void setStoreroom()
'''
pass
def setNonStoreroom():
'''public void setNonStoreroom()
'''
pass
def getDataList():
'''public String[][] getDataList(final String[] attributes, final int overFlowValue, final MboRemote parent)
public String[][] getDataList(final String[] attributes, final int overFlowValue, final MboRemote parent, final String locSiteId)
'''
pass
def filterLocSet():
'''public void filterLocSet(final String locSiteId)
'''
pass
def setDrilldownFlag():
'''public void setDrilldownFlag()
'''
pass
def applyLocationModifyDefaults():
'''public void applyLocationModifyDefaults(final AssetModifyDfltSetRemote assetModifyDfltSet)
'''
pass
def setItemForAddToStore():
'''public void setItemForAddToStore(final MboRemote item)
'''
pass
def getItemForAddToStore():
'''public MboRemote getItemForAddToStore()
'''
pass
def getSqlForAuthorizedStorerooms():
'''public String getSqlForAuthorizedStorerooms()
'''
pass
def authorizedStoreRoomSet():
'''public void authorizedStoreRoomSet()
'''
pass
def getMultiSiteWhere():
'''public String getMultiSiteWhere()
'''
pass
def getRoleRestrictionWhere():
'''public String getRoleRestrictionWhere()
'''
pass
def addAtIndex():
'''public MboRemote addAtIndex(final long accessModifier, final int ind)
'''
pass
def addLocationOpSKD():
'''public void addLocationOpSKD(final MboSetRemote npLocationOpSKDSet)
'''
pass
def addLocationMntSKD():
'''public void addLocationMntSKD(final MboSetRemote npLocationOpSKDSet)
'''
pass
def addWorkZones():
'''public void addWorkZones(final String workzone, final String type, final String orgid)
'''
pass
def addReorderStorelocUpdatedWarning():
'''public void addReorderStorelocUpdatedWarning()
'''
pass
