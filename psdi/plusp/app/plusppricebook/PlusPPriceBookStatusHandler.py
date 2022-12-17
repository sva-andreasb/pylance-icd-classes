def ():
    '''returns PlusPPriceBookStatusHandler\n\n
    (final StatefulMbo statefulMbo, final boolean isRevision)\n
    '''
def convertStatusToInt():
    '''returns int\n\n
    convertStatusToInt(final String value)\n
    '''
def possibleStatusChange():
    '''returns None\n\n
    possibleStatusChange(final String value, final String value2)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String s, final String val, final Date val2, final String s2)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String s)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def updateMboForStatus():
    '''returns None\n\n
    updateMboForStatus(final String s)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String s, final String s2, final Date date, final String s3)\n
    '''
