def WOSet():
    '''public WOSet(final MboServerInterface ms)
    '''
def workordersForLaborOrCraft():
    '''public void workordersForLaborOrCraft(final String labor, final String craft)
    '''
def onlyTopLevels():
    '''public void onlyTopLevels()
    '''
def findAllOpenWOsReportedBy():
    '''public void findAllOpenWOsReportedBy(final String user)
    '''
def setHistory():
    '''public void setHistory(final boolean historyWOs)
    '''
def setCurrent():
    '''public void setCurrent(final boolean currentWOs)
    '''
def setLocsystem():
    '''public void setLocsystem(final String locationSystem)
    '''
def setLocgroup():
    '''public void setLocgroup(final String locationGroup)
    '''
def setNoCancelled():
    '''public void setNoCancelled(final boolean turnOn)
    '''
def getHistory():
    '''public boolean getHistory()
    '''
def getCurrent():
    '''public boolean getCurrent()
    '''
def getLocsystem():
    '''public String getLocsystem()
    '''
def getLocgroup():
    '''public String getLocgroup()
    '''
def getNoCancelled():
    '''public boolean getNoCancelled()
    '''
def getUserPrefWhere():
    '''public String getUserPrefWhere()
    '''
def canAdd():
    '''public void canAdd()
    '''
def deleteAll():
    '''public void deleteAll()
    '''
def addAtIndex():
    '''public MboRemote addAtIndex(final long accessModifier, final int index)
    '''
def remove():
    '''public void remove(final MboRemote mbo)
    '''
def changeWorkOrderParent():
    '''public void changeWorkOrderParent(final MboRemote woparent)
    '''
def addListener():
    '''public void addListener(final MboSetListener l)
    '''
def removeListener():
    '''public void removeListener(final MboSetListener l)
    '''
def reportModifiedMbo():
    '''public void reportModifiedMbo(final MboRemote modifiedMbo)
    '''
def setQbe():
    '''public void setQbe(final String attribute, final String expression)
    '''
def resetQbe():
    '''public void resetQbe()
    '''
def getUserWhere():
    '''public String getUserWhere(final String alias)
    '''
def getExternalList():
    '''public String getExternalList(final String listName, final String internalValue, final String siteID, final String orgID)
    '''
def getExternalValues():
    '''public String getExternalValues(final String listName, final String internalValue, final String siteID, final String orgID)
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
def getPathToTop():
    '''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def clearMoveAssetFieldsDefault():
    '''public void clearMoveAssetFieldsDefault()
    '''
def filterByLinearAsset():
    '''public void filterByLinearAsset(final MboSetRemote fltrSet)
    '''
def getOriginalWOQbe():
    '''public Hashtable getOriginalWOQbe()
    '''
def getOriginalWOUserWhere():
    '''public String getOriginalWOUserWhere()
    '''
def setOriginalWOUserWhere():
    '''public void setOriginalWOUserWhere(final String inWhere)
    '''
def setOriginalWOQbe():
    '''public void setOriginalWOQbe(final Hashtable inQbe)
    '''
def getListFromAllSites():
    '''public MboSetRemote getListFromAllSites(final int row, final String attribute)
    '''
def setSkipRepairFacilityOnNewWOs():
    '''public void setSkipRepairFacilityOnNewWOs(final boolean skipRepairFacilityOnNewWOs)
    '''
def appendToWhere():
    '''public String appendToWhere()
    '''
def getUncommittedAncestorVector():
    '''public Vector getUncommittedAncestorVector()
    '''
def storeUncommittedAncestorVector():
    '''public void storeUncommittedAncestorVector(final MXTransaction uncommitted)
    '''
def setSourceWODuplicatedBy():
    '''public void setSourceWODuplicatedBy(final MboRemote wo)
    '''
def getSourceWODuplicatedBy():
    '''public MboRemote getSourceWODuplicatedBy()
    '''
def save():
    '''public void save()
    '''
def getMaxAppsWhere():
    '''public String getMaxAppsWhere()
    '''
