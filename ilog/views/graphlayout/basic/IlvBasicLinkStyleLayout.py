STRAIGHT_LINE_STYLE = "int  1"
NO_RESHAPE_STYLE = "int  0"
NO_BUNDLE = "int  0"
STRAIGHT_LINE_BUNDLE = "int  1"
NARROW_STRAIGHT_LINE_BUNDLE = "int  10"
CONNECTED_ONE_BEND_BUNDLE = "int  11"
FREE_ONE_BEND_BUNDLE = "int  12"
NO_BENDS = "int  0"
CONNECTED_RECTANGULAR = "int  16"
FREE_RECTANGULAR = "int  17"
CONNECTED_SQUARE = "int  32"
FREE_SQUARE = "int  33"
NARROW_CONNECTED_RECTANGULAR = "int  18"
NARROW_FREE_RECTANGULAR = "int  19"
NARROW_CONNECTED_SQUARE = "int  34"
NARROW_FREE_SQUARE = "int  35"
TOP_LEFT = "int  1"
BOTTOM_LEFT = "int  2"
TOP_RIGHT = "int  4"
BOTTOM_RIGHT = "int  8"
ALL_CORNERS = "int  15"
CLOCK_WISE = "int  0"
COUNTER_CLOCK_WISE = "int  1"
HORIZONTAL_TO_VERTICAL = "int  2"
VERTICAL_TO_HORIZONTAL = "int  3"
CENTERED = "int  0"
OUTER = "int  1"
INNER = "int  2"
def ():
    '''returns IlvBasicLinkStyleLayout\n\n
    ()\n
    (final IlvBasicLinkStyleLayout ilvBasicLinkStyleLayout)\n
    '''
def copy():
    '''returns IlvGraphLayout\n\n
    copy()\n
    '''
def copyParameters():
    '''returns None\n\n
    copyParameters(final IlvGraphLayout ilvGraphLayout)\n
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
def increasePercentageComplete():
    '''returns None\n\n
    increasePercentageComplete(final int n)\n
    '''
def setLinkStyle():
    '''returns None\n\n
    setLinkStyle(final int q)\n
    '''
def getLinkStyle():
    '''returns int\n\n
    getLinkStyle()\n
    '''
def setConnectLinksToNodeCenters():
    '''returns None\n\n
    setConnectLinksToNodeCenters(final boolean p)\n
    '''
def isConnectLinksToNodeCenters():
    '''returns boolean\n\n
    isConnectLinksToNodeCenters()\n
    '''
def setMultiLinkMode():
    '''returns None\n\n
    setMultiLinkMode(final int r)\n
    '''
def getMultiLinkMode():
    '''returns int\n\n
    getMultiLinkMode()\n
    '''
def setSelfLinkMode():
    '''returns None\n\n
    setSelfLinkMode(final int u)\n
    '''
def getSelfLinkMode():
    '''returns int\n\n
    getSelfLinkMode()\n
    '''
def setSelfLinkOrientation():
    '''returns None\n\n
    setSelfLinkOrientation(final int v)\n
    '''
def getSelfLinkOrientation():
    '''returns int\n\n
    getSelfLinkOrientation()\n
    '''
def setSelfLinkAllowedCorners():
    '''returns None\n\n
    setSelfLinkAllowedCorners(final int w)\n
    '''
def setMultiSelfLinkDistribution():
    '''returns None\n\n
    setMultiSelfLinkDistribution(final int ab)\n
    '''
def getMultiSelfLinkDistribution():
    '''returns int\n\n
    getMultiSelfLinkDistribution()\n
    '''
def checkAppropriateLinks():
    '''returns None\n\n
    checkAppropriateLinks()\n
    '''
def checkAppropriateLink():
    '''returns int\n\n
    checkAppropriateLink(final Object o)\n
    '''
def getMovingNodes():
    '''returns IlvGraphicVector\n\n
    getMovingNodes()\n
    '''
