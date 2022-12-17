def ():
    '''returns MaxLicStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalStatus)\n
    '''
def checkUserSecurity():
    '''returns None\n\n
    checkUserSecurity(final String desiredMaxStatus)\n
    checkUserSecurity(final String desiredMaxStatus, final boolean applevel)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
