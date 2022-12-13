def POService():
    '''    public POService()
    public POService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def doesWoHaveServices():
    '''    public boolean doesWoHaveServices(final UserInfo userInfo, final String wonum)
    '''
def createReceipt():
    '''    public MboRemote createReceipt(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final String siteid)
    '''
def createReturn():
    '''    public MboRemote createReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final String siteid)
    public MboRemote createReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final List assets, final String siteid, final boolean returnHasReference, final MboRemote origReceipt, final String binnum, final String lotnum)
    '''
def initCriteriaList():
    '''    public void initCriteriaList(final Hashtable criteriaTable)
    '''
def getInternalStatus():
    '''    public String getInternalStatus(final String extStatus)
    '''
def getPOReferences():
    '''    public Vector getPOReferences(final String mrnum, final String mrlinenum, final UserInfo userInfo)
    '''
def createReceipts():
    '''    public void createReceipts(final UserInfo ui, String ponum, String catalogCode, String itemnum, final String itemsetid, String mrnum, String modelnum, String packingSlipNum, String requestedby, final int noOfRows)
    public Vector createReceipts(final UserInfo ui, String ponum, String catalogCode, String itemnum, final String itemsetid, String mrnum, String modelnum, String packingSlipNum, String requestedby, final boolean isPowerApp)
    public Vector createReceipts(final UserInfo ui, final String ponum, final String catalogCode, final String itemnum, final String itemsetid, final String mrnum, final String modelnum, final String packingSlipNum, final String requestedby)
    public Vector createReceipts(final UserInfo ui, final String ponum)
    '''
def servicesToBeReceived():
    '''    public MboSetRemote servicesToBeReceived(final MboSetRemote poLineSetRemote, final boolean checkInvBalance, final String ownerSysId, final UserInfo userInfo)
    '''
def itemsToBeReceived():
    '''    public MboSetRemote itemsToBeReceived(final MboSetRemote poLineSetRemote, final boolean checkInvBalance, final String ownerSysId, final UserInfo userInfo, final boolean isPowerApp)
    '''
def isRotating():
    '''    public boolean isRotating(final MboRemote poLineRemote)
    '''
def generateReceipts():
    '''    public boolean generateReceipts(final UserInfo ui, final MboSetRemote targetMbos, final MboSetRemote dataSheet)
    '''
def getReceiptSetForReturn():
    '''    public MboSetRemote getReceiptSetForReturn(final MboRemote poRemote)
    '''
def returnReceiptSetForReturn():
    '''    public MboSetRemote returnReceiptSetForReturn(final MboSetRemote receiptSetForReturn, final MboSetRemote matRecTransSetRemote)
    '''
def checkPOValidity():
    '''    public void checkPOValidity(final MboRemote poRemote)
    '''
def compareCopyTerms():
    '''    public void compareCopyTerms(final MboSetRemote fromTermSet, final MboSetRemote toTermSet)
    public void compareCopyTerms(final MboSetRemote fromTermSet, final MboSetRemote toTermSet, final MboRemote mbo)
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("PO") final PORemote po, final String status, final Date date, final String memo)
    '''
