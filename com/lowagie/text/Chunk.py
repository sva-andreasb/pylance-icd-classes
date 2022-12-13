OBJECT_REPLACEMENT_CHARACTER = "String  \ufffc""
SUBSUPSCRIPT = "String  SUBSUPSCRIPT""
UNDERLINE = "String  UNDERLINE""
COLOR = "String  COLOR""
ENCODING = "String  ENCODING""
REMOTEGOTO = "String  REMOTEGOTO""
LOCALGOTO = "String  LOCALGOTO""
LOCALDESTINATION = "String  LOCALDESTINATION""
IMAGE = "String  IMAGE""
GENERICTAG = "String  GENERICTAG""
NEWPAGE = "String  NEWPAGE""
SPLITCHARACTER = "String  SPLITCHARACTER""
ACTION = "String  ACTION""
BACKGROUND = "String  BACKGROUND""
PDFANNOTATION = "String  PDFANNOTATION""
HYPHENATION = "String  HYPHENATION""
TEXTRENDERMODE = "String  TEXTRENDERMODE""
SKEW = "String  SKEW""
HSCALE = "String  HSCALE""
def Chunk():
'''public Chunk(final String content, final Font font)
public Chunk(final String content)
public Chunk(final char c, final Font font)
public Chunk(final char c)
public Chunk(final Image image, final float offsetX, final float offsetY)
public Chunk(final Image image, final float offsetX, final float offsetY, final boolean changeLeading)
public Chunk(final Properties attributes)
'''
pass
def process():
'''public boolean process(final ElementListener listener)
'''
pass
def type():
'''public int type()
'''
pass
def getChunks():
'''public ArrayList getChunks()
'''
pass
def append():
'''public StringBuffer append(final String string)
'''
pass
def font():
'''public Font font()
'''
pass
def setFont():
'''public void setFont(final Font font)
'''
pass
def content():
'''public String content()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def getWidthPoint():
'''public float getWidthPoint()
'''
pass
def setTextRise():
'''public Chunk setTextRise(final float rise)
'''
pass
def getTextRise():
'''public float getTextRise()
'''
pass
def setTextRenderMode():
'''public Chunk setTextRenderMode(final int mode, final float strokeWidth, final Color strokeColor)
'''
pass
def setSkew():
'''public Chunk setSkew(float alpha, float beta)
'''
pass
def setHorizontalScaling():
'''public Chunk setHorizontalScaling(final float scale)
'''
pass
def getHorizontalScaling():
'''public float getHorizontalScaling()
'''
pass
def setAction():
'''public Chunk setAction(final PdfAction action)
'''
pass
def setAnchor():
'''public Chunk setAnchor(final URL url)
public Chunk setAnchor(final String url)
'''
pass
def setLocalGoto():
'''public Chunk setLocalGoto(final String name)
'''
pass
def setBackground():
'''public Chunk setBackground(final Color color)
public Chunk setBackground(final Color color, final float extraLeft, final float extraBottom, final float extraRight, final float extraTop)
'''
pass
def setUnderline():
'''public Chunk setUnderline(final float thickness, final float yPosition)
public Chunk setUnderline(final Color color, final float thickness, final float thicknessMul, final float yPosition, final float yPositionMul, final int cap)
'''
pass
def addToArray():
'''public static Object[][] addToArray(Object[][] original, final Object[] item)
'''
pass
def setAnnotation():
'''public Chunk setAnnotation(final PdfAnnotation annotation)
'''
pass
def setHyphenation():
'''public Chunk setHyphenation(final HyphenationEvent hyphenation)
'''
pass
def setRemoteGoto():
'''public Chunk setRemoteGoto(final String filename, final String name)
public Chunk setRemoteGoto(final String filename, final int page)
'''
pass
def setLocalDestination():
'''public Chunk setLocalDestination(final String name)
'''
pass
def setGenericTag():
'''public Chunk setGenericTag(final String text)
'''
pass
def setSplitCharacter():
'''public Chunk setSplitCharacter(final SplitCharacter splitCharacter)
'''
pass
def setNewPage():
'''public Chunk setNewPage()
'''
pass
def getAttributes():
'''public HashMap getAttributes()
'''
pass
def hasAttributes():
'''public boolean hasAttributes()
'''
pass
def getImage():
'''public Image getImage()
'''
pass
def isTag():
'''public static boolean isTag(final String tag)
'''
pass
def setMarkupAttribute():
'''public void setMarkupAttribute(final String name, final String value)
'''
pass
def setMarkupAttributes():
'''public void setMarkupAttributes(final Properties markupAttributes)
'''
pass
def getMarkupAttribute():
'''public String getMarkupAttribute(final String name)
'''
pass
def getMarkupAttributeNames():
'''public Set getMarkupAttributeNames()
'''
pass
def getMarkupAttributes():
'''public Properties getMarkupAttributes()
'''
pass
def getKeySet():
'''public static Set getKeySet(final Hashtable table)
'''
pass
