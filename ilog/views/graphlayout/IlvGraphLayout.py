INVERSE_VIEW_COORDINATES = "int  0"
MANAGER_COORDINATES = "int  1"
VIEW_COORDINATES = "int  2"
def ():
    '''returns IlvGraphLayout\n\n
    ()\n
    (final IlvGraphLayout ilvGraphLayout)\n
    '''
def copyParameters():
    '''returns None\n\n
    copyParameters(final IlvGraphLayout ilvGraphLayout)\n
    '''
def cleanGraphModel():
    '''returns None\n\n
    cleanGraphModel(final IlvGraphModel ilvGraphModel)\n
    '''
def cleanNode():
    '''returns None\n\n
    cleanNode(final IlvGraphModel ilvGraphModel, final Object o)\n
    '''
def cleanLink():
    '''returns None\n\n
    cleanLink(final IlvGraphModel ilvGraphModel, final Object o)\n
    '''
def setGraphModel():
    '''returns None\n\n
    setGraphModel(final IlvGraphModel bm)\n
    '''
def getGraphModel():
    '''returns IlvGraphModel\n\n
    getGraphModel()\n
    '''
def setGrapher():
    '''returns None\n\n
    setGrapher(final IlvGrapher ilvGrapher)\n
    '''
def getGrapher():
    '''returns IlvGrapher\n\n
    getGrapher()\n
    '''
def setParentLayout():
    '''returns None\n\n
    setParentLayout(final IlvGraphLayout bo)\n
    '''
def getParentLayout():
    '''returns IlvGraphLayout\n\n
    getParentLayout()\n
    '''
def createLayoutReport():
    '''returns IlvGraphLayoutReport\n\n
    createLayoutReport()\n
    '''
def checkAppropriateLinks():
    '''returns None\n\n
    checkAppropriateLinks()\n
    '''
def checkAppropriateLink():
    '''returns int\n\n
    checkAppropriateLink(final Object o)\n
    '''
def setAutoCheckAppropriateLinksEnabled():
    '''returns boolean\n\n
    setAutoCheckAppropriateLinksEnabled(final boolean b)\n
    '''
def getMovingNodes():
    '''returns IlvGraphicVector\n\n
    getMovingNodes()\n
    '''
def getRecursiveLayout():
    '''returns IlvRecursiveLayout\n\n
    getRecursiveLayout()\n
    '''
def getLayouts():
    '''returns Enumeration\n\n
    getLayouts(final boolean b)\n
    '''
def getLayout():
    '''returns IlvGraphLayout\n\n
    getLayout(final Object o)\n
    '''
def isLocalRecursiveLayoutNeeded():
    '''returns boolean\n\n
    isLocalRecursiveLayoutNeeded(final IlvLayoutProvider ilvLayoutProvider, final IlvGraphLayout ilvGraphLayout, final IlvGraphModel ilvGraphModel, final boolean b)\n
    '''
def setLayoutRunning():
    '''returns None\n\n
    setLayoutRunning(final boolean bf, final boolean b)\n
    '''
def layoutStepPerformed():
    '''returns None\n\n
    layoutStepPerformed()\n
    '''
def getMinBusyTime():
    '''returns long\n\n
    getMinBusyTime()\n
    '''
def setStructureUpToDate():
    '''returns None\n\n
    setStructureUpToDate(final boolean bc)\n
    '''
def isStructureUpToDate():
    '''returns boolean\n\n
    isStructureUpToDate()\n
    '''
def setGeometryUpToDate():
    '''returns None\n\n
    setGeometryUpToDate(final boolean bd)\n
    '''
def isGeometryUpToDate():
    '''returns boolean\n\n
    isGeometryUpToDate()\n
    '''
def setCoordinatesMode():
    '''returns None\n\n
    setCoordinatesMode(final int an)\n
    '''
def getCoordinatesMode():
    '''returns int\n\n
    getCoordinatesMode()\n
    '''
