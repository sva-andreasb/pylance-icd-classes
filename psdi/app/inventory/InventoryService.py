def InventoryService():
'''public InventoryService()
public InventoryService(final MXServer mxServer)
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
def setAdjustmentType():
'''public void setAdjustmentType(final int type, final MboRemote invAdjust)
'''
pass
def getItemsInStore():
'''public MboSetRemote getItemsInStore(final UserInfo userInfo, final String storeroom)
'''
pass
def createIssue():
'''public MboRemote createIssue(final UserInfo userInfo, final MboSetRemote issueSet, final String itemnum, final String location, final String siteid, final String ownersysid1)
public MboRemote createIssue(final UserInfo userInfo, final String itemnum, final String location, final String siteid, final String bin, final String lot, final String rotasset, final double qty)
'''
pass
def getItemSetIdFromSite():
'''public String getItemSetIdFromSite(final UserInfo userInfo, final String siteid)
'''
pass
def createMiscReceipt():
'''public MboRemote createMiscReceipt(final UserInfo userInfo, final MboSetRemote existingReceiptSet, final String itemnum, final String toStoreLoc, final String siteid, final String ownersysid)
'''
pass
def getCurrentBalance():
'''public double getCurrentBalance(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String binnum, final String lotnum)
'''
pass
def getBalances():
'''public MboSetRemote getBalances(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String siteid)
'''
pass
def getBalancesForInventorySet():
'''public MboSetRemote getBalancesForInventorySet(final MboSetRemote inventorySet)
'''
pass
def getUnauthInvSet():
'''public Vector getUnauthInvSet()
'''
pass
def canGoNegative():
'''public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location, final String siteid)
public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location)
public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double totalAvailable, final MboRemote sourceMbo)
public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location, final String binnum, final String lotnum, final String siteid)
public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo)
public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo, final String costType)
'''
pass
def isSameStoreroomTransfer():
'''public boolean isSameStoreroomTransfer(final MboRemote sourceMbo)
'''
pass
def findItemsForPhysCount():
'''public MboSetRemote findItemsForPhysCount(final UserInfo userInfo, final String location)
'''
pass
def getBins():
'''public MboSetRemote getBins(final UserInfo userInfo, final String location, final String binnum)
'''
pass
def getLots():
'''public MboSetRemote getLots(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String binnum)
'''
pass
def getReservationsForWO():
'''public MboSetRemote getReservationsForWO(final UserInfo userInfo, final String wonum)
'''
pass
def getReservationsForMR():
'''public MboSetRemote getReservationsForMR(final UserInfo userInfo, final String mrnum)
'''
pass
def isWOValid():
'''public MboRemote isWOValid(final UserInfo userInfo, final String wonum)
'''
pass
def isMRValid():
'''public void isMRValid(final UserInfo userInfo, final String mrnum)
'''
pass
def getMatReceiptSet():
'''public MboSetRemote getMatReceiptSet(final UserInfo ui, final String ponum)
'''
pass
def validateBinLot():
'''public void validateBinLot(final Inventory inv, final String binnum, final String lotnum)
'''
pass
def validateInventory():
'''public MboRemote validateInventory(final UserInfo userInfo, final String item, final String itemsetid, final String location)
'''
pass
def isCourierOrLabor():
'''public boolean isCourierOrLabor(final UserInfo userInfo, final String location)
'''
pass
def getDefaultLotNum():
'''public String getDefaultLotNum(final MboRemote mbo)
'''
pass
def getConversionFactor():
'''public double getConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID, final String itemNum)
public double getConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID)
'''
pass
def getUnitConversionFactor():
'''public String getUnitConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID, final String itemNum)
'''
pass
def adjustCurrentBalance():
'''public void adjustCurrentBalance(@WSMboKey("INVBALANCES") final MboRemote invBalances, final String newBalance, final double stdcost, final double avgcost, final String conditioncode)
'''
pass
def getConversionFactorToStoreroom():
'''public MboRemote getConversionFactorToStoreroom(@WSMboKey("TRANSFERCURITEM") final MboRemote mbo, final String tostoreloc, final String tositeid)
'''
pass
def createInvbalances():
'''public void createInvbalances(@WSMboKey("INVENTORY") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String binnum, final String lotnum, final String conditioncode, final String itemsetid, final String curbal, final UserInfo userInfo)
'''
pass
def adjustPhysicalCount():
'''public void adjustPhysicalCount(@WSMboKey("INVBALANCES") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String binnum, final String lotnum, final String itemsetid, final double physcnt, final UserInfo userInfo)
'''
pass
def previewReconcile():
'''public void previewReconcile(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo)
'''
pass
def reconcile():
'''public MboSetRemote reconcile(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo)
'''
pass
def createReturnForIssueStoreloc():
'''public MboRemote createReturnForIssueStoreloc(@WSMboKey("MAUSETRANS") final MboRemote issueMbo)
'''
pass
def updateInventory():
'''public MboRemote updateInventory(@WSMboKey("INVBALANCES") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String itemsetid, final UserInfo userInfo)
'''
pass
def getStoreroom():
'''public MboRemote getStoreroom(final UserInfo userInfo, final String location, final String siteid)
'''
pass
def updateAllInventory():
'''public MboSetRemote updateAllInventory(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo, final UserInfo userInfo)
'''
pass
def createIssueForNonStock():
'''public MboRemote createIssueForNonStock(final UserInfo userInfo, MboSetRemote issueSet, final String itemnum, final String itemsetid, final String location, final String siteid, final String ownersysid1)
'''
pass
def createPickList():
'''public MboRemote createPickList(@WSMboSetQbe("INVRESERVE") final MboSetRemote msr, final String pldescription, final String plnum, final Date reqdate, final String storeroom, final String siteid, final UserInfo userInfo, MXTransaction trans)
'''
pass
def updateInvUseLines():
'''public void updateInvUseLines(final MboSetRemote msr, final String plnum, final MXTransaction trans)
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("INVPICKLIST") final MboRemote mbo, final String status, final Date asOfDate, final String memo, final long accessModifier)
'''
pass
def autoSplitRecordSet():
'''public MboSetRemote autoSplitRecordSet(@WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)
'''
pass
def getLineSplitRecords():
'''public MboSetRemote getLineSplitRecords(@WSMboSetQbe("INVBALANCES") final MboSetRemote invbalmsr, @WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)
'''
pass
def getLineSplitForRotItems():
'''public MboSetRemote getLineSplitForRotItems(@WSMboSetQbe("ASSET") final MboSetRemote assetmsr, @WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)
'''
pass
def addReservation():
'''public MboRemote addReservation(@WSMboSetQbe("INVRESERVE") final MboSetRemote msr, final String pl_num, final String siteid, final UserInfo userInfo, MXTransaction trans)
'''
pass
def setZeroNewPhysCnt():
'''public void setZeroNewPhysCnt(final long uniqueId, final boolean toRemove)
'''
pass
def isZeroNewPhysCnt():
'''public boolean isZeroNewPhysCnt(final long uniqueId)
'''
pass
