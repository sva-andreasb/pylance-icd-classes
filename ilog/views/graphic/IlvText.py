OUTLINE_ONLY = "int  2048"
OUTLINE_FRONT = "int  6144"
OUTLINE_BACK = "int  4096"
OUTLINE_DISABLED = "int  0"
WRAP_NONE = "short  0"
WRAP_WORD = "short  1"
WRAP_CHARACTER = "short  4"
WRAP_TRUNCATE = "short  2"
NO_AUTO_WRAPPING = "int  0"
SIZE_AUTO_WRAPPING = "int  1"
ZOOM_AUTO_WRAPPING = "int  2"
def ():
    '''returns LabelSetter\n\n
    ()\n
    (final IlvPoint location, final String s)\n
    (final IlvText ilvText)\n
    (final IlvInputStream ilvInputStream)\n
    ()\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(final IlvRect ilvRect)\n
    '''
def translate():
    '''returns None\n\n
    translate(float n, float n2)\n
    '''
def resize():
    '''returns None\n\n
    resize(final float n, final float n2)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final IlvPoint ilvPoint, final double n)\n
    '''
def getAnchorPoints():
    '''returns IlvPoint[]\n\n
    getAnchorPoints(final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String s)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def setAttributedLabel():
    '''returns None\n\n
    setAttributedLabel(final AttributedString t)\n
    '''
def getAttributedLabel():
    '''returns AttributedString\n\n
    getAttributedLabel()\n
    '''
def addLabelAttribute():
    '''returns None\n\n
    addLabelAttribute(final AttributedCharacterIterator.Attribute attribute, final Object value)\n
    addLabelAttribute(final AttributedCharacterIterator.Attribute attribute, final Object value, final int beginIndex, final int endIndex)\n
    '''
def addLabelAttributes():
    '''returns None\n\n
    addLabelAttributes(final Map attributes, final int beginIndex, final int endIndex)\n
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
    setFont(final Font v)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def getOutlineMode():
    '''returns int\n\n
    getOutlineMode()\n
    '''
def setOutlineMode():
    '''returns None\n\n
    setOutlineMode(final int n)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color x)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setOutlineColor():
    '''returns None\n\n
    setOutlineColor(final Color aj)\n
    '''
def getOutlineColor():
    '''returns Color\n\n
    getOutlineColor()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color fillPaint)\n
    '''
def setFillPaint():
    '''returns None\n\n
    setFillPaint(final Paint ad)\n
    '''
def getFillPaint():
    '''returns Paint\n\n
    getFillPaint()\n
    '''
def setOutlineThickness():
    '''returns None\n\n
    setOutlineThickness(final float ak)\n
    '''
def getOutlineThickness():
    '''returns float\n\n
    getOutlineThickness()\n
    '''
def setRotationAlignmentThresholdAngle():
    '''returns None\n\n
    setRotationAlignmentThresholdAngle(float al)\n
    '''
def setRotationAlignmentAngle():
    '''returns None\n\n
    setRotationAlignmentAngle(float am)\n
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
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def getDefaultInteractor():
    '''returns String\n\n
    getDefaultInteractor()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
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
def isLocaleSensitive():
    '''returns boolean\n\n
    isLocaleSensitive()\n
    '''
def localeChanged():
    '''returns None\n\n
    localeChanged(final ULocale uLocale, final ULocale uLocale2)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
