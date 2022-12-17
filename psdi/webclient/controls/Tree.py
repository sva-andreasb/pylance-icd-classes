CONST_RESTRICT_ACTION_ON_LEAFNODES = "String  \"LEAF_NODES\""
CONST_RESTRICT_ACTION_ON_BRANCHNODES = "String  \"BRANCH_NODES\""
def ():
    '''returns Tree\n\n
    ()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def collectNodeAttributes():
    '''returns None\n\n
    collectNodeAttributes()\n
    '''
def supportsMarkedForDelete():
    '''returns boolean\n\n
    supportsMarkedForDelete()\n
    '''
def selectnode():
    '''returns None\n\n
    selectnode()\n
    '''
def setcurrentnode():
    '''returns None\n\n
    setcurrentnode(final String newobjectname, final String newuniqueIdName, final String newuniqueIdValue)\n
    '''
def createNodes():
    '''returns None\n\n
    createNodes()\n
    '''
def getTop():
    '''returns Object[][]\n\n
    getTop(final String[] dataattributes, final int maxchildren)\n
    '''
def getChildren():
    '''returns Object[][]\n\n
    getChildren(final String objectname, final String uniqueId, final String[] dataAttributes, final int maxChildren)\n
    getChildren(final String objectname, final String uniqueId)\n
    '''
def getPathToTop():
    '''returns Object[][]\n\n
    getPathToTop(final String objectname, final String uniqueid, final String[] dataattributes, final int maxchildren)\n
    '''
def getpathtotop():
    '''returns None\n\n
    getpathtotop()\n
    '''
def getMboValueData():
    '''returns Object[]\n\n
    getMboValueData(final String[] dataAttributes)\n
    '''
def setHierarchy():
    '''returns None\n\n
    setHierarchy(final String objectname, final String uniqueId, final String hierarchy)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName()\n
    '''
def setObjectName():
    '''returns None\n\n
    setObjectName(final String newobjectname)\n
    '''
def getUniqueIdName():
    '''returns String\n\n
    getUniqueIdName()\n
    '''
def setUniqueIdName():
    '''returns None\n\n
    setUniqueIdName(final String newuniqueIdName)\n
    '''
def getUniqueIdValue():
    '''returns String\n\n
    getUniqueIdValue()\n
    '''
def setUniqueIdValue():
    '''returns None\n\n
    setUniqueIdValue(final String newUniqueIdValue)\n
    '''
def getRestrictActionOn():
    '''returns String\n\n
    getRestrictActionOn()\n
    '''
def setRefreshTree():
    '''returns None\n\n
    setRefreshTree(final boolean flag)\n
    '''
def getSourceAttributeValue():
    '''returns String\n\n
    getSourceAttributeValue()\n
    '''
def setSourceAttributeValue():
    '''returns None\n\n
    setSourceAttributeValue(final String sourceAttributeValue)\n
    '''
def getSourceDataAttribute():
    '''returns String\n\n
    getSourceDataAttribute()\n
    '''
def setSourceDataAttribute():
    '''returns None\n\n
    setSourceDataAttribute(final String sourceDataAttribute)\n
    '''
def getTreeDataBean():
    '''returns TreeControlBean\n\n
    getTreeDataBean()\n
    '''
def setTreeDataBean():
    '''returns None\n\n
    setTreeDataBean(final TreeControlBean treeDataBean)\n
    '''
def openFirstLevel():
    '''returns boolean\n\n
    openFirstLevel()\n
    '''
def expandAllNodes():
    '''returns boolean\n\n
    expandAllNodes()\n
    '''
def selectFirstNode():
    '''returns boolean\n\n
    selectFirstNode()\n
    '''
def getNodeDataAttributes():
    '''returns String[]\n\n
    getNodeDataAttributes()\n
    '''
def getNodeDelimiter():
    '''returns String\n\n
    getNodeDelimiter()\n
    '''
def getNodeAttributeDefinition():
    '''returns ArrayList\n\n
    getNodeAttributeDefinition()\n
    '''
def setTreeNodeInfo():
    '''returns None\n\n
    setTreeNodeInfo(final Hashtable<String, String> treeNodeInfo)\n
    '''
def dataChangedEvent():
    '''returns None\n\n
    dataChangedEvent(final DataBean speaker)\n
    '''
def structureChangedEvent():
    '''returns None\n\n
    structureChangedEvent(final DataBean speaker)\n
    '''
def getSelectedNode():
    '''returns TreeNode\n\n
    getSelectedNode()\n
    '''
def getLastSelectedNodeId():
    '''returns String\n\n
    getLastSelectedNodeId()\n
    '''
def setSelectedNode():
    '''returns None\n\n
    setSelectedNode(final TreeNode newSelectedNode)\n
    '''
def getBreadcrumbs():
    '''returns ArrayList\n\n
    getBreadcrumbs()\n
    '''
def setBreadcrumbs():
    '''returns None\n\n
    setBreadcrumbs(final ArrayList newBreadcrumbs)\n
    '''
def getBreadcrumbPath():
    '''returns ArrayList\n\n
    getBreadcrumbPath()\n
    '''
def setBreadcrumbPath():
    '''returns None\n\n
    setBreadcrumbPath(final ArrayList newBreadcrumbPath)\n
    '''
def breadcrumbselected():
    '''returns int\n\n
    breadcrumbselected()\n
    '''
def boundToBreadcrumbs():
    '''returns None\n\n
    boundToBreadcrumbs()\n
    '''
def isBoundToBreadcrumbs():
    '''returns boolean\n\n
    isBoundToBreadcrumbs()\n
    '''
def clearbreadcrumbs():
    '''returns int\n\n
    clearbreadcrumbs()\n
    '''
def checkForNewNodes():
    '''returns boolean\n\n
    checkForNewNodes()\n
    '''
def getTopULId():
    '''returns String\n\n
    getTopULId()\n
    '''
def setTopULId():
    '''returns None\n\n
    setTopULId(final String id)\n
    '''
