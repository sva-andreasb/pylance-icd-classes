LEVEL_DEFAULT_LTR = "byte 126"
LEVEL_DEFAULT_RTL = "byte Byte.MAX_VALUE"
MAX_EXPLICIT_LEVEL = "byte 125"
LEVEL_OVERRIDE = "byte Byte.MIN_VALUE"
MAP_NOWHERE = "int -1"
LTR = "byte 0"
RTL = "byte 1"
MIXED = "byte 2"
NEUTRAL = "byte 3"
KEEP_BASE_COMBINING = "short 1"
DO_MIRRORING = "short 2"
INSERT_LRM_FOR_NUMERIC = "short 4"
REMOVE_BIDI_CONTROLS = "short 8"
OUTPUT_REVERSE = "short 16"
REORDER_DEFAULT = "short 0"
REORDER_NUMBERS_SPECIAL = "short 1"
REORDER_GROUP_NUMBERS_WITH_R = "short 2"
REORDER_RUNS_ONLY = "short 3"
REORDER_INVERSE_NUMBERS_AS_L = "short 4"
REORDER_INVERSE_LIKE_DIRECT = "short 5"
REORDER_INVERSE_FOR_NUMBERS_SPECIAL = "short 6"
OPTION_DEFAULT = "int 0"
OPTION_INSERT_MARKS = "int 1"
OPTION_REMOVE_CONTROLS = "int 2"
OPTION_STREAMING = "int 4"
CLASS_DEFAULT = "int 23"
DIRECTION_LEFT_TO_RIGHT = "int 0"
DIRECTION_RIGHT_TO_LEFT = "int 1"
DIRECTION_DEFAULT_LEFT_TO_RIGHT = "int 126"
DIRECTION_DEFAULT_RIGHT_TO_LEFT = "int 127"
def Bidi():
'''public Bidi()
public Bidi(final int maxLength, final int maxRunCount)
public Bidi(final String paragraph, final int flags)
public Bidi(final AttributedCharacterIterator paragraph)
public Bidi(final char[] text, final int textStart, final byte[] embeddings, final int embStart, final int paragraphLength, final int flags)
'''
pass
def setInverse():
'''public void setInverse(final boolean isInverse)
'''
pass
def isInverse():
'''public boolean isInverse()
'''
pass
def setReorderingMode():
'''public void setReorderingMode(final int reorderingMode)
'''
pass
def getReorderingMode():
'''public int getReorderingMode()
'''
pass
def setReorderingOptions():
'''public void setReorderingOptions(final int options)
'''
pass
def getReorderingOptions():
'''public int getReorderingOptions()
'''
pass
def getBaseDirection():
'''public static byte getBaseDirection(final CharSequence paragraph)
'''
pass
def setContext():
'''public void setContext(final String prologue, final String epilogue)
'''
pass
def setPara():
'''public void setPara(final String text, final byte paraLevel, final byte[] embeddingLevels)
public void setPara(char[] chars, final byte paraLevel, final byte[] embeddingLevels)
public void setPara(final AttributedCharacterIterator paragraph)
'''
pass
def orderParagraphsLTR():
'''public void orderParagraphsLTR(final boolean ordarParaLTR)
'''
pass
def isOrderParagraphsLTR():
'''public boolean isOrderParagraphsLTR()
'''
pass
def getDirection():
'''public byte getDirection()
'''
pass
def getTextAsString():
'''public String getTextAsString()
'''
pass
def getText():
'''public char[] getText()
'''
pass
def getLength():
'''public int getLength()
'''
pass
def getProcessedLength():
'''public int getProcessedLength()
'''
pass
def getResultLength():
'''public int getResultLength()
'''
pass
def getParaLevel():
'''public byte getParaLevel()
'''
pass
def countParagraphs():
'''public int countParagraphs()
'''
pass
def getParagraphByIndex():
'''public BidiRun getParagraphByIndex(final int paraIndex)
'''
pass
def getParagraph():
'''public BidiRun getParagraph(final int charIndex)
'''
pass
def getParagraphIndex():
'''public int getParagraphIndex(final int charIndex)
'''
pass
def setCustomClassifier():
'''public void setCustomClassifier(final BidiClassifier classifier)
'''
pass
def getCustomClassifier():
'''public BidiClassifier getCustomClassifier()
'''
pass
def getCustomizedClass():
'''public int getCustomizedClass(final int c)
'''
pass
def setLine():
'''public Bidi setLine(final int start, final int limit)
'''
pass
def getLevelAt():
'''public byte getLevelAt(final int charIndex)
'''
pass
def getLevels():
'''public byte[] getLevels()
'''
pass
def getLogicalRun():
'''public BidiRun getLogicalRun(final int logicalPosition)
'''
pass
def countRuns():
'''public int countRuns()
'''
pass
def getVisualRun():
'''public BidiRun getVisualRun(final int runIndex)
'''
pass
def getVisualIndex():
'''public int getVisualIndex(final int logicalIndex)
'''
pass
def getLogicalIndex():
'''public int getLogicalIndex(final int visualIndex)
'''
pass
def getLogicalMap():
'''public int[] getLogicalMap()
'''
pass
def getVisualMap():
'''public int[] getVisualMap()
'''
pass
def reorderLogical():
'''public static int[] reorderLogical(final byte[] levels)
'''
pass
def reorderVisual():
'''public static int[] reorderVisual(final byte[] levels)
'''
pass
def invertMap():
'''public static int[] invertMap(final int[] srcMap)
'''
pass
def createLineBidi():
'''public Bidi createLineBidi(final int lineStart, final int lineLimit)
'''
pass
def isMixed():
'''public boolean isMixed()
'''
pass
def isLeftToRight():
'''public boolean isLeftToRight()
'''
pass
def isRightToLeft():
'''public boolean isRightToLeft()
'''
pass
def baseIsLeftToRight():
'''public boolean baseIsLeftToRight()
'''
pass
def getBaseLevel():
'''public int getBaseLevel()
'''
pass
def getRunCount():
'''public int getRunCount()
'''
pass
def getRunLevel():
'''public int getRunLevel(final int run)
'''
pass
def getRunStart():
'''public int getRunStart(final int run)
'''
pass
def getRunLimit():
'''public int getRunLimit(final int run)
'''
pass
def requiresBidi():
'''public static boolean requiresBidi(final char[] text, final int start, final int limit)
'''
pass
def reorderVisually():
'''public static void reorderVisually(final byte[] levels, final int levelStart, final Object[] objects, final int objectStart, final int count)
'''
pass
def writeReordered():
'''public String writeReordered(final int options)
'''
pass
def writeReverse():
'''public static String writeReverse(final String src, final int options)
'''
pass
