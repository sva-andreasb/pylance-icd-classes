def ():
    '''returns ReceiptInputSet\n\n
    (final MboServerInterface ms)\n
    '''
def setStorelocString():
    '''returns None\n\n
    setStorelocString(final String storeLoc)\n
    '''
def setup():
    '''returns MboRemote\n\n
    setup()\n
    '''
def setupShipmentReceipt():
    '''returns None\n\n
    setupShipmentReceipt(final ShipmentRemote owningShipment)\n
    '''
def createReceiptsForReturnPrepSrv():
    '''returns None\n\n
    createReceiptsForReturnPrepSrv(final MboRemote po)\n
    '''
def getShipmentLineSet():
    '''returns MboSetRemote\n\n
    getShipmentLineSet(final MboRemote shipmentRemote)\n
    '''
def getPOLineSet():
    '''returns MboSetRemote\n\n
    getPOLineSet(final MboRemote poRemote)\n
    '''
def setRelationshipStringFromPO():
    '''returns None\n\n
    setRelationshipStringFromPO(final String relationship)\n
    '''
def getRelationshipStringFromPO():
    '''returns String\n\n
    getRelationshipStringFromPO()\n
    '''
def createReceiptsForReturnPrep():
    '''returns None\n\n
    createReceiptsForReturnPrep(final MboRemote po)\n
    '''
def createShipmentReceiptsForReturnPrep():
    '''returns None\n\n
    createShipmentReceiptsForReturnPrep(final MboRemote shipment)\n
    '''
def setShipmentReturnVariablesPrep():
    '''returns None\n\n
    setShipmentReturnVariablesPrep(final MboRemote matRecRemote, final MboRemote receiptInputRemote)\n
    '''
def createServReceiptsPrep():
    '''returns None\n\n
    createServReceiptsPrep(final MboSetRemote poLineSet, final MboRemote po)\n
    '''
def createReturnsForAssets():
    '''returns None\n\n
    createReturnsForAssets(final MboSetRemote poLineSet, final MboRemote po)\n
    '''
def diHasFinancialTransactions():
    '''returns boolean\n\n
    diHasFinancialTransactions(final MatRecTrans mrt, final Asset asset)\n
    '''
def createMatReceiptsPrep():
    '''returns None\n\n
    createMatReceiptsPrep(final MboSetRemote poLineSet, final MboRemote po)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def generateServiceReturnReceipts():
    '''returns None\n\n
    generateServiceReturnReceipts(final MboSetRemote servRecTransSetRemote)\n
    '''
def generateReceipts():
    '''returns boolean\n\n
    generateReceipts(final MboSetRemote targetMbos)\n
    '''
def generateReturnReceipts():
    '''returns None\n\n
    generateReturnReceipts(final MboSetRemote targetMboSet)\n
    '''
def getInvAdjLifoFifo():
    '''returns double\n\n
    getInvAdjLifoFifo(final MboRemote inv, final long receiptId)\n
    '''
