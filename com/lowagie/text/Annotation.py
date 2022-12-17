TEXT = "int  0"
URL_NET = "int  1"
URL_AS_STRING = "int  2"
FILE_DEST = "int  3"
FILE_PAGE = "int  4"
NAMED_DEST = "int  5"
LAUNCH = "int  6"
SCREEN = "int  7"
def ():
    '''returns Annotation\n\n
    (final String title, final String text)\n
    (final String title, final String text, final float llx, final float lly, final float urx, final float ury)\n
    (final float llx, final float lly, final float urx, final float ury, final URL url)\n
    (final float llx, final float lly, final float urx, final float ury, final String url)\n
    (final float llx, final float lly, final float urx, final float ury, final String file, final String dest)\n
    (final float llx, final float lly, final float urx, final float ury, final String moviePath, final String mimeType, final boolean showOnDisplay)\n
    (final float llx, final float lly, final float urx, final float ury, final String file, final int page)\n
    (final float llx, final float lly, final float urx, final float ury, final int named)\n
    (final float llx, final float lly, final float urx, final float ury, final String application, final String parameters, final String operation, final String defaultdir)\n
    (final Properties attributes)\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def process():
    '''returns boolean\n\n
    process(final ElementListener listener)\n
    '''
def getChunks():
    '''returns ArrayList\n\n
    getChunks()\n
    '''
def setDimensions():
    '''returns None\n\n
    setDimensions(final float llx, final float lly, final float urx, final float ury)\n
    '''
def llx():
    '''returns float\n\n
    llx()\n
    llx(final float def)\n
    '''
def lly():
    '''returns float\n\n
    lly()\n
    lly(final float def)\n
    '''
def urx():
    '''returns float\n\n
    urx()\n
    urx(final float def)\n
    '''
def ury():
    '''returns float\n\n
    ury()\n
    ury(final float def)\n
    '''
def annotationType():
    '''returns int\n\n
    annotationType()\n
    '''
def title():
    '''returns String\n\n
    title()\n
    '''
def content():
    '''returns String\n\n
    content()\n
    '''
def attributes():
    '''returns HashMap\n\n
    attributes()\n
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
