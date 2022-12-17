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
def ():
    '''returns PdfContentByte\n\n
    (final PdfWriter wr)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getInternalBuffer():
    '''returns ByteBuffer\n\n
    getInternalBuffer()\n
    '''
def toPdf():
    '''returns byte[]\n\n
    toPdf(final PdfWriter writer)\n
    '''
def add():
    '''returns None\n\n
    add(final PdfContentByte other)\n
    '''
def getXTLM():
    '''returns float\n\n
    getXTLM()\n
    '''
def getYTLM():
    '''returns float\n\n
    getYTLM()\n
    '''
def getLeading():
    '''returns float\n\n
    getLeading()\n
    '''
def setFlatness():
    '''returns None\n\n
    setFlatness(final float flatness)\n
    '''
def setLineCap():
    '''returns None\n\n
    setLineCap(final int style)\n
    '''
def setLineDash():
    '''returns None\n\n
    setLineDash(final float phase)\n
    setLineDash(final float unitsOn, final float phase)\n
    setLineDash(final float unitsOn, final float unitsOff, final float phase)\n
    '''
def setLineJoin():
    '''returns None\n\n
    setLineJoin(final int style)\n
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final float w)\n
    '''
def setMiterLimit():
    '''returns None\n\n
    setMiterLimit(final float miterLimit)\n
    '''
def clip():
    '''returns None\n\n
    clip()\n
    '''
def eoClip():
    '''returns None\n\n
    eoClip()\n
    '''
def setGrayFill():
    '''returns None\n\n
    setGrayFill(final float gray)\n
    '''
def resetGrayFill():
    '''returns None\n\n
    resetGrayFill()\n
    '''
def setGrayStroke():
    '''returns None\n\n
    setGrayStroke(final float gray)\n
    '''
def resetGrayStroke():
    '''returns None\n\n
    resetGrayStroke()\n
    '''
def setRGBColorFillF():
    '''returns None\n\n
    setRGBColorFillF(final float red, final float green, final float blue)\n
    '''
def resetRGBColorFill():
    '''returns None\n\n
    resetRGBColorFill()\n
    '''
def setRGBColorStrokeF():
    '''returns None\n\n
    setRGBColorStrokeF(final float red, final float green, final float blue)\n
    '''
def resetRGBColorStroke():
    '''returns None\n\n
    resetRGBColorStroke()\n
    '''
def setCMYKColorFillF():
    '''returns None\n\n
    setCMYKColorFillF(final float cyan, final float magenta, final float yellow, final float black)\n
    '''
def resetCMYKColorFill():
    '''returns None\n\n
    resetCMYKColorFill()\n
    '''
def setCMYKColorStrokeF():
    '''returns None\n\n
    setCMYKColorStrokeF(final float cyan, final float magenta, final float yellow, final float black)\n
    '''
def resetCMYKColorStroke():
    '''returns None\n\n
    resetCMYKColorStroke()\n
    '''
def moveTo():
    '''returns None\n\n
    moveTo(final float x, final float y)\n
    '''
def lineTo():
    '''returns None\n\n
    lineTo(final float x, final float y)\n
    '''
def curveTo():
    '''returns None\n\n
    curveTo(final float x1, final float y1, final float x2, final float y2, final float x3, final float y3)\n
    curveTo(final float x2, final float y2, final float x3, final float y3)\n
    '''
def curveFromTo():
    '''returns None\n\n
    curveFromTo(final float x1, final float y1, final float x3, final float y3)\n
    '''
def circle():
    '''returns None\n\n
    circle(final float x, final float y, final float r)\n
    '''
def rectangle():
    '''returns None\n\n
    rectangle(final float x, final float y, final float w, final float h)\n
    rectangle(final Rectangle rectangle)\n
    '''
def variableRectangle():
    '''returns None\n\n
    variableRectangle(final Rectangle rect)\n
    '''
def closePath():
    '''returns None\n\n
    closePath()\n
    '''
def newPath():
    '''returns None\n\n
    newPath()\n
    '''
def stroke():
    '''returns None\n\n
    stroke()\n
    '''
def closePathStroke():
    '''returns None\n\n
    closePathStroke()\n
    '''
def fill():
    '''returns None\n\n
    fill()\n
    '''
def eoFill():
    '''returns None\n\n
    eoFill()\n
    '''
def fillStroke():
    '''returns None\n\n
    fillStroke()\n
    '''
def closePathFillStroke():
    '''returns None\n\n
    closePathFillStroke()\n
    '''
def eoFillStroke():
    '''returns None\n\n
    eoFillStroke()\n
    '''
def closePathEoFillStroke():
    '''returns None\n\n
    closePathEoFillStroke()\n
    '''
def addImage():
    '''returns None\n\n
    addImage(final Image image)\n
    addImage(final Image image, final float a, final float b, final float c, final float d, final float e, final float f)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def beginText():
    '''returns None\n\n
    beginText()\n
    '''
