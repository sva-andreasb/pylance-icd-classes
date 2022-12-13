EVENT_AGREESTATUS = "String  \"maximo.pluspagreement.statuschange.*\""
EVENT_AGREERATESTATUS = "String  \"maximo.pluspratesched.statuschange.*\""
def PlusPAgreeEventListener():
    '''    public PlusPAgreeEventListener(final PluspAgreeStateful agreestate, final String status, final Date date, final String memo, final long modifier, final String s)
    '''
def removeListener():
    '''    public void removeListener()
    '''
def eventAction():
    '''    public void eventAction(final EventMessage eventMessage)
    '''
def eventValidate():
    '''    public boolean eventValidate(final EventMessage eventMessage)
    '''
def postCommitEventAction():
    '''    public void postCommitEventAction(final EventMessage eventMessage)
    '''
def preSaveEventAction():
    '''    public void preSaveEventAction(final EventMessage eventMessage)
    '''
