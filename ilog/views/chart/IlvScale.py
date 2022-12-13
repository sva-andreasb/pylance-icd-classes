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
def IlvScale():
    '''public IlvScale()
    public IlvScale(final double value, final double value2)
    public IlvScale(final IlvTimeUnit timeUnit)
    '''
def getComponentOrientation():
    '''public final ComponentOrientation getComponentOrientation()
    '''
def getAxisStroke():
    '''public final Stroke getAxisStroke()
    '''
def setAxisStroke():
    '''public void setAxisStroke(final Stroke stroke)
    '''
def getResolvedBaseTextDirection():
    '''public int getResolvedBaseTextDirection()
    '''
def getLabelFont():
    '''public final Font getLabelFont()
    '''
def setLabelFont():
    '''public void setLabelFont(final Font as)
    '''
def getLabelColor():
    '''public final Color getLabelColor()
    '''
def setLabelColor():
    '''public void setLabelColor(final Color ao)
    '''
def getForeground():
    '''public Color getForeground()
    '''
def setForeground():
    '''public void setForeground(Color ag)
    '''
def getDrawOrder():
    '''public final int getDrawOrder()
    '''
def setDrawOrder():
    '''public void setDrawOrder(final int s)
    '''
def getMajorTickSize():
    '''public final int getMajorTickSize()
    '''
def setMajorTickSize():
    '''public void setMajorTickSize(final int t)
    '''
def getMinorTickSize():
    '''public final int getMinorTickSize()
    '''
def setMinorTickSize():
    '''public void setMinorTickSize(final int u)
    '''
def getTickLayout():
    '''public final int getTickLayout()
    '''
def setTickLayout():
    '''public void setTickLayout(final int y)
    '''
def getLabelOffset():
    '''public final int getLabelOffset()
    '''
def setLabelOffset():
    '''public void setLabelOffset(final int v)
    '''
def getTitleOffset():
    '''public final int getTitleOffset()
    '''
def setTitleOffset():
    '''public void setTitleOffset(final int w)
    '''
def isAutoWrapping():
    '''public final boolean isAutoWrapping()
    '''
def setAutoWrapping():
    '''public void setAutoWrapping(final boolean ab)
    '''
def getLabelAlignment():
    '''public final int getLabelAlignment()
    '''
def setLabelAlignment():
    '''public void setLabelAlignment(final int x)
    '''
def getTitleRotation():
    '''public double getTitleRotation()
    '''
def setTitleRotation():
    '''public void setTitleRotation(final double rotation)
    '''
def getTitleFont():
    '''public Font getTitleFont()
    '''
def setTitleFont():
    '''public void setTitleFont(final Font font)
    '''
def getTitle():
    '''public final String getTitle()
    '''
def setTitle():
    '''public void setTitle(final String text)
    public void setTitle(final String text, final double rotation)
    '''
def getTitleRenderer():
    '''public IlvLabelRenderer getTitleRenderer()
    '''
def getTitlePlacement():
    '''public int getTitlePlacement()
    '''
def setTitlePlacement():
    '''public void setTitlePlacement(final int placement)
    '''
def isViewable():
    '''public final boolean isViewable()
    '''
def getLabelRotation():
    '''public double getLabelRotation()
    '''
def setLabelRotation():
    '''public void setLabelRotation(final double aa)
    '''
def isSkippingLabel():
    '''public final boolean isSkippingLabel()
    '''
def setSkippingLabel():
    '''public void setSkippingLabel(final boolean b)
    '''
def getSkipLabelMode():
    '''public final int getSkipLabelMode()
    '''
def setSkipLabelMode():
    '''public void setSkipLabelMode(final int z)
    '''
def has3DSupport():
    '''public boolean has3DSupport()
    '''
def isVisible():
    '''public final boolean isVisible()
    '''
def setVisible():
    '''public void setVisible(final boolean b)
    '''
def isAxisVisible():
    '''public final boolean isAxisVisible()
    '''
def setAxisVisible():
    '''public void setAxisVisible(final boolean b)
    '''
def isMajorTickVisible():
    '''public final boolean isMajorTickVisible()
    '''
def setMajorTickVisible():
    '''public void setMajorTickVisible(final boolean b)
    '''
def isMinorTickVisible():
    '''public final boolean isMinorTickVisible()
    '''
def setMinorTickVisible():
    '''public void setMinorTickVisible(final boolean b)
    '''
def isLabelVisible():
    '''public final boolean isLabelVisible()
    '''
def setLabelVisible():
    '''public void setLabelVisible(final boolean b)
    '''
def isAutoCrossing():
    '''public final boolean isAutoCrossing()
    '''
def setAutoCrossing():
    '''public void setAutoCrossing(final boolean b)
    '''
def setCrossing():
    '''public void setCrossing(final IlvAxis.Crossing crossing)
    '''
def getCrossingValue():
    '''public final double getCrossingValue()
    '''
def setCrossingValue():
    '''public void setCrossingValue(final double n)
    '''
