def ():
    '''returns PlusPRPStatusHandler\n\n
    (final StatefulMbo statefulMbo)\n
    '''
def preStatusChange():
    '''returns None\n\n
    preStatusChange(final String s, final String s2, final Date date, final String s3)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String s, final String s2, final Date date, final String s3)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String s)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String s, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String s, final String s2, final Date val, final String s3)\n
    '''
