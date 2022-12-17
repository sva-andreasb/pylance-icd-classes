FLAGS_INVISIBLE = "int  1"
FLAGS_HIDDEN = "int  2"
FLAGS_PRINT = "int  4"
FLAGS_NOZOOM = "int  8"
FLAGS_NOROTATE = "int  16"
FLAGS_NOVIEW = "int  32"
FLAGS_READONLY = "int  64"
FLAGS_LOCKED = "int  128"
FLAGS_TOGGLENOVIEW = "int  256"
MARKUP_HIGHLIGHT = "int  0"
MARKUP_UNDERLINE = "int  1"
MARKUP_STRIKEOUT = "int  2"
def ():
    '''returns PdfAnnotation\n\n
    (final PdfWriter writer, final float llx, final float lly, final float urx, final float ury, final PdfAction action)\n
    '''
def setDefaultAppearanceString():
    '''returns None\n\n
    setDefaultAppearanceString(final PdfContentByte cb)\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final int flags)\n
    '''
def setBorder():
    '''returns None\n\n
    setBorder(final PdfBorderArray border)\n
    '''
def setBorderStyle():
    '''returns None\n\n
    setBorderStyle(final PdfBorderDictionary border)\n
    '''
def setHighlighting():
    '''returns None\n\n
    setHighlighting(final PdfName highlight)\n
    '''
def setAppearance():
    '''returns None\n\n
    setAppearance(final PdfName ap, final PdfTemplate template)\n
    setAppearance(final PdfName ap, final String state, final PdfTemplate template)\n
    '''
def setAppearanceState():
    '''returns None\n\n
    setAppearanceState(final String state)\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final Color color)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def setPopup():
    '''returns None\n\n
    setPopup(final PdfAnnotation popup)\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final PdfAction action)\n
    '''
def setAdditionalActions():
    '''returns None\n\n
    setAdditionalActions(final PdfName key, final PdfAction action)\n
    '''
def isUsed():
    '''returns boolean\n\n
    isUsed()\n
    '''
def isForm():
    '''returns boolean\n\n
    isForm()\n
    '''
def isAnnotation():
    '''returns boolean\n\n
    isAnnotation()\n
    '''
def setPage():
    '''returns None\n\n
    setPage(final int page)\n
    setPage()\n
    '''
def getPlaceInPage():
    '''returns int\n\n
    getPlaceInPage()\n
    '''
def setPlaceInPage():
    '''returns None\n\n
    setPlaceInPage(final int placeInPage)\n
    '''
def setRotate():
    '''returns None\n\n
    setRotate(final int v)\n
    '''
def setMKRotation():
    '''returns None\n\n
    setMKRotation(final int rotation)\n
    '''
def setMKBorderColor():
    '''returns None\n\n
    setMKBorderColor(final Color color)\n
    '''
def setMKBackgroundColor():
    '''returns None\n\n
    setMKBackgroundColor(final Color color)\n
    '''
def setMKNormalCaption():
    '''returns None\n\n
    setMKNormalCaption(final String caption)\n
    '''
def setMKRolloverCaption():
    '''returns None\n\n
    setMKRolloverCaption(final String caption)\n
    '''
def setMKAlternateCaption():
    '''returns None\n\n
    setMKAlternateCaption(final String caption)\n
    '''
def setMKNormalIcon():
    '''returns None\n\n
    setMKNormalIcon(final PdfTemplate template)\n
    '''
def setMKRolloverIcon():
    '''returns None\n\n
    setMKRolloverIcon(final PdfTemplate template)\n
    '''
def setMKAlternateIcon():
    '''returns None\n\n
    setMKAlternateIcon(final PdfTemplate template)\n
    '''
def setMKIconFit():
    '''returns None\n\n
    setMKIconFit(final PdfName scale, final PdfName scalingType, final float leftoverLeft, final float leftoverBottom, final boolean fitInBounds)\n
    '''
def setMKTextPosition():
    '''returns None\n\n
    setMKTextPosition(final int tp)\n
    '''
def setLayer():
    '''returns None\n\n
    setLayer(final PdfOCG layer)\n
    '''
