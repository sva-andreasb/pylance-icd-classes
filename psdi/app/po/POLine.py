def ():
    '''returns POLine\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def isInspectionRequired():
    '''returns boolean\n\n
    isInspectionRequired()\n
    '''
def updatePOPOLine():
    '''returns None\n\n
    updatePOPOLine(final double receivedQty, final double rejectedQty, final double receivedTotalCost, final MboRemote po, double conversion)\n
    updatePOPOLine(final double receivedQty, final double rejectedQty, final double receivedTotalCost, final MboRemote po)\n
    updatePOPOLine(final double receivedQty, final double rejectedQty, final double receivedTotalCost, final MboRemote po, final double conversion, final boolean fromMeaUsingUpdateReceipt)\n
    '''
def receiptComplete():
    '''returns None\n\n
    receiptComplete()\n
    '''
def updateWOAssetOnReceipt():
    '''returns None\n\n
    updateWOAssetOnReceipt(final double cost)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessmodifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def checkPOCostValidity():
    '''returns None\n\n
    checkPOCostValidity()\n
    '''
def isServicePOLineByCost():
    '''returns boolean\n\n
    isServicePOLineByCost()\n
    '''
def doPOLineReceiptsExist():
    '''returns boolean\n\n
    doPOLineReceiptsExist()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def updateCost1s():
    '''returns None\n\n
    updateCost1s()\n
    '''
def updateInvVendor():
    '''returns MboRemote\n\n
    updateInvVendor()\n
    '''
def generateWO():
    '''returns None\n\n
    generateWO()\n
    '''
def afterAdd():
    '''returns None\n\n
    afterAdd()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def canDistribute():
    '''returns None\n\n
    canDistribute()\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy(final MboSetRemote mboset)\n
    '''
def propagateKeyValue():
    '''returns None\n\n
    propagateKeyValue(final String keyName, final String keyValue)\n
    '''
def calculateUnInvoicedQtyCost():
    '''returns double[]\n\n
    calculateUnInvoicedQtyCost()\n
    '''
def setVendorItem():
    '''returns None\n\n
    setVendorItem(final boolean value)\n
    '''
def getVendorItem():
    '''returns boolean\n\n
    getVendorItem()\n
    '''
def getInternalLineType():
    '''returns String\n\n
    getInternalLineType()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def isServiceType():
    '''returns boolean\n\n
    isServiceType()\n
    '''
def canCancelIfScheduleInvoice():
    '''returns None\n\n
    canCancelIfScheduleInvoice()\n
    '''
def cancelScheduleInvoice():
    '''returns None\n\n
    cancelScheduleInvoice()\n
    '''
def deleteReservation():
    '''returns None\n\n
    deleteReservation()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def getInternalRevStatus():
    '''returns String\n\n
    getInternalRevStatus()\n
    '''
def checkInvUseStatus():
    '''returns None\n\n
    checkInvUseStatus()\n
    '''
def setConsignmentFlags():
    '''returns None\n\n
    setConsignmentFlags()\n
    '''
def setReceiptQtyAndCostInfo():
    '''returns None\n\n
    setReceiptQtyAndCostInfo(final double receivedQty, final double rejectedQty, final double receivedTotalCost, final MboRemote po)\n
    '''
def getQtyAndCostsFromReceipt():
    '''returns double[]\n\n
    getQtyAndCostsFromReceipt()\n
    '''
def getPOFromReceipt():
    '''returns MboRemote\n\n
    getPOFromReceipt()\n
    '''
def isPOLineReceived():
    '''returns boolean\n\n
    isPOLineReceived()\n
    '''
def checkPOLineReceipts():
    '''returns None\n\n
    checkPOLineReceipts(final int source)\n
    '''
