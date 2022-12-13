ALIGN_CENTER = "int  1"
ALIGN_LEFT = "int  0"
ALIGN_RIGHT = "int  2"
LINE_CAP_BUTT = "int  0"
LINE_CAP_ROUND = "int  1"
LINE_CAP_PROJECTING_SQUARE = "int  2"
LINE_JOIN_MITER = "int  0"
LINE_JOIN_ROUND = "int  1"
LINE_JOIN_BEVEL = "int  2"
TEXT_RENDER_MODE_FILL = "int  0"
TEXT_RENDER_MODE_STROKE = "int  1"
TEXT_RENDER_MODE_FILL_STROKE = "int  2"
TEXT_RENDER_MODE_INVISIBLE = "int  3"
TEXT_RENDER_MODE_FILL_CLIP = "int  4"
TEXT_RENDER_MODE_STROKE_CLIP = "int  5"
TEXT_RENDER_MODE_FILL_STROKE_CLIP = "int  6"
TEXT_RENDER_MODE_CLIP = "int  7"
def PdfContentByte():
    '''public PdfContentByte(final PdfWriter wr)
    '''
def toString():
    '''public String toString()
    '''
def getInternalBuffer():
    '''public ByteBuffer getInternalBuffer()
    '''
def toPdf():
    '''public byte[] toPdf(final PdfWriter writer)
    '''
def add():
    '''public void add(final PdfContentByte other)
    '''
def getXTLM():
    '''public float getXTLM()
    '''
def getYTLM():
    '''public float getYTLM()
    '''
def getLeading():
    '''public float getLeading()
    '''
def setFlatness():
    '''public void setFlatness(final float flatness)
    '''
def setLineCap():
    '''public void setLineCap(final int style)
    '''
def setLineDash():
    '''public void setLineDash(final float phase)
    public void setLineDash(final float unitsOn, final float phase)
    public void setLineDash(final float unitsOn, final float unitsOff, final float phase)
    public final void setLineDash(final float[] array, final float phase)
    '''
def setLineJoin():
    '''public void setLineJoin(final int style)
    '''
def setLineWidth():
    '''public void setLineWidth(final float w)
    '''
def setMiterLimit():
    '''public void setMiterLimit(final float miterLimit)
    '''
def clip():
    '''public void clip()
    '''
def eoClip():
    '''public void eoClip()
    '''
def setGrayFill():
    '''public void setGrayFill(final float gray)
    '''
def resetGrayFill():
    '''public void resetGrayFill()
    '''
def setGrayStroke():
    '''public void setGrayStroke(final float gray)
    '''
def resetGrayStroke():
    '''public void resetGrayStroke()
    '''
def setRGBColorFillF():
    '''public void setRGBColorFillF(final float red, final float green, final float blue)
    '''
def resetRGBColorFill():
    '''public void resetRGBColorFill()
    '''
def setRGBColorStrokeF():
    '''public void setRGBColorStrokeF(final float red, final float green, final float blue)
    '''
def resetRGBColorStroke():
    '''public void resetRGBColorStroke()
    '''
def setCMYKColorFillF():
    '''public void setCMYKColorFillF(final float cyan, final float magenta, final float yellow, final float black)
    '''
def resetCMYKColorFill():
    '''public void resetCMYKColorFill()
    '''
def setCMYKColorStrokeF():
    '''public void setCMYKColorStrokeF(final float cyan, final float magenta, final float yellow, final float black)
    '''
def resetCMYKColorStroke():
    '''public void resetCMYKColorStroke()
    '''
def moveTo():
    '''public void moveTo(final float x, final float y)
    '''
def lineTo():
    '''public void lineTo(final float x, final float y)
    '''
def curveTo():
    '''public void curveTo(final float x1, final float y1, final float x2, final float y2, final float x3, final float y3)
    public void curveTo(final float x2, final float y2, final float x3, final float y3)
    '''
def curveFromTo():
    '''public void curveFromTo(final float x1, final float y1, final float x3, final float y3)
    '''
def circle():
    '''public void circle(final float x, final float y, final float r)
    '''
def rectangle():
    '''public void rectangle(final float x, final float y, final float w, final float h)
    public void rectangle(final Rectangle rectangle)
    '''
def variableRectangle():
    '''public void variableRectangle(final Rectangle rect)
    '''
def closePath():
    '''public void closePath()
    '''
def newPath():
    '''public void newPath()
    '''
def stroke():
    '''public void stroke()
    '''
