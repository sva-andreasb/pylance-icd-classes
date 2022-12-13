def getBeanDescriptor():
'''public BeanDescriptor getBeanDescriptor()
public BeanDescriptor getBeanDescriptor()
public BeanDescriptor getBeanDescriptor()
'''
pass
def getAdditionalBeanInfo():
'''public BeanInfo[] getAdditionalBeanInfo()
public BeanInfo[] getAdditionalBeanInfo()
public BeanInfo[] getAdditionalBeanInfo()
'''
pass
def getPropertyDescriptors():
'''public PropertyDescriptor[] getPropertyDescriptors()
public PropertyDescriptor[] getPropertyDescriptors()
public PropertyDescriptor[] getPropertyDescriptors()
'''
pass
def getIcon():
'''public Image getIcon(final int n)
public Image getIcon(final int n)
public Image getIcon(final int n)
'''
pass
def IlvStyle():
'''public IlvStyle()
public IlvStyle(final Paint paint, final Paint paint2)
public IlvStyle(final Stroke stroke, final Paint paint)
public IlvStyle(final float width, final Paint paint)
public IlvStyle(final Paint paint)
public IlvStyle(final Stroke stroke, final Paint paint, final Paint paint2)
'''
pass
def createStroked():
'''public static IlvStyle createStroked(final Paint paint)
'''
pass
def isAbsolutePaint():
'''public final boolean isAbsolutePaint()
'''
pass
def setAbsolutePaint():
'''public void setAbsolutePaint(final boolean p)
'''
pass
def isStrokeOn():
'''public final boolean isStrokeOn()
'''
pass
def setStrokeOn():
'''public IlvStyle setStrokeOn(final boolean m)
'''
pass
def isFillOn():
'''public final boolean isFillOn()
'''
pass
def setFillOn():
'''public IlvStyle setFillOn(final boolean l)
'''
pass
def getStroke():
'''public Stroke getStroke()
'''
pass
def getStrokePaint():
'''public Paint getStrokePaint()
'''
pass
def getStrokeColor():
'''public Color getStrokeColor()
'''
pass
def setStroke():
'''public IlvStyle setStroke(final Stroke stroke)
public IlvStyle setStroke(final Stroke stroke, final Paint paint)
'''
pass
def setStrokePaint():
'''public IlvStyle setStrokePaint(final Paint paint)
'''
pass
def getFillPaint():
'''public Paint getFillPaint()
'''
pass
def getFillColor():
'''public Color getFillColor()
'''
pass
def setFillPaint():
'''public IlvStyle setFillPaint(final Paint paint)
'''
pass
def applyStroke():
'''public void applyStroke(final Graphics graphics)
'''
pass
def restoreStroke():
'''public void restoreStroke(final Graphics graphics)
'''
pass
def renderRect():
'''public void renderRect(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
public void renderRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def renderSquare():
'''public void renderSquare(final Graphics graphics, int n, int n2, int n3)
'''
pass
def renderPoints():
'''public void renderPoints(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)
public void renderPoints(final Graphics graphics, final int[] array, final int[] array2, final int n)
'''
pass
def renderOval():
'''public void renderOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def renderCircle():
'''public void renderCircle(final Graphics graphics, int n, int n2, int n3)
'''
pass
def renderShape():
'''public void renderShape(final Graphics graphics, final Shape shape)
'''
pass
def drawPolyline():
'''public void drawPolyline(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)
public void drawPolyline(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts, final IlvMarker ilvMarker, final int n)
public void drawPolyline(final Graphics graphics, final int[] array, final int[] array2, final int n)
'''
pass
def fillPolygon():
'''public void fillPolygon(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)
public void fillPolygon(final Graphics graphics, final int[] array, final int[] array2, final int n)
'''
pass
def drawRect():
'''public void drawRect(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
public void drawRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def fillRect():
'''public void fillRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def drawLine():
'''public void drawLine(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
public void drawLine(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def drawOval():
'''public void drawOval(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
public void drawOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def fillOval():
'''public void fillOval(final Graphics graphics, final double n, final double n2, final double n3, final double n4)
public void fillOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)
'''
pass
def draw():
'''public void draw(final Graphics graphics, final Shape shape)
'''
pass
def fill():
'''public void fill(final Graphics graphics, final Shape shape)
'''
pass
def quickBounds():
'''public boolean quickBounds()
'''
pass
def expand():
'''public final void expand(final Rectangle2D rectangle2D)
public void expand(final boolean b, final Rectangle2D rectangle2D)
'''
pass
def getBounds():
'''public final Rectangle2D getBounds(final int[] array, final int[] array2, final int n, final Rectangle2D rectangle2D)
public Rectangle2D getBounds(final int[] array, final int[] array2, final int n, final boolean b, final boolean b2, Rectangle2D shapeBounds)
public final Rectangle2D getBounds(final double[] array, final double[] array2, final int n, final Rectangle2D rectangle2D)
public Rectangle2D getBounds(final double[] array, final double[] array2, int doubleToInts, final boolean b, final boolean b2, Rectangle2D bounds)
'''
pass
def getShapeBounds():
'''public Rectangle2D getShapeBounds(final Shape shape)
'''
pass
def brighther():
'''public IlvStyle brighther()
'''
pass
def brighter():
'''public IlvStyle brighter()
'''
pass
def darker():
'''public IlvStyle darker()
'''
pass
def pointsContains():
'''public boolean pointsContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)
'''
pass
def distanceToPoints():
'''public double distanceToPoints(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)
'''
pass
def polygonContains():
'''public boolean polygonContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)
'''
pass
def distanceToPolygon():
'''public double distanceToPolygon(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)
'''
pass
def polylineContains():
'''public boolean polylineContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)
'''
pass
def distanceToPolyline():
'''public double distanceToPolyline(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)
'''
pass
def shapeContains():
'''public boolean shapeContains(final Shape shape, final double n, final double n2)
'''
pass
def distanceToShape():
'''public double distanceToShape(final Shape shape, final double n, final double n2, final boolean b)
'''
pass
def isFilterOn():
'''public static final boolean isFilterOn()
'''
pass
def setFilterOn():
'''public static void setFilterOn(final boolean d)
'''
pass
def copy():
'''public IlvStyle copy()
'''
pass
def copyInto():
'''public void copyInto(final IlvStyle ilvStyle)
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def IntensityChange():
'''public IntensityChange(final int a)
'''
pass
def getLevel():
'''public int getLevel()
'''
pass
def change():
'''public IlvStyle change(final IlvStyle ilvStyle)
public IlvChartRenderer change(final IlvChartRenderer ilvChartRenderer)
'''
pass
def isCompatibleValue():
'''public boolean isCompatibleValue(final Object o)
'''
pass
