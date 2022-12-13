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
'''public PRTokeniser(final String filename)
public PRTokeniser(final byte[] pdfIn)
public PRTokeniser(final RandomAccessFileOrArray file)
'''
pass
def seek():
'''public void seek(final int pos)
'''
pass
def getFilePointer():
'''public int getFilePointer()
'''
pass
def close():
'''public void close()
'''
pass
def length():
'''public int length()
'''
pass
def read():
'''public int read()
'''
pass
def getSafeFile():
'''public RandomAccessFileOrArray getSafeFile()
'''
pass
def getFile():
'''public RandomAccessFileOrArray getFile()
'''
pass
def readString():
'''public String readString(int size)
'''
pass
def isWhitespace():
'''public static final boolean isWhitespace(final int ch)
'''
pass
def isDelimiter():
'''public static final boolean isDelimiter(final int ch)
'''
pass
def isDelimiterWhitespace():
'''public static final boolean isDelimiterWhitespace(final int ch)
'''
pass
def getTokenType():
'''public int getTokenType()
'''
pass
def getStringValue():
'''public String getStringValue()
'''
pass
def getReference():
'''public int getReference()
'''
pass
def getGeneration():
'''public int getGeneration()
'''
pass
def backOnePosition():
'''public void backOnePosition(final int ch)
'''
pass
def throwError():
'''public void throwError(final String error)
'''
pass
def checkPdfHeader():
'''public char checkPdfHeader()
'''
pass
def checkFdfHeader():
'''public void checkFdfHeader()
'''
pass
def getStartxref():
'''public int getStartxref()
'''
pass
def getHex():
'''public static int getHex(final int v)
'''
pass
def nextValidToken():
'''public void nextValidToken()
'''
pass
def nextToken():
'''public boolean nextToken()
'''
pass
def intValue():
'''public int intValue()
'''
pass
def readLineSegment():
'''public boolean readLineSegment(final byte[] input)
'''
pass
def checkObjectStart():
'''public static int[] checkObjectStart(final byte[] line)
'''
pass
def isHexString():
'''public boolean isHexString()
'''
pass
