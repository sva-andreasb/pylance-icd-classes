def ():
    '''returns IlvLabel\n\n
    ()\n
    (final IlvPoint center, final String label)\n
    (final IlvLabel ilvLabel)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String s)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def supportMultiline():
    '''returns boolean\n\n
    supportMultiline()\n
    '''
def setCenter():
    '''returns None\n\n
    setCenter(final IlvPoint ilvPoint)\n
    '''
def getCenter():
    '''returns IlvPoint\n\n
    getCenter()\n
    '''
def setAntialiasing():
    '''returns None\n\n
    setAntialiasing(final boolean b)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def getLabelBBox():
    '''returns IlvRect\n\n
    getLabelBBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color a)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font c)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def usesBidiMarkers():
    '''returns boolean\n\n
    usesBidiMarkers()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int n, final int n2)\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getCaretShape():
    '''returns Shape\n\n
    getCaretShape(final IlvTextSelection.Range range, final IlvTransformer ilvTransformer)\n
    '''
def pickCharacter():
    '''returns int\n\n
    pickCharacter(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def lineCount():
    '''returns int\n\n
    lineCount()\n
    '''
def lineOffset():
    '''returns int\n\n
    lineOffset(final int n)\n
    '''
