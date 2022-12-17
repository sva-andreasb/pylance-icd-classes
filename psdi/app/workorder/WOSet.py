def ():
    '''returns WOSet\n\n
    (final MboServerInterface ms)\n
    '''
def workordersForLaborOrCraft():
    '''returns None\n\n
    workordersForLaborOrCraft(final String labor, final String craft)\n
    '''
def onlyTopLevels():
    '''returns None\n\n
    onlyTopLevels()\n
    '''
def findAllOpenWOsReportedBy():
    '''returns None\n\n
    findAllOpenWOsReportedBy(final String user)\n
    '''
def setHistory():
    '''returns None\n\n
    setHistory(final boolean historyWOs)\n
    '''
def setCurrent():
    '''returns None\n\n
    setCurrent(final boolean currentWOs)\n
    '''
def setLocsystem():
    '''returns None\n\n
    setLocsystem(final String locationSystem)\n
    '''
def setLocgroup():
    '''returns None\n\n
    setLocgroup(final String locationGroup)\n
    '''
def setNoCancelled():
    '''returns None\n\n
    setNoCancelled(final boolean turnOn)\n
    '''
def getHistory():
    '''returns boolean\n\n
    getHistory()\n
    '''
def getCurrent():
    '''returns boolean\n\n
    getCurrent()\n
    '''
def getLocsystem():
    '''returns String\n\n
    getLocsystem()\n
    '''
def getLocgroup():
    '''returns String\n\n
    getLocgroup()\n
    '''
def getNoCancelled():
    '''returns boolean\n\n
    getNoCancelled()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll()\n
    '''
def addAtIndex():
    '''returns MboRemote\n\n
    addAtIndex(final long accessModifier, final int index)\n
    '''
def remove():
    '''returns None\n\n
    remove(final MboRemote mbo)\n
    '''
def changeWorkOrderParent():
    '''returns None\n\n
    changeWorkOrderParent(final MboRemote woparent)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final MboSetListener l)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final MboSetListener l)\n
    '''
def reportModifiedMbo():
    '''returns None\n\n
    reportModifiedMbo(final MboRemote modifiedMbo)\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attribute, final String expression)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def getUserWhere():
    '''returns String\n\n
    getUserWhere(final String alias)\n
    '''
def getExternalList():
    '''returns String\n\n
    getExternalList(final String listName, final String internalValue, final String siteID, final String orgID)\n
    '''
def getExternalValues():
    '''returns String\n\n
    getExternalValues(final String listName, final String internalValue, final String siteID, final String orgID)\n
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
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def clearMoveAssetFieldsDefault():
    '''returns None\n\n
    clearMoveAssetFieldsDefault()\n
    '''
def filterByLinearAsset():
    '''returns None\n\n
    filterByLinearAsset(final MboSetRemote fltrSet)\n
    '''
def getOriginalWOQbe():
    '''returns Hashtable\n\n
    getOriginalWOQbe()\n
    '''
def getOriginalWOUserWhere():
    '''returns String\n\n
    getOriginalWOUserWhere()\n
    '''
def setOriginalWOUserWhere():
    '''returns None\n\n
    setOriginalWOUserWhere(final String inWhere)\n
    '''
def setOriginalWOQbe():
    '''returns None\n\n
    setOriginalWOQbe(final Hashtable inQbe)\n
    '''
def getListFromAllSites():
    '''returns MboSetRemote\n\n
    getListFromAllSites(final int row, final String attribute)\n
    '''
def setSkipRepairFacilityOnNewWOs():
    '''returns None\n\n
    setSkipRepairFacilityOnNewWOs(final boolean skipRepairFacilityOnNewWOs)\n
    '''
def appendToWhere():
    '''returns String\n\n
    appendToWhere()\n
    '''
def getUncommittedAncestorVector():
    '''returns Vector\n\n
    getUncommittedAncestorVector()\n
    '''
def storeUncommittedAncestorVector():
    '''returns None\n\n
    storeUncommittedAncestorVector(final MXTransaction uncommitted)\n
    '''
def setSourceWODuplicatedBy():
    '''returns None\n\n
    setSourceWODuplicatedBy(final MboRemote wo)\n
    '''
def getSourceWODuplicatedBy():
    '''returns MboRemote\n\n
    getSourceWODuplicatedBy()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def getMaxAppsWhere():
    '''returns String\n\n
    getMaxAppsWhere()\n
    '''
