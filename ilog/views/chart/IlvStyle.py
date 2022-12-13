def getBeanDescriptor():
    '''    public BeanDescriptor getBeanDescriptor()
    public BeanDescriptor getBeanDescriptor()
    public BeanDescriptor getBeanDescriptor()
    '''
def getAdditionalBeanInfo():
    '''    public BeanInfo[] getAdditionalBeanInfo()
    public BeanInfo[] getAdditionalBeanInfo()
    public BeanInfo[] getAdditionalBeanInfo()
    '''
def getPropertyDescriptors():
    '''    public PropertyDescriptor[] getPropertyDescriptors()
    public PropertyDescriptor[] getPropertyDescriptors()
    public PropertyDescriptor[] getPropertyDescriptors()
    '''
def getIcon():
    '''    public Image getIcon(final int n)
    public Image getIcon(final int n)
    public Image getIcon(final int n)
    '''
def IlvStyle():
    '''    public IlvStyle()
    public IlvStyle(final Paint paint, final Paint paint2)
    public IlvStyle(final Stroke stroke, final Paint paint)
    public IlvStyle(final float width, final Paint paint)
    public IlvStyle(final Paint paint)
    public IlvStyle(final Stroke stroke, final Paint paint, final Paint paint2)
    '''
def createStroked():
    '''    public static IlvStyle createStroked(final Paint paint)
    '''
def isAbsolutePaint():
    '''    public final boolean isAbsolutePaint()
    '''
def setAbsolutePaint():
    '''    public void setAbsolutePaint(final boolean p)
    '''
def isStrokeOn():
    '''    public final boolean isStrokeOn()
    '''
def setStrokeOn():
    '''    public IlvStyle setStrokeOn(final boolean m)
    '''
def isFillOn():
    '''    public final boolean isFillOn()
    '''
def setFillOn():
    '''    public IlvStyle setFillOn(final boolean l)
    '''
def getStroke():
    '''    public Stroke getStroke()
    '''
def getStrokePaint():
    '''    public Paint getStrokePaint()
    '''
def getStrokeColor():
    '''    public Color getStrokeColor()
    '''
def setStroke():
    '''    public IlvStyle setStroke(final Stroke stroke)
    public IlvStyle setStroke(final Stroke stroke, final Paint paint)
    '''
def setStrokePaint():
    '''    public IlvStyle setStrokePaint(final Paint paint)
    '''
def getFillPaint():
    '''    public Paint getFillPaint()
    '''
def getFillColor():
    '''    public Color getFillColor()
    '''
def setFillPaint():
    '''    public IlvStyle setFillPaint(final Paint paint)
    '''
def applyStroke():
    '''    public void applyStroke(final Graphics graphics)
    '''
def restoreStroke():
    '''    public void restoreStroke(final Graphics graphics)
    '''
def renderRect():
    '''    public void renderRect(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
    public void renderRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def renderSquare():
    '''    public void renderSquare(final Graphics graphics, int n, int n2, int n3)
    '''
def renderPoints():
    '''    public void renderPoints(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)
    public void renderPoints(final Graphics graphics, final int[] array, final int[] array2, final int n)
    '''
def renderOval():
    '''    public void renderOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def renderCircle():
    '''    public void renderCircle(final Graphics graphics, int n, int n2, int n3)
    '''
def renderShape():
    '''    public void renderShape(final Graphics graphics, final Shape shape)
    '''
def drawPolyline():
    '''    public void drawPolyline(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)
    public void drawPolyline(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts, final IlvMarker ilvMarker, final int n)
    public void drawPolyline(final Graphics graphics, final int[] array, final int[] array2, final int n)
    '''
def fillPolygon():
    '''    public void fillPolygon(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)
    public void fillPolygon(final Graphics graphics, final int[] array, final int[] array2, final int n)
    '''
def drawRect():
    '''    public void drawRect(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
    public void drawRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def fillRect():
    '''    public void fillRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def drawLine():
    '''    public void drawLine(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
    public void drawLine(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def drawOval():
    '''    public void drawOval(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
    public void drawOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def fillOval():
    '''    public void fillOval(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
    public void fillOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
    '''
def draw():
    '''    public void draw(final Graphics graphics, final Shape shape)
    '''
def fill():
    '''    public void fill(final Graphics graphics, final Shape shape)
    '''
def quickBounds():
    '''    public boolean quickBounds()
    '''
def expand():
    '''    public final void expand(final Rectangle2D rectangle2D)
    public void expand(final boolean b, final Rectangle2D rectangle2D)
    '''
def getBounds():
    '''    public final Rectangle2D getBounds(final int[] array, final int[] array2, final int n, final Rectangle2D rectangle2D)
    public Rectangle2D getBounds(final int[] array, final int[] array2, final int n, final boolean b, final boolean b2, Rectangle2D shapeBounds)
    public final Rectangle2D getBounds(final double[] array, final double[] array2, final int n, final Rectangle2D rectangle2D)
    public Rectangle2D getBounds(final double[] array, final double[] array2, int doubleToInts, final boolean b, final boolean b2, Rectangle2D bounds)
    '''
def getShapeBounds():
    '''    public Rectangle2D getShapeBounds(final Shape shape)
    '''
def brighther():
    '''    public IlvStyle brighther()
    '''
def brighter():
    '''    public IlvStyle brighter()
    '''
def darker():
    '''    public IlvStyle darker()
    '''
def pointsContains():
    '''    public boolean pointsContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)
    '''
def distanceToPoints():
    '''    public double distanceToPoints(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)
    '''
def polygonContains():
    '''    public boolean polygonContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)
    '''
def distanceToPolygon():
    '''    public double distanceToPolygon(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)
    '''
def polylineContains():
    '''    public boolean polylineContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)
    '''
def distanceToPolyline():
    '''    public double distanceToPolyline(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)
    '''
def shapeContains():
    '''    public boolean shapeContains(final Shape shape, final double n, final double n2)
    '''
def distanceToShape():
    '''    public double distanceToShape(final Shape shape, final double n, final double n2, final boolean b)
    '''
def isFilterOn():
    '''    public static final boolean isFilterOn()
    '''
def setFilterOn():
    '''    public static void setFilterOn(final boolean d)
    '''
def copy():
    '''    public IlvStyle copy()
    '''
def copyInto():
    '''    public void copyInto(final IlvStyle ilvStyle)
    '''
def clone():
    '''    public Object clone()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def IntensityChange():
    '''    public IntensityChange(final int a)
    '''
def getLevel():
    '''    public int getLevel()
    '''
def change():
    '''    public IlvStyle change(final IlvStyle ilvStyle)
    public IlvChartRenderer change(final IlvChartRenderer ilvChartRenderer)
    '''
def isCompatibleValue():
    '''    public boolean isCompatibleValue(final Object o)
    '''
