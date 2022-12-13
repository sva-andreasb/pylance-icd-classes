def InventoryService():
    '''    public InventoryService()
    public InventoryService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def setAdjustmentType():
    '''    public void setAdjustmentType(final int type, final MboRemote invAdjust)
    '''
def getItemsInStore():
    '''    public MboSetRemote getItemsInStore(final UserInfo userInfo, final String storeroom)
    '''
def createIssue():
    '''    public MboRemote createIssue(final UserInfo userInfo, final MboSetRemote issueSet, final String itemnum, final String location, final String siteid, final String ownersysid1)
    public MboRemote createIssue(final UserInfo userInfo, final String itemnum, final String location, final String siteid, final String bin, final String lot, final String rotasset, final double qty)
    '''
def getItemSetIdFromSite():
    '''    public String getItemSetIdFromSite(final UserInfo userInfo, final String siteid)
    '''
def createMiscReceipt():
    '''    public MboRemote createMiscReceipt(final UserInfo userInfo, final MboSetRemote existingReceiptSet, final String itemnum, final String toStoreLoc, final String siteid, final String ownersysid)
    '''
def getCurrentBalance():
    '''    public double getCurrentBalance(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String binnum, final String lotnum)
    '''
def getBalances():
    '''    public MboSetRemote getBalances(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String siteid)
    '''
def getBalancesForInventorySet():
    '''    public MboSetRemote getBalancesForInventorySet(final MboSetRemote inventorySet)
    '''
def getUnauthInvSet():
    '''    public Vector getUnauthInvSet()
    '''
def canGoNegative():
    '''    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location, final String siteid)
    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location)
    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double totalAvailable, final MboRemote sourceMbo)
    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location, final String binnum, final String lotnum, final String siteid)
    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo)
    public void canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo, final String costType)
    '''
def isSameStoreroomTransfer():
    '''    public boolean isSameStoreroomTransfer(final MboRemote sourceMbo)
    '''
def findItemsForPhysCount():
    '''    public MboSetRemote findItemsForPhysCount(final UserInfo userInfo, final String location)
    '''
def getBins():
    '''    public MboSetRemote getBins(final UserInfo userInfo, final String location, final String binnum)
    '''
def getLots():
    '''    public MboSetRemote getLots(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String binnum)
    '''
def getReservationsForWO():
    '''    public MboSetRemote getReservationsForWO(final UserInfo userInfo, final String wonum)
    '''
def getReservationsForMR():
    '''    public MboSetRemote getReservationsForMR(final UserInfo userInfo, final String mrnum)
    '''
def isWOValid():
    '''    public MboRemote isWOValid(final UserInfo userInfo, final String wonum)
    '''
def isMRValid():
    '''    public void isMRValid(final UserInfo userInfo, final String mrnum)
    '''
def getMatReceiptSet():
    '''    public MboSetRemote getMatReceiptSet(final UserInfo ui, final String ponum)
    '''
def validateBinLot():
    '''    public void validateBinLot(final Inventory inv, final String binnum, final String lotnum)
    '''
def validateInventory():
    '''    public MboRemote validateInventory(final UserInfo userInfo, final String item, final String itemsetid, final String location)
    '''
def isCourierOrLabor():
    '''    public boolean isCourierOrLabor(final UserInfo userInfo, final String location)
    '''
def getDefaultLotNum():
    '''    public String getDefaultLotNum(final MboRemote mbo)
    '''
def getConversionFactor():
    '''    public double getConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID, final String itemNum)
    public double getConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID)
    '''
def getUnitConversionFactor():
    '''    public String getUnitConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID, final String itemNum)
    '''
def adjustCurrentBalance():
    '''    public void adjustCurrentBalance(@WSMboKey("INVBALANCES") final MboRemote invBalances, final String newBalance, final double stdcost, final double avgcost, final String conditioncode)
    '''
def getConversionFactorToStoreroom():
    '''    public MboRemote getConversionFactorToStoreroom(@WSMboKey("TRANSFERCURITEM") final MboRemote mbo, final String tostoreloc, final String tositeid)
    '''
def createInvbalances():
    '''    public void createInvbalances(@WSMboKey("INVENTORY") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String binnum, final String lotnum, final String conditioncode, final String itemsetid, final String curbal, final UserInfo userInfo)
    '''
def adjustPhysicalCount():
    '''    public void adjustPhysicalCount(@WSMboKey("INVBALANCES") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String binnum, final String lotnum, final String itemsetid, final double physcnt, final UserInfo userInfo)
    '''
def previewReconcile():
    '''    public void previewReconcile(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo)
    '''
def reconcile():
    '''    public MboSetRemote reconcile(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo)
    '''
def createReturnForIssueStoreloc():
    '''    public MboRemote createReturnForIssueStoreloc(@WSMboKey("MAUSETRANS") final MboRemote issueMbo)
    '''
def updateInventory():
    '''    public MboRemote updateInventory(@WSMboKey("INVBALANCES") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String itemsetid, final UserInfo userInfo)
    '''
def getStoreroom():
    '''    public MboRemote getStoreroom(final UserInfo userInfo, final String location, final String siteid)
    '''
def updateAllInventory():
    '''    public MboSetRemote updateAllInventory(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo, final UserInfo userInfo)
    '''
def createIssueForNonStock():
    '''    public MboRemote createIssueForNonStock(final UserInfo userInfo, MboSetRemote issueSet, final String itemnum, final String itemsetid, final String location, final String siteid, final String ownersysid1)
    '''
def createPickList():
    '''    public MboRemote createPickList(@WSMboSetQbe("INVRESERVE") final MboSetRemote msr, final String pldescription, final String plnum, final Date reqdate, final String storeroom, final String siteid, final UserInfo userInfo, MXTransaction trans)
    '''
def updateInvUseLines():
    '''    public void updateInvUseLines(final MboSetRemote msr, final String plnum, final MXTransaction trans)
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("INVPICKLIST") final MboRemote mbo, final String status, final Date asOfDate, final String memo, final long accessModifier)
    '''
def autoSplitRecordSet():
    '''    public MboSetRemote autoSplitRecordSet(@WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)
    '''
def getLineSplitRecords():
    '''    public MboSetRemote getLineSplitRecords(@WSMboSetQbe("INVBALANCES") final MboSetRemote invbalmsr, @WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)
    '''
def getLineSplitForRotItems():
    '''    public MboSetRemote getLineSplitForRotItems(@WSMboSetQbe("ASSET") final MboSetRemote assetmsr, @WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)
    '''
def addReservation():
    '''    public MboRemote addReservation(@WSMboSetQbe("INVRESERVE") final MboSetRemote msr, final String pl_num, final String siteid, final UserInfo userInfo, MXTransaction trans)
    '''
def setZeroNewPhysCnt():
    '''    public void setZeroNewPhysCnt(final long uniqueId, final boolean toRemove)
    '''
def isZeroNewPhysCnt():
    '''    public boolean isZeroNewPhysCnt(final long uniqueId)
    '''
