def BidiLine():
    '''    public BidiLine()
    public BidiLine(final BidiLine org)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def clearChunks():
    '''    public void clearChunks()
    '''
def getParagraph():
    '''    public boolean getParagraph(final int runDirection)
    '''
def addChunk():
    '''    public void addChunk(final PdfChunk chunk)
    '''
def addChunks():
    '''    public void addChunks(final ArrayList chunks)
    '''
def addPiece():
    '''    public void addPiece(final char c, final PdfChunk chunk)
    '''
def save():
    '''    public void save()
    '''
def restore():
    '''    public void restore()
    '''
def mirrorGlyphs():
    '''    public void mirrorGlyphs()
    '''
def doArabicShapping():
    '''    public void doArabicShapping()
    '''
def processLine():
    '''    public PdfLine processLine(float width, final int alignment, final int runDirection, final int arabicOptions)
    '''
def getWidth():
    '''    public float getWidth(int startIdx, final int lastIdx)
    '''
def createArrayOfPdfChunks():
    '''    public ArrayList createArrayOfPdfChunks(final int startIdx, final int endIdx)
    public ArrayList createArrayOfPdfChunks(int startIdx, final int endIdx, final PdfChunk extraPdfChunk)
    '''
def getWord():
    '''    public int[] getWord(final int startIdx, final int idx)
    '''
def trimRight():
    '''    public int trimRight(final int startIdx, final int endIdx)
    '''
def trimLeft():
    '''    public int trimLeft(final int startIdx, final int endIdx)
    '''
def trimRightEx():
    '''    public int trimRightEx(final int startIdx, final int endIdx)
    '''
def trimLeftEx():
    '''    public int trimLeftEx(final int startIdx, final int endIdx)
    '''
def reorder():
    '''    public void reorder(final int start, final int end)
    '''
def flip():
    '''    public void flip(int start, int end)
    '''
def isWS():
    '''    public static boolean isWS(final char c)
    '''
