def ():
    '''returns PlusPLineStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def possibleStatusChange():
    '''returns None\n\n
    possibleStatusChange(final String s, final String s2)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String s, final Date date, final String memo)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String s, final String s2, final long accessModifier)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
def toInternalStatus():
    '''returns String\n\n
    toInternalStatus(final String value)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String s)\n
    '''
def isStatusBillable():
    '''returns boolean\n\n
    isStatusBillable(final String s)\n
    '''