def onParameterChanged():
    '''returns None\n\n
    onParameterChanged(final String s)\n
    onParameterChanged(final Object o, final String s)\n
    '''
def setParametersUpToDate():
    '''returns None\n\n
    setParametersUpToDate(final boolean be)\n
    '''
def isParametersUpToDate():
    '''returns boolean\n\n
    isParametersUpToDate()\n
    '''
def isUseDefaultParameters():
    '''returns boolean\n\n
    isUseDefaultParameters()\n
    '''
def setInputCheckEnabled():
    '''returns None\n\n
    setInputCheckEnabled(final boolean al)\n
    '''
def supportsPreserveFixedNodes():
    '''returns boolean\n\n
    supportsPreserveFixedNodes()\n
    '''
def isPreserveFixedNodes():
    '''returns boolean\n\n
    isPreserveFixedNodes()\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed(final Object o)\n
    '''
def supportsPreserveFixedLinks():
    '''returns boolean\n\n
    supportsPreserveFixedLinks()\n
    '''
def isPreserveFixedLinks():
    '''returns boolean\n\n
    isPreserveFixedLinks()\n
    '''
def supportsAnimation():
    '''returns boolean\n\n
    supportsAnimation()\n
    '''
def isAnimate():
    '''returns boolean\n\n
    isAnimate()\n
    '''
def useAnimateRedraw():
    '''returns boolean\n\n
    useAnimateRedraw()\n
    '''
def supportsPercentageComplete():
    '''returns boolean\n\n
    supportsPercentageComplete()\n
    '''
def increasePercentageComplete():
    '''returns None\n\n
    increasePercentageComplete(final int n)\n
    '''
def supportsStopImmediately():
    '''returns boolean\n\n
    supportsStopImmediately()\n
    '''
def stopImmediately():
    '''returns boolean\n\n
    stopImmediately()\n
    '''
def isStoppedImmediately():
    '''returns boolean\n\n
    isStoppedImmediately()\n
    '''
def setLayoutOfConnectedComponentsEnabled():
    '''returns None\n\n
    setLayoutOfConnectedComponentsEnabled(final boolean am)\n
    '''
def isLayoutOfConnectedComponentsEnabled():
    '''returns boolean\n\n
    isLayoutOfConnectedComponentsEnabled()\n
    '''
def setLayoutOfConnectedComponents():
    '''returns None\n\n
    setLayoutOfConnectedComponents(final IlvGraphLayout a6)\n
    '''
def getLayoutOfConnectedComponents():
    '''returns IlvGraphLayout\n\n
    getLayoutOfConnectedComponents()\n
    '''
def supportsMemorySavings():
    '''returns boolean\n\n
    supportsMemorySavings()\n
    '''
def isMemorySavings():
    '''returns boolean\n\n
    isMemorySavings()\n
    '''
def supportsLayoutRegion():
    '''returns boolean\n\n
    supportsLayoutRegion()\n
    '''
def getSpecLayoutRegion():
    '''returns IlvRect\n\n
    getSpecLayoutRegion()\n
    '''
def getLayoutRegion():
    '''returns IlvRect\n\n
    getLayoutRegion()\n
    '''
def getCalcLayoutRegion():
    '''returns IlvRect\n\n
    getCalcLayoutRegion()\n
    '''
def isFitToView():
    '''returns boolean\n\n
    isFitToView()\n
    '''
def supportsRandomGenerator():
    '''returns boolean\n\n
    supportsRandomGenerator()\n
    '''
def setSeedValueForRandomGenerator():
    '''returns None\n\n
    setSeedValueForRandomGenerator(final long aj)\n
    '''
def getSeedValueForRandomGenerator():
    '''returns long\n\n
    getSeedValueForRandomGenerator()\n
    '''
def setUseSeedValueForRandomGenerator():
    '''returns None\n\n
    setUseSeedValueForRandomGenerator(final boolean ak)\n
    '''
