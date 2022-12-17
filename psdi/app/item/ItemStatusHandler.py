def ():
    '''returns ItemStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredStatus)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def canPending():
    '''returns None\n\n
    canPending()\n
    '''
def canPlanning():
    '''returns None\n\n
    canPlanning()\n
    '''
def canActive():
    '''returns None\n\n
    canActive()\n
    '''
def canPendobs():
    '''returns None\n\n
    canPendobs()\n
    '''
def canObsolete():
    '''returns None\n\n
    canObsolete()\n
    '''
def validateChangeStatus():
    '''returns None\n\n
    validateChangeStatus(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date asOfDate, final String memo)\n
    '''
