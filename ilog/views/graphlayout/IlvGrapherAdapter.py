def ():
    '''returns IlvNeighborsEnumerationWhenHasSameAdjacencies\n\n
    (final IlvGrapher e)\n
    (final IlvGraphic c)\n
    '''
def getParentModel():
    '''returns IlvGraphModel\n\n
    getParentModel()\n
    '''
def getGrapher():
    '''returns IlvGrapher\n\n
    getGrapher()\n
    '''
def setConstantModeManagerFrameAutoMargin():
    '''returns None\n\n
    setConstantModeManagerFrameAutoMargin(final boolean n)\n
    '''
def isConstantModeManagerFrameAutoMargin():
    '''returns boolean\n\n
    isConstantModeManagerFrameAutoMargin()\n
    '''
def setCoordinatesMode():
    '''returns None\n\n
    setCoordinatesMode(final int coordinatesModeInternal)\n
    setCoordinatesMode(final int coordinatesMode)\n
    '''
def getCoordinatesMode():
    '''returns int\n\n
    getCoordinatesMode()\n
    getCoordinatesMode()\n
    '''
def beforeLayout():
    '''returns None\n\n
    beforeLayout(final IlvGraphLayout ilvGraphLayout, final boolean b)\n
    '''
def setAnimationRedrawMode():
    '''returns None\n\n
    setAnimationRedrawMode(final int j)\n
    '''
def getAnimationRedrawMode():
    '''returns int\n\n
    getAnimationRedrawMode()\n
    '''
def afterLayout():
    '''returns None\n\n
    afterLayout(final IlvGraphLayout ilvGraphLayout, final IlvGraphLayoutReport ilvGraphLayoutReport, final boolean b)\n
    '''
def isLayoutNeeded():
    '''returns boolean\n\n
    isLayoutNeeded(final IlvGraphLayout ilvGraphLayout)\n
    '''
def beforeAnimationStep():
    '''returns None\n\n
    beforeAnimationStep()\n
    '''
def afterAnimationStep():
    '''returns None\n\n
    afterAnimationStep()\n
    '''
def moveNode():
    '''returns None\n\n
    moveNode(final Object o, final float n, final float n2, final boolean b)\n
    '''
def getFilter():
    '''returns IlvLayoutGraphicFilter\n\n
    getFilter()\n
    '''
def getLayers():
    '''returns Enumeration\n\n
    getLayers()\n
    '''
def setFullLayerNotification():
    '''returns None\n\n
    setFullLayerNotification(final boolean fullLayerNotification)\n
    '''
def getNodeComparator():
    '''returns Comparator\n\n
    getNodeComparator()\n
    '''
def getLinkComparator():
    '''returns Comparator\n\n
    getLinkComparator()\n
    '''
def setReferenceTransformer():
    '''returns None\n\n
    setReferenceTransformer(final IlvTransformer referenceTransformerInternal)\n
    '''
def getReferenceTransformer():
    '''returns IlvTransformer\n\n
    getReferenceTransformer()\n
    '''
def setReferenceView():
    '''returns None\n\n
    setReferenceView(final IlvManagerView referenceView)\n
    '''
def getReferenceView():
    '''returns IlvManagerView\n\n
    getReferenceView()\n
    '''
def getNodesAndLinks():
    '''returns Enumeration\n\n
    getNodesAndLinks()\n
    '''
def getNodes():
    '''returns Enumeration\n\n
    getNodes()\n
    '''
def getLinks():
    '''returns Enumeration\n\n
    getLinks()\n
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
def getLinksCount():
    '''returns int\n\n
    getLinksCount(final Object o)\n
    '''
def getNeighbors():
    '''returns Enumeration\n\n
    getNeighbors(final Object o)\n
    '''
def getOpposite():
    '''returns Object\n\n
    getOpposite(final Object o, final Object o2)\n
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
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer(final IlvGraphModel ilvGraphModel)\n
    '''
def isLinkBetween():
    '''returns boolean\n\n
    isLinkBetween(final Object o, final Object o2)\n
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
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final Object o)\n
    '''
def getLinkWidth():
    '''returns float\n\n
    getLinkWidth(final Object o)\n
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
def saveAndEnableViewCoordinates():
    '''returns None\n\n
    saveAndEnableViewCoordinates(final IlvGrapherAdapter ilvGrapherAdapter)\n
    '''
def restoreAndDisableViewCoordinates():
    '''returns None\n\n
    restoreAndDisableViewCoordinates()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getLayout():
    '''returns Object\n\n
    getLayout()\n
    '''
def getInstanceId():
    '''returns int\n\n
    getInstanceId()\n
    '''
def getModel():
    '''returns Object\n\n
    getModel()\n
    '''
def setOriginalCoordModeOfModel():
    '''returns None\n\n
    setOriginalCoordModeOfModel(final int n)\n
    '''
def getOriginalCoordModeOfModel():
    '''returns int\n\n
    getOriginalCoordModeOfModel()\n
    '''
def supportsSaveParametersToNamedProperties():
    '''returns boolean\n\n
    supportsSaveParametersToNamedProperties()\n
    '''
def createLayoutManagerProperty():
    '''returns IlvNamedProperty\n\n
    createLayoutManagerProperty(final String s, final boolean b)\n
    '''
def addLayer():
    '''returns None\n\n
    addLayer(final IlvManagerLayer ilvManagerLayer)\n
    '''
def managerCollapsed():
    '''returns None\n\n
    managerCollapsed(final ManagerExpansionEvent managerExpansionEvent)\n
    '''
def managerExpanded():
    '''returns None\n\n
    managerExpanded(final ManagerExpansionEvent managerExpansionEvent)\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphicVector ilvGraphicVector, final Object o)\n
    '''
