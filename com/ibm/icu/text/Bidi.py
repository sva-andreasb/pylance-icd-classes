LEVEL_DEFAULT_LTR = "byte  126"
LEVEL_DEFAULT_RTL = "byte  Byte.MAX_VALUE"
MAX_EXPLICIT_LEVEL = "byte  61"
LEVEL_OVERRIDE = "byte  Byte.MIN_VALUE"
MAP_NOWHERE = "int  -1"
LTR = "byte  0"
RTL = "byte  1"
MIXED = "byte  2"
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
CLASS_DEFAULT = "int  19"
DIRECTION_LEFT_TO_RIGHT = "int  0"
DIRECTION_RIGHT_TO_LEFT = "int  1"
DIRECTION_DEFAULT_LEFT_TO_RIGHT = "int  126"
DIRECTION_DEFAULT_RIGHT_TO_LEFT = "int  127"
def ():
    '''returns Bidi\n\n
    ()\n
    (final int maxLength, final int maxRunCount)\n
    (final String paragraph, final int flags)\n
    (final AttributedCharacterIterator paragraph)\n
    (final char[] text, final int textStart, final byte[] embeddings, final int embStart, final int paragraphLength, final int flags)\n
    '''
def setInverse():
    '''returns None\n\n
    setInverse(final boolean isInverse)\n
    '''
def isInverse():
    '''returns boolean\n\n
    isInverse()\n
    '''
def setReorderingMode():
    '''returns None\n\n
    setReorderingMode(final int reorderingMode)\n
    '''
def getReorderingMode():
    '''returns int\n\n
    getReorderingMode()\n
    '''
def setReorderingOptions():
    '''returns None\n\n
    setReorderingOptions(final int options)\n
    '''
def getReorderingOptions():
    '''returns int\n\n
    getReorderingOptions()\n
    '''
def setPara():
    '''returns None\n\n
    setPara(final String text, final byte paraLevel, final byte[] embeddingLevels)\n
    setPara(char[] chars, byte paraLevel, final byte[] embeddingLevels)\n
    setPara(final AttributedCharacterIterator paragraph)\n
    '''
def orderParagraphsLTR():
    '''returns None\n\n
    orderParagraphsLTR(final boolean ordarParaLTR)\n
    '''
def isOrderParagraphsLTR():
    '''returns boolean\n\n
    isOrderParagraphsLTR()\n
    '''
def getDirection():
    '''returns byte\n\n
    getDirection()\n
    '''
def getTextAsString():
    '''returns String\n\n
    getTextAsString()\n
    '''
def getText():
    '''returns char[]\n\n
    getText()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getProcessedLength():
    '''returns int\n\n
    getProcessedLength()\n
    '''
def getResultLength():
    '''returns int\n\n
    getResultLength()\n
    '''
def getParaLevel():
    '''returns byte\n\n
    getParaLevel()\n
    '''
def countParagraphs():
    '''returns int\n\n
    countParagraphs()\n
    '''
def getParagraphByIndex():
    '''returns BidiRun\n\n
    getParagraphByIndex(final int paraIndex)\n
    '''
def getParagraph():
    '''returns BidiRun\n\n
    getParagraph(final int charIndex)\n
    '''
def getParagraphIndex():
    '''returns int\n\n
    getParagraphIndex(final int charIndex)\n
    '''
def setCustomClassifier():
    '''returns None\n\n
    setCustomClassifier(final BidiClassifier classifier)\n
    '''
def getCustomClassifier():
    '''returns BidiClassifier\n\n
    getCustomClassifier()\n
    '''
def getCustomizedClass():
    '''returns int\n\n
    getCustomizedClass(final int c)\n
    '''
def setLine():
    '''returns Bidi\n\n
    setLine(final int start, final int limit)\n
    '''
def getLevelAt():
    '''returns byte\n\n
    getLevelAt(final int charIndex)\n
    '''
def getLevels():
    '''returns byte[]\n\n
    getLevels()\n
    '''
def getLogicalRun():
    '''returns BidiRun\n\n
    getLogicalRun(final int logicalPosition)\n
    '''
def countRuns():
    '''returns int\n\n
    countRuns()\n
    '''
def getVisualRun():
    '''returns BidiRun\n\n
    getVisualRun(final int runIndex)\n
    '''
def getVisualIndex():
    '''returns int\n\n
    getVisualIndex(final int logicalIndex)\n
    '''
def getLogicalIndex():
    '''returns int\n\n
    getLogicalIndex(final int visualIndex)\n
    '''
def getLogicalMap():
    '''returns int[]\n\n
    getLogicalMap()\n
    '''
def getVisualMap():
    '''returns int[]\n\n
    getVisualMap()\n
    '''
def createLineBidi():
    '''returns Bidi\n\n
    createLineBidi(final int lineStart, final int lineLimit)\n
    '''
def isMixed():
    '''returns boolean\n\n
    isMixed()\n
    '''
def isLeftToRight():
    '''returns boolean\n\n
    isLeftToRight()\n
    '''
def isRightToLeft():
    '''returns boolean\n\n
    isRightToLeft()\n
    '''
def baseIsLeftToRight():
    '''returns boolean\n\n
    baseIsLeftToRight()\n
    '''
def getBaseLevel():
    '''returns int\n\n
    getBaseLevel()\n
    '''
def getRunCount():
    '''returns int\n\n
    getRunCount()\n
    '''
def getRunLevel():
    '''returns int\n\n
    getRunLevel(final int run)\n
    '''
def getRunStart():
    '''returns int\n\n
    getRunStart(final int run)\n
    '''
def getRunLimit():
    '''returns int\n\n
    getRunLimit(final int run)\n
    '''
def writeReordered():
    '''returns String\n\n
    writeReordered(final int options)\n
    '''
