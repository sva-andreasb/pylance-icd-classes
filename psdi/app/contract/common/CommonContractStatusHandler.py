def ():
    '''returns CommonContractStatusHandler\n\n
    (final StatefulMbo sm)\n
    '''
def possibleStatusChange():
    '''returns None\n\n
    possibleStatusChange(final String currentMaxStatus, final String desiredMaxStatus)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String desiredExternalStatus)\n
    '''
def canClose():
    '''returns None\n\n
    canClose(final String currentMaxStatus)\n
    '''
def canExpire():
    '''returns None\n\n
    canExpire(final String currentMaxStatus)\n
    '''
def canSuspnd():
    '''returns None\n\n
    canSuspnd(final String currentMaxStatus)\n
    '''
def canPndRev():
    '''returns None\n\n
    canPndRev(final String currentMaxStatus)\n
    '''
def canRevise():
    '''returns None\n\n
    canRevise(final String currentMaxStatus)\n
    '''
def canWStart():
    '''returns None\n\n
    canWStart(final String currentMaxStatus)\n
    '''
def canApprove():
    '''returns None\n\n
    canApprove(final String currentMaxStatus)\n
    '''
def canDraft():
    '''returns None\n\n
    canDraft(final String currentMaxStatus)\n
    '''
def canUnapprove():
    '''returns None\n\n
    canUnapprove(final String currentMaxStatus)\n
    '''
def canCancel():
    '''returns None\n\n
    canCancel(final String currentMaxStatus)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)\n
    '''
def revise():
    '''returns None\n\n
    revise(final String desiredStatus, final Date date)\n
    '''
def expire():
    '''returns None\n\n
    expire(final String desiredStatus, final Date date)\n
    '''
def unapprove():
    '''returns None\n\n
    unapprove(final String desiredStatus, final Date date)\n
    '''
def doesContractReferenceExistOnPO():
    '''returns None\n\n
    doesContractReferenceExistOnPO()\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final String desiredStatus, final Date date)\n
    '''
def getNextRevision():
    '''returns MboRemote\n\n
    getNextRevision()\n
    '''
def draft():
    '''returns None\n\n
    draft(final String desiredStatus, final Date date)\n
    '''
def close():
    '''returns None\n\n
    close(final String desiredStatus, final Date date)\n
    '''
def suspnd():
    '''returns None\n\n
    suspnd(final String desiredStatus, final Date date)\n
    '''
def approve():
    '''returns None\n\n
    approve(final String desiredStatus, final Date date)\n
    '''
def setLineStatus():
    '''returns None\n\n
    setLineStatus(final String externalStatus)\n
    '''
def postStatusChange():
    '''returns None\n\n
    postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)\n
    '''