def isAutoSide():
    '''public final boolean isAutoSide()
    '''
def setAutoSide():
    '''public void setAutoSide(final boolean b)
    '''
def getDefaultSide():
    '''public int getDefaultSide()
    '''
def getSide():
    '''public int getSide()
    '''
def setSide():
    '''public void setSide(final int n)
    '''
def getRadialSide():
    '''public int getRadialSide()
    '''
def setRadialSide():
    '''public void setRadialSide(final int n)
    '''
def getCircleSide():
    '''public int getCircleSide()
    '''
def setCircleSide():
    '''public void setCircleSide(final int n)
    '''
def getStepsDefinition():
    '''public final IlvStepsDefinition getStepsDefinition()
    '''
def setStepsDefinition():
    '''public void setStepsDefinition(final IlvStepsDefinition al)
    '''
def setStepUnit():
    '''public void setStepUnit(final Double n, final Double n2)
    '''
def setTimeUnit():
    '''public void setTimeUnit(final IlvTimeUnit unit)
    '''
def isCategory():
    '''public final boolean isCategory()
    '''
def setCategory():
    '''public final void setCategory(final boolean b)
    public void setCategory(final IlvDataSet set, final boolean b)
    '''
def setLogarithmic():
    '''public void setLogarithmic(final double n)
    '''
def getAxis():
    '''public final IlvAxis getAxis()
    '''
def getDualAxis():
    '''public final IlvAxis getDualAxis()
    '''
def getCoordinateSystem():
    '''public final IlvCoordinateSystem getCoordinateSystem()
    '''
def getChart():
    '''public final IlvChart getChart()
    '''
def getStepValues():
    '''public final IlvDoubleArray getStepValues()
    '''
def getSubStepValues():
    '''public final IlvDoubleArray getSubStepValues()
    '''
def recalc():
    '''public final void recalc()
    '''
def draw():
    '''public synchronized void draw(final Graphics graphics)
    '''
def toValue():
    '''public double toValue(final int n, final int n2)
    '''
def toPoint():
    '''public Point toPoint(final double n)
    '''
def getBounds():
    '''public synchronized Rectangle2D getBounds(final Rectangle2D rectangle2D)
    '''
def getBoundsUsingCache():
    '''public Rectangle2D getBoundsUsingCache(Rectangle2D rectangle2D)
    '''
def drawSelectionHandles():
    '''public void drawSelectionHandles(final Graphics graphics, final IlvHandlesSelectionStyle ilvHandlesSelectionStyle)
    '''
def drawHighlight():
    '''public void drawHighlight(final Graphics graphics)
    '''
def hit():
    '''public boolean hit(final Point2D point2D)
    '''
def drawIntoHitmap():
    '''public void drawIntoHitmap(final IlvChartHitmapDefinition ilvChartHitmapDefinition, final IlvChartHitmapAccumulator ilvChartHitmapAccumulator)
    '''
def getAnnotations():
    '''public IlvScaleAnnotation[] getAnnotations()
    '''
def setAnnotations():
    '''public void setAnnotations(final IlvScaleAnnotation[] array)
    '''
def addAnnotation():
    '''public void addAnnotation(final IlvScaleAnnotation ilvScaleAnnotation)
    '''
def removeAnnotation():
    '''public void removeAnnotation(final IlvScaleAnnotation ilvScaleAnnotation)
    '''
def updateAnnotations():
    '''public void updateAnnotations()
    '''
def getLabelBounds():
    '''public Rectangle2D getLabelBounds(final int n, final Rectangle2D rectangle2D)
    '''
def getLabelCount():
    '''public int getLabelCount()
    '''
def getLabelValue():
    '''public double getLabelValue(final int n)
    '''
def getLabelFormat():
    '''public final IlvValueFormat getLabelFormat()
    '''
def setLabelFormat():
    '''public void setLabelFormat(final IlvValueFormat ar)
    '''
def computeLabel():
    '''public String computeLabel(final double n)
    '''
def getTitleBackgroundShape():
    '''public Shape getTitleBackgroundShape()
    '''
def getAxisIndex():
    '''public static int getAxisIndex(final IlvScale ilvScale)
    '''
def axisRangeChanged():
    '''public void axisRangeChanged(final AxisRangeEvent axisRangeEvent)
    '''
def axisChanged():
    '''public void axisChanged(final AxisChangeEvent axisChangeEvent)
    '''
def Title():
    '''public Title(final String d, final double rotation)
    '''
def stateChanged():
    '''public void stateChanged()
    '''
def getText():
    '''public String getText()
    '''
def setText():
    '''public void setText(final String d)
    '''
def getLabelRenderer():
    '''public IlvLabelRenderer getLabelRenderer()
    '''
def setPlacement():
    '''public void setPlacement(int c)
    '''
def getPlacement():
    '''public int getPlacement()
    '''
def getSize2D():
    '''public Dimension2D getSize2D(final boolean b)
    '''
