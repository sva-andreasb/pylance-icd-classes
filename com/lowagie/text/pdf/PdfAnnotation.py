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
'''public PdfAnnotation(final PdfWriter writer, final float llx, final float lly, final float urx, final float ury, final PdfAction action)
'''
pass
def createScreen():
'''public static PdfAnnotation createScreen(final PdfWriter writer, final Rectangle rect, final String clipTitle, final PdfFileSpecification fs, final String mimeType, final boolean playOnDisplay)
'''
pass
def createText():
'''public static PdfAnnotation createText(final PdfWriter writer, final Rectangle rect, final String title, final String contents, final boolean open, final String icon)
'''
pass
def createLink():
'''public static PdfAnnotation createLink(final PdfWriter writer, final Rectangle rect, final PdfName highlight, final PdfAction action)
public static PdfAnnotation createLink(final PdfWriter writer, final Rectangle rect, final PdfName highlight, final String namedDestination)
public static PdfAnnotation createLink(final PdfWriter writer, final Rectangle rect, final PdfName highlight, final int page, final PdfDestination dest)
'''
pass
def createFreeText():
'''public static PdfAnnotation createFreeText(final PdfWriter writer, final Rectangle rect, final String contents, final PdfContentByte defaultAppearance)
'''
pass
def createLine():
'''public static PdfAnnotation createLine(final PdfWriter writer, final Rectangle rect, final String contents, final float x1, final float y1, final float x2, final float y2)
'''
pass
def createSquareCircle():
'''public static PdfAnnotation createSquareCircle(final PdfWriter writer, final Rectangle rect, final String contents, final boolean square)
'''
pass
def createMarkup():
'''public static PdfAnnotation createMarkup(final PdfWriter writer, final Rectangle rect, final String contents, final int type, final float[] quadPoints)
'''
pass
def createStamp():
'''public static PdfAnnotation createStamp(final PdfWriter writer, final Rectangle rect, final String contents, final String name)
'''
pass
def createInk():
'''public static PdfAnnotation createInk(final PdfWriter writer, final Rectangle rect, final String contents, final float[][] inkList)
'''
pass
def createFileAttachment():
'''public static PdfAnnotation createFileAttachment(final PdfWriter writer, final Rectangle rect, final String contents, final byte[] fileStore, final String file, final String fileDisplay)
public static PdfAnnotation createFileAttachment(final PdfWriter writer, final Rectangle rect, final String contents, final PdfFileSpecification fs)
'''
pass
def createPopup():
'''public static PdfAnnotation createPopup(final PdfWriter writer, final Rectangle rect, final String contents, final boolean open)
'''
pass
def setDefaultAppearanceString():
'''public void setDefaultAppearanceString(final PdfContentByte cb)
'''
pass
def setFlags():
'''public void setFlags(final int flags)
'''
pass
def setBorder():
'''public void setBorder(final PdfBorderArray border)
'''
pass
def setBorderStyle():
'''public void setBorderStyle(final PdfBorderDictionary border)
'''
pass
def setHighlighting():
'''public void setHighlighting(final PdfName highlight)
'''
pass
def setAppearance():
'''public void setAppearance(final PdfName ap, final PdfTemplate template)
public void setAppearance(final PdfName ap, final String state, final PdfTemplate template)
'''
pass
def setAppearanceState():
'''public void setAppearanceState(final String state)
'''
pass
def setColor():
'''public void setColor(final Color color)
'''
pass
def setTitle():
'''public void setTitle(final String title)
'''
pass
def setPopup():
'''public void setPopup(final PdfAnnotation popup)
'''
pass
def setAction():
'''public void setAction(final PdfAction action)
'''
pass
def setAdditionalActions():
'''public void setAdditionalActions(final PdfName key, final PdfAction action)
'''
pass
def isUsed():
'''public boolean isUsed()
'''
pass
def isForm():
'''public boolean isForm()
'''
pass
def isAnnotation():
'''public boolean isAnnotation()
'''
pass
def setPage():
'''public void setPage(final int page)
public void setPage()
'''
pass
def getPlaceInPage():
'''public int getPlaceInPage()
'''
pass
def setPlaceInPage():
'''public void setPlaceInPage(final int placeInPage)
'''
pass
def setRotate():
'''public void setRotate(final int v)
'''
pass
def setMKRotation():
'''public void setMKRotation(final int rotation)
'''
pass
def getMKColor():
'''public static PdfArray getMKColor(final Color color)
'''
pass
def setMKBorderColor():
'''public void setMKBorderColor(final Color color)
'''
pass
def setMKBackgroundColor():
'''public void setMKBackgroundColor(final Color color)
'''
pass
def setMKNormalCaption():
'''public void setMKNormalCaption(final String caption)
'''
pass
def setMKRolloverCaption():
'''public void setMKRolloverCaption(final String caption)
'''
pass
def setMKAlternateCaption():
'''public void setMKAlternateCaption(final String caption)
'''
pass
def setMKNormalIcon():
'''public void setMKNormalIcon(final PdfTemplate template)
'''
pass
def setMKRolloverIcon():
'''public void setMKRolloverIcon(final PdfTemplate template)
'''
pass
def setMKAlternateIcon():
'''public void setMKAlternateIcon(final PdfTemplate template)
'''
pass
def setMKIconFit():
'''public void setMKIconFit(final PdfName scale, final PdfName scalingType, final float leftoverLeft, final float leftoverBottom, final boolean fitInBounds)
'''
pass
def setMKTextPosition():
'''public void setMKTextPosition(final int tp)
'''
pass
def setLayer():
'''public void setLayer(final PdfOCG layer)
'''
pass
