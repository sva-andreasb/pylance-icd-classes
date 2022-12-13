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
pass
def toString():
'''public String toString()
'''
pass
def getInternalBuffer():
'''public ByteBuffer getInternalBuffer()
'''
pass
def toPdf():
'''public byte[] toPdf(final PdfWriter writer)
'''
pass
def add():
'''public void add(final PdfContentByte other)
'''
pass
def getXTLM():
'''public float getXTLM()
'''
pass
def getYTLM():
'''public float getYTLM()
'''
pass
def getLeading():
'''public float getLeading()
'''
pass
def setFlatness():
'''public void setFlatness(final float flatness)
'''
pass
def setLineCap():
'''public void setLineCap(final int style)
'''
pass
def setLineDash():
'''public void setLineDash(final float phase)
public void setLineDash(final float unitsOn, final float phase)
public void setLineDash(final float unitsOn, final float unitsOff, final float phase)
public final void setLineDash(final float[] array, final float phase)
'''
pass
def setLineJoin():
'''public void setLineJoin(final int style)
'''
pass
def setLineWidth():
'''public void setLineWidth(final float w)
'''
pass
def setMiterLimit():
'''public void setMiterLimit(final float miterLimit)
'''
pass
def clip():
'''public void clip()
'''
pass
def eoClip():
'''public void eoClip()
'''
pass
def setGrayFill():
'''public void setGrayFill(final float gray)
'''
pass
def resetGrayFill():
'''public void resetGrayFill()
'''
pass
def setGrayStroke():
'''public void setGrayStroke(final float gray)
'''
pass
def resetGrayStroke():
'''public void resetGrayStroke()
'''
pass
def setRGBColorFillF():
'''public void setRGBColorFillF(final float red, final float green, final float blue)
'''
pass
def resetRGBColorFill():
'''public void resetRGBColorFill()
'''
pass
def setRGBColorStrokeF():
'''public void setRGBColorStrokeF(final float red, final float green, final float blue)
'''
pass
def resetRGBColorStroke():
'''public void resetRGBColorStroke()
'''
pass
def setCMYKColorFillF():
'''public void setCMYKColorFillF(final float cyan, final float magenta, final float yellow, final float black)
'''
pass
def resetCMYKColorFill():
'''public void resetCMYKColorFill()
'''
pass
def setCMYKColorStrokeF():
'''public void setCMYKColorStrokeF(final float cyan, final float magenta, final float yellow, final float black)
'''
pass
def resetCMYKColorStroke():
'''public void resetCMYKColorStroke()
'''
pass
def moveTo():
'''public void moveTo(final float x, final float y)
'''
pass
def lineTo():
'''public void lineTo(final float x, final float y)
'''
pass
def curveTo():
'''public void curveTo(final float x1, final float y1, final float x2, final float y2, final float x3, final float y3)
public void curveTo(final float x2, final float y2, final float x3, final float y3)
'''
pass
def curveFromTo():
'''public void curveFromTo(final float x1, final float y1, final float x3, final float y3)
'''
pass
def circle():
'''public void circle(final float x, final float y, final float r)
'''
pass
def rectangle():
'''public void rectangle(final float x, final float y, final float w, final float h)
public void rectangle(final Rectangle rectangle)
'''
pass
def variableRectangle():
'''public void variableRectangle(final Rectangle rect)
'''
pass
def closePath():
'''public void closePath()
'''
pass
def newPath():
'''public void newPath()
'''
pass
def stroke():
'''public void stroke()
'''
pass
def closePathStroke():
'''public void closePathStroke()
'''
pass
def fill():
'''public void fill()
'''
pass
def eoFill():
'''public void eoFill()
'''
pass
def fillStroke():
'''public void fillStroke()
'''
pass
def closePathFillStroke():
'''public void closePathFillStroke()
'''
pass
def eoFillStroke():
'''public void eoFillStroke()
'''
pass
def closePathEoFillStroke():
'''public void closePathEoFillStroke()
'''
pass
def addImage():
'''public void addImage(final Image image)
public void addImage(final Image image, final float a, final float b, final float c, final float d, final float e, final float f)
'''
pass
def reset():
'''public void reset()
'''
pass
def beginText():
'''public void beginText()
'''
pass
def endText():
'''public void endText()
'''
pass
def saveState():
'''public void saveState()
'''
pass
def restoreState():
'''public void restoreState()
'''
pass
def setCharacterSpacing():
'''public void setCharacterSpacing(final float charSpace)
'''
pass
def setWordSpacing():
'''public void setWordSpacing(final float wordSpace)
'''
pass
def setHorizontalScaling():
'''public void setHorizontalScaling(final float scale)
'''
pass
def setLeading():
'''public void setLeading(final float leading)
'''
pass
def setFontAndSize():
'''public void setFontAndSize(final BaseFont bf, final float size)
'''
pass
def setTextRenderingMode():
'''public void setTextRenderingMode(final int rendering)
'''
pass
def setTextRise():
'''public void setTextRise(final float rise)
'''
pass
def showText():
'''public void showText(final String text)
public void showText(final PdfTextArray text)
'''
pass
def getKernArray():
'''public static PdfTextArray getKernArray(final String text, final BaseFont font)
'''
pass
def showTextKerned():
'''public void showTextKerned(final String text)
'''
pass
def newlineShowText():
'''public void newlineShowText(final String text)
public void newlineShowText(final float wordSpacing, final float charSpacing, final String text)
'''
pass
def setTextMatrix():
'''public void setTextMatrix(final float a, final float b, final float c, final float d, final float x, final float y)
public void setTextMatrix(final float x, final float y)
'''
pass
def moveText():
'''public void moveText(final float x, final float y)
'''
pass
def moveTextWithLeading():
'''public void moveTextWithLeading(final float x, final float y)
'''
pass
def newlineText():
'''public void newlineText()
'''
pass
def addOutline():
'''public void addOutline(final PdfOutline outline)
public void addOutline(final PdfOutline outline, final String name)
'''
pass
def getRootOutline():
'''public PdfOutline getRootOutline()
'''
pass
def showTextAligned():
'''public void showTextAligned(final int alignment, final String text, float x, float y, final float rotation)
'''
pass
def showTextAlignedKerned():
'''public void showTextAlignedKerned(final int alignement, final String text, float x, float y, final float rotation)
'''
pass
def concatCTM():
'''public void concatCTM(final float a, final float b, final float c, final float d, final float e, final float f)
'''
pass
def bezierArc():
'''public static ArrayList bezierArc(float x1, float y1, float x2, float y2, final float startAng, final float extent)
'''
pass
def arc():
'''public void arc(final float x1, final float y1, final float x2, final float y2, final float startAng, final float extent)
'''
pass
def ellipse():
'''public void ellipse(final float x1, final float y1, final float x2, final float y2)
'''
pass
def createPattern():
'''public PdfPatternPainter createPattern(final float width, final float height, final float xstep, final float ystep)
public PdfPatternPainter createPattern(final float width, final float height)
public PdfPatternPainter createPattern(final float width, final float height, final float xstep, final float ystep, final Color color)
public PdfPatternPainter createPattern(final float width, final float height, final Color color)
'''
pass
def createTemplate():
'''public PdfTemplate createTemplate(final float width, final float height)
'''
pass
def createAppearance():
'''public PdfAppearance createAppearance(final float width, final float height)
'''
pass
def addPSXObject():
'''public void addPSXObject(final PdfPSXObject psobject)
'''
pass
def addTemplate():
'''public void addTemplate(final PdfTemplate template, final float a, final float b, final float c, final float d, final float e, final float f)
public void addTemplate(final PdfTemplate template, final float x, final float y)
'''
pass
def setCMYKColorFill():
'''public void setCMYKColorFill(final int cyan, final int magenta, final int yellow, final int black)
'''
pass
def setCMYKColorStroke():
'''public void setCMYKColorStroke(final int cyan, final int magenta, final int yellow, final int black)
'''
pass
def setRGBColorFill():
'''public void setRGBColorFill(final int red, final int green, final int blue)
'''
pass
def setRGBColorStroke():
'''public void setRGBColorStroke(final int red, final int green, final int blue)
'''
pass
def setColorStroke():
'''public void setColorStroke(final Color color)
public void setColorStroke(final PdfSpotColor sp, final float tint)
'''
pass
def setColorFill():
'''public void setColorFill(final Color color)
public void setColorFill(final PdfSpotColor sp, final float tint)
'''
pass
def setPatternFill():
'''public void setPatternFill(final PdfPatternPainter p)
public void setPatternFill(final PdfPatternPainter p, final Color color)
public void setPatternFill(final PdfPatternPainter p, final Color color, final float tint)
'''
pass
def setPatternStroke():
'''public void setPatternStroke(final PdfPatternPainter p, final Color color)
public void setPatternStroke(final PdfPatternPainter p, final Color color, final float tint)
public void setPatternStroke(final PdfPatternPainter p)
'''
pass
def paintShading():
'''public void paintShading(final PdfShading shading)
public void paintShading(final PdfShadingPattern shading)
'''
pass
def setShadingFill():
'''public void setShadingFill(final PdfShadingPattern shading)
'''
pass
def setShadingStroke():
'''public void setShadingStroke(final PdfShadingPattern shading)
'''
pass
def getPdfWriter():
'''public PdfWriter getPdfWriter()
'''
pass
def getPdfDocument():
'''public PdfDocument getPdfDocument()
'''
pass
def localGoto():
'''public void localGoto(final String name, final float llx, final float lly, final float urx, final float ury)
'''
pass
def localDestination():
'''public boolean localDestination(final String name, final PdfDestination destination)
'''
pass
def getDuplicate():
'''public PdfContentByte getDuplicate()
'''
pass
def remoteGoto():
'''public void remoteGoto(final String filename, final String name, final float llx, final float lly, final float urx, final float ury)
public void remoteGoto(final String filename, final int page, final float llx, final float lly, final float urx, final float ury)
'''
pass
def roundRectangle():
'''public void roundRectangle(float x, float y, float w, float h, float r)
'''
pass
def setAction():
'''public void setAction(final PdfAction action, final float llx, final float lly, final float urx, final float ury)
'''
pass
def setLiteral():
'''public void setLiteral(final String s)
public void setLiteral(final char c)
public void setLiteral(final float n)
'''
pass
def drawRadioField():
'''public void drawRadioField(float llx, float lly, float urx, float ury, final boolean on)
'''
pass
def drawTextField():
'''public void drawTextField(float llx, float lly, float urx, float ury)
'''
pass
def drawButton():
'''public void drawButton(float llx, float lly, float urx, float ury, final String text, final BaseFont bf, final float size)
'''
pass
def createGraphicsShapes():
'''public Graphics2D createGraphicsShapes(final float width, final float height)
public Graphics2D createGraphicsShapes(final float width, final float height, final boolean convertImagesToJPEG, final float quality)
'''
pass
def createPrinterGraphicsShapes():
'''public Graphics2D createPrinterGraphicsShapes(final float width, final float height, final PrinterJob printerJob)
public Graphics2D createPrinterGraphicsShapes(final float width, final float height, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)
'''
pass
def createGraphics():
'''public Graphics2D createGraphics(final float width, final float height)
public Graphics2D createGraphics(final float width, final float height, final boolean convertImagesToJPEG, final float quality)
public Graphics2D createGraphics(final float width, final float height, final FontMapper fontMapper)
public Graphics2D createGraphics(final float width, final float height, final FontMapper fontMapper, final boolean convertImagesToJPEG, final float quality)
'''
pass
def createPrinterGraphics():
'''public Graphics2D createPrinterGraphics(final float width, final float height, final PrinterJob printerJob)
public Graphics2D createPrinterGraphics(final float width, final float height, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)
public Graphics2D createPrinterGraphics(final float width, final float height, final FontMapper fontMapper, final PrinterJob printerJob)
public Graphics2D createPrinterGraphics(final float width, final float height, final FontMapper fontMapper, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)
'''
pass
def setGState():
'''public void setGState(final PdfGState gstate)
'''
pass
def beginLayer():
'''public void beginLayer(final PdfOCG layer)
'''
pass
def endLayer():
'''public void endLayer()
'''
pass
def transform():
'''public void transform(final AffineTransform af)
'''
pass
def setDefaultColorspace():
'''public void setDefaultColorspace(final PdfName name, final PdfObject obj)
'''
pass
