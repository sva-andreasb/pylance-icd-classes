def POService():
'''public POService()
public POService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def doesWoHaveServices():
'''public boolean doesWoHaveServices(final UserInfo userInfo, final String wonum)
'''
pass
def createReceipt():
'''public MboRemote createReceipt(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final String siteid)
'''
pass
def createReturn():
'''public MboRemote createReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final String siteid)
public MboRemote createReturn(final UserInfo userInfo, final MboSetRemote receiptSet, final String ponum, final long polinenum, final String porevnum, final String ownersysid, final List assets, final String siteid, final boolean returnHasReference, final MboRemote origReceipt, final String binnum, final String lotnum)
'''
pass
def initCriteriaList():
'''public void initCriteriaList(final Hashtable criteriaTable)
'''
pass
def getInternalStatus():
'''public String getInternalStatus(final String extStatus)
'''
pass
def getPOReferences():
'''public Vector getPOReferences(final String mrnum, final String mrlinenum, final UserInfo userInfo)
'''
pass
def createReceipts():
'''public void createReceipts(final UserInfo ui, String ponum, String catalogCode, String itemnum, final String itemsetid, String mrnum, String modelnum, String packingSlipNum, String requestedby, final int noOfRows)
public Vector createReceipts(final UserInfo ui, String ponum, String catalogCode, String itemnum, final String itemsetid, String mrnum, String modelnum, String packingSlipNum, String requestedby, final boolean isPowerApp)
public Vector createReceipts(final UserInfo ui, final String ponum, final String catalogCode, final String itemnum, final String itemsetid, final String mrnum, final String modelnum, final String packingSlipNum, final String requestedby)
public Vector createReceipts(final UserInfo ui, final String ponum)
'''
pass
def servicesToBeReceived():
'''public MboSetRemote servicesToBeReceived(final MboSetRemote poLineSetRemote, final boolean checkInvBalance, final String ownerSysId, final UserInfo userInfo)
'''
pass
def itemsToBeReceived():
'''public MboSetRemote itemsToBeReceived(final MboSetRemote poLineSetRemote, final boolean checkInvBalance, final String ownerSysId, final UserInfo userInfo, final boolean isPowerApp)
'''
pass
def isRotating():
'''public boolean isRotating(final MboRemote poLineRemote)
'''
pass
def generateReceipts():
'''public boolean generateReceipts(final UserInfo ui, final MboSetRemote targetMbos, final MboSetRemote dataSheet)
'''
pass
def getReceiptSetForReturn():
'''public MboSetRemote getReceiptSetForReturn(final MboRemote poRemote)
'''
pass
def returnReceiptSetForReturn():
'''public MboSetRemote returnReceiptSetForReturn(final MboSetRemote receiptSetForReturn, final MboSetRemote matRecTransSetRemote)
'''
pass
def checkPOValidity():
'''public void checkPOValidity(final MboRemote poRemote)
'''
pass
def compareCopyTerms():
'''public void compareCopyTerms(final MboSetRemote fromTermSet, final MboSetRemote toTermSet)
public void compareCopyTerms(final MboSetRemote fromTermSet, final MboSetRemote toTermSet, final MboRemote mbo)
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("PO") final PORemote po, final String status, final Date date, final String memo)
'''
pass
