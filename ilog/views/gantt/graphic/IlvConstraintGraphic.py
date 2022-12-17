DEFAULT_HORIZONTAL_EXTREMITY_SEGMENT_LENGTH = "float  10.0f"
DEFAULT_VERTICAL_EXTREMITY_SEGMENT_LENGTH = "float  10.0f"
TIME_INTERVAL_CONNECTION = "int  0"
BOUNDING_BOX_CONNECTION = "int  1"
def ():
    '''returns IlvConstraintGraphic\n\n
    ()\n
    (final IlvActivityGraphic ilvActivityGraphic, final IlvActivityGraphic ilvActivityGraphic2, final IlvConstraint b)\n
    '''
def getConstraint():
    '''returns IlvConstraint\n\n
    getConstraint()\n
    '''
def setConstraint():
    '''returns None\n\n
    setConstraint(final IlvConstraint b)\n
    '''
def getGanttSheet():
    '''returns IlvGanttSheet\n\n
    getGanttSheet()\n
    '''
def getHorizontalExtremitySegmentLength():
    '''returns float\n\n
    getHorizontalExtremitySegmentLength()\n
    '''
def setHorizontalExtremitySegmentLength():
    '''returns None\n\n
    setHorizontalExtremitySegmentLength(final float c)\n
    '''
def getConnectionPoints():
    '''returns None\n\n
    getConnectionPoints(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int n, final IlvTransformer ilvTransformer)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def allowsPointInsertion():
    '''returns boolean\n\n
    allowsPointInsertion()\n
    '''
def allowsPointRemoval():
    '''returns boolean\n\n
    allowsPointRemoval()\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def getArrowSize():
    '''returns float\n\n
    getArrowSize()\n
    '''
def setArrowSize():
    '''returns None\n\n
    setArrowSize(final float f)\n
    '''
def getConnectionType():
    '''returns int\n\n
    getConnectionType()\n
    '''
def setConnectionType():
    '''returns None\n\n
    setConnectionType(final int a)\n
    '''
def getEndCap():
    '''returns int\n\n
    getEndCap()\n
    '''
def getLineJoin():
    '''returns int\n\n
    getLineJoin()\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
