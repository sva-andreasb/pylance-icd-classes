def getBeanDescriptor():
    '''returns BeanDescriptor\n\n
    getBeanDescriptor()\n
    getBeanDescriptor()\n
    getBeanDescriptor()\n
    '''
def getAdditionalBeanInfo():
    '''returns BeanInfo[]\n\n
    getAdditionalBeanInfo()\n
    getAdditionalBeanInfo()\n
    getAdditionalBeanInfo()\n
    '''
def getPropertyDescriptors():
    '''returns PropertyDescriptor[]\n\n
    getPropertyDescriptors()\n
    getPropertyDescriptors()\n
    getPropertyDescriptors()\n
    '''
def getIcon():
    '''returns Image\n\n
    getIcon(final int n)\n
    getIcon(final int n)\n
    getIcon(final int n)\n
    '''
def ():
    '''returns IntensityChange\n\n
    ()\n
    (final Paint paint, final Paint paint2)\n
    (final Stroke stroke, final Paint paint)\n
    (final float width, final Paint paint)\n
    (final Paint paint)\n
    (final Stroke stroke, final Paint paint, final Paint paint2)\n
    (final int a)\n
    '''
def setAbsolutePaint():
    '''returns None\n\n
    setAbsolutePaint(final boolean p)\n
    '''
def setStrokeOn():
    '''returns IlvStyle\n\n
    setStrokeOn(final boolean m)\n
    '''
def setFillOn():
    '''returns IlvStyle\n\n
    setFillOn(final boolean l)\n
    '''
def getStroke():
    '''returns Stroke\n\n
    getStroke()\n
    '''
def getStrokePaint():
    '''returns Paint\n\n
    getStrokePaint()\n
    '''
def getStrokeColor():
    '''returns Color\n\n
    getStrokeColor()\n
    '''
def setStroke():
    '''returns IlvStyle\n\n
    setStroke(final Stroke stroke)\n
    setStroke(final Stroke stroke, final Paint paint)\n
    '''
def setStrokePaint():
    '''returns IlvStyle\n\n
    setStrokePaint(final Paint paint)\n
    '''
def getFillPaint():
    '''returns Paint\n\n
    getFillPaint()\n
    '''
def getFillColor():
    '''returns Color\n\n
    getFillColor()\n
    '''
def setFillPaint():
    '''returns IlvStyle\n\n
    setFillPaint(final Paint paint)\n
    '''
def applyStroke():
    '''returns None\n\n
    applyStroke(final Graphics graphics)\n
    '''
def restoreStroke():
    '''returns None\n\n
    restoreStroke(final Graphics graphics)\n
    '''
def renderRect():
    '''returns None\n\n
    renderRect(final Graphics graphics, final double n, final double n2, final double n3, final double n4)\n
    renderRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def renderSquare():
    '''returns None\n\n
    renderSquare(final Graphics graphics, int n, int n2, int n3)\n
    '''
def renderPoints():
    '''returns None\n\n
    renderPoints(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)\n
    renderPoints(final Graphics graphics, final int[] array, final int[] array2, final int n)\n
    '''
def renderOval():
    '''returns None\n\n
    renderOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def renderCircle():
    '''returns None\n\n
    renderCircle(final Graphics graphics, int n, int n2, int n3)\n
    '''
def renderShape():
    '''returns None\n\n
    renderShape(final Graphics graphics, final Shape shape)\n
    '''
def drawPolyline():
    '''returns None\n\n
    drawPolyline(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)\n
    drawPolyline(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts, final IlvMarker ilvMarker, final int n)\n
    drawPolyline(final Graphics graphics, final int[] array, final int[] array2, final int n)\n
    '''
def fillPolygon():
    '''returns None\n\n
    fillPolygon(final Graphics graphics, final double[] array, final double[] array2, int doubleToInts)\n
    fillPolygon(final Graphics graphics, final int[] array, final int[] array2, final int n)\n
    '''
def drawRect():
    '''returns None\n\n
    drawRect(final Graphics graphics, final double n, final double n2, final double n3, final double n4)\n
    drawRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def fillRect():
    '''returns None\n\n
    fillRect(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def drawLine():
    '''returns None\n\n
    drawLine(final Graphics graphics, final double n, final double n2, final double n3, final double n4)\n
    drawLine(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def drawOval():
    '''returns None\n\n
    drawOval(final Graphics graphics, final double n, final double n2, final double n3, final double n4)\n
    drawOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def fillOval():
    '''returns None\n\n
    fillOval(final Graphics graphics, final double n, final double n2, final double n3, final double n4)\n
    fillOval(final Graphics graphics, final int n, final int n2, final int n3, final int n4)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final Shape shape)\n
    '''
def fill():
    '''returns None\n\n
    fill(final Graphics graphics, final Shape shape)\n
    '''
def quickBounds():
    '''returns boolean\n\n
    quickBounds()\n
    '''
def expand():
    '''returns None\n\n
    expand(final boolean b, final Rectangle2D rectangle2D)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(final int[] array, final int[] array2, final int n, final boolean b, final boolean b2, Rectangle2D shapeBounds)\n
    getBounds(final double[] array, final double[] array2, int doubleToInts, final boolean b, final boolean b2, Rectangle2D bounds)\n
    '''
def getShapeBounds():
    '''returns Rectangle2D\n\n
    getShapeBounds(final Shape shape)\n
    '''
def brighther():
    '''returns IlvStyle\n\n
    brighther()\n
    '''
def brighter():
    '''returns IlvStyle\n\n
    brighter()\n
    '''
def darker():
    '''returns IlvStyle\n\n
    darker()\n
    '''
def pointsContains():
    '''returns boolean\n\n
    pointsContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)\n
    '''
def distanceToPoints():
    '''returns double\n\n
    distanceToPoints(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)\n
    '''
def polygonContains():
    '''returns boolean\n\n
    polygonContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)\n
    '''
def distanceToPolygon():
    '''returns double\n\n
    distanceToPolygon(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)\n
    '''
def polylineContains():
    '''returns boolean\n\n
    polylineContains(final double[] array, final double[] array2, final int n, final double n2, final double n3)\n
    '''
def distanceToPolyline():
    '''returns double\n\n
    distanceToPolyline(final double[] array, final double[] array2, final int n, final double n2, final double n3, final boolean b)\n
    '''
def shapeContains():
    '''returns boolean\n\n
    shapeContains(final Shape shape, final double n, final double n2)\n
    '''
def distanceToShape():
    '''returns double\n\n
    distanceToShape(final Shape shape, final double n, final double n2, final boolean b)\n
    '''
def copy():
    '''returns IlvStyle\n\n
    copy()\n
    '''
def copyInto():
    '''returns None\n\n
    copyInto(final IlvStyle ilvStyle)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def getLevel():
    '''returns int\n\n
    getLevel()\n
    '''
def change():
    '''returns IlvChartRenderer\n\n
    change(final IlvStyle ilvStyle)\n
    change(final IlvChartRenderer ilvChartRenderer)\n
    '''
def isCompatibleValue():
    '''returns boolean\n\n
    isCompatibleValue(final Object o)\n
    '''
