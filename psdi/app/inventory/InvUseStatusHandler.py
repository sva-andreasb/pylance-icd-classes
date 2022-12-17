def ():
    '''returns InvUseStatusHandler\n\n
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
def canStaged():
    '''returns None\n\n
    canStaged()\n
    '''
def canCancelled():
    '''returns None\n\n
    canCancelled()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, String desiredStatus, final Date asOfDate, final String memo)\n
    '''
def chkPickListMbo():
    '''returns boolean\n\n
    chkPickListMbo(final MboRemote owner)\n
    '''
