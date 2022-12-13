def MatUseTransSet():
'''public MatUseTransSet(final MboServerInterface ms)
'''
pass
def copyInvReserveSet():
'''public void copyInvReserveSet(final MboSetRemote invReserveSet)
'''
pass
def copySparePartSet():
'''public void copySparePartSet(final MboSetRemote sparePartSet)
'''
pass
def addMatUseFromInvReserve():
'''public MboRemote addMatUseFromInvReserve(final MboRemote invRes)
'''
pass
def copyMatUseTransSet():
'''public void copyMatUseTransSet(final MboSetRemote matUseSet)
'''
pass
def setDateRange():
'''public void setDateRange(final int type)
'''
pass
def getDateRange():
'''public int getDateRange()
'''
pass
def setLastNDays():
'''public void setLastNDays(final int nDays)
'''
pass
def getLastNDays():
'''public int getLastNDays()
'''
pass
def setStartDate():
'''public void setStartDate(final Date startDateActLab)
'''
pass
def setEndDate():
'''public void setEndDate(final Date endDateActLab)
'''
pass
def getStartDate():
'''public Date getStartDate()
'''
pass
def getEndDate():
'''public Date getEndDate()
'''
pass
def getUserPrefWhere():
'''public String getUserPrefWhere()
'''
pass
def addDates():
'''public Date addDates(final Date date, final int days)
'''
pass
def canAdd():
'''public void canAdd()
'''
pass
def addAtIndex():
'''public MboRemote addAtIndex(final long accessModifier, final int index)
'''
pass
def remove():
'''public void remove(final MboRemote mbo)
'''
pass
def addListener():
'''public void addListener(final MboSetListener l)
'''
pass
def removeListener():
'''public void removeListener(final MboSetListener l)
'''
pass
def reportModifiedMbo():
'''public void reportModifiedMbo(final MboRemote modifiedMbo)
'''
pass
def returnIPCParts():
'''public void returnIPCParts(final IpcSelectedPartsSetRemote partset)
'''
pass
def preValidateIpcBom():
'''public void preValidateIpcBom(final IpcBomSetRemote bomset)
'''
pass
def addDeltaCurbal():
'''public void addDeltaCurbal(final MboRemote invBal, final double quantity, final MboRemote currentMatUse)
'''
pass
def addDeltaIssueYTD():
'''public void addDeltaIssueYTD(final MboRemote inventory, final double quantity, final MboRemote currentMatUse)
'''
pass
def transCommitted():
'''public void transCommitted()
'''
pass
def getInvReserveVector():
'''public Vector getInvReserveVector()
'''
pass
def getUncommittedTransVector():
'''public Vector getUncommittedTransVector()
'''
pass
def setUncommittedTransVector():
'''public void setUncommittedTransVector(final Vector uncommitted)
'''
pass
def clearVectors():
'''public void clearVectors()
'''
pass
def storeToRotatingAssetHash():
'''public void storeToRotatingAssetHash(final MboRemote matUse)
'''
pass
def rotAssetExists():
'''public MboRemote rotAssetExists(final MboRemote matUse)
'''
pass
def getLifoFifoInHash():
'''public Hashtable getLifoFifoInHash()
'''
pass