def endText():
    '''returns None\n\n
    endText()\n
    '''
def saveState():
    '''returns None\n\n
    saveState()\n
    '''
def restoreState():
    '''returns None\n\n
    restoreState()\n
    '''
def setCharacterSpacing():
    '''returns None\n\n
    setCharacterSpacing(final float charSpace)\n
    '''
def setWordSpacing():
    '''returns None\n\n
    setWordSpacing(final float wordSpace)\n
    '''
def setHorizontalScaling():
    '''returns None\n\n
    setHorizontalScaling(final float scale)\n
    '''
def setLeading():
    '''returns None\n\n
    setLeading(final float leading)\n
    '''
def setFontAndSize():
    '''returns None\n\n
    setFontAndSize(final BaseFont bf, final float size)\n
    '''
def setTextRenderingMode():
    '''returns None\n\n
    setTextRenderingMode(final int rendering)\n
    '''
def setTextRise():
    '''returns None\n\n
    setTextRise(final float rise)\n
    '''
def showText():
    '''returns None\n\n
    showText(final String text)\n
    showText(final PdfTextArray text)\n
    '''
def showTextKerned():
    '''returns None\n\n
    showTextKerned(final String text)\n
    '''
def newlineShowText():
    '''returns None\n\n
    newlineShowText(final String text)\n
    newlineShowText(final float wordSpacing, final float charSpacing, final String text)\n
    '''
def setTextMatrix():
    '''returns None\n\n
    setTextMatrix(final float a, final float b, final float c, final float d, final float x, final float y)\n
    setTextMatrix(final float x, final float y)\n
    '''
def moveText():
    '''returns None\n\n
    moveText(final float x, final float y)\n
    '''
def moveTextWithLeading():
    '''returns None\n\n
    moveTextWithLeading(final float x, final float y)\n
    '''
def newlineText():
    '''returns None\n\n
    newlineText()\n
    '''
def addOutline():
    '''returns None\n\n
    addOutline(final PdfOutline outline)\n
    addOutline(final PdfOutline outline, final String name)\n
    '''
def getRootOutline():
    '''returns PdfOutline\n\n
    getRootOutline()\n
    '''
def showTextAligned():
    '''returns None\n\n
    showTextAligned(final int alignment, final String text, float x, float y, final float rotation)\n
    '''
def showTextAlignedKerned():
    '''returns None\n\n
    showTextAlignedKerned(final int alignement, final String text, float x, float y, final float rotation)\n
    '''
def concatCTM():
    '''returns None\n\n
    concatCTM(final float a, final float b, final float c, final float d, final float e, final float f)\n
    '''
def arc():
    '''returns None\n\n
    arc(final float x1, final float y1, final float x2, final float y2, final float startAng, final float extent)\n
    '''
def ellipse():
    '''returns None\n\n
    ellipse(final float x1, final float y1, final float x2, final float y2)\n
    '''
def createPattern():
    '''returns PdfPatternPainter\n\n
    createPattern(final float width, final float height, final float xstep, final float ystep)\n
    createPattern(final float width, final float height)\n
    createPattern(final float width, final float height, final float xstep, final float ystep, final Color color)\n
    createPattern(final float width, final float height, final Color color)\n
    '''
def createTemplate():
    '''returns PdfTemplate\n\n
    createTemplate(final float width, final float height)\n
    '''
def createAppearance():
    '''returns PdfAppearance\n\n
    createAppearance(final float width, final float height)\n
    '''
def addPSXObject():
    '''returns None\n\n
    addPSXObject(final PdfPSXObject psobject)\n
    '''
def addTemplate():
    '''returns None\n\n
    addTemplate(final PdfTemplate template, final float a, final float b, final float c, final float d, final float e, final float f)\n
    addTemplate(final PdfTemplate template, final float x, final float y)\n
    '''
def setCMYKColorFill():
    '''returns None\n\n
    setCMYKColorFill(final int cyan, final int magenta, final int yellow, final int black)\n
    '''
def setCMYKColorStroke():
    '''returns None\n\n
    setCMYKColorStroke(final int cyan, final int magenta, final int yellow, final int black)\n
    '''
def setRGBColorFill():
    '''returns None\n\n
    setRGBColorFill(final int red, final int green, final int blue)\n
    '''
def setRGBColorStroke():
    '''returns None\n\n
    setRGBColorStroke(final int red, final int green, final int blue)\n
    '''
def setColorStroke():
    '''returns None\n\n
    setColorStroke(final Color color)\n
    setColorStroke(final PdfSpotColor sp, final float tint)\n
    '''
