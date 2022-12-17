def ():
    '''returns BaseSubgraphData\n\n
    ()\n
    '''
def clean():
    '''returns None\n\n
    clean()\n
    '''
def collectData():
    '''returns None\n\n
    collectData(final IlvGraphModel ilvGraphModel)\n
    collectData(final IlvGraphModel a, final boolean b, final boolean b2)\n
    '''
def getNodeBox():
    '''returns IlvRect\n\n
    getNodeBox(final IlvNodeBoxInterface ilvNodeBoxInterface, final Object o)\n
    '''
def getTangentialOffset():
    '''returns float\n\n
    getTangentialOffset(final IlvLinkConnectionBoxInterface ilvLinkConnectionBoxInterface, final Object o, final int n)\n
    '''
def getClippedConnectionPoint():
    '''returns IlvPoint\n\n
    getClippedConnectionPoint(final IlvLinkClipInterface ilvLinkClipInterface, final Object o, final IlvRect ilvRect, final Object o2, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final boolean b)\n
    '''
def getParentModel():
    '''returns IlvGraphModel\n\n
    getParentModel()\n
    '''
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer(final IlvGraphModel ilvGraphModel)\n
    '''
def getNodes():
    '''returns Enumeration\n\n
    getNodes()\n
    getNodes(final Object o)\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    '''
def getNodesCount():
    '''returns int\n\n
    getNodesCount()\n
    '''
def getLinks():
    '''returns Enumeration\n\n
    getLinks()\n
    getLinks(final Object o, final boolean b, final boolean b2)\n
    '''
def getLinksCount():
    '''returns int\n\n
    getLinksCount()\n
    '''
def getLabels():
    '''returns Enumeration\n\n
    getLabels()\n
    getLabels(final Object o)\n
    '''
def getLabelsCount():
    '''returns int\n\n
    getLabelsCount()\n
    '''
def getSubgraphs():
    '''returns Enumeration\n\n
    getSubgraphs()\n
    getSubgraphs(final Object o)\n
    '''
def getSubgraphsCount():
    '''returns int\n\n
    getSubgraphsCount()\n
    '''
def getInterGraphLinks():
    '''returns Enumeration\n\n
    getInterGraphLinks()\n
    '''
def getInterGraphLinksCount():
    '''returns int\n\n
    getInterGraphLinksCount()\n
    '''
def getLinksFrom():
    '''returns Enumeration\n\n
    getLinksFrom(final Object o)\n
    '''
def getLinksFromCount():
    '''returns int\n\n
    getLinksFromCount(final Object o)\n
    '''
def getLinksTo():
    '''returns Enumeration\n\n
    getLinksTo(final Object o)\n
    '''
def getLinksToCount():
    '''returns int\n\n
    getLinksToCount(final Object o)\n
    '''
def getFrom():
    '''returns Object\n\n
    getFrom(final Object o)\n
    '''
def getTo():
    '''returns Object\n\n
    getTo(final Object o)\n
    '''
def nodeInsideGraph():
    '''returns boolean\n\n
    nodeInsideGraph(final Object o, final Object o2)\n
    '''
def linkInsideGraph():
    '''returns boolean\n\n
    linkInsideGraph(final Object o, final Object o2)\n
    '''
def fromEndsInside():
    '''returns boolean\n\n
    fromEndsInside(final Object o, final Object o2)\n
    '''
def toEndsInside():
    '''returns boolean\n\n
    toEndsInside(final Object o, final Object o2)\n
    '''
def isNode():
    '''returns boolean\n\n
    isNode(final Object o)\n
    '''
def isLink():
    '''returns boolean\n\n
    isLink(final Object o)\n
    '''
def isInterGraphLink():
    '''returns boolean\n\n
    isInterGraphLink(final Object o)\n
    '''
def isSubgraph():
    '''returns boolean\n\n
    isSubgraph(final Object o)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final Object o, final String s, final Object o2)\n
    setProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final Object o, final String s)\n
    getProperty(final String s)\n
    '''
def moveNode():
    '''returns None\n\n
    moveNode(final Object o, final float x, final float y, final boolean b)\n
    '''
def moveLabel():
    '''returns None\n\n
    moveLabel(final Object o, final float x, final float y, final boolean b)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final Object o)\n
    '''
def getLinkPointsCount():
    '''returns int\n\n
    getLinkPointsCount(final Object o)\n
    '''
def getLinkPointAt():
    '''returns IlvPoint\n\n
    getLinkPointAt(final Object o, final int n)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final Object o)\n
    '''
def reshapeLink():
    '''returns None\n\n
    reshapeLink(final Object o, final IlvPoint ilvPoint, final IlvPoint[] array, final int n, final int n2, final IlvPoint ilvPoint2, final boolean b)\n
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
def isSpline():
    '''returns boolean\n\n
    isSpline(final Object o, final IlvSplineLinkFilter ilvSplineLinkFilter)\n
    '''
def refreshBoundingBox():
    '''returns None\n\n
    refreshBoundingBox(final Object o)\n
    '''
def getOriginal():
    '''returns Object\n\n
    getOriginal(final Object o)\n
    '''
def getReplacement():
    '''returns Object\n\n
    getReplacement(final Object key)\n
    '''
def getOriginalGraphModel():
    '''returns IlvGraphModel\n\n
    getOriginalGraphModel(final Object o)\n
    getOriginalGraphModel()\n
    '''
def getOriginalLabelingModel():
    '''returns IlvLabelingModel\n\n
    getOriginalLabelingModel(final Object o)\n
    '''
def getOriginalSubgraphModel():
    '''returns IlvGraphModel\n\n
    getOriginalSubgraphModel(final Object o)\n
    '''
def getGraphModel():
    '''returns IlvGraphModel\n\n
    getGraphModel(final Object o)\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object o)\n
    '''
def getLowestCommonAncestor():
    '''returns Object\n\n
    getLowestCommonAncestor(final Object o, final Object o2)\n
    '''
def getAncestorContainedIn():
    '''returns Object\n\n
    getAncestorContainedIn(Object o, final Object o2)\n
    '''
def getFlattenedSubgraphsCount():
    '''returns int\n\n
    getFlattenedSubgraphsCount()\n
    '''
def getSubgraphMargin():
    '''returns float\n\n
    getSubgraphMargin(final Object o, final int n)\n
    '''
def wasIntergraphLink():
    '''returns boolean\n\n
    wasIntergraphLink(final Object o)\n
    '''
def getHierarchyRoot():
    '''returns Object\n\n
    getHierarchyRoot()\n
    '''
def setFilter():
    '''returns None\n\n
    setFilter(final Object o)\n
    '''
def getFilter():
    '''returns Object\n\n
    getFilter()\n
    '''
