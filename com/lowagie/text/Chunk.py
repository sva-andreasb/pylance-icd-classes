OBJECT_REPLACEMENT_CHARACTER = "String  \"\ufffc\""
SUBSUPSCRIPT = "String  \"SUBSUPSCRIPT\""
UNDERLINE = "String  \"UNDERLINE\""
COLOR = "String  \"COLOR\""
ENCODING = "String  \"ENCODING\""
REMOTEGOTO = "String  \"REMOTEGOTO\""
LOCALGOTO = "String  \"LOCALGOTO\""
LOCALDESTINATION = "String  \"LOCALDESTINATION\""
IMAGE = "String  \"IMAGE\""
GENERICTAG = "String  \"GENERICTAG\""
NEWPAGE = "String  \"NEWPAGE\""
SPLITCHARACTER = "String  \"SPLITCHARACTER\""
ACTION = "String  \"ACTION\""
BACKGROUND = "String  \"BACKGROUND\""
PDFANNOTATION = "String  \"PDFANNOTATION\""
HYPHENATION = "String  \"HYPHENATION\""
TEXTRENDERMODE = "String  \"TEXTRENDERMODE\""
SKEW = "String  \"SKEW\""
HSCALE = "String  \"HSCALE\""
def ():
    '''returns Chunk\n\n
    (final String content, final Font font)\n
    (final String content)\n
    (final char c, final Font font)\n
    (final char c)\n
    (final Image image, final float offsetX, final float offsetY)\n
    (final Image image, final float offsetX, final float offsetY, final boolean changeLeading)\n
    (final Properties attributes)\n
    '''
def process():
    '''returns boolean\n\n
    process(final ElementListener listener)\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def getChunks():
    '''returns ArrayList\n\n
    getChunks()\n
    '''
def append():
    '''returns StringBuffer\n\n
    append(final String string)\n
    '''
def font():
    '''returns Font\n\n
    font()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font font)\n
    '''
def content():
    '''returns String\n\n
    content()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def getWidthPoint():
    '''returns float\n\n
    getWidthPoint()\n
    '''
def setTextRise():
    '''returns Chunk\n\n
    setTextRise(final float rise)\n
    '''
def getTextRise():
    '''returns float\n\n
    getTextRise()\n
    '''
def setTextRenderMode():
    '''returns Chunk\n\n
    setTextRenderMode(final int mode, final float strokeWidth, final Color strokeColor)\n
    '''
def setSkew():
    '''returns Chunk\n\n
    setSkew(float alpha, float beta)\n
    '''
def setHorizontalScaling():
    '''returns Chunk\n\n
    setHorizontalScaling(final float scale)\n
    '''
def getHorizontalScaling():
    '''returns float\n\n
    getHorizontalScaling()\n
    '''
def setAction():
    '''returns Chunk\n\n
    setAction(final PdfAction action)\n
    '''
def setAnchor():
    '''returns Chunk\n\n
    setAnchor(final URL url)\n
    setAnchor(final String url)\n
    '''
def setLocalGoto():
    '''returns Chunk\n\n
    setLocalGoto(final String name)\n
    '''
def setBackground():
    '''returns Chunk\n\n
    setBackground(final Color color)\n
    setBackground(final Color color, final float extraLeft, final float extraBottom, final float extraRight, final float extraTop)\n
    '''
def setUnderline():
    '''returns Chunk\n\n
    setUnderline(final float thickness, final float yPosition)\n
    setUnderline(final Color color, final float thickness, final float thicknessMul, final float yPosition, final float yPositionMul, final int cap)\n
    '''
def setAnnotation():
    '''returns Chunk\n\n
    setAnnotation(final PdfAnnotation annotation)\n
    '''
def setHyphenation():
    '''returns Chunk\n\n
    setHyphenation(final HyphenationEvent hyphenation)\n
    '''
def setRemoteGoto():
    '''returns Chunk\n\n
    setRemoteGoto(final String filename, final String name)\n
    setRemoteGoto(final String filename, final int page)\n
    '''
def setLocalDestination():
    '''returns Chunk\n\n
    setLocalDestination(final String name)\n
    '''
def setGenericTag():
    '''returns Chunk\n\n
    setGenericTag(final String text)\n
    '''
def setSplitCharacter():
    '''returns Chunk\n\n
    setSplitCharacter(final SplitCharacter splitCharacter)\n
    '''
def setNewPage():
    '''returns Chunk\n\n
    setNewPage()\n
    '''
def getAttributes():
    '''returns HashMap\n\n
    getAttributes()\n
    '''
def hasAttributes():
    '''returns boolean\n\n
    hasAttributes()\n
    '''
def getImage():
    '''returns Image\n\n
    getImage()\n
    '''
def setMarkupAttribute():
    '''returns None\n\n
    setMarkupAttribute(final String name, final String value)\n
    '''
def setMarkupAttributes():
    '''returns None\n\n
    setMarkupAttributes(final Properties markupAttributes)\n
    '''
def getMarkupAttribute():
    '''returns String\n\n
    getMarkupAttribute(final String name)\n
    '''
def getMarkupAttributeNames():
    '''returns Set\n\n
    getMarkupAttributeNames()\n
    '''
def getMarkupAttributes():
    '''returns Properties\n\n
    getMarkupAttributes()\n
    '''
