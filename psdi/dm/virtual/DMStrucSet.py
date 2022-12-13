def DMStrucSet():
    '''    public DMStrucSet(final MboServerInterface ms)
    '''
def add():
    '''    public MboRemote add(final long uniqueId, final String nodeDesc, final String relationship)
    '''
def getAllHierarchies():
    '''    public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getChildren():
    '''    public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getHierarchy():
    '''    public MboValueData[] getHierarchy(final String object, final String key)
    '''
def getParent():
    '''    public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    '''
def getPathToTop():
    '''    public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getSiblings():
    '''    public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getTop():
    '''    public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getUniqueIDValue():
    '''    public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
def setHierarchy():
    '''    public void setHierarchy(final String object, final String key, final String hierarchy)
    '''
def getRelatedMbo():
    '''    public MboRemote getRelatedMbo(final long uniqueId)
    '''
def getNodeMap():
    '''    public DMStrucNodeMap getNodeMap()
    '''
def setNodeMap():
    '''    public void setNodeMap(final DMStrucNodeMap nodeMap)
    '''
