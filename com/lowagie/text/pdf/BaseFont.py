COURIER = "String  Courier""
COURIER_BOLD = "String  Courier-Bold""
COURIER_OBLIQUE = "String  Courier-Oblique""
COURIER_BOLDOBLIQUE = "String  Courier-BoldOblique""
HELVETICA = "String  Helvetica""
HELVETICA_BOLD = "String  Helvetica-Bold""
HELVETICA_OBLIQUE = "String  Helvetica-Oblique""
HELVETICA_BOLDOBLIQUE = "String  Helvetica-BoldOblique""
SYMBOL = "String  Symbol""
TIMES_ROMAN = "String  Times-Roman""
TIMES_BOLD = "String  Times-Bold""
TIMES_ITALIC = "String  Times-Italic""
TIMES_BOLDITALIC = "String  Times-BoldItalic""
ZAPFDINGBATS = "String  ZapfDingbats""
ASCENT = "int  1"
CAPHEIGHT = "int  2"
DESCENT = "int  3"
ITALICANGLE = "int  4"
BBOXLLX = "int  5"
BBOXLLY = "int  6"
BBOXURX = "int  7"
BBOXURY = "int  8"
AWT_ASCENT = "int  9"
AWT_DESCENT = "int  10"
AWT_LEADING = "int  11"
AWT_MAXADVANCE = "int  12"
FONT_TYPE_T1 = "int  0"
FONT_TYPE_TT = "int  1"
FONT_TYPE_CJK = "int  2"
FONT_TYPE_TTUNI = "int  3"
FONT_TYPE_DOCUMENT = "int  4"
IDENTITY_H = "String  Identity-H""
IDENTITY_V = "String  Identity-V""
CP1250 = "String  Cp1250""
CP1252 = "String  Cp1252""
CP1257 = "String  Cp1257""
WINANSI = "String  Cp1252""
MACROMAN = "String  MacRoman""
EMBEDDED = "boolean  true"
NOT_EMBEDDED = "boolean  false"
CACHED = "boolean  true"
NOT_CACHED = "boolean  false"
RESOURCE_PATH = "String  com/lowagie/text/pdf/fonts/""
CID_NEWLINE = "char  '\u7fff'"
notdef = "String  .notdef""
def createFont():
'''public static BaseFont createFont(final String name, final String encoding, final boolean embedded)
public static BaseFont createFont(final String name, String encoding, boolean embedded, final boolean cached, final byte[] ttfAfm, final byte[] pfb)
public static BaseFont createFont(final PRIndirectReference fontRef)
'''
pass
def getWidth():
'''public int getWidth(final char char1)
public int getWidth(final String text)
'''
pass
def getDescent():
'''public int getDescent(final String text)
'''
pass
def getAscent():
'''public int getAscent(final String text)
'''
pass
def getDescentPoint():
'''public float getDescentPoint(final String text, final float fontSize)
'''
pass
def getAscentPoint():
'''public float getAscentPoint(final String text, final float fontSize)
'''
pass
def getWidthPointKerned():
'''public float getWidthPointKerned(final String text, final float fontSize)
'''
pass
def getWidthPoint():
'''public float getWidthPoint(final String text, final float fontSize)
public float getWidthPoint(final char char1, final float fontSize)
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def getFontType():
'''public int getFontType()
'''
pass
def isEmbedded():
'''public boolean isEmbedded()
'''
pass
def isFontSpecific():
'''public boolean isFontSpecific()
'''
pass
def createSubsetPrefix():
'''public static String createSubsetPrefix()
'''
pass
def getFullFontName():
'''public static String[][] getFullFontName(final String name, final String encoding, final byte[] ttfAfm)
'''
pass
def getAllFontNames():
'''public static Object[] getAllFontNames(final String name, final String encoding, final byte[] ttfAfm)
'''
pass
def getCodePagesSupported():
'''public String[] getCodePagesSupported()
'''
pass
def enumerateTTCNames():
'''public static String[] enumerateTTCNames(final String ttcFile)
public static String[] enumerateTTCNames(final byte[] ttcArray)
'''
pass
def getWidths():
'''public int[] getWidths()
'''
pass
def getDifferences():
'''public String[] getDifferences()
'''
pass
def getUnicodeDifferences():
'''public char[] getUnicodeDifferences()
'''
pass
def isForceWidthsOutput():
'''public boolean isForceWidthsOutput()
'''
pass
def setForceWidthsOutput():
'''public void setForceWidthsOutput(final boolean forceWidthsOutput)
'''
pass
def isDirectTextToByte():
'''public boolean isDirectTextToByte()
'''
pass
def setDirectTextToByte():
'''public void setDirectTextToByte(final boolean directTextToByte)
'''
pass
def isSubset():
'''public boolean isSubset()
'''
pass
def setSubset():
'''public void setSubset(final boolean subset)
'''
pass
def getResourceStream():
'''public static InputStream getResourceStream(final String key)
public static InputStream getResourceStream(final String key, final ClassLoader loader)
'''
pass
def getUnicodeEquivalent():
'''public char getUnicodeEquivalent(final char c)
'''
pass
def getCidCode():
'''public char getCidCode(final char c)
'''
pass
def charExists():
'''public boolean charExists(final char c)
'''
pass
def setCharAdvance():
'''public boolean setCharAdvance(final char c, final int advance)
'''
pass
def getDocumentFonts():
'''public static ArrayList getDocumentFonts(final PdfReader reader)
public static ArrayList getDocumentFonts(final PdfReader reader, final int page)
'''
pass
def getCharBBox():
'''public int[] getCharBBox(final char c)
'''
pass
def StreamFont():
'''public StreamFont(final byte[] contents, final int[] lengths)
public StreamFont(final byte[] contents, final String subType)
'''
pass
