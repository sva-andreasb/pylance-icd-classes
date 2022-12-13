def ClassStructureSet():
    '''public ClassStructureSet(final MboServerInterface ms)
    '''
def concatAll():
    '''public String concatAll(final String[] sa)
    '''
def setAnyLevel():
    '''public void setAnyLevel(final boolean anyLevelValue)
    '''
def getAnyLevel():
    '''public boolean getAnyLevel()
    '''
def getChildren():
    '''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getParent():
    '''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    public String getParent()
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
def reSetForNewUniqueId():
    '''public void reSetForNewUniqueId(final String key)
    '''
def setOriginatingObjectAndAttribute():
    '''public void setOriginatingObjectAndAttribute(String origObjectName, String origAttribute, final MboRemote origMbo)
    '''
def setOriginatingObject():
    '''public void setOriginatingObject(final MboRemote origObject, final boolean inClassify)
    public void setOriginatingObject(final String actualObjectForUseWith)
    public void setOriginatingObject(final MboRemote origObject)
    '''
def getMboValueDataForNoTreeNodes():
    '''public MboValueData[][] getMboValueDataForNoTreeNodes(final String[] attribute, final String reason)
    '''
def getUseWithSql():
    '''public String getUseWithSql()
    '''
def hasAFakeTreeNode():
    '''public boolean hasAFakeTreeNode()
    '''
def setIsLookup():
    '''public void setIsLookup(final boolean is)
    '''
def isLookup():
    '''public boolean isLookup()
    '''
def getbjectNameForUseWith():
    '''public String getbjectNameForUseWith()
    '''
def getoriginatingOrgId():
    '''public String getoriginatingOrgId()
    '''
def originatingSiteId():
    '''public String originatingSiteId()
    '''
def setCheckIfClassUsedByObject():
    '''public void setCheckIfClassUsedByObject(final boolean toSet)
    '''
def getMaxAppsWhere():
    '''public String getMaxAppsWhere()
    '''
def qbeStartRemoved():
    '''public String qbeStartRemoved(final String qbeStr)
    '''
def saveTransaction():
    '''public void saveTransaction(final MXTransaction txn)
    '''
def reprocessSortOrder():
    '''public void reprocessSortOrder()
    '''
def SortableClassstructure():
    '''public SortableClassstructure(final Integer id, final String parent, final Integer sortOrder)
    '''
def getId():
    '''public Integer getId()
    '''
def setId():
    '''public void setId(final Integer id)
    '''
def setParent():
    '''public void setParent(final String parent)
    '''
def getSortOrder():
    '''public Integer getSortOrder()
    '''
def setSortOrder():
    '''public void setSortOrder(final Integer sortOrder)
    '''
def compareTo():
    '''public int compareTo(final SortableClassstructure o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
