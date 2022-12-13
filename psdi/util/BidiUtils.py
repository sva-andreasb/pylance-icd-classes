LTR_DIRECTION = "String  LTR""
RTL_DIRECTION = "String  RTL""
CONTEXTUAL_DIRECTION = "String  CONTEXTUAL""
NONE = "String  "
LRE = "String  \u202a""
RLE = "String  \u202b""
PDF = "String  \u202c""
LRM = "String  \u200e""
RLM = "String  \u200f""
PATH = "String  FILEPATH""
EMAIL = "String  EMAIL""
URL = "String  URL""
JAVAPATH = "String  JAVAPATH""
SQL = "String  SQL""
XML = "String  XML""
DNS = "String  DNS""
JNDI = "String  JNDI""
CHAINED_SEQUENCE_COLON = "String  CHAINED-SEQ-COLON""
CHAINED_SEQUENCE_SLASH = "String  CHAINED-SEQ-SLASH""
CHAINED_SEQUENCE_COMMA = "String  CHAINED-SEQ-COMMA""
CHAINED_SEQUENCE_DASH = "String  CHAINED-SEQ-DASH""
def isBidiEnabled():
'''public static boolean isBidiEnabled()
'''
pass
def isTestAppMirrored():
'''public static boolean isTestAppMirrored()
'''
pass
def getTestLanguage():
'''public static String getTestLanguage()
'''
pass
def getInstanceTextDirection():
'''public static String getInstanceTextDirection()
'''
pass
def buildTagAttribute():
'''public static String buildTagAttribute(final String value, final String attrTextdirection, final String attrComplexexpression, final boolean includeHandlers)
public static String buildTagAttribute(final String value, final String attrTextdirection, final String attrComplexexpression, final boolean includeHandlers, final String langCode)
'''
pass
def getMboTextDirection():
'''public static String getMboTextDirection(final MboSetInfo msi, final String attrName, final boolean countInstanceDirection)
public static String getMboTextDirection(final String mboName, final String attrName, final boolean countInstanceDirection)
'''
pass
def getMboComplexExpressionType():
'''public static String getMboComplexExpressionType(final String mboName, final String attrName)
public static String getMboComplexExpressionType(final MboSetInfo msi, final String attrName)
'''
pass
def isBidiAttributeSet():
'''public static boolean isBidiAttributeSet(final String attr)
'''
pass
def isBiDiString():
'''public static boolean isBiDiString(final String str)
'''
pass
def analyzeBidiTextDirection():
'''public static String analyzeBidiTextDirection(final String str, final String bidiDirection)
'''
pass
def enforceBidiDirection():
'''public static String enforceBidiDirection(String str, final String bidiDirection)
'''
pass
def checkLastSegment():
'''public static String checkLastSegment(final String str)
'''
pass
def processComplexexpression():
'''public static String processComplexexpression(final String buffer, final String textDirection, final String complexExpressionType, final MXSession s)
public static String processComplexexpression(final String buffer, final String textDirection, final String complexExpressionType, final MXSession s, final boolean forInput)
public static String processComplexexpression(final String buffer, final String textDirection, final String complexExpressionType, final String langCode)
public static String processComplexexpression(final String buffer, final String textDirection, final String complexExpressionType, final String langCode, final boolean forInput)
public static String processComplexexpression(final String buffer, final String complexExpressionType)
public static String processComplexexpression(final String buffer, final String complexExpressionType, final MXSession s)
'''
pass
def processChainedSequencePattern():
'''public static String processChainedSequencePattern(final String buffer, final String textDirection, final String complexExpressionType, final String langCode)
'''
pass
def removeMarkers():
'''public static String removeMarkers(final String str)
'''
pass
def isCharBeforeBiDiChar():
'''public static boolean isCharBeforeBiDiChar(final char[] buffer, int i, final int previous)
'''
pass
def isGUIMirrored():
'''public static boolean isGUIMirrored(final UserInfo userInfo)
public static boolean isGUIMirrored(final MXSession s)
public static boolean isGUIMirrored(final String langCode)
'''
pass
def isArabicLanguage():
'''public static boolean isArabicLanguage(final String langCode)
'''
pass
def isHebrewLanguage():
'''public static boolean isHebrewLanguage(final String langCode)
'''
pass
def getLayoutOrientation():
'''public static String getLayoutOrientation(final String langcode)
'''
pass
def getDelimeterPrefix():
'''public static String getDelimeterPrefix(final MXSession s)
public static String getDelimeterPrefix(final String langCode)
'''
pass
def getStartingMarkers():
'''public static String getStartingMarkers(final String langCode)
'''
pass
def getFinalMarkers():
'''public static String getFinalMarkers(final String langCode)
'''
pass
def keepBidiDirection():
'''public static String keepBidiDirection(String str, final String wrapper)
'''
pass
def applyBidiAttributes():
'''public static String applyBidiAttributes(final String mboName, final String attribute, final String value, final MXSession s)
public static String applyBidiAttributes(final MboSetInfo msi, final String attribute, final String value, final MXSession s)
public static String applyBidiAttributes(final String mboName, final String attribute, final String value, final String langCode)
public static String applyBidiAttributes(final MboSetInfo msi, final String attribute, final String value, final String langCode)
'''
pass
def hasDifferDirection():
'''public static boolean hasDifferDirection(final String txt, final String langCode)
'''
pass
def appendBidiString():
'''public static String appendBidiString(final String src, final String txt)
'''
pass
def pushBidiStringToDir():
'''public static String pushBidiStringToDir(final String str, final String direction)
'''
pass
def pushBidiString():
'''public static String pushBidiString(final String str, final String langCode)
public static String pushBidiString(final String str, final MXSession s)
'''
pass
def buildAndPush():
'''public static String buildAndPush(final String mboName, final String attribute, final String value, final MXSession s)
public static String buildAndPush(final MboSetInfo msi, final String attribute, final String value, final MXSession s)
public static String buildAndPush(final String mboName, final String attribute, final String value, final String langCode)
public static String buildAndPush(final MboSetInfo msi, final String attribute, final String value, final String langCode)
public static String buildAndPush(final String value, final String langCode)
'''
pass
def isChain():
'''public static boolean isChain(final String prop)
'''
pass
def isLTRExpression():
'''public static boolean isLTRExpression(final String prop)
'''
pass
def logValue():
'''public static String logValue(final String str)
'''
pass
def fixTextDirection():
'''public static String fixTextDirection(final Locale locale, final String text, final String direction)
'''
pass
def getTextDirection():
'''public static String getTextDirection(final Locale locale, final String text)
'''
pass
def join():
'''public static String join(final boolean mirrored, final String sepString, final String... parts)
'''
pass
def concat():
'''public static String concat(final boolean mirrored, final String... parts)
'''
pass
