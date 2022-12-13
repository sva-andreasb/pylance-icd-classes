TYPE_ERROR = "int  0"
TYPE_WARNING = "int  1"
TYPE_ALERT = "int  2"
TYPE_REPLACEMENT_REQUIRED = "int  3"
def Message():
'''public Message(final int type, final String msgId, final Object[] msgArgs)
'''
pass
def getType():
'''public int getType()
'''
pass
def getMsgId():
'''public String getMsgId()
'''
pass
def getMsgArgs():
'''public Object[] getMsgArgs()
'''
pass
def newError():
'''public static Message newError(final String msgId, final Object[] msgArgs)
'''
pass
def newWarning():
'''public static Message newWarning(final String msgId, final Object[] msgArgs)
'''
pass
def newAlert():
'''public static Message newAlert(final String msgId, final Object[] msgArgs)
'''
pass
def newReplacementRequired():
'''public static Message newReplacementRequired(final String msgId, final Object[] msgArgs)
'''
pass
def isError():
'''public boolean isError()
'''
pass
def isWarning():
'''public boolean isWarning()
'''
pass
def isAlert():
'''public boolean isAlert()
'''
pass
def isReplacementRequired():
'''public boolean isReplacementRequired()
'''
pass
