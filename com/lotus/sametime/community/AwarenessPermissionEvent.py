GOT_AWARENESS_PERMISSION_REQUESTS = "int  -2147483647"
ACK_ACCEPTED_REQUESTORS = "int  -2147483646"
AWARENESS_PERMISSION_REQ_CANCELLED = "int  -2147483645"
AWARENESS_PERMISSION_REQ_FAILED = "int  -2147483644"
def ():
    '''returns AwarenessPermissionEvent\n\n
    (final Object o, final int n)\n
    (final Object o, final int n, final STUser[] users)\n
    (final Object o, final int n, final Integer reason)\n
    '''
def getRequestors():
    '''returns STUser[]\n\n
    getRequestors()\n
    '''
def getTargets():
    '''returns STUser[]\n\n
    getTargets()\n
    '''
def getReason():
    '''returns Integer\n\n
    getReason()\n
    '''