def closePathStroke():
    '''public void closePathStroke()
    '''
def fill():
    '''public void fill()
    '''
def eoFill():
    '''public void eoFill()
    '''
def fillStroke():
    '''public void fillStroke()
    '''
def closePathFillStroke():
    '''public void closePathFillStroke()
    '''
def eoFillStroke():
    '''public void eoFillStroke()
    '''
def closePathEoFillStroke():
    '''public void closePathEoFillStroke()
    '''
def addImage():
    '''public void addImage(final Image image)
    public void addImage(final Image image, final float a, final float b, final float c, final float d, final float e, final float f)
    '''
def reset():
    '''public void reset()
    '''
def beginText():
    '''public void beginText()
    '''
def endText():
    '''public void endText()
    '''
def saveState():
    '''public void saveState()
    '''
def restoreState():
    '''public void restoreState()
    '''
def setCharacterSpacing():
    '''public void setCharacterSpacing(final float charSpace)
    '''
def setWordSpacing():
    '''public void setWordSpacing(final float wordSpace)
    '''
def setHorizontalScaling():
    '''public void setHorizontalScaling(final float scale)
    '''
def setLeading():
    '''public void setLeading(final float leading)
    '''
def setFontAndSize():
    '''public void setFontAndSize(final BaseFont bf, final float size)
    '''
def setTextRenderingMode():
    '''public void setTextRenderingMode(final int rendering)
    '''
def setTextRise():
    '''public void setTextRise(final float rise)
    '''
def showText():
    '''public void showText(final String text)
    public void showText(final PdfTextArray text)
    '''
def getKernArray():
    '''public static PdfTextArray getKernArray(final String text, final BaseFont font)
    '''
def showTextKerned():
    '''public void showTextKerned(final String text)
    '''
def newlineShowText():
    '''public void newlineShowText(final String text)
    public void newlineShowText(final float wordSpacing, final float charSpacing, final String text)
    '''
def setTextMatrix():
    '''public void setTextMatrix(final float a, final float b, final float c, final float d, final float x, final float y)
    public void setTextMatrix(final float x, final float y)
    '''
def moveText():
    '''public void moveText(final float x, final float y)
    '''
def moveTextWithLeading():
    '''public void moveTextWithLeading(final float x, final float y)
    '''
def newlineText():
    '''public void newlineText()
    '''
def addOutline():
    '''public void addOutline(final PdfOutline outline)
    public void addOutline(final PdfOutline outline, final String name)
    '''
def getRootOutline():
    '''public PdfOutline getRootOutline()
    '''
def showTextAligned():
    '''public void showTextAligned(final int alignment, final String text, float x, float y, final float rotation)
    '''
def showTextAlignedKerned():
    '''public void showTextAlignedKerned(final int alignement, final String text, float x, float y, final float rotation)
    '''
def concatCTM():
    '''public void concatCTM(final float a, final float b, final float c, final float d, final float e, final float f)
    '''
def bezierArc():
    '''public static ArrayList bezierArc(float x1, float y1, float x2, float y2, final float startAng, final float extent)
    '''
def arc():
    '''public void arc(final float x1, final float y1, final float x2, final float y2, final float startAng, final float extent)
    '''
def ellipse():
    '''public void ellipse(final float x1, final float y1, final float x2, final float y2)
    '''
def createPattern():
    '''public PdfPatternPainter createPattern(final float width, final float height, final float xstep, final float ystep)
    public PdfPatternPainter createPattern(final float width, final float height)
    public PdfPatternPainter createPattern(final float width, final float height, final float xstep, final float ystep, final Color color)
    public PdfPatternPainter createPattern(final float width, final float height, final Color color)
    '''
def createTemplate():
    '''public PdfTemplate createTemplate(final float width, final float height)
    '''
def createAppearance():
    '''public PdfAppearance createAppearance(final float width, final float height)
    '''
def addPSXObject():
    '''public void addPSXObject(final PdfPSXObject psobject)
    '''
def addTemplate():
    '''public void addTemplate(final PdfTemplate template, final float a, final float b, final float c, final float d, final float e, final float f)
    public void addTemplate(final PdfTemplate template, final float x, final float y)
    '''
def setCMYKColorFill():
    '''public void setCMYKColorFill(final int cyan, final int magenta, final int yellow, final int black)
    '''
def setCMYKColorStroke():
    '''public void setCMYKColorStroke(final int cyan, final int magenta, final int yellow, final int black)
    '''
def setRGBColorFill():
    '''public void setRGBColorFill(final int red, final int green, final int blue)
    '''
