def ():
    '''returns AutoScriptStateHandler\n\n
    (final StatefulMbo sm)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalState)\n
    '''
def checkUserSecurity():
    '''returns None\n\n
    checkUserSecurity(final String desiredMaxState)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentState, final String desiredState, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentState, final String desiredState, final Date date, final String memo)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String currentState, final String State, final Date asOfDate, final String memo)\n
    '''
