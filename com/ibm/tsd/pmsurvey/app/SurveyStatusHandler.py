def ():
    '''returns SurveyStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalStatus)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(String currentStatus, String desiredStatus, final Date asOfDate, final String memo)\n
    '''
def preStatusChange():
    '''returns None\n\n
    preStatusChange(final String currentStatus, String desiredStatus, final Date asOfDate, final String memo)\n
    '''
