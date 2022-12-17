def ():
    '''returns SortableClassstructure\n\n
    (final MboServerInterface ms)\n
    (final Integer id, final String parent, final Integer sortOrder)\n
    '''
def concatAll():
    '''returns String\n\n
    concatAll(final String[] sa)\n
    '''
def setAnyLevel():
    '''returns None\n\n
    setAnyLevel(final boolean anyLevelValue)\n
    '''
def getAnyLevel():
    '''returns boolean\n\n
    getAnyLevel()\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getParent():
    '''returns String\n\n
    getParent(final String object, final String key, final String[] attrs)\n
    getParent()\n
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
def reSetForNewUniqueId():
    '''returns None\n\n
    reSetForNewUniqueId(final String key)\n
    '''
def setOriginatingObjectAndAttribute():
    '''returns None\n\n
    setOriginatingObjectAndAttribute(String origObjectName, String origAttribute, final MboRemote origMbo)\n
    '''
def setOriginatingObject():
    '''returns None\n\n
    setOriginatingObject(final MboRemote origObject, final boolean inClassify)\n
    setOriginatingObject(final String actualObjectForUseWith)\n
    setOriginatingObject(final MboRemote origObject)\n
    '''
def getMboValueDataForNoTreeNodes():
    '''returns MboValueData[][]\n\n
    getMboValueDataForNoTreeNodes(final String[] attribute, final String reason)\n
    '''
def getUseWithSql():
    '''returns String\n\n
    getUseWithSql()\n
    '''
def hasAFakeTreeNode():
    '''returns boolean\n\n
    hasAFakeTreeNode()\n
    '''
def setIsLookup():
    '''returns None\n\n
    setIsLookup(final boolean is)\n
    '''
def isLookup():
    '''returns boolean\n\n
    isLookup()\n
    '''
def getbjectNameForUseWith():
    '''returns String\n\n
    getbjectNameForUseWith()\n
    '''
def getoriginatingOrgId():
    '''returns String\n\n
    getoriginatingOrgId()\n
    '''
def originatingSiteId():
    '''returns String\n\n
    originatingSiteId()\n
    '''
def setCheckIfClassUsedByObject():
    '''returns None\n\n
    setCheckIfClassUsedByObject(final boolean toSet)\n
    '''
def getMaxAppsWhere():
    '''returns String\n\n
    getMaxAppsWhere()\n
    '''
def qbeStartRemoved():
    '''returns String\n\n
    qbeStartRemoved(final String qbeStr)\n
    '''
def saveTransaction():
    '''returns None\n\n
    saveTransaction(final MXTransaction txn)\n
    '''
def reprocessSortOrder():
    '''returns None\n\n
    reprocessSortOrder()\n
    '''
def getId():
    '''returns Integer\n\n
    getId()\n
    '''
def setId():
    '''returns None\n\n
    setId(final Integer id)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final String parent)\n
    '''
def getSortOrder():
    '''returns Integer\n\n
    getSortOrder()\n
    '''
def setSortOrder():
    '''returns None\n\n
    setSortOrder(final Integer sortOrder)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final SortableClassstructure o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
