def ():
    '''returns WrappedNodeBoxInterface\n\n
    (final IlvGraphModel ilvGraphModel, final boolean b, final IlvTransformer ilvTransformer)\n
    (final IlvGraphModel ilvGraphModel, final boolean b, final IlvPoint ilvPoint, final double n)\n
    (final IlvLinkClipInterface a)\n
    (final IlvLinkConnectionBoxInterface a)\n
    (final IlvNodeBoxInterface a)\n
    '''
def contentsChanged():
    '''returns None\n\n
    contentsChanged(final GraphModelEvent graphModelEvent)\n
    '''
def getOriginalGraphModel():
    '''returns IlvGraphModel\n\n
    getOriginalGraphModel()\n
    '''
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer()\n
    getTransformer(IlvGraphModel a)\n
    '''
def setTransformer():
    '''returns None\n\n
    setTransformer(final IlvTransformer ilvTransformer)\n
    '''
def transform():
    '''returns None\n\n
    transform(final IlvPoint ilvPoint)\n
    transform(final IlvRect ilvRect)\n
    '''
def inverseTransform():
    '''returns None\n\n
    inverseTransform(final IlvPoint ilvPoint)\n
    inverseTransform(final IlvRect ilvRect)\n
    '''
def getGrapher():
    '''returns IlvGrapher\n\n
    getGrapher()\n
    '''
def getParentModel():
    '''returns IlvGraphModel\n\n
    getParentModel()\n
    '''
def getGraphModel():
    '''returns IlvGraphModel\n\n
    getGraphModel(final Object o)\n
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
def getNodes():
    '''returns Enumeration\n\n
    getNodes()\n
    '''
def getNodesCount():
    '''returns int\n\n
    getNodesCount()\n
    '''
def getLinks():
    '''returns Enumeration\n\n
    getLinks()\n
    '''
def getLinksCount():
    '''returns int\n\n
    getLinksCount()\n
    '''
def getSubgraphs():
    '''returns Enumeration\n\n
    getSubgraphs()\n
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
    moveNode(final Object o, final float n, final float n2, final boolean b)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final Object o)\n
    '''
def getLinkPointsCount():
    '''returns int\n\n
    getLinkPointsCount(final Object o)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final Object o)\n
    '''
def getLinkPointAt():
    '''returns IlvPoint\n\n
    getLinkPointAt(final Object o, final int n)\n
    '''
def setLinkCheckEnabled():
    '''returns None\n\n
    setLinkCheckEnabled(final boolean b)\n
    '''
def setConnectionPointCheckEnabled():
    '''returns None\n\n
    setConnectionPointCheckEnabled(final boolean b)\n
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
def saveParametersToNamedProperties():
    '''returns String\n\n
    saveParametersToNamedProperties(final IlvGraphLayout ilvGraphLayout, final boolean b)\n
    saveParametersToNamedProperties(final IlvGraphLayout ilvGraphLayout, final String s, final boolean b)\n
    '''
def savePreferredLayoutsToNamedProperties():
    '''returns boolean\n\n
    savePreferredLayoutsToNamedProperties(final IlvDefaultLayoutProvider ilvDefaultLayoutProvider, final boolean b, final boolean b2, final boolean b3)\n
    '''
def loadParametersFromNamedProperties():
    '''returns IlvGraphLayout\n\n
    loadParametersFromNamedProperties(final IlvGraphLayout ilvGraphLayout)\n
    loadParametersFromNamedProperties(final IlvGraphLayout ilvGraphLayout, final String s)\n
    loadParametersFromNamedProperties(final String s)\n
    '''
def loadPreferredLayoutsFromNamedProperties():
    '''returns boolean\n\n
    loadPreferredLayoutsFromNamedProperties(final IlvDefaultLayoutProvider ilvDefaultLayoutProvider, final boolean b, final boolean b2)\n
    '''
def removeParametersFromNamedProperties():
    '''returns None\n\n
    removeParametersFromNamedProperties()\n
    removeParametersFromNamedProperties(final String s)\n
    removeParametersFromNamedProperties(final Class clazz)\n
    '''
def setPreferredLayoutPropertyPrefix():
    '''returns None\n\n
    setPreferredLayoutPropertyPrefix(final String preferredLayoutPropertyPrefix)\n
    '''
def getPreferredLayoutPropertyPrefix():
    '''returns String\n\n
    getPreferredLayoutPropertyPrefix()\n
    '''
def getLayoutPropertyPrefix():
    '''returns String\n\n
    getLayoutPropertyPrefix(final IlvGraphLayout ilvGraphLayout)\n
    '''
def getNodeBoxInterface():
    '''returns IlvNodeBoxInterface\n\n
    getNodeBoxInterface(final IlvNodeBoxInterface ilvNodeBoxInterface)\n
    '''
def getLinkConnectionBoxInterface():
    '''returns IlvLinkConnectionBoxInterface\n\n
    getLinkConnectionBoxInterface(final IlvLinkConnectionBoxInterface ilvLinkConnectionBoxInterface)\n
    '''
def getLinkClipInterface():
    '''returns IlvLinkClipInterface\n\n
    getLinkClipInterface(final IlvLinkClipInterface ilvLinkClipInterface)\n
    '''
def getConnectionPoint():
    '''returns IlvPoint\n\n
    getConnectionPoint(final IlvGraphModel ilvGraphModel, final Object o, final IlvRect ilvRect, final Object o2, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final boolean b)\n
    '''
def getBox():
    '''returns IlvRect\n\n
    getBox(final IlvGraphModel ilvGraphModel, final Object o)\n
    getBox(final IlvGraphModel ilvGraphModel, final Object o)\n
    '''
def getTangentialOffset():
    '''returns float\n\n
    getTangentialOffset(IlvGraphModel a, final Object o, final int n)\n
    '''
