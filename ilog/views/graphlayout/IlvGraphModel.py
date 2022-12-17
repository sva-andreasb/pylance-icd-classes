def ():
    '''returns IlvGraphModel\n\n
    ()\n
    '''
def getGrapher():
    '''returns IlvGrapher\n\n
    getGrapher()\n
    '''
def getRootModel():
    '''returns IlvGraphModel\n\n
    getRootModel()\n
    '''
def getGraphModel():
    '''returns IlvGraphModel\n\n
    getGraphModel(final Object obj)\n
    '''
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer(final IlvGraphModel ilvGraphModel)\n
    '''
def getLayouts():
    '''returns Enumeration\n\n
    getLayouts(final IlvLayoutProvider ilvLayoutProvider, final boolean b)\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    nextElement()\n
    '''
def getLayout():
    '''returns IlvGraphLayout\n\n
    getLayout(final IlvLayoutProvider ilvLayoutProvider, final Object o)\n
    '''
def performLayout():
    '''returns int\n\n
    performLayout(final IlvLayoutProvider ilvLayoutProvider, final boolean b, final boolean b2, final boolean b3)\n
    performLayout(final IlvLayoutProvider ilvLayoutProvider, final IlvGraphLayout ilvGraphLayout, final boolean b, final boolean b2, final boolean b3)\n
    '''
def isLayoutNeeded():
    '''returns boolean\n\n
    isLayoutNeeded(final IlvGraphLayout ilvGraphLayout)\n
    '''
def beforeLayout():
    '''returns None\n\n
    beforeLayout(final IlvGraphLayout ilvGraphLayout, final boolean b)\n
    '''
def afterLayout():
    '''returns None\n\n
    afterLayout(final IlvGraphLayout ilvGraphLayout, final IlvGraphLayoutReport ilvGraphLayoutReport, final boolean b)\n
    '''
def beforeAnimationStep():
    '''returns None\n\n
    beforeAnimationStep()\n
    '''
def afterAnimationStep():
    '''returns None\n\n
    afterAnimationStep()\n
    '''
def getNodesAndLinks():
    '''returns Enumeration\n\n
    getNodesAndLinks()\n
    '''
def getNodesCount():
    '''returns int\n\n
    getNodesCount()\n
    '''
def getLinksCount():
    '''returns int\n\n
    getLinksCount()\n
    getLinksCount(final Object o)\n
    '''
def getSubgraphsCount():
    '''returns int\n\n
    getSubgraphsCount()\n
    '''
def getInterGraphLinksCount():
    '''returns int\n\n
    getInterGraphLinksCount()\n
    '''
def getLinksFromCount():
    '''returns int\n\n
    getLinksFromCount(final Object o)\n
    '''
def getLinksToCount():
    '''returns int\n\n
    getLinksToCount(final Object o)\n
    '''
def getLinks():
    '''returns Enumeration\n\n
    getLinks(final Object o)\n
    '''
def getNeighbors():
    '''returns Enumeration\n\n
    getNeighbors(final Object o)\n
    '''
def getNodeDegree():
    '''returns int\n\n
    getNodeDegree(final Object o)\n
    '''
def getOpposite():
    '''returns Object\n\n
    getOpposite(final Object o, final Object o2)\n
    '''
def isLinkBetween():
    '''returns boolean\n\n
    isLinkBetween(final Object o, final Object o2)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final Object key, final String s, final Object o)\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final Object key, final String s)\n
    getProperty(final String s)\n
    '''
def move():
    '''returns None\n\n
    move(final float n, final float n2, final boolean b)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox()\n
    '''
def getLinkPointAt():
    '''returns IlvPoint\n\n
    getLinkPointAt(final Object o, final int n)\n
    '''
def setLinkCheckEnabled():
    '''returns None\n\n
    setLinkCheckEnabled(final boolean l)\n
    '''
def isLinkCheckEnabled():
    '''returns boolean\n\n
    isLinkCheckEnabled()\n
    '''
def setConnectionPointCheckEnabled():
    '''returns None\n\n
    setConnectionPointCheckEnabled(final boolean m)\n
    '''
def isConnectionPointCheckEnabled():
    '''returns boolean\n\n
    isConnectionPointCheckEnabled()\n
    '''
def isReshapeableLink():
    '''returns boolean\n\n
    isReshapeableLink(final Object o, final boolean b)\n
    '''
def hasMoveableConnectionPoint():
    '''returns boolean\n\n
    hasMoveableConnectionPoint(final Object o, final boolean b)\n
    '''
def hasPinnedConnectionPoint():
    '''returns boolean\n\n
    hasPinnedConnectionPoint(final Object o, final boolean b)\n
    '''
def getLinkWidth():
    '''returns float\n\n
    getLinkWidth(final Object o)\n
    '''
