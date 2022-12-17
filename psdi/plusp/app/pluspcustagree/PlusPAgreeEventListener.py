EVENT_AGREESTATUS = "String  \"maximo.pluspagreement.statuschange.*\""
EVENT_AGREERATESTATUS = "String  \"maximo.pluspratesched.statuschange.*\""
def ():
    '''returns PlusPAgreeEventListener\n\n
    (final PluspAgreeStateful agreestate, final String status, final Date date, final String memo, final long modifier, final String s)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener()\n
    '''
def eventAction():
    '''returns None\n\n
    eventAction(final EventMessage eventMessage)\n
    '''
def eventValidate():
    '''returns boolean\n\n
    eventValidate(final EventMessage eventMessage)\n
    '''
def postCommitEventAction():
    '''returns None\n\n
    postCommitEventAction(final EventMessage eventMessage)\n
    '''
def preSaveEventAction():
    '''returns None\n\n
    preSaveEventAction(final EventMessage eventMessage)\n
    '''
