TYPE_ERROR = "int  0"
TYPE_WARNING = "int  1"
TYPE_ALERT = "int  2"
TYPE_REPLACEMENT_REQUIRED = "int  3"
def ():
    '''returns Message\n\n
    (final int type, final String msgId, final Object[] msgArgs)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getMsgId():
    '''returns String\n\n
    getMsgId()\n
    '''
def getMsgArgs():
    '''returns Object[]\n\n
    getMsgArgs()\n
    '''
def isError():
    '''returns boolean\n\n
    isError()\n
    '''
def isWarning():
    '''returns boolean\n\n
    isWarning()\n
    '''
def isAlert():
    '''returns boolean\n\n
    isAlert()\n
    '''
def isReplacementRequired():
    '''returns boolean\n\n
    isReplacementRequired()\n
    '''
