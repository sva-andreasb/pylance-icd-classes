TK_NUMBER = "int  1"
TK_STRING = "int  2"
TK_NAME = "int  3"
TK_COMMENT = "int  4"
TK_START_ARRAY = "int  5"
TK_END_ARRAY = "int  6"
TK_START_DIC = "int  7"
TK_END_DIC = "int  8"
TK_REF = "int  9"
TK_OTHER = "int  10"
def PRTokeniser():
    '''    public PRTokeniser(final String filename)
    public PRTokeniser(final byte[] pdfIn)
    public PRTokeniser(final RandomAccessFileOrArray file)
    '''
def seek():
    '''    public void seek(final int pos)
    '''
def getFilePointer():
    '''    public int getFilePointer()
    '''
def close():
    '''    public void close()
    '''
def length():
    '''    public int length()
    '''
def read():
    '''    public int read()
    '''
def getSafeFile():
    '''    public RandomAccessFileOrArray getSafeFile()
    '''
def getFile():
    '''    public RandomAccessFileOrArray getFile()
    '''
def readString():
    '''    public String readString(int size)
    '''
def isWhitespace():
    '''    public static final boolean isWhitespace(final int ch)
    '''
def isDelimiter():
    '''    public static final boolean isDelimiter(final int ch)
    '''
def isDelimiterWhitespace():
    '''    public static final boolean isDelimiterWhitespace(final int ch)
    '''
def getTokenType():
    '''    public int getTokenType()
    '''
def getStringValue():
    '''    public String getStringValue()
    '''
def getReference():
    '''    public int getReference()
    '''
def getGeneration():
    '''    public int getGeneration()
    '''
def backOnePosition():
    '''    public void backOnePosition(final int ch)
    '''
def throwError():
    '''    public void throwError(final String error)
    '''
def checkPdfHeader():
    '''    public char checkPdfHeader()
    '''
def checkFdfHeader():
    '''    public void checkFdfHeader()
    '''
def getStartxref():
    '''    public int getStartxref()
    '''
def getHex():
    '''    public static int getHex(final int v)
    '''
def nextValidToken():
    '''    public void nextValidToken()
    '''
def nextToken():
    '''    public boolean nextToken()
    '''
def intValue():
    '''    public int intValue()
    '''
def readLineSegment():
    '''    public boolean readLineSegment(final byte[] input)
    '''
def checkObjectStart():
    '''    public static int[] checkObjectStart(final byte[] line)
    '''
def isHexString():
    '''    public boolean isHexString()
    '''
