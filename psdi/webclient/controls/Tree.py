CONST_RESTRICT_ACTION_ON_LEAFNODES = "String  \"LEAF_NODES\""
CONST_RESTRICT_ACTION_ON_BRANCHNODES = "String  \"BRANCH_NODES\""
def Tree():
    '''public Tree()
    '''
def cleanup():
    '''public void cleanup()
    '''
def initialize():
    '''public void initialize()
    '''
def render():
    '''public int render()
    '''
def collectNodeAttributes():
    '''public void collectNodeAttributes()
    '''
def supportsMarkedForDelete():
    '''public boolean supportsMarkedForDelete()
    '''
def selectnode():
    '''public void selectnode()
    '''
def setcurrentnode():
    '''public void setcurrentnode(final String newobjectname, final String newuniqueIdName, final String newuniqueIdValue)
    '''
def createNodes():
    '''public void createNodes()
    '''
def getTop():
    '''public Object[][] getTop(final String[] dataattributes, final int maxchildren)
    '''
def getChildren():
    '''public Object[][] getChildren(final String objectname, final String uniqueId, final String[] dataAttributes, final int maxChildren)
    public Object[][] getChildren(final String objectname, final String uniqueId)
    '''
def getPathToTop():
    '''public Object[][] getPathToTop(final String objectname, final String uniqueid, final String[] dataattributes, final int maxchildren)
    '''
def getpathtotop():
    '''public void getpathtotop()
    '''
def getMboValueData():
    '''public Object[] getMboValueData(final String[] dataAttributes)
    '''
def setHierarchy():
    '''public void setHierarchy(final String objectname, final String uniqueId, final String hierarchy)
    '''
def getObjectName():
    '''public String getObjectName()
    '''
def setObjectName():
    '''public void setObjectName(final String newobjectname)
    '''
def getUniqueIdName():
    '''public String getUniqueIdName()
    '''
def setUniqueIdName():
    '''public void setUniqueIdName(final String newuniqueIdName)
    '''
def getUniqueIdValue():
    '''public String getUniqueIdValue()
    '''
def setUniqueIdValue():
    '''public void setUniqueIdValue(final String newUniqueIdValue)
    '''
def getRestrictActionOn():
    '''public String getRestrictActionOn()
    '''
def setRefreshTree():
    '''public void setRefreshTree(final boolean flag)
    '''
def getSourceAttributeValue():
    '''public String getSourceAttributeValue()
    '''
def setSourceAttributeValue():
    '''public void setSourceAttributeValue(final String sourceAttributeValue)
    '''
def getSourceDataAttribute():
    '''public String getSourceDataAttribute()
    '''
def setSourceDataAttribute():
    '''public void setSourceDataAttribute(final String sourceDataAttribute)
    '''
def getTreeDataBean():
    '''public TreeControlBean getTreeDataBean()
    '''
def setTreeDataBean():
    '''public void setTreeDataBean(final TreeControlBean treeDataBean)
    '''
def openFirstLevel():
    '''public boolean openFirstLevel()
    '''
def expandAllNodes():
    '''public boolean expandAllNodes()
    '''
def selectFirstNode():
    '''public boolean selectFirstNode()
    '''
def getNodeDataAttributes():
    '''public String[] getNodeDataAttributes()
    '''
def getNodeDelimiter():
    '''public String getNodeDelimiter()
    '''
def getNodeAttributeDefinition():
    '''public ArrayList getNodeAttributeDefinition()
    '''
def getTreeNodeInfo():
    '''public Hashtable<String, String> getTreeNodeInfo()
    '''
def setTreeNodeInfo():
    '''public void setTreeNodeInfo(final Hashtable<String, String> treeNodeInfo)
    '''
def dataChangedEvent():
    '''public void dataChangedEvent(final DataBean speaker)
    '''
def structureChangedEvent():
    '''public void structureChangedEvent(final DataBean speaker)
    '''
def getSelectedNode():
    '''public TreeNode getSelectedNode()
    '''
def getLastSelectedNodeId():
    '''public String getLastSelectedNodeId()
    '''
def setSelectedNode():
    '''public void setSelectedNode(final TreeNode newSelectedNode)
    '''
def getBreadcrumbs():
    '''public ArrayList getBreadcrumbs()
    '''
def setBreadcrumbs():
    '''public void setBreadcrumbs(final ArrayList newBreadcrumbs)
    '''
def getBreadcrumbPath():
    '''public ArrayList getBreadcrumbPath()
    '''
def setBreadcrumbPath():
    '''public void setBreadcrumbPath(final ArrayList newBreadcrumbPath)
    '''
def breadcrumbselected():
    '''public int breadcrumbselected()
    '''
def boundToBreadcrumbs():
    '''public void boundToBreadcrumbs()
    '''
def isBoundToBreadcrumbs():
    '''public boolean isBoundToBreadcrumbs()
    '''
def clearbreadcrumbs():
    '''public int clearbreadcrumbs()
    '''
def checkForNewNodes():
    '''public boolean checkForNewNodes()
    '''
def getTopULId():
    '''public String getTopULId()
    '''
def setTopULId():
    '''public void setTopULId(final String id)
    '''
