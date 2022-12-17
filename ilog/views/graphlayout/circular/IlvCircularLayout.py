NO_INDEX = "int  -1"
BY_CLUSTER_IDS = "int  0"
BY_SUBGRAPHS = "int  1"
AUTOMATIC = "int  2"
STRAIGHT_LINE_STYLE = "int  1"
NO_RESHAPE_STYLE = "int  0"
def ():
    '''returns IlvCircularLayout\n\n
    ()\n
    (final IlvCircularLayout ilvCircularLayout)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o, final Object o2)\n
    compare(final Object o, final Object o2)\n
    '''
def copyParameters():
    '''returns None\n\n
    copyParameters(final IlvGraphLayout ilvGraphLayout)\n
    '''
def copy():
    '''returns IlvGraphLayout\n\n
    copy()\n
    '''
def getRootClusterIds():
    '''returns IlvClusterId[]\n\n
    getRootClusterIds()\n
    '''
def setStructureUpToDate():
    '''returns None\n\n
    setStructureUpToDate(final boolean structureUpToDate)\n
    '''
def isStarCenter():
    '''returns boolean\n\n
    isStarCenter(final Object o)\n
    '''
def getClusterIds():
    '''returns Enumeration\n\n
    getClusterIds()\n
    getClusterIds(final Object o)\n
    '''
def getClusterRadius():
    '''returns float\n\n
    getClusterRadius(final int n)\n
    '''
def getClusterCenter():
    '''returns IlvPoint\n\n
    getClusterCenter(final int n)\n
    '''
def getClusterNodes():
    '''returns Vector\n\n
    getClusterNodes(final int n)\n
    '''
def getClusterIdsCount():
    '''returns int\n\n
    getClusterIdsCount(final Object o)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final Object o, final IlvClusterId ilvClusterId)\n
    '''
def setLayoutOfClusterGraph():
    '''returns None\n\n
    setLayoutOfClusterGraph(final IlvGraphLayout af)\n
    '''
def getLayoutOfClusterGraph():
    '''returns IlvGraphLayout\n\n
    getLayoutOfClusterGraph()\n
    '''
def supportsAllowedTime():
    '''returns boolean\n\n
    supportsAllowedTime()\n
    '''
def supportsStopImmediately():
    '''returns boolean\n\n
    supportsStopImmediately()\n
    '''
def supportsPercentageComplete():
    '''returns boolean\n\n
    supportsPercentageComplete()\n
    '''
def isAreaMinimizationEnabled():
    '''returns boolean\n\n
    isAreaMinimizationEnabled()\n
    '''
def getOffset():
    '''returns float\n\n
    getOffset()\n
    '''
def getLevelOffset():
    '''returns float\n\n
    getLevelOffset()\n
    '''
def getDisconnectedGraphOffset():
    '''returns float\n\n
    getDisconnectedGraphOffset()\n
    '''
