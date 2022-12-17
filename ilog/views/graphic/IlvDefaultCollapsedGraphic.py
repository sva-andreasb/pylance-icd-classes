def ():
    '''returns IlvDefaultCollapsedGraphic\n\n
    ()\n
    (final IlvDefaultCollapsedGraphic ilvDefaultCollapsedGraphic)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
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
def getLabelBBox():
    '''returns IlvRect\n\n
    getLabelBBox(final IlvTransformer ilvTransformer)\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font font)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setLabelFillPaint():
    '''returns None\n\n
    setLabelFillPaint(final Paint fillPaint)\n
    '''
def getLabelFillPaint():
    '''returns Paint\n\n
    getLabelFillPaint()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def usesBidiMarkers():
    '''returns boolean\n\n
    usesBidiMarkers()\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int n, final int baseTextDirection)\n
    '''
