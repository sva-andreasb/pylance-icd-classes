def MatUseTransSet():
    '''    public MatUseTransSet(final MboServerInterface ms)
    '''
def copyInvReserveSet():
    '''    public void copyInvReserveSet(final MboSetRemote invReserveSet)
    '''
def copySparePartSet():
    '''    public void copySparePartSet(final MboSetRemote sparePartSet)
    '''
def addMatUseFromInvReserve():
    '''    public MboRemote addMatUseFromInvReserve(final MboRemote invRes)
    '''
def copyMatUseTransSet():
    '''    public void copyMatUseTransSet(final MboSetRemote matUseSet)
    '''
def setDateRange():
    '''    public void setDateRange(final int type)
    '''
def getDateRange():
    '''    public int getDateRange()
    '''
def setLastNDays():
    '''    public void setLastNDays(final int nDays)
    '''
def getLastNDays():
    '''    public int getLastNDays()
    '''
def setStartDate():
    '''    public void setStartDate(final Date startDateActLab)
    '''
def setEndDate():
    '''    public void setEndDate(final Date endDateActLab)
    '''
def getStartDate():
    '''    public Date getStartDate()
    '''
def getEndDate():
    '''    public Date getEndDate()
    '''
def getUserPrefWhere():
    '''    public String getUserPrefWhere()
    '''
def addDates():
    '''    public Date addDates(final Date date, final int days)
    '''
def canAdd():
    '''    public void canAdd()
    '''
def addAtIndex():
    '''    public MboRemote addAtIndex(final long accessModifier, final int index)
    '''
def remove():
    '''    public void remove(final MboRemote mbo)
    '''
def addListener():
    '''    public void addListener(final MboSetListener l)
    '''
def removeListener():
    '''    public void removeListener(final MboSetListener l)
    '''
def reportModifiedMbo():
    '''    public void reportModifiedMbo(final MboRemote modifiedMbo)
    '''
def returnIPCParts():
    '''    public void returnIPCParts(final IpcSelectedPartsSetRemote partset)
    '''
def preValidateIpcBom():
    '''    public void preValidateIpcBom(final IpcBomSetRemote bomset)
    '''
def addDeltaCurbal():
    '''    public void addDeltaCurbal(final MboRemote invBal, final double quantity, final MboRemote currentMatUse)
    '''
def addDeltaIssueYTD():
    '''    public void addDeltaIssueYTD(final MboRemote inventory, final double quantity, final MboRemote currentMatUse)
    '''
def transCommitted():
    '''    public void transCommitted()
    '''
def getInvReserveVector():
    '''    public Vector getInvReserveVector()
    '''
def getUncommittedTransVector():
    '''    public Vector getUncommittedTransVector()
    '''
def setUncommittedTransVector():
    '''    public void setUncommittedTransVector(final Vector uncommitted)
    '''
def clearVectors():
    '''    public void clearVectors()
    '''
def storeToRotatingAssetHash():
    '''    public void storeToRotatingAssetHash(final MboRemote matUse)
    '''
def rotAssetExists():
    '''    public MboRemote rotAssetExists(final MboRemote matUse)
    '''
def getLifoFifoInHash():
    '''    public Hashtable getLifoFifoInHash()
    '''
