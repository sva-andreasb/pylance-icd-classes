def ():
    '''returns AbstractGraphics2D\n\n
    (final boolean textAsShapes)\n
    (final AbstractGraphics2D g)\n
    '''
def translate():
    '''returns None\n\n
    translate(final int x, final int y)\n
    translate(final double tx, final double ty)\n
    '''
def getColor():
    '''returns Color\n\n
    getColor()\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final Color c)\n
    '''
def setPaintMode():
    '''returns None\n\n
    setPaintMode()\n
    '''
def getFont():
    '''returns Font\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font font)\n
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
    setClip(final Shape clip)\n
    '''
def getClip():
    '''returns Shape\n\n
    getClip()\n
    '''
def drawLine():
    '''returns None\n\n
    drawLine(final int x1, final int y1, final int x2, final int y2)\n
    '''
def fillRect():
    '''returns None\n\n
    fillRect(final int x, final int y, final int width, final int height)\n
    '''
def drawRect():
    '''returns None\n\n
    drawRect(final int x, final int y, final int width, final int height)\n
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
    drawPolyline(final int[] xPoints, final int[] yPoints, final int nPoints)\n
    '''
def drawPolygon():
    '''returns None\n\n
    drawPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)\n
    '''
def fillPolygon():
    '''returns None\n\n
    fillPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)\n
    '''
def drawString():
    '''returns None\n\n
    drawString(final String str, final int x, final int y)\n
    drawString(final AttributedCharacterIterator iterator, final float x, final float y)\n
    drawString(final AttributedCharacterIterator iterator, final int x, final int y)\n
    '''
def drawImage():
    '''returns None\n\n
    drawImage(final Image img, final int x, final int y, final Color bgcolor, final ImageObserver observer)\n
    drawImage(final Image img, final int x, final int y, final int width, final int height, final Color bgcolor, final ImageObserver observer)\n
    drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final ImageObserver observer)\n
    drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final Color bgcolor, final ImageObserver observer)\n
    drawImage(final Image img, AffineTransform xform, final ImageObserver obs)\n
    drawImage(BufferedImage img, final BufferedImageOp op, final int x, final int y)\n
    '''
def drawGlyphVector():
    '''returns None\n\n
    drawGlyphVector(final GlyphVector g, final float x, final float y)\n
    '''
def hit():
    '''returns boolean\n\n
    hit(final Rectangle rect, Shape s, final boolean onStroke)\n
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
    setRenderingHint(final RenderingHints.Key hintKey, final Object hintValue)\n
    '''
def getRenderingHint():
    '''returns Object\n\n
    getRenderingHint(final RenderingHints.Key hintKey)\n
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
    setTransform(final AffineTransform tx)\n
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
def clip():
    '''returns None\n\n
    clip(final Shape s)\n
    '''
def getFontRenderContext():
    '''returns FontRenderContext\n\n
    getFontRenderContext()\n
    '''
def getGraphicContext():
    '''returns GraphicContext\n\n
    getGraphicContext()\n
    '''
