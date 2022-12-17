def ():
    '''returns InventoryService\n\n
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
def setAdjustmentType():
    '''returns None\n\n
    setAdjustmentType(final int type, final MboRemote invAdjust)\n
    '''
def getItemsInStore():
    '''returns MboSetRemote\n\n
    getItemsInStore(final UserInfo userInfo, final String storeroom)\n
    '''
def createIssue():
    '''returns MboRemote\n\n
    createIssue(final UserInfo userInfo, final MboSetRemote issueSet, final String itemnum, final String location, final String siteid, final String ownersysid1)\n
    createIssue(final UserInfo userInfo, final String itemnum, final String location, final String siteid, final String bin, final String lot, final String rotasset, final double qty)\n
    '''
def getItemSetIdFromSite():
    '''returns String\n\n
    getItemSetIdFromSite(final UserInfo userInfo, final String siteid)\n
    '''
def createMiscReceipt():
    '''returns MboRemote\n\n
    createMiscReceipt(final UserInfo userInfo, final MboSetRemote existingReceiptSet, final String itemnum, final String toStoreLoc, final String siteid, final String ownersysid)\n
    '''
def getCurrentBalance():
    '''returns double\n\n
    getCurrentBalance(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String binnum, final String lotnum)\n
    '''
def getBalances():
    '''returns MboSetRemote\n\n
    getBalances(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String siteid)\n
    '''
def getBalancesForInventorySet():
    '''returns MboSetRemote\n\n
    getBalancesForInventorySet(final MboSetRemote inventorySet)\n
    '''
def getUnauthInvSet():
    '''returns Vector\n\n
    getUnauthInvSet()\n
    '''
def canGoNegative():
    '''returns None\n\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location, final String siteid)\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location)\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final double totalAvailable, final MboRemote sourceMbo)\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final String itemnum, final String itemsetid, final String location, final String binnum, final String lotnum, final String siteid)\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo)\n
    canGoNegative(final UserInfo userInfo, final double toBeIssued, final double curbal, final double totalAvailable, final MboRemote sourceMbo, final String costType)\n
    '''
def isSameStoreroomTransfer():
    '''returns boolean\n\n
    isSameStoreroomTransfer(final MboRemote sourceMbo)\n
    '''
def findItemsForPhysCount():
    '''returns MboSetRemote\n\n
    findItemsForPhysCount(final UserInfo userInfo, final String location)\n
    '''
def getBins():
    '''returns MboSetRemote\n\n
    getBins(final UserInfo userInfo, final String location, final String binnum)\n
    '''
def getLots():
    '''returns MboSetRemote\n\n
    getLots(final UserInfo userInfo, final String itemnum, final String itemsetid, final String location, final String binnum)\n
    '''
def getReservationsForWO():
    '''returns MboSetRemote\n\n
    getReservationsForWO(final UserInfo userInfo, final String wonum)\n
    '''
def getReservationsForMR():
    '''returns MboSetRemote\n\n
    getReservationsForMR(final UserInfo userInfo, final String mrnum)\n
    '''
def isWOValid():
    '''returns MboRemote\n\n
    isWOValid(final UserInfo userInfo, final String wonum)\n
    '''
def isMRValid():
    '''returns None\n\n
    isMRValid(final UserInfo userInfo, final String mrnum)\n
    '''
def getMatReceiptSet():
    '''returns MboSetRemote\n\n
    getMatReceiptSet(final UserInfo ui, final String ponum)\n
    '''
def validateBinLot():
    '''returns None\n\n
    validateBinLot(final Inventory inv, final String binnum, final String lotnum)\n
    '''
def validateInventory():
    '''returns MboRemote\n\n
    validateInventory(final UserInfo userInfo, final String item, final String itemsetid, final String location)\n
    '''
def isCourierOrLabor():
    '''returns boolean\n\n
    isCourierOrLabor(final UserInfo userInfo, final String location)\n
    '''
def getDefaultLotNum():
    '''returns String\n\n
    getDefaultLotNum(final MboRemote mbo)\n
    '''
def getConversionFactor():
    '''returns double\n\n
    getConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID, final String itemNum)\n
    getConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID)\n
    '''
def getUnitConversionFactor():
    '''returns String\n\n
    getUnitConversionFactor(final UserInfo userInfo, final String fromUOM, final String toUOM, final String itemSetID, final String itemNum)\n
    '''
def adjustCurrentBalance():
    '''returns None\n\n
    adjustCurrentBalance(@WSMboKey("INVBALANCES") final MboRemote invBalances, final String newBalance, final double stdcost, final double avgcost, final String conditioncode)\n
    '''
def getConversionFactorToStoreroom():
    '''returns MboRemote\n\n
    getConversionFactorToStoreroom(@WSMboKey("TRANSFERCURITEM") final MboRemote mbo, final String tostoreloc, final String tositeid)\n
    '''
def createInvbalances():
    '''returns None\n\n
    createInvbalances(@WSMboKey("INVENTORY") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String binnum, final String lotnum, final String conditioncode, final String itemsetid, final String curbal, final UserInfo userInfo)\n
    '''
def adjustPhysicalCount():
    '''returns None\n\n
    adjustPhysicalCount(@WSMboKey("INVBALANCES") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String binnum, final String lotnum, final String itemsetid, final double physcnt, final UserInfo userInfo)\n
    '''
def previewReconcile():
    '''returns None\n\n
    previewReconcile(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo)\n
    '''
def reconcile():
    '''returns MboSetRemote\n\n
    reconcile(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo)\n
    '''
def createReturnForIssueStoreloc():
    '''returns MboRemote\n\n
    createReturnForIssueStoreloc(@WSMboKey("MAUSETRANS") final MboRemote issueMbo)\n
    '''
def updateInventory():
    '''returns MboRemote\n\n
    updateInventory(@WSMboKey("INVBALANCES") final MboRemote invMbo, final String itemnum, final String location, final String siteid, final String itemsetid, final UserInfo userInfo)\n
    '''
def getStoreroom():
    '''returns MboRemote\n\n
    getStoreroom(final UserInfo userInfo, final String location, final String siteid)\n
    '''
def updateAllInventory():
    '''returns MboSetRemote\n\n
    updateAllInventory(@WSMboSetQbe("INVBALANCES") final MboSetRemote invBalSetMbo, final UserInfo userInfo)\n
    '''
def createIssueForNonStock():
    '''returns MboRemote\n\n
    createIssueForNonStock(final UserInfo userInfo, MboSetRemote issueSet, final String itemnum, final String itemsetid, final String location, final String siteid, final String ownersysid1)\n
    '''
def createPickList():
    '''returns MboRemote\n\n
    createPickList(@WSMboSetQbe("INVRESERVE") final MboSetRemote msr, final String pldescription, final String plnum, final Date reqdate, final String storeroom, final String siteid, final UserInfo userInfo, MXTransaction trans)\n
    '''
def updateInvUseLines():
    '''returns None\n\n
    updateInvUseLines(final MboSetRemote msr, final String plnum, final MXTransaction trans)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("INVPICKLIST") final MboRemote mbo, final String status, final Date asOfDate, final String memo, final long accessModifier)\n
    '''
def autoSplitRecordSet():
    '''returns MboSetRemote\n\n
    autoSplitRecordSet(@WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)\n
    '''
def getLineSplitRecords():
    '''returns MboSetRemote\n\n
    getLineSplitRecords(@WSMboSetQbe("INVBALANCES") final MboSetRemote invbalmsr, @WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)\n
    '''
def getLineSplitForRotItems():
    '''returns MboSetRemote\n\n
    getLineSplitForRotItems(@WSMboSetQbe("ASSET") final MboSetRemote assetmsr, @WSMboKey("INVUSELINE") final MboRemote invUseLineMbo, final UserInfo userInfo)\n
    '''
def addReservation():
    '''returns MboRemote\n\n
    addReservation(@WSMboSetQbe("INVRESERVE") final MboSetRemote msr, final String pl_num, final String siteid, final UserInfo userInfo, MXTransaction trans)\n
    '''
def setZeroNewPhysCnt():
    '''returns None\n\n
    setZeroNewPhysCnt(final long uniqueId, final boolean toRemove)\n
    '''
def isZeroNewPhysCnt():
    '''returns boolean\n\n
    isZeroNewPhysCnt(final long uniqueId)\n
    '''
