ERR_INVALID_TT_FLAG = "int  1"
ERR_INVALID_TO_FLAG = "int  2"
ERR_INVALID_SS_FLAG = "int  4"
ERR_INVALID_TS_FLAG = "int  8"
ERR_INVALID_NS_FLAG = "int  16"
ERR_INVALID_FLAG_SET = "int  31"
ERR_IDENTICAL_IN_OUT_ATTRIBUTES = "int  100"
ERR_INVALID_IN_OUT_ATTRIBUTES = "int  101"
ERR_CONFLICTING_ATTRIBUTES = "int  102"
ERR_NULL_ATTRIBUTES = "int  103"
ERR_NULL_XML_DOCUMENT = "int  104"
ERR_ARABIC_SHAPING = "int  1000"
def BidiTransformationException():
'''public BidiTransformationException(final Throwable cause)
public BidiTransformationException(final int errorCode)
public BidiTransformationException(final int errorCode, final Object messageData)
'''
pass
def getTracingMessage():
'''public static String getTracingMessage(final int errorCode, final Object messageData)
'''
pass
def getErrorCode():
'''public final int getErrorCode()
'''
pass
def getMessageData():
'''public final Object getMessageData()
'''
pass
