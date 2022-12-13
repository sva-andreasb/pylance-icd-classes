def CommonContractStatusHandler():
'''public CommonContractStatusHandler(final StatefulMbo sm)
'''
pass
def possibleStatusChange():
'''public void possibleStatusChange(final String currentMaxStatus, final String desiredMaxStatus)
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final String currentStatus, final String desiredStatus, final long accessModifier)
'''
pass
def checkStatusChangeAuthorization():
'''public void checkStatusChangeAuthorization(final String desiredExternalStatus)
'''
pass
def getOptionName():
'''public static String getOptionName(final String status)
'''
pass
def canClose():
'''public void canClose(final String currentMaxStatus)
'''
pass
def canExpire():
'''public void canExpire(final String currentMaxStatus)
'''
pass
def canSuspnd():
'''public void canSuspnd(final String currentMaxStatus)
'''
pass
def canPndRev():
'''public void canPndRev(final String currentMaxStatus)
'''
pass
def canRevise():
'''public void canRevise(final String currentMaxStatus)
'''
pass
def canWStart():
'''public void canWStart(final String currentMaxStatus)
'''
pass
def canApprove():
'''public void canApprove(final String currentMaxStatus)
'''
pass
def canDraft():
'''public void canDraft(final String currentMaxStatus)
'''
pass
def canUnapprove():
'''public void canUnapprove(final String currentMaxStatus)
'''
pass
def canCancel():
'''public void canCancel(final String currentMaxStatus)
'''
pass
def changeStatus():
'''public void changeStatus(final String currentStatus, final String desiredStatus, final Date date, final String memo)
'''
pass
def revise():
'''public void revise(final String desiredStatus, final Date date)
'''
pass
def expire():
'''public void expire(final String desiredStatus, final Date date)
'''
pass
def unapprove():
'''public void unapprove(final String desiredStatus, final Date date)
'''
pass
def doesContractReferenceExistOnPO():
'''public void doesContractReferenceExistOnPO()
'''
pass
def cancel():
'''public void cancel(final String desiredStatus, final Date date)
'''
pass
def getNextRevision():
'''public MboRemote getNextRevision()
'''
pass
def draft():
'''public void draft(final String desiredStatus, final Date date)
'''
pass
def close():
'''public void close(final String desiredStatus, final Date date)
'''
pass
def suspnd():
'''public void suspnd(final String desiredStatus, final Date date)
'''
pass
def approve():
'''public void approve(final String desiredStatus, final Date date)
'''
pass
def setLineStatus():
'''public void setLineStatus(final String externalStatus)
'''
pass
def postStatusChange():
'''public void postStatusChange(final String currentStatus, final String status, final Date asOfDate, final String memo)
'''
pass
