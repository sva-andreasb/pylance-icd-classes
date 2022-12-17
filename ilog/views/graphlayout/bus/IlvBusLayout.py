NO_ORDERING = "int  0"
ORDER_BY_HEIGHT = "int  1"
ORDER_BY_INDEX = "int  2"
NO_INDEX = "int  -1"
STRAIGHT_LINE_STYLE = "int  1"
NO_RESHAPE_STYLE = "int  0"
CENTER = "int  0"
TOP = "int  3"
BOTTOM = "int  4"
MIXED = "int  99"
LEFT_TO_RIGHT = "int  0"
ALTERNATE = "int  1"
NODES_ABOVE_BUS = "int  0"
NODES_BELOW_BUS = "int  1"
def ():
    '''returns IlvBusLayout\n\n
    ()\n
    (final IlvBusLayout ilvBusLayout)\n
    '''
def copy():
    '''returns IlvGraphLayout\n\n
    copy()\n
    '''
def copyParameters():
    '''returns None\n\n
    copyParameters(final IlvGraphLayout ilvGraphLayout)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def setBus():
    '''returns None\n\n
    setBus(final IlvPolyPointsInterface ilvPolyPointsInterface)\n
    '''
def getBus():
    '''returns IlvPolyPointsInterface\n\n
    getBus()\n
    '''
def setIndex():
    '''returns None\n\n
    setIndex(final Object o, final int n)\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final Object o)\n
    '''
def getLinkConnector():
    '''returns IlvBusLinkConnector\n\n
    getLinkConnector()\n
    '''
def getConnectionPoint():
    '''returns IlvPoint\n\n
    getConnectionPoint(final Object o, final IlvPolyPointsInterface ilvPolyPointsInterface)\n
    '''
def getFlowDirection():
    '''returns int\n\n
    getFlowDirection()\n
    '''
def getOrdering():
    '''returns int\n\n
    getOrdering()\n
    '''
def getNodeComparator():
    '''returns Comparator\n\n
    getNodeComparator()\n
    '''
def setHorizontalOffset():
    '''returns None\n\n
    setHorizontalOffset(final float u)\n
    '''
def getHorizontalOffset():
    '''returns float\n\n
    getHorizontalOffset()\n
    '''
def setVerticalOffsetToLevel():
    '''returns None\n\n
    setVerticalOffsetToLevel(final float v)\n
    '''
def getVerticalOffsetToLevel():
    '''returns float\n\n
    getVerticalOffsetToLevel()\n
    '''
def setVerticalOffsetToPreviousLevel():
    '''returns None\n\n
    setVerticalOffsetToPreviousLevel(final float w)\n
    '''
def getVerticalOffsetToPreviousLevel():
    '''returns float\n\n
    getVerticalOffsetToPreviousLevel()\n
    '''
def setMargin():
    '''returns None\n\n
    setMargin(final float x)\n
    '''
def getMargin():
    '''returns float\n\n
    getMargin()\n
    '''
def setMarginOnBus():
    '''returns None\n\n
    setMarginOnBus(final float y)\n
    '''
def getMarginOnBus():
    '''returns float\n\n
    getMarginOnBus()\n
    '''
def setConnectionOnBusMargin():
    '''returns None\n\n
    setConnectionOnBusMargin(final float z)\n
    '''
def getConnectionOnBusMargin():
    '''returns float\n\n
    getConnectionOnBusMargin()\n
    '''
def setMaxNumberOfNodesPerLevel():
    '''returns None\n\n
    setMaxNumberOfNodesPerLevel(final int aa)\n
    '''
def getMaxNumberOfNodesPerLevel():
    '''returns int\n\n
    getMaxNumberOfNodesPerLevel()\n
    '''
def setBusWidthAdjustingEnabled():
    '''returns None\n\n
    setBusWidthAdjustingEnabled(final boolean ab)\n
    '''
def isBusWidthAdjustingEnabled():
    '''returns boolean\n\n
    isBusWidthAdjustingEnabled()\n
    '''
def setBusLineExtremityAdjustingEnabled():
    '''returns None\n\n
    setBusLineExtremityAdjustingEnabled(final boolean ac)\n
    '''
def isBusLineExtremityAdjustingEnabled():
    '''returns boolean\n\n
    isBusLineExtremityAdjustingEnabled()\n
    '''
def setLinkStyle():
    '''returns None\n\n
    setLinkStyle(final int ae)\n
    '''
def getLinkStyle():
    '''returns int\n\n
    getLinkStyle()\n
    '''
def setIncrementalMode():
    '''returns None\n\n
    setIncrementalMode(final boolean af)\n
    '''
def isIncrementalMode():
    '''returns boolean\n\n
    isIncrementalMode()\n
    '''
def checkAppropriateLink():
    '''returns int\n\n
    checkAppropriateLink(final Object o)\n
    '''
def getMovingNodes():
    '''returns IlvGraphicVector\n\n
    getMovingNodes()\n
    '''
def isFloatingNodeValid():
    '''returns boolean\n\n
    isFloatingNodeValid(final Object o)\n
    '''
def isFixedNodeValid():
    '''returns boolean\n\n
    isFixedNodeValid(final Object o)\n
    '''
def isReversedOrder():
    '''returns boolean\n\n
    isReversedOrder(final int n, final int n2, final IlvRect ilvRect, final float n3)\n
    '''
def transferLayoutOptions():
    '''returns None\n\n
    transferLayoutOptions(final IlvRect ilvRect)\n
    '''
