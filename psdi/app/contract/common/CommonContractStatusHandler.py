def CommonContractStatusHandler():
    '''    public CommonContractStatusHandler(final StatefulMbo sm)
    '''
def possibleStatusChange():
    '''    public void possibleStatusChange(final String currentMaxStatus, final String desiredMaxStatus)
    '''
def canChangeStatus():
    '''    public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
    '''
def checkStatusChangeAuthorization():
    '''    public void checkStatusChangeAuthorization(final String desiredExternalStatus)
    '''
def getOptionName():
    '''    public static String getOptionName(final String status)
    '''
def canClose():
    '''    public void canClose(final String currentMaxStatus)
    '''
def canExpire():
    '''    public void canExpire(final String currentMaxStatus)
    '''
def canSuspnd():
    '''    public void canSuspnd(final String currentMaxStatus)
    '''
def canPndRev():
    '''    public void canPndRev(final String currentMaxStatus)
    '''
def canRevise():
    '''    public void canRevise(final String currentMaxStatus)
    '''
def canWStart():
    '''    public void canWStart(final String currentMaxStatus)
    '''
def canApprove():
    '''    public void canApprove(final String currentMaxStatus)
    '''
def canDraft():
    '''    public void canDraft(final String currentMaxStatus)
    '''
def canUnapprove():
    '''    public void canUnapprove(final String currentMaxStatus)
    '''
def canCancel():
    '''    public void canCancel(final String currentMaxStatus)
    '''
def changeStatus():
    '''    public void changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)
    '''
def revise():
    '''    public void revise(final String desiredStatus, final Date date)
    '''
def expire():
    '''    public void expire(final String desiredStatus, final Date date)
    '''
def unapprove():
    '''    public void unapprove(final String desiredStatus, final Date date)
    '''
def doesContractReferenceExistOnPO():
    '''    public void doesContractReferenceExistOnPO()
    '''
def cancel():
    '''    public void cancel(final String desiredStatus, final Date date)
    '''
def getNextRevision():
    '''    public MboRemote getNextRevision()
    '''
def draft():
    '''    public void draft(final String desiredStatus, final Date date)
    '''
def close():
    '''    public void close(final String desiredStatus, final Date date)
    '''
def suspnd():
    '''    public void suspnd(final String desiredStatus, final Date date)
    '''
def approve():
    '''    public void approve(final String desiredStatus, final Date date)
    '''
def setLineStatus():
    '''    public void setLineStatus(final String externalStatus)
    '''
def postStatusChange():
    '''    public void postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)
    '''
