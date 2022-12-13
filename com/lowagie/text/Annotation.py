TEXT = "int  0"
URL_NET = "int  1"
URL_AS_STRING = "int  2"
FILE_DEST = "int  3"
FILE_PAGE = "int  4"
NAMED_DEST = "int  5"
LAUNCH = "int  6"
SCREEN = "int  7"
def Annotation():
'''public Annotation(final String title, final String text)
public Annotation(final String title, final String text, final float llx, final float lly, final float urx, final float ury)
public Annotation(final float llx, final float lly, final float urx, final float ury, final URL url)
public Annotation(final float llx, final float lly, final float urx, final float ury, final String url)
public Annotation(final float llx, final float lly, final float urx, final float ury, final String file, final String dest)
public Annotation(final float llx, final float lly, final float urx, final float ury, final String moviePath, final String mimeType, final boolean showOnDisplay)
public Annotation(final float llx, final float lly, final float urx, final float ury, final String file, final int page)
public Annotation(final float llx, final float lly, final float urx, final float ury, final int named)
public Annotation(final float llx, final float lly, final float urx, final float ury, final String application, final String parameters, final String operation, final String defaultdir)
public Annotation(final Properties attributes)
'''
pass
def type():
'''public int type()
'''
pass
def process():
'''public boolean process(final ElementListener listener)
'''
pass
def getChunks():
'''public ArrayList getChunks()
'''
pass
def setDimensions():
'''public void setDimensions(final float llx, final float lly, final float urx, final float ury)
'''
pass
def llx():
'''public float llx()
public float llx(final float def)
'''
pass
def lly():
'''public float lly()
public float lly(final float def)
'''
pass
def urx():
'''public float urx()
public float urx(final float def)
'''
pass
def ury():
'''public float ury()
public float ury(final float def)
'''
pass
def annotationType():
'''public int annotationType()
'''
pass
def title():
'''public String title()
'''
pass
def content():
'''public String content()
'''
pass
def attributes():
'''public HashMap attributes()
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