def setRGBColorStroke():
    '''public void setRGBColorStroke(final int red, final int green, final int blue)
    '''
def setColorStroke():
    '''public void setColorStroke(final Color color)
    public void setColorStroke(final PdfSpotColor sp, final float tint)
    '''
def setColorFill():
    '''public void setColorFill(final Color color)
    public void setColorFill(final PdfSpotColor sp, final float tint)
    '''
def setPatternFill():
    '''public void setPatternFill(final PdfPatternPainter p)
    public void setPatternFill(final PdfPatternPainter p, final Color color)
    public void setPatternFill(final PdfPatternPainter p, final Color color, final float tint)
    '''
def setPatternStroke():
    '''public void setPatternStroke(final PdfPatternPainter p, final Color color)
    public void setPatternStroke(final PdfPatternPainter p, final Color color, final float tint)
    public void setPatternStroke(final PdfPatternPainter p)
    '''
def paintShading():
    '''public void paintShading(final PdfShading shading)
    public void paintShading(final PdfShadingPattern shading)
    '''
def setShadingFill():
    '''public void setShadingFill(final PdfShadingPattern shading)
    '''
def setShadingStroke():
    '''public void setShadingStroke(final PdfShadingPattern shading)
    '''
def getPdfWriter():
    '''public PdfWriter getPdfWriter()
    '''
def getPdfDocument():
    '''public PdfDocument getPdfDocument()
    '''
def localGoto():
    '''public void localGoto(final String name, final float llx, final float lly, final float urx, final float ury)
    '''
def localDestination():
    '''public boolean localDestination(final String name, final PdfDestination destination)
    '''
def getDuplicate():
    '''public PdfContentByte getDuplicate()
    '''
def remoteGoto():
    '''public void remoteGoto(final String filename, final String name, final float llx, final float lly, final float urx, final float ury)
    public void remoteGoto(final String filename, final int page, final float llx, final float lly, final float urx, final float ury)
    '''
def roundRectangle():
    '''public void roundRectangle(float x, float y, float w, float h, float r)
    '''
def setAction():
    '''public void setAction(final PdfAction action, final float llx, final float lly, final float urx, final float ury)
    '''
def setLiteral():
    '''public void setLiteral(final String s)
    public void setLiteral(final char c)
    public void setLiteral(final float n)
    '''
def drawRadioField():
    '''public void drawRadioField(float llx, float lly, float urx, float ury, final boolean on)
    '''
def drawTextField():
    '''public void drawTextField(float llx, float lly, float urx, float ury)
    '''
def drawButton():
    '''public void drawButton(float llx, float lly, float urx, float ury, final String text, final BaseFont bf, final float size)
    '''
def createGraphicsShapes():
    '''public Graphics2D createGraphicsShapes(final float width, final float height)
    public Graphics2D createGraphicsShapes(final float width, final float height, final boolean convertImagesToJPEG, final float quality)
    '''
def createPrinterGraphicsShapes():
    '''public Graphics2D createPrinterGraphicsShapes(final float width, final float height, final PrinterJob printerJob)
    public Graphics2D createPrinterGraphicsShapes(final float width, final float height, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)
    '''
def createGraphics():
    '''public Graphics2D createGraphics(final float width, final float height)
    public Graphics2D createGraphics(final float width, final float height, final boolean convertImagesToJPEG, final float quality)
    public Graphics2D createGraphics(final float width, final float height, final FontMapper fontMapper)
    public Graphics2D createGraphics(final float width, final float height, final FontMapper fontMapper, final boolean convertImagesToJPEG, final float quality)
    '''
def createPrinterGraphics():
    '''public Graphics2D createPrinterGraphics(final float width, final float height, final PrinterJob printerJob)
    public Graphics2D createPrinterGraphics(final float width, final float height, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)
    public Graphics2D createPrinterGraphics(final float width, final float height, final FontMapper fontMapper, final PrinterJob printerJob)
    public Graphics2D createPrinterGraphics(final float width, final float height, final FontMapper fontMapper, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)
    '''
def setGState():
    '''public void setGState(final PdfGState gstate)
    '''
def beginLayer():
    '''public void beginLayer(final PdfOCG layer)
    '''
def endLayer():
    '''public void endLayer()
    '''
def transform():
    '''public void transform(final AffineTransform af)
    '''
def setDefaultColorspace():
    '''public void setDefaultColorspace(final PdfName name, final PdfObject obj)
    '''
