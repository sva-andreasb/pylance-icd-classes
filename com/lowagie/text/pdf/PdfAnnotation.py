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
def PdfAnnotation():
    '''    public PdfAnnotation(final PdfWriter writer, final float llx, final float lly, final float urx, final float ury, final PdfAction action)
    '''
def createScreen():
    '''    public static PdfAnnotation createScreen(final PdfWriter writer, final Rectangle rect, final String clipTitle, final PdfFileSpecification fs, final String mimeType, final boolean playOnDisplay)
    '''
def createText():
    '''    public static PdfAnnotation createText(final PdfWriter writer, final Rectangle rect, final String title, final String contents, final boolean open, final String icon)
    '''
def createLink():
    '''    public static PdfAnnotation createLink(final PdfWriter writer, final Rectangle rect, final PdfName highlight, final PdfAction action)
    public static PdfAnnotation createLink(final PdfWriter writer, final Rectangle rect, final PdfName highlight, final String namedDestination)
    public static PdfAnnotation createLink(final PdfWriter writer, final Rectangle rect, final PdfName highlight, final int page, final PdfDestination dest)
    '''
def createFreeText():
    '''    public static PdfAnnotation createFreeText(final PdfWriter writer, final Rectangle rect, final String contents, final PdfContentByte defaultAppearance)
    '''
def createLine():
    '''    public static PdfAnnotation createLine(final PdfWriter writer, final Rectangle rect, final String contents, final float x1, final float y1, final float x2, final float y2)
    '''
def createSquareCircle():
    '''    public static PdfAnnotation createSquareCircle(final PdfWriter writer, final Rectangle rect, final String contents, final boolean square)
    '''
def createMarkup():
    '''    public static PdfAnnotation createMarkup(final PdfWriter writer, final Rectangle rect, final String contents, final int type, final float[] quadPoints)
    '''
def createStamp():
    '''    public static PdfAnnotation createStamp(final PdfWriter writer, final Rectangle rect, final String contents, final String name)
    '''
def createInk():
    '''    public static PdfAnnotation createInk(final PdfWriter writer, final Rectangle rect, final String contents, final float[][] inkList)
    '''
def createFileAttachment():
    '''    public static PdfAnnotation createFileAttachment(final PdfWriter writer, final Rectangle rect, final String contents, final byte[] fileStore, final String file, final String fileDisplay)
    public static PdfAnnotation createFileAttachment(final PdfWriter writer, final Rectangle rect, final String contents, final PdfFileSpecification fs)
    '''
def createPopup():
    '''    public static PdfAnnotation createPopup(final PdfWriter writer, final Rectangle rect, final String contents, final boolean open)
    '''
def setDefaultAppearanceString():
    '''    public void setDefaultAppearanceString(final PdfContentByte cb)
    '''
def setFlags():
    '''    public void setFlags(final int flags)
    '''
def setBorder():
    '''    public void setBorder(final PdfBorderArray border)
    '''
def setBorderStyle():
    '''    public void setBorderStyle(final PdfBorderDictionary border)
    '''
def setHighlighting():
    '''    public void setHighlighting(final PdfName highlight)
    '''
def setAppearance():
    '''    public void setAppearance(final PdfName ap, final PdfTemplate template)
    public void setAppearance(final PdfName ap, final String state, final PdfTemplate template)
    '''
def setAppearanceState():
    '''    public void setAppearanceState(final String state)
    '''
def setColor():
    '''    public void setColor(final Color color)
    '''
def setTitle():
    '''    public void setTitle(final String title)
    '''
def setPopup():
    '''    public void setPopup(final PdfAnnotation popup)
    '''
def setAction():
    '''    public void setAction(final PdfAction action)
    '''
def setAdditionalActions():
    '''    public void setAdditionalActions(final PdfName key, final PdfAction action)
    '''
def isUsed():
    '''    public boolean isUsed()
    '''
def isForm():
    '''    public boolean isForm()
    '''
def isAnnotation():
    '''    public boolean isAnnotation()
    '''
def setPage():
    '''    public void setPage(final int page)
    public void setPage()
    '''
def getPlaceInPage():
    '''    public int getPlaceInPage()
    '''
def setPlaceInPage():
    '''    public void setPlaceInPage(final int placeInPage)
    '''
def setRotate():
    '''    public void setRotate(final int v)
    '''
def setMKRotation():
    '''    public void setMKRotation(final int rotation)
    '''
def getMKColor():
    '''    public static PdfArray getMKColor(final Color color)
    '''
def setMKBorderColor():
    '''    public void setMKBorderColor(final Color color)
    '''
def setMKBackgroundColor():
    '''    public void setMKBackgroundColor(final Color color)
    '''
def setMKNormalCaption():
    '''    public void setMKNormalCaption(final String caption)
    '''
def setMKRolloverCaption():
    '''    public void setMKRolloverCaption(final String caption)
    '''
def setMKAlternateCaption():
    '''    public void setMKAlternateCaption(final String caption)
    '''
def setMKNormalIcon():
    '''    public void setMKNormalIcon(final PdfTemplate template)
    '''
def setMKRolloverIcon():
    '''    public void setMKRolloverIcon(final PdfTemplate template)
    '''
def setMKAlternateIcon():
    '''    public void setMKAlternateIcon(final PdfTemplate template)
    '''
def setMKIconFit():
    '''    public void setMKIconFit(final PdfName scale, final PdfName scalingType, final float leftoverLeft, final float leftoverBottom, final boolean fitInBounds)
    '''
def setMKTextPosition():
    '''    public void setMKTextPosition(final int tp)
    '''
def setLayer():
    '''    public void setLayer(final PdfOCG layer)
    '''
