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
def Chunk():
    '''public Chunk(final String content, final Font font)
    public Chunk(final String content)
    public Chunk(final char c, final Font font)
    public Chunk(final char c)
    public Chunk(final Image image, final float offsetX, final float offsetY)
    public Chunk(final Image image, final float offsetX, final float offsetY, final boolean changeLeading)
    public Chunk(final Properties attributes)
    '''
def process():
    '''public boolean process(final ElementListener listener)
    '''
def type():
    '''public int type()
    '''
def getChunks():
    '''public ArrayList getChunks()
    '''
def append():
    '''public StringBuffer append(final String string)
    '''
def font():
    '''public Font font()
    '''
def setFont():
    '''public void setFont(final Font font)
    '''
def content():
    '''public String content()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def getWidthPoint():
    '''public float getWidthPoint()
    '''
def setTextRise():
    '''public Chunk setTextRise(final float rise)
    '''
def getTextRise():
    '''public float getTextRise()
    '''
def setTextRenderMode():
    '''public Chunk setTextRenderMode(final int mode, final float strokeWidth, final Color strokeColor)
    '''
def setSkew():
    '''public Chunk setSkew(float alpha, float beta)
    '''
def setHorizontalScaling():
    '''public Chunk setHorizontalScaling(final float scale)
    '''
def getHorizontalScaling():
    '''public float getHorizontalScaling()
    '''
def setAction():
    '''public Chunk setAction(final PdfAction action)
    '''
def setAnchor():
    '''public Chunk setAnchor(final URL url)
    public Chunk setAnchor(final String url)
    '''
def setLocalGoto():
    '''public Chunk setLocalGoto(final String name)
    '''
def setBackground():
    '''public Chunk setBackground(final Color color)
    public Chunk setBackground(final Color color, final float extraLeft, final float extraBottom, final float extraRight, final float extraTop)
    '''
def setUnderline():
    '''public Chunk setUnderline(final float thickness, final float yPosition)
    public Chunk setUnderline(final Color color, final float thickness, final float thicknessMul, final float yPosition, final float yPositionMul, final int cap)
    '''
def addToArray():
    '''public static Object[][] addToArray(Object[][] original, final Object[] item)
    '''
def setAnnotation():
    '''public Chunk setAnnotation(final PdfAnnotation annotation)
    '''
def setHyphenation():
    '''public Chunk setHyphenation(final HyphenationEvent hyphenation)
    '''
def setRemoteGoto():
    '''public Chunk setRemoteGoto(final String filename, final String name)
    public Chunk setRemoteGoto(final String filename, final int page)
    '''
def setLocalDestination():
    '''public Chunk setLocalDestination(final String name)
    '''
def setGenericTag():
    '''public Chunk setGenericTag(final String text)
    '''
def setSplitCharacter():
    '''public Chunk setSplitCharacter(final SplitCharacter splitCharacter)
    '''
def setNewPage():
    '''public Chunk setNewPage()
    '''
def getAttributes():
    '''public HashMap getAttributes()
    '''
def hasAttributes():
    '''public boolean hasAttributes()
    '''
def getImage():
    '''public Image getImage()
    '''
def isTag():
    '''public static boolean isTag(final String tag)
    '''
def setMarkupAttribute():
    '''public void setMarkupAttribute(final String name, final String value)
    '''
def setMarkupAttributes():
    '''public void setMarkupAttributes(final Properties markupAttributes)
    '''
def getMarkupAttribute():
    '''public String getMarkupAttribute(final String name)
    '''
def getMarkupAttributeNames():
    '''public Set getMarkupAttributeNames()
    '''
def getMarkupAttributes():
    '''public Properties getMarkupAttributes()
    '''
def getKeySet():
    '''public static Set getKeySet(final Hashtable table)
    '''
