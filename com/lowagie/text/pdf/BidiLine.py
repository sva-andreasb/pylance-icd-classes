def BidiLine():
'''public BidiLine()
public BidiLine(final BidiLine org)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def clearChunks():
'''public void clearChunks()
'''
pass
def getParagraph():
'''public boolean getParagraph(final int runDirection)
'''
pass
def addChunk():
'''public void addChunk(final PdfChunk chunk)
'''
pass
def addChunks():
'''public void addChunks(final ArrayList chunks)
'''
pass
def addPiece():
'''public void addPiece(final char c, final PdfChunk chunk)
'''
pass
def save():
'''public void save()
'''
pass
def restore():
'''public void restore()
'''
pass
def mirrorGlyphs():
'''public void mirrorGlyphs()
'''
pass
def doArabicShapping():
'''public void doArabicShapping()
'''
pass
def processLine():
'''public PdfLine processLine(float width, final int alignment, final int runDirection, final int arabicOptions)
'''
pass
def getWidth():
'''public float getWidth(int startIdx, final int lastIdx)
'''
pass
def createArrayOfPdfChunks():
'''public ArrayList createArrayOfPdfChunks(final int startIdx, final int endIdx)
public ArrayList createArrayOfPdfChunks(int startIdx, final int endIdx, final PdfChunk extraPdfChunk)
'''
pass
def getWord():
'''public int[] getWord(final int startIdx, final int idx)
'''
pass
def trimRight():
'''public int trimRight(final int startIdx, final int endIdx)
'''
pass
def trimLeft():
'''public int trimLeft(final int startIdx, final int endIdx)
'''
pass
def trimRightEx():
'''public int trimRightEx(final int startIdx, final int endIdx)
'''
pass
def trimLeftEx():
'''public int trimLeftEx(final int startIdx, final int endIdx)
'''
pass
def reorder():
'''public void reorder(final int start, final int end)
'''
pass
def flip():
'''public void flip(int start, int end)
'''
pass
def isWS():
'''public static boolean isWS(final char c)
'''
pass