def isUseSeedValueForRandomGenerator():
    '''returns boolean\n\n
    isUseSeedValueForRandomGenerator()\n
    '''
def supportsAllowedTime():
    '''returns boolean\n\n
    supportsAllowedTime()\n
    '''
def getAllowedTime():
    '''returns long\n\n
    getAllowedTime()\n
    '''
def supportsLayoutOfConnectedComponents():
    '''returns boolean\n\n
    supportsLayoutOfConnectedComponents()\n
    '''
def contentsChanged():
    '''returns None\n\n
    contentsChanged(final GraphModelEvent graphModelEvent)\n
    '''
def setAutoLayoutHandler():
    '''returns None\n\n
    setAutoLayoutHandler(final IlvAutoLayoutHandler ar)\n
    '''
def getAutoLayoutHandler():
    '''returns IlvAutoLayoutHandler\n\n
    getAutoLayoutHandler()\n
    '''
def setAutoLayout():
    '''returns None\n\n
    setAutoLayout(final boolean ai)\n
    '''
def supportsLinkConnectionBox():
    '''returns boolean\n\n
    supportsLinkConnectionBox()\n
    '''
def setLinkConnectionBoxInterface():
    '''returns None\n\n
    setLinkConnectionBoxInterface(final IlvLinkConnectionBoxInterface aq)\n
    '''
def getLinkConnectionBoxInterface():
    '''returns IlvLinkConnectionBoxInterface\n\n
    getLinkConnectionBoxInterface()\n
    '''
def supportsLinkClipping():
    '''returns boolean\n\n
    supportsLinkClipping()\n
    '''
def setLinkClipInterface():
    '''returns None\n\n
    setLinkClipInterface(final IlvLinkClipInterface ap)\n
    '''
def getLinkClipInterface():
    '''returns IlvLinkClipInterface\n\n
    getLinkClipInterface()\n
    '''
def clipLink():
    '''returns None\n\n
    clipLink(final Object o, final boolean b, final boolean b2, final boolean b3, final boolean b4)\n
    '''
def clipAllLinks():
    '''returns None\n\n
    clipAllLinks(final boolean b, final boolean b2)\n
    '''
def connectLinkToCenter():
    '''returns None\n\n
    connectLinkToCenter(final Object o, final boolean b, final boolean b2, final boolean b3)\n
    '''
def connectAllLinksToCenter():
    '''returns None\n\n
    connectAllLinksToCenter(final boolean b)\n
    '''
def supportsSplineRouting():
    '''returns boolean\n\n
    supportsSplineRouting()\n
    '''
def setSplineRoutingEnabled():
    '''returns None\n\n
    setSplineRoutingEnabled(final boolean as)\n
    '''
def isSplineRoutingEnabled():
    '''returns boolean\n\n
    isSplineRoutingEnabled()\n
    '''
def setMinSplineCurveSize():
    '''returns None\n\n
    setMinSplineCurveSize(final float at)\n
    '''
def getMinSplineCurveSize():
    '''returns float\n\n
    getMinSplineCurveSize()\n
    '''
def setMaxSplineCurveSize():
    '''returns None\n\n
    setMaxSplineCurveSize(final float au)\n
    '''
def getMaxSplineCurveSize():
    '''returns float\n\n
    getMaxSplineCurveSize()\n
    '''
def setBalanceSplineCurveThreshold():
    '''returns None\n\n
    setBalanceSplineCurveThreshold(final float av)\n
    '''
def getBalanceSplineCurveThreshold():
    '''returns float\n\n
    getBalanceSplineCurveThreshold()\n
    '''
def setSplineLinkFilter():
    '''returns None\n\n
    setSplineLinkFilter(final IlvSplineLinkFilter aw)\n
    '''
def getSplineLinkFilter():
    '''returns IlvSplineLinkFilter\n\n
    getSplineLinkFilter()\n
    '''
def supportsSaveParametersToNamedProperties():
    '''returns boolean\n\n
    supportsSaveParametersToNamedProperties()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
