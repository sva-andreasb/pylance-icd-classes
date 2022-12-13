def AbstractGraphics2D():
'''public AbstractGraphics2D(final boolean textAsShapes)
public AbstractGraphics2D(final AbstractGraphics2D g)
'''
pass
def translate():
'''public void translate(final int x, final int y)
public void translate(final double tx, final double ty)
'''
pass
def getColor():
'''public Color getColor()
'''
pass
def setColor():
'''public void setColor(final Color c)
'''
pass
def setPaintMode():
'''public void setPaintMode()
'''
pass
def getFont():
'''public Font getFont()
'''
pass
def setFont():
'''public void setFont(final Font font)
'''
pass
def getClipBounds():
'''public Rectangle getClipBounds()
'''
pass
def clipRect():
'''public void clipRect(final int x, final int y, final int width, final int height)
'''
pass
def setClip():
'''public void setClip(final int x, final int y, final int width, final int height)
public void setClip(final Shape clip)
'''
pass
def getClip():
'''public Shape getClip()
'''
pass
def drawLine():
'''public void drawLine(final int x1, final int y1, final int x2, final int y2)
'''
pass
def fillRect():
'''public void fillRect(final int x, final int y, final int width, final int height)
'''
pass
def drawRect():
'''public void drawRect(final int x, final int y, final int width, final int height)
'''
pass
def clearRect():
'''public void clearRect(final int x, final int y, final int width, final int height)
'''
pass
def drawRoundRect():
'''public void drawRoundRect(final int x, final int y, final int width, final int height, final int arcWidth, final int arcHeight)
'''
pass
def fillRoundRect():
'''public void fillRoundRect(final int x, final int y, final int width, final int height, final int arcWidth, final int arcHeight)
'''
pass
def drawOval():
'''public void drawOval(final int x, final int y, final int width, final int height)
'''
pass
def fillOval():
'''public void fillOval(final int x, final int y, final int width, final int height)
'''
pass
def drawArc():
'''public void drawArc(final int x, final int y, final int width, final int height, final int startAngle, final int arcAngle)
'''
pass
def fillArc():
'''public void fillArc(final int x, final int y, final int width, final int height, final int startAngle, final int arcAngle)
'''
pass
def drawPolyline():
'''public void drawPolyline(final int[] xPoints, final int[] yPoints, final int nPoints)
'''
pass
def drawPolygon():
'''public void drawPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)
'''
pass
def fillPolygon():
'''public void fillPolygon(final int[] xPoints, final int[] yPoints, final int nPoints)
'''
pass
def drawString():
'''public void drawString(final String str, final int x, final int y)
public void drawString(final AttributedCharacterIterator iterator, final float x, final float y)
public void drawString(final AttributedCharacterIterator iterator, final int x, final int y)
'''
pass
def drawImage():
'''public boolean drawImage(final Image img, final int x, final int y, final Color bgcolor, final ImageObserver observer)
public boolean drawImage(final Image img, final int x, final int y, final int width, final int height, final Color bgcolor, final ImageObserver observer)
public boolean drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final ImageObserver observer)
public boolean drawImage(final Image img, final int dx1, final int dy1, final int dx2, final int dy2, final int sx1, final int sy1, final int sx2, final int sy2, final Color bgcolor, final ImageObserver observer)
public boolean drawImage(final Image img, AffineTransform xform, final ImageObserver obs)
public void drawImage(BufferedImage img, final BufferedImageOp op, final int x, final int y)
'''
pass
def drawGlyphVector():
'''public void drawGlyphVector(final GlyphVector g, final float x, final float y)
'''
pass
def hit():
'''public boolean hit(final Rectangle rect, Shape s, final boolean onStroke)
'''
pass
def setComposite():
'''public void setComposite(final Composite comp)
'''
pass
def setPaint():
'''public void setPaint(final Paint paint)
'''
pass
def setStroke():
'''public void setStroke(final Stroke s)
'''
pass
def setRenderingHint():
'''public void setRenderingHint(final RenderingHints.Key hintKey, final Object hintValue)
'''
pass
def getRenderingHint():
'''public Object getRenderingHint(final RenderingHints.Key hintKey)
'''
pass
def setRenderingHints():
'''public void setRenderingHints(final Map hints)
'''
pass
def addRenderingHints():
'''public void addRenderingHints(final Map hints)
'''
pass
def getRenderingHints():
'''public RenderingHints getRenderingHints()
'''
pass
def rotate():
'''public void rotate(final double theta)
public void rotate(final double theta, final double x, final double y)
'''
pass
def scale():
'''public void scale(final double sx, final double sy)
'''
pass
def shear():
'''public void shear(final double shx, final double shy)
'''
pass
def transform():
'''public void transform(final AffineTransform tx)
'''
pass
def setTransform():
'''public void setTransform(final AffineTransform tx)
'''
pass
def getTransform():
'''public AffineTransform getTransform()
'''
pass
def getPaint():
'''public Paint getPaint()
'''
pass
def getComposite():
'''public Composite getComposite()
'''
pass
def setBackground():
'''public void setBackground(final Color color)
'''
pass
def getBackground():
'''public Color getBackground()
'''
pass
def getStroke():
'''public Stroke getStroke()
'''
pass
def clip():
'''public void clip(final Shape s)
'''
pass
def getFontRenderContext():
'''public FontRenderContext getFontRenderContext()
'''
pass
def getGraphicContext():
'''public GraphicContext getGraphicContext()
'''
pass
