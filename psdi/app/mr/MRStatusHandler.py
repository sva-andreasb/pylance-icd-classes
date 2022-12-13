def MRStatusHandler():
    '''    public MRStatusHandler(final MR sm)
    '''
def changeStatus():
    '''    public void changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)
    '''
def canChangeStatus():
    '''    public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
    '''
def canUnapprove():
    '''    public void canUnapprove(final String currentInternalStatus)
    '''
def canApprove():
    '''    public void canApprove(final String currentInternalStatus)
    '''
def canClose():
    '''    public void canClose(final String currentInternalStatus)
    '''
def canCancel():
    '''    public void canCancel(final String currentInternalStatus)
    '''
def checkStatusChangeAuthorization():
    '''    public void checkStatusChangeAuthorization(final String desiredExternalStatus)
    '''
def checkUserSecurity():
    '''    public void checkUserSecurity(final String desiredMaxStatus)
    '''
def updateMboForStatus():
    '''    public void updateMboForStatus(final String status)
    '''
def canAddInvReserve():
    '''    public boolean canAddInvReserve(final MboRemote mrlineMbo)
    '''
