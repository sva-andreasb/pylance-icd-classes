LEVEL_DEFAULT_LTR = "byte  126"
LEVEL_DEFAULT_RTL = "byte  Byte.MAX_VALUE"
MAX_EXPLICIT_LEVEL = "byte  125"
LEVEL_OVERRIDE = "byte  Byte.MIN_VALUE"
MAP_NOWHERE = "int  -1"
LTR = "byte  0"
RTL = "byte  1"
MIXED = "byte  2"
NEUTRAL = "byte  3"
KEEP_BASE_COMBINING = "short  1"
DO_MIRRORING = "short  2"
INSERT_LRM_FOR_NUMERIC = "short  4"
REMOVE_BIDI_CONTROLS = "short  8"
OUTPUT_REVERSE = "short  16"
REORDER_DEFAULT = "short  0"
REORDER_NUMBERS_SPECIAL = "short  1"
REORDER_GROUP_NUMBERS_WITH_R = "short  2"
REORDER_RUNS_ONLY = "short  3"
REORDER_INVERSE_NUMBERS_AS_L = "short  4"
REORDER_INVERSE_LIKE_DIRECT = "short  5"
REORDER_INVERSE_FOR_NUMBERS_SPECIAL = "short  6"
OPTION_DEFAULT = "int  0"
OPTION_INSERT_MARKS = "int  1"
OPTION_REMOVE_CONTROLS = "int  2"
OPTION_STREAMING = "int  4"
CLASS_DEFAULT = "int  23"
DIRECTION_LEFT_TO_RIGHT = "int  0"
DIRECTION_RIGHT_TO_LEFT = "int  1"
DIRECTION_DEFAULT_LEFT_TO_RIGHT = "int  126"
DIRECTION_DEFAULT_RIGHT_TO_LEFT = "int  127"
def Bidi():
    '''    public Bidi()
    public Bidi(final int maxLength, final int maxRunCount)
    public Bidi(final String paragraph, final int flags)
    public Bidi(final AttributedCharacterIterator paragraph)
    public Bidi(final char[] text, final int textStart, final byte[] embeddings, final int embStart, final int paragraphLength, final int flags)
    '''
def setInverse():
    '''    public void setInverse(final boolean isInverse)
    '''
def isInverse():
    '''    public boolean isInverse()
    '''
def setReorderingMode():
    '''    public void setReorderingMode(final int reorderingMode)
    '''
def getReorderingMode():
    '''    public int getReorderingMode()
    '''
def setReorderingOptions():
    '''    public void setReorderingOptions(final int options)
    '''
def getReorderingOptions():
    '''    public int getReorderingOptions()
    '''
def getBaseDirection():
    '''    public static byte getBaseDirection(final CharSequence paragraph)
    '''
def setContext():
    '''    public void setContext(final String prologue, final String epilogue)
    '''
def setPara():
    '''    public void setPara(final String text, final byte paraLevel, final byte[] embeddingLevels)
    public void setPara(char[] chars, final byte paraLevel, final byte[] embeddingLevels)
    public void setPara(final AttributedCharacterIterator paragraph)
    '''
def orderParagraphsLTR():
    '''    public void orderParagraphsLTR(final boolean ordarParaLTR)
    '''
def isOrderParagraphsLTR():
    '''    public boolean isOrderParagraphsLTR()
    '''
def getDirection():
    '''    public byte getDirection()
    '''
def getTextAsString():
    '''    public String getTextAsString()
    '''
def getText():
    '''    public char[] getText()
    '''
def getLength():
    '''    public int getLength()
    '''
def getProcessedLength():
    '''    public int getProcessedLength()
    '''
def getResultLength():
    '''    public int getResultLength()
    '''
def getParaLevel():
    '''    public byte getParaLevel()
    '''
def countParagraphs():
    '''    public int countParagraphs()
    '''
def getParagraphByIndex():
    '''    public BidiRun getParagraphByIndex(final int paraIndex)
    '''
def getParagraph():
    '''    public BidiRun getParagraph(final int charIndex)
    '''
def getParagraphIndex():
    '''    public int getParagraphIndex(final int charIndex)
    '''
def setCustomClassifier():
    '''    public void setCustomClassifier(final BidiClassifier classifier)
    '''
def getCustomClassifier():
    '''    public BidiClassifier getCustomClassifier()
    '''
def getCustomizedClass():
    '''    public int getCustomizedClass(final int c)
    '''
def setLine():
    '''    public Bidi setLine(final int start, final int limit)
    '''
def getLevelAt():
    '''    public byte getLevelAt(final int charIndex)
    '''
def getLevels():
    '''    public byte[] getLevels()
    '''
def getLogicalRun():
    '''    public BidiRun getLogicalRun(final int logicalPosition)
    '''
def countRuns():
    '''    public int countRuns()
    '''
def getVisualRun():
    '''    public BidiRun getVisualRun(final int runIndex)
    '''
def getVisualIndex():
    '''    public int getVisualIndex(final int logicalIndex)
    '''
def getLogicalIndex():
    '''    public int getLogicalIndex(final int visualIndex)
    '''
def getLogicalMap():
    '''    public int[] getLogicalMap()
    '''
def getVisualMap():
    '''    public int[] getVisualMap()
    '''
def reorderLogical():
    '''    public static int[] reorderLogical(final byte[] levels)
    '''
def reorderVisual():
    '''    public static int[] reorderVisual(final byte[] levels)
    '''
def invertMap():
    '''    public static int[] invertMap(final int[] srcMap)
    '''
def createLineBidi():
    '''    public Bidi createLineBidi(final int lineStart, final int lineLimit)
    '''
def isMixed():
    '''    public boolean isMixed()
    '''
def isLeftToRight():
    '''    public boolean isLeftToRight()
    '''
def isRightToLeft():
    '''    public boolean isRightToLeft()
    '''
def baseIsLeftToRight():
    '''    public boolean baseIsLeftToRight()
    '''
def getBaseLevel():
    '''    public int getBaseLevel()
    '''
def getRunCount():
    '''    public int getRunCount()
    '''
def getRunLevel():
    '''    public int getRunLevel(final int run)
    '''
def getRunStart():
    '''    public int getRunStart(final int run)
    '''
def getRunLimit():
    '''    public int getRunLimit(final int run)
    '''
def requiresBidi():
    '''    public static boolean requiresBidi(final char[] text, final int start, final int limit)
    '''
def reorderVisually():
    '''    public static void reorderVisually(final byte[] levels, final int levelStart, final Object[] objects, final int objectStart, final int count)
    '''
def writeReordered():
    '''    public String writeReordered(final int options)
    '''
def writeReverse():
    '''    public static String writeReverse(final String src, final int options)
    '''
