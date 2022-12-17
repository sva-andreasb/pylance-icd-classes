TICK_INSIDE = "int  1"
TICK_OUTSIDE = "int  2"
TICK_CROSS = "int  3"
CONSTANT_SKIP = "int  1"
ADAPTIVE_SKIP = "int  2"
LOWER_SIDE = "int  -1"
UPPER_SIDE = "int  1"
LEFT_SIDE = "int  1"
RIGHT_SIDE = "int  2"
OUTSIDE = "int  1"
INSIDE = "int  2"
def ():
    '''returns Title\n\n
    ()\n
    (final double value, final double value2)\n
    (final IlvTimeUnit timeUnit)\n
    (final String d, final double rotation)\n
    '''
def setAxisStroke():
    '''returns None\n\n
    setAxisStroke(final Stroke stroke)\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def setLabelFont():
    '''returns None\n\n
    setLabelFont(final Font as)\n
    '''
def setLabelColor():
    '''returns None\n\n
    setLabelColor(final Color ao)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(Color ag)\n
    '''
def setDrawOrder():
    '''returns None\n\n
    setDrawOrder(final int s)\n
    '''
def setMajorTickSize():
    '''returns None\n\n
    setMajorTickSize(final int t)\n
    '''
def setMinorTickSize():
    '''returns None\n\n
    setMinorTickSize(final int u)\n
    '''
def setTickLayout():
    '''returns None\n\n
    setTickLayout(final int y)\n
    '''
def setLabelOffset():
    '''returns None\n\n
    setLabelOffset(final int v)\n
    '''
def setTitleOffset():
    '''returns None\n\n
    setTitleOffset(final int w)\n
    '''
def setAutoWrapping():
    '''returns None\n\n
    setAutoWrapping(final boolean ab)\n
    '''
def setLabelAlignment():
    '''returns None\n\n
    setLabelAlignment(final int x)\n
    '''
def getTitleRotation():
    '''returns double\n\n
    getTitleRotation()\n
    '''
def setTitleRotation():
    '''returns None\n\n
    setTitleRotation(final double rotation)\n
    '''
def getTitleFont():
    '''returns Font\n\n
    getTitleFont()\n
    '''
def setTitleFont():
    '''returns None\n\n
    setTitleFont(final Font font)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String text)\n
    setTitle(final String text, final double rotation)\n
    '''
def getTitleRenderer():
    '''returns IlvLabelRenderer\n\n
    getTitleRenderer()\n
    '''
def getTitlePlacement():
    '''returns int\n\n
    getTitlePlacement()\n
    '''
def setTitlePlacement():
    '''returns None\n\n
    setTitlePlacement(final int placement)\n
    '''
def getLabelRotation():
    '''returns double\n\n
    getLabelRotation()\n
    '''
def setLabelRotation():
    '''returns None\n\n
    setLabelRotation(final double aa)\n
    '''
def setSkippingLabel():
    '''returns None\n\n
    setSkippingLabel(final boolean b)\n
    '''
def setSkipLabelMode():
    '''returns None\n\n
    setSkipLabelMode(final int z)\n
    '''
def has3DSupport():
    '''returns boolean\n\n
    has3DSupport()\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final boolean b)\n
    '''
def setAxisVisible():
    '''returns None\n\n
    setAxisVisible(final boolean b)\n
    '''
def setMajorTickVisible():
    '''returns None\n\n
    setMajorTickVisible(final boolean b)\n
    '''
def setMinorTickVisible():
    '''returns None\n\n
    setMinorTickVisible(final boolean b)\n
    '''
def setLabelVisible():
    '''returns None\n\n
    setLabelVisible(final boolean b)\n
    '''
def setAutoCrossing():
    '''returns None\n\n
    setAutoCrossing(final boolean b)\n
    '''
def setCrossing():
    '''returns None\n\n
    setCrossing(final IlvAxis.Crossing crossing)\n
    '''
def setCrossingValue():
    '''returns None\n\n
    setCrossingValue(final double n)\n
    '''
def setAutoSide():
    '''returns None\n\n
    setAutoSide(final boolean b)\n
    '''
def getDefaultSide():
    '''returns int\n\n
    getDefaultSide()\n
    '''
def getSide():
    '''returns int\n\n
    getSide()\n
    '''
def setSide():
    '''returns None\n\n
    setSide(final int n)\n
    '''
def getRadialSide():
    '''returns int\n\n
    getRadialSide()\n
    '''
def setRadialSide():
    '''returns None\n\n
    setRadialSide(final int n)\n
    '''
def getCircleSide():
    '''returns int\n\n
    getCircleSide()\n
    '''
def setCircleSide():
    '''returns None\n\n
    setCircleSide(final int n)\n
    '''
def setStepsDefinition():
    '''returns None\n\n
    setStepsDefinition(final IlvStepsDefinition al)\n
    '''
def setStepUnit():
    '''returns None\n\n
    setStepUnit(final Double n, final Double n2)\n
    '''
def setTimeUnit():
    '''returns None\n\n
    setTimeUnit(final IlvTimeUnit unit)\n
    '''
def setCategory():
    '''returns None\n\n
    setCategory(final IlvDataSet set, final boolean b)\n
    '''
def setLogarithmic():
    '''returns None\n\n
    setLogarithmic(final double n)\n
    '''
def toValue():
    '''returns double\n\n
    toValue(final int n, final int n2)\n
    '''
def toPoint():
    '''returns Point\n\n
    toPoint(final double n)\n
    '''
def getBoundsUsingCache():
    '''returns Rectangle2D\n\n
    getBoundsUsingCache(Rectangle2D rectangle2D)\n
    '''
def drawSelectionHandles():
    '''returns None\n\n
    drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle)\n
    '''
def drawHighlight():
    '''returns None\n\n
    drawHighlight(final Graphics graphics)\n
    '''
def hit():
    '''returns boolean\n\n
    hit(final Point2D point2D)\n
    '''
def drawIntoHitmap():
    '''returns None\n\n
    drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)\n
    '''
def getAnnotations():
    '''returns IlvScaleAnnotation[]\n\n
    getAnnotations()\n
    '''
def setAnnotations():
    '''returns None\n\n
    setAnnotations(final IlvScaleAnnotation[] array)\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final IlvScaleAnnotation ilvScaleAnnotation)\n
    '''
def removeAnnotation():
    '''returns None\n\n
    removeAnnotation(final IlvScaleAnnotation ilvScaleAnnotation)\n
    '''
def updateAnnotations():
    '''returns None\n\n
    updateAnnotations()\n
    '''
def getLabelBounds():
    '''returns Rectangle2D\n\n
    getLabelBounds(final int n, final Rectangle2D rectangle2D)\n
    '''
def getLabelCount():
    '''returns int\n\n
    getLabelCount()\n
    '''
def getLabelValue():
    '''returns double\n\n
    getLabelValue(final int n)\n
    '''
def setLabelFormat():
    '''returns None\n\n
    setLabelFormat(final IlvValueFormat ar)\n
    '''
def computeLabel():
    '''returns String\n\n
    computeLabel(final double n)\n
    '''
def getTitleBackgroundShape():
    '''returns Shape\n\n
    getTitleBackgroundShape()\n
    '''
def axisRangeChanged():
    '''returns None\n\n
    axisRangeChanged(final AxisRangeEvent axisRangeEvent)\n
    '''
def axisChanged():
    '''returns None\n\n
    axisChanged(final AxisChangeEvent axisChangeEvent)\n
    '''
def stateChanged():
    '''returns None\n\n
    stateChanged()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String d)\n
    '''
def getLabelRenderer():
    '''returns IlvLabelRenderer\n\n
    getLabelRenderer()\n
    '''
def setPlacement():
    '''returns None\n\n
    setPlacement(int c)\n
    '''
def getPlacement():
    '''returns int\n\n
    getPlacement()\n
    '''
def getSize2D():
    '''returns Dimension2D\n\n
    getSize2D(final boolean b)\n
    '''
