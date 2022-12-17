def ():
    '''returns GlyphInfo\n\n
    (final Shape shape, final String s)\n
    (final Shape shape, final String k, final int h, final int i, final double j)\n
    (final IlvTextPath ilvTextPath)\n
    (final IlvInputStream ilvInputStream)\n
    (final Shape shape, final double n)\n
    (final GlyphVector a)\n
    (final double a, final double b, final int e, final double c, final GlyphVector d)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setShape():
    '''returns None\n\n
    setShape(final Shape shape)\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font l)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setAntialiasing():
    '''returns None\n\n
    setAntialiasing(final boolean isAntiAliased)\n
    '''
def setFractionalMetrics():
    '''returns None\n\n
    setFractionalMetrics(final boolean usesFractionalMetrics)\n
    '''
def setExtendedBaseline():
    '''returns None\n\n
    setExtendedBaseline(final boolean b)\n
    '''
def getComponentOrientation():
    '''returns ComponentOrientation\n\n
    getComponentOrientation()\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int t)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
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
def getLength():
    '''returns double\n\n
    getLength()\n
    '''
def isStrokeOn():
    '''returns boolean\n\n
    isStrokeOn()\n
    '''
def setStrokeOn():
    '''returns None\n\n
    setStrokeOn(final boolean strokeOn)\n
    '''
def setStroke():
    '''returns None\n\n
    setStroke(final Stroke stroke)\n
    '''
def setFillPaint():
    '''returns None\n\n
    setFillPaint(final Paint fillPaint)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color fillPaint)\n
    '''
def getVisualBounds():
    '''returns Shape\n\n
    getVisualBounds(final IlvTransformer ilvTransformer)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def getLabelBBox():
    '''returns IlvRect\n\n
    getLabelBBox(final IlvTransformer ilvTransformer)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String k)\n
    '''
def supportMultiline():
    '''returns boolean\n\n
    supportMultiline()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
