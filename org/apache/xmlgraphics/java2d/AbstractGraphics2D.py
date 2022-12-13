def AbstractGraphics2D():
    '''    public AbstractGraphics2D(final boolean textAsShapes)
    public AbstractGraphics2D(final AbstractGraphics2D g)
    '''
def translate():
    '''    public void translate(final int x, final int y)
    public void translate(final double tx, final double ty)
    '''
def getColor():
    '''    public Color getColor()
    '''
def setColor():
    '''    public void setColor(final Color c)
    '''
def setPaintMode():
    '''    public void setPaintMode()
    '''
def getFont():
    '''    public Font getFont()
    '''
def setFont():
    '''    public void setFont(final Font font)
    '''
def getClipBounds():
    '''    public Rectangle getClipBounds()
    '''
def clipRect():
    '''    public void clipRect(final int x, final int y, final int width, final int height)
    '''
def setClip():
    '''    public void setClip(final int x, final int y, final int width, final int height)
    public void setClip(final Shape clip)
    '''
def getClip():
    '''    public Shape getClip()
    '''
def drawLine():
    '''    public void drawLine(final int x1, final int y1, final int x2, final int y2)
    '''
def fillRect():
    '''    public void fillRect(final int x, final int y, final int width, final int height)
    '''
def drawRect():
    '''    public void drawRect(final int x, final int y, final int width, final int height)
    '''
def clearRect():
    '''    public void clearRect(final int x, final int y, final int width, final int height)
    '''
def drawRoundRect():
    '''    public void drawRoundRect(final int x, final int y, final int width, final int height, final int arcWidth, final int arcHeight)
    '''
def fillRoundRect():
    '''    public void fillRoundRect(final int x, final int y, final int width, final int height, final int arcWidth, final int arcHeight)
    '''
def drawOval():
    '''    public void drawOval(final int x, final int y, final int width, final int height)
    '''
def fillOval():
    '''    public void fillOval(final int x, final int y, final int width, final int height)
    '''
def drawArc():
    '''    public void drawArc(final int x, final int y, final int width, final int height, final int startAngle, final int arcAngle)
    '''
def fillArc():
    '''    public void fillArc(final int x, final int y, final int width, final int height, final int startAngle, final int arcAngle)
    '''
def drawPolyline():
    '''    public void drawPolyline(final int[] xPoints, final int[] yPoints, final int nPoints)
    '''
def drawPolygon():
    '''    public void drawPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)
    '''
def fillPolygon():
    '''    public void fillPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)
    '''
def drawString():
    '''    public void drawString(final String str, final int x, final int y)
    public void drawString(final AttributedCharacterIterator iterator, final float x, final float y)
    public void drawString(final AttributedCharacterIterator iterator, final int x, final int y)
    '''
def drawImage():
    '''    public boolean drawImage(final Image img, final int x, final int y, final Color bgcolor, final ImageObserver observer)
    public boolean drawImage(final Image img, final int x, final int y, final int width, final int height, final Color bgcolor, final ImageObserver observer)
    public boolean drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final ImageObserver observer)
    public boolean drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final Color bgcolor, final ImageObserver observer)
    public boolean drawImage(final Image img, AffineTransform xform, final ImageObserver obs)
    public void drawImage(BufferedImage img, final BufferedImageOp op, final int x, final int y)
    '''
def drawGlyphVector():
    '''    public void drawGlyphVector(final GlyphVector g, final float x, final float y)
    '''
def hit():
    '''    public boolean hit(final Rectangle rect, Shape s, final boolean onStroke)
    '''
def setComposite():
    '''    public void setComposite(final Composite comp)
    '''
def setPaint():
    '''    public void setPaint(final Paint paint)
    '''
def setStroke():
    '''    public void setStroke(final Stroke s)
    '''
def setRenderingHint():
    '''    public void setRenderingHint(final RenderingHints.Key hintKey, final Object hintValue)
    '''
def getRenderingHint():
    '''    public Object getRenderingHint(final RenderingHints.Key hintKey)
    '''
def setRenderingHints():
    '''    public void setRenderingHints(final Map hints)
    '''
def addRenderingHints():
    '''    public void addRenderingHints(final Map hints)
    '''
def getRenderingHints():
    '''    public RenderingHints getRenderingHints()
    '''
def rotate():
    '''    public void rotate(final double theta)
    public void rotate(final double theta, final double x, final double y)
    '''
def scale():
    '''    public void scale(final double sx, final double sy)
    '''
def shear():
    '''    public void shear(final double shx, final double shy)
    '''
def transform():
    '''    public void transform(final AffineTransform tx)
    '''
def setTransform():
    '''    public void setTransform(final AffineTransform tx)
    '''
def getTransform():
    '''    public AffineTransform getTransform()
    '''
def getPaint():
    '''    public Paint getPaint()
    '''
def getComposite():
    '''    public Composite getComposite()
    '''
def setBackground():
    '''    public void setBackground(final Color color)
    '''
def getBackground():
    '''    public Color getBackground()
    '''
def getStroke():
    '''    public Stroke getStroke()
    '''
def clip():
    '''    public void clip(final Shape s)
    '''
def getFontRenderContext():
    '''    public FontRenderContext getFontRenderContext()
    '''
def getGraphicContext():
    '''    public GraphicContext getGraphicContext()
    '''
