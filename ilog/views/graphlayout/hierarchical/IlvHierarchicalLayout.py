NO_RESHAPE_STYLE = "int  0"
STRAIGHT_LINE_STYLE = "int  1"
ORTHOGONAL_STYLE = "int  2"
POLYLINE_STYLE = "int  3"
MIXED_STYLE = "int  99"
AUTOMATIC_PINS = "int  0"
CENTERED_PINS = "int  1"
CLIPPED_PINS = "int  2"
EVENLY_SPACED_PINS = "int  3"
EAST = "int  6"
WEST = "int  7"
NORTH = "int  8"
SOUTH = "int  9"
UNSPECIFIED = "int  -1"
FREE_MODE = "int  0"
FIXED_MODE = "int  3"
FIXED_IN_X_MODE = "int  1"
FIXED_IN_Y_MODE = "int  2"
MIXED_MODE = "int  99"
OPTIMAL = "int  0"
SEMI_OPTIMAL = "int  1"
HIGHER_LEVELS = "int  2"
LOWER_LEVELS = "int  3"
SPREAD_OUT = "int  4"
def ():
    '''returns IlvHierarchicalLayout\n\n
    ()\n
    (final IlvHierarchicalLayout ilvHierarchicalLayout)\n
    '''
def copy():
    '''returns IlvGraphLayout\n\n
    copy()\n
    '''
def copyParameters():
    '''returns None\n\n
    copyParameters(final IlvGraphLayout ilvGraphLayout)\n
    '''
def getAllowedTime():
    '''returns long\n\n
    getAllowedTime()\n
    '''
def supportsStopImmediately():
    '''returns boolean\n\n
    supportsStopImmediately()\n
    '''
def stopImmediately():
    '''returns boolean\n\n
    stopImmediately()\n
    '''
def supportsLinkConnectionBox():
    '''returns boolean\n\n
    supportsLinkConnectionBox()\n
    '''
def supportsLinkClipping():
    '''returns boolean\n\n
    supportsLinkClipping()\n
    '''
def supportsSaveParametersToNamedProperties():
    '''returns boolean\n\n
    supportsSaveParametersToNamedProperties()\n
    '''
def setMinForkSegmentLength():
    '''returns None\n\n
    setMinForkSegmentLength(final float ad)\n
    '''
def setPreferredForkAxisLength():
    '''returns None\n\n
    setPreferredForkAxisLength(final float ae)\n
    '''
def getFromPortIndex():
    '''returns int\n\n
    getFromPortIndex(final Object o)\n
    '''
def getToPortIndex():
    '''returns int\n\n
    getToPortIndex(final Object o)\n
    '''
def getFromPortSide():
    '''returns int\n\n
    getFromPortSide(final Object o)\n
    '''
def getToPortSide():
    '''returns int\n\n
    getToPortSide(final Object o)\n
    '''
def getNumberOfPorts():
    '''returns int\n\n
    getNumberOfPorts(final Object o, final int n)\n
    '''
def getOriginPointMode():
    '''returns int\n\n
    getOriginPointMode(final Object o)\n
    '''
def getDestinationPointMode():
    '''returns int\n\n
    getDestinationPointMode(final Object o)\n
    '''
def getNumberOfNodeGroups():
    '''returns int\n\n
    getNumberOfNodeGroups()\n
    '''
def getNodeGroups():
    '''returns Enumeration\n\n
    getNodeGroups()\n
    '''
def getLabelLayout():
    '''returns IlvAnnealingLabelLayout\n\n
    getLabelLayout()\n
    '''
def supportsSplineRouting():
    '''returns boolean\n\n
    supportsSplineRouting()\n
    '''
def isLocalRecursiveLayoutNeeded():
    '''returns boolean\n\n
    isLocalRecursiveLayoutNeeded(final IlvLayoutProvider c7, final IlvGraphLayout ilvGraphLayout, final IlvGraphModel ilvGraphModel, final boolean b)\n
    '''
def cleanNode():
    '''returns None\n\n
    cleanNode(final IlvGraphModel ilvGraphModel, final Object o)\n
    '''
def cleanLink():
    '''returns None\n\n
    cleanLink(final IlvGraphModel ilvGraphModel, final Object o)\n
    '''
def checkAppropriateLinks():
    '''returns None\n\n
    checkAppropriateLinks()\n
    '''
def getGraphLayout():
    '''returns IlvGraphLayout\n\n
    getGraphLayout(final IlvGraphModel ilvGraphModel)\n
    '''
def checkAppropriateLink():
    '''returns int\n\n
    checkAppropriateLink(final Object o)\n
    '''
def getMovingNodes():
    '''returns IlvGraphicVector\n\n
    getMovingNodes()\n
    '''
def layoutStepPerformed():
    '''returns None\n\n
    layoutStepPerformed()\n
    '''