def setColorFill():
    '''returns None\n\n
    setColorFill(final Color color)\n
    setColorFill(final PdfSpotColor sp, final float tint)\n
    '''
def setPatternFill():
    '''returns None\n\n
    setPatternFill(final PdfPatternPainter p)\n
    setPatternFill(final PdfPatternPainter p, final Color color)\n
    setPatternFill(final PdfPatternPainter p, final Color color, final float tint)\n
    '''
def setPatternStroke():
    '''returns None\n\n
    setPatternStroke(final PdfPatternPainter p, final Color color)\n
    setPatternStroke(final PdfPatternPainter p, final Color color, final float tint)\n
    setPatternStroke(final PdfPatternPainter p)\n
    '''
def paintShading():
    '''returns None\n\n
    paintShading(final PdfShading shading)\n
    paintShading(final PdfShadingPattern shading)\n
    '''
def setShadingFill():
    '''returns None\n\n
    setShadingFill(final PdfShadingPattern shading)\n
    '''
def setShadingStroke():
    '''returns None\n\n
    setShadingStroke(final PdfShadingPattern shading)\n
    '''
def getPdfWriter():
    '''returns PdfWriter\n\n
    getPdfWriter()\n
    '''
def getPdfDocument():
    '''returns PdfDocument\n\n
    getPdfDocument()\n
    '''
def localGoto():
    '''returns None\n\n
    localGoto(final String name, final float llx, final float lly, final float urx, final float ury)\n
    '''
def localDestination():
    '''returns boolean\n\n
    localDestination(final String name, final PdfDestination destination)\n
    '''
def getDuplicate():
    '''returns PdfContentByte\n\n
    getDuplicate()\n
    '''
def remoteGoto():
    '''returns None\n\n
    remoteGoto(final String filename, final String name, final float llx, final float lly, final float urx, final float ury)\n
    remoteGoto(final String filename, final int page, final float llx, final float lly, final float urx, final float ury)\n
    '''
def roundRectangle():
    '''returns None\n\n
    roundRectangle(float x, float y, float w, float h, float r)\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final PdfAction action, final float llx, final float lly, final float urx, final float ury)\n
    '''
def setLiteral():
    '''returns None\n\n
    setLiteral(final String s)\n
    setLiteral(final char c)\n
    setLiteral(final float n)\n
    '''
def drawRadioField():
    '''returns None\n\n
    drawRadioField(float llx, float lly, float urx, float ury, final boolean on)\n
    '''
def drawTextField():
    '''returns None\n\n
    drawTextField(float llx, float lly, float urx, float ury)\n
    '''
def drawButton():
    '''returns None\n\n
    drawButton(float llx, float lly, float urx, float ury, final String text, final BaseFont bf, final float size)\n
    '''
def createGraphicsShapes():
    '''returns Graphics2D\n\n
    createGraphicsShapes(final float width, final float height)\n
    createGraphicsShapes(final float width, final float height, final boolean convertImagesToJPEG, final float quality)\n
    '''
def createPrinterGraphicsShapes():
    '''returns Graphics2D\n\n
    createPrinterGraphicsShapes(final float width, final float height, final PrinterJob printerJob)\n
    createPrinterGraphicsShapes(final float width, final float height, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)\n
    '''
def createGraphics():
    '''returns Graphics2D\n\n
    createGraphics(final float width, final float height)\n
    createGraphics(final float width, final float height, final boolean convertImagesToJPEG, final float quality)\n
    createGraphics(final float width, final float height, final FontMapper fontMapper)\n
    createGraphics(final float width, final float height, final FontMapper fontMapper, final boolean convertImagesToJPEG, final float quality)\n
    '''
def createPrinterGraphics():
    '''returns Graphics2D\n\n
    createPrinterGraphics(final float width, final float height, final PrinterJob printerJob)\n
    createPrinterGraphics(final float width, final float height, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)\n
    createPrinterGraphics(final float width, final float height, final FontMapper fontMapper, final PrinterJob printerJob)\n
    createPrinterGraphics(final float width, final float height, final FontMapper fontMapper, final boolean convertImagesToJPEG, final float quality, final PrinterJob printerJob)\n
    '''
def setGState():
    '''returns None\n\n
    setGState(final PdfGState gstate)\n
    '''
def beginLayer():
    '''returns None\n\n
    beginLayer(final PdfOCG layer)\n
    '''
def endLayer():
    '''returns None\n\n
    endLayer()\n
    '''
def transform():
    '''returns None\n\n
    transform(final AffineTransform af)\n
    '''
def setDefaultColorspace():
    '''returns None\n\n
    setDefaultColorspace(final PdfName name, final PdfObject obj)\n
    '''
