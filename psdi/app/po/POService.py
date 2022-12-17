def ():
    '''returns POService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def doesWoHaveServices():
    '''returns boolean\n\n
    doesWoHaveServices(final UserInfo userInfo, final String wonum)\n
    '''
def createReceipt():
    '''returns MboRemote\n\n
    createReceipt(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final String siteid)\n
    '''
def createReturn():
    '''returns MboRemote\n\n
    createReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final String siteid)\n
    createReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final List assets, final String siteid, final boolean returnHasReference, final MboRemote origReceipt, final String binnum, final String lotnum)\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def getInternalStatus():
    '''returns String\n\n
    getInternalStatus(final String extStatus)\n
    '''
def getPOReferences():
    '''returns Vector\n\n
    getPOReferences(final String mrnum, final String mrlinenum, final UserInfo userInfo)\n
    '''
def createReceipts():
    '''returns Vector\n\n
    createReceipts(final UserInfo ui, String ponum, String catalogCode, String itemnum, final String itemsetid, String mrnum, String modelnum, String packingSlipNum, String requestedby, final int noOfRows)\n
    createReceipts(final UserInfo ui, String ponum, String catalogCode, String itemnum, final String itemsetid, String mrnum, String modelnum, String packingSlipNum, String requestedby, final boolean isPowerApp)\n
    createReceipts(final UserInfo ui, final String ponum, final String catalogCode, final String itemnum, final String itemsetid, final String mrnum, final String modelnum, final String packingSlipNum, final String requestedby)\n
    createReceipts(final UserInfo ui, final String ponum)\n
    '''
def servicesToBeReceived():
    '''returns MboSetRemote\n\n
    servicesToBeReceived(final MboSetRemote poLineSetRemote, final boolean checkInvBalance, final String ownerSysId, final UserInfo userInfo)\n
    '''
def itemsToBeReceived():
    '''returns MboSetRemote\n\n
    itemsToBeReceived(final MboSetRemote poLineSetRemote, final boolean checkInvBalance, final String ownerSysId, final UserInfo userInfo, final boolean isPowerApp)\n
    '''
def isRotating():
    '''returns boolean\n\n
    isRotating(final MboRemote poLineRemote)\n
    '''
def generateReceipts():
    '''returns boolean\n\n
    generateReceipts(final UserInfo ui, final MboSetRemote targetMbos, final MboSetRemote dataSheet)\n
    '''
def getReceiptSetForReturn():
    '''returns MboSetRemote\n\n
    getReceiptSetForReturn(final MboRemote poRemote)\n
    '''
def returnReceiptSetForReturn():
    '''returns MboSetRemote\n\n
    returnReceiptSetForReturn(final MboSetRemote receiptSetForReturn, final MboSetRemote matRecTransSetRemote)\n
    '''
def checkPOValidity():
    '''returns None\n\n
    checkPOValidity(final MboRemote poRemote)\n
    '''
def compareCopyTerms():
    '''returns None\n\n
    compareCopyTerms(final MboSetRemote fromTermSet, final MboSetRemote toTermSet)\n
    compareCopyTerms(final MboSetRemote fromTermSet, final MboSetRemote toTermSet, final MboRemote mbo)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("PO") final PORemote po, final String status, final Date date, final String memo)\n
    '''
