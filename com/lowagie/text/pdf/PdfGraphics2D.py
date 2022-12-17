def draw():
    '''returns None\n\n
    draw(final Shape s)\n
    '''
def drawImage():
    '''returns boolean\n\n
    drawImage(final Image img, final AffineTransform xform, final ImageObserver obs)\n
    drawImage(final BufferedImage img, final BufferedImageOp op, final int x, final int y)\n
    drawImage(final Image img, final int x, final int y, final ImageObserver observer)\n
    drawImage(final Image img, final int x, final int y, final int width, final int height, final ImageObserver observer)\n
    drawImage(final Image img, final int x, final int y, final Color bgcolor, final ImageObserver observer)\n
    drawImage(final Image img, final int x, final int y, final int width, final int height, final Color bgcolor, final ImageObserver observer)\n
    drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final ImageObserver observer)\n
    drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final Color bgcolor, final ImageObserver observer)\n
    '''
def drawRenderedImage():
    '''returns None\n\n
    drawRenderedImage(final RenderedImage img, final AffineTransform xform)\n
    '''
def drawRenderableImage():
    '''returns None\n\n
    drawRenderableImage(final RenderableImage img, final AffineTransform xform)\n
    '''
def drawString():
    '''returns None\n\n
    drawString(final String s, final int x, final int y)\n
    drawString(final String s, final float x, float y)\n
    drawString(final AttributedCharacterIterator iterator, final int x, final int y)\n
    drawString(final AttributedCharacterIterator iter, float x, final float y)\n
    '''
def drawGlyphVector():
    '''returns None\n\n
    drawGlyphVector(final GlyphVector g, final float x, final float y)\n
    '''
def fill():
    '''returns None\n\n
    fill(final Shape s)\n
    '''
def hit():
    '''returns boolean\n\n
    hit(final Rectangle rect, Shape s, final boolean onStroke)\n
    '''
def getDeviceConfiguration():
    '''returns GraphicsConfiguration\n\n
    getDeviceConfiguration()\n
    '''
def setComposite():
    '''returns None\n\n
    setComposite(final Composite comp)\n
    '''
def setPaint():
    '''returns None\n\n
    setPaint(final Paint paint)\n
    '''
def setStroke():
    '''returns None\n\n
    setStroke(final Stroke s)\n
    '''
def setRenderingHint():
    '''returns None\n\n
    setRenderingHint(final RenderingHints.Key arg0, final Object arg1)\n
    '''
def getRenderingHint():
    '''returns Object\n\n
    getRenderingHint(final RenderingHints.Key arg0)\n
    '''
def setRenderingHints():
    '''returns None\n\n
    setRenderingHints(final Map hints)\n
    '''
def addRenderingHints():
    '''returns None\n\n
    addRenderingHints(final Map hints)\n
    '''
def getRenderingHints():
    '''returns RenderingHints\n\n
    getRenderingHints()\n
    '''
def translate():
    '''returns None\n\n
    translate(final int x, final int y)\n
    translate(final double tx, final double ty)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final double theta)\n
    rotate(final double theta, final double x, final double y)\n
    '''
def scale():
    '''returns None\n\n
    scale(final double sx, final double sy)\n
    '''
def shear():
    '''returns None\n\n
    shear(final double shx, final double shy)\n
    '''
def transform():
    '''returns None\n\n
    transform(final AffineTransform tx)\n
    '''
def setTransform():
    '''returns None\n\n
    setTransform(final AffineTransform t)\n
    '''
def getTransform():
    '''returns AffineTransform\n\n
    getTransform()\n
    '''
def getPaint():
    '''returns Paint\n\n
    getPaint()\n
    '''
def getComposite():
    '''returns Composite\n\n
    getComposite()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color color)\n
    '''
def getBackground():
    '''returns Color\n\n
    getBackground()\n
    '''
def getStroke():
    '''returns Stroke\n\n
    getStroke()\n
    '''
def getFontRenderContext():
    '''returns FontRenderContext\n\n
    getFontRenderContext()\n
    '''
def create():
    '''returns Graphics\n\n
    create()\n
    '''
def getContent():
    '''returns PdfContentByte\n\n
    getContent()\n
    '''
def getColor():
    '''returns Color\n\n
    getColor()\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final Color color)\n
    '''
def setPaintMode():
    '''returns None\n\n
    setPaintMode()\n
    '''
def setXORMode():
    '''returns None\n\n
    setXORMode(final Color c1)\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font f)\n
    '''
def getFontMetrics():
    '''returns FontMetrics\n\n
    getFontMetrics(final Font f)\n
    '''
def getClipBounds():
    '''returns Rectangle\n\n
    getClipBounds()\n
    '''
def clipRect():
    '''returns None\n\n
    clipRect(final int x, final int y, final int width, final int height)\n
    '''
def setClip():
    '''returns None\n\n
    setClip(final int x, final int y, final int width, final int height)\n
    setClip(Shape s)\n
    '''
def clip():
    '''returns None\n\n
    clip(Shape s)\n
    '''
def getClip():
    '''returns Shape\n\n
    getClip()\n
    '''
def copyArea():
    '''returns None\n\n
    copyArea(final int x, final int y, final int width, final int height, final int dx, final int dy)\n
    '''
def drawLine():
    '''returns None\n\n
    drawLine(final int x1, final int y1, final int x2, final int y2)\n
    '''
def drawRect():
    '''returns None\n\n
    drawRect(final int x, final int y, final int width, final int height)\n
    '''
def fillRect():
    '''returns None\n\n
    fillRect(final int x, final int y, final int width, final int height)\n
    '''
def clearRect():
    '''returns None\n\n
    clearRect(final int x, final int y, final int width, final int height)\n
    '''
def drawRoundRect():
    '''returns None\n\n
    drawRoundRect(final int x, final int y, final int width, final int height, final int arcWidth, final int arcHeight)\n
    '''
def fillRoundRect():
    '''returns None\n\n
    fillRoundRect(final int x, final int y, final int width, final int height, final int arcWidth, final int arcHeight)\n
    '''
def drawOval():
    '''returns None\n\n
    drawOval(final int x, final int y, final int width, final int height)\n
    '''
def fillOval():
    '''returns None\n\n
    fillOval(final int x, final int y, final int width, final int height)\n
    '''
def drawArc():
    '''returns None\n\n
    drawArc(final int x, final int y, final int width, final int height, final int startAngle, final int arcAngle)\n
    '''
def fillArc():
    '''returns None\n\n
    fillArc(final int x, final int y, final int width, final int height, final int startAngle, final int arcAngle)\n
    '''
def drawPolyline():
    '''returns None\n\n
    drawPolyline(final int[] x, final int[] y, final int nPoints)\n
    '''
def drawPolygon():
    '''returns None\n\n
    drawPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)\n
    '''
def fillPolygon():
    '''returns None\n\n
    fillPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
