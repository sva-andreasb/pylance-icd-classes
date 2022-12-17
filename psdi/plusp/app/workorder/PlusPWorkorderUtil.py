LABTRANS = "String  \"LABTRANS\""
MATUSETRANS = "String  \"MATUSETRANS\""
SERVRECTRANS = "String  \"SERVRECTRANS\""
TOOLTRANS = "String  \"TOOLTRANS\""
PLUSPGBTRANS = "String  \"PLUSPGBTRANS\""
LABTRANSID = "String  \"LABTRANSID\""
MATUSETRANSID = "String  \"MATUSETRANSID\""
SERVRECTRANSID = "String  \"SERVRECTRANSID\""
TOOLTRANSID = "String  \"TOOLTRANSID\""
PLUSPGBTRANSID = "String  \"PLUSPGBTRANSID\""
SERVICES = "String  \"SERVICES\""
def isBillBatchWarned():
    '''returns boolean\n\n
    isBillBatchWarned()\n
    '''
def setBillBatchWarned():
    '''returns None\n\n
    setBillBatchWarned(final boolean billBatchWarned)\n
    '''
def isToRemoveAgreement():
    '''returns boolean\n\n
    isToRemoveAgreement()\n
    '''
def setToRemoveAgreement():
    '''returns None\n\n
    setToRemoveAgreement(final boolean toRemoveAgreement)\n
    '''
def setUserInputWarnAssociatedWithBillBatch():
    '''returns None\n\n
    setUserInputWarnAssociatedWithBillBatch(final Object userInputWarnAssociatedWithBillBatch)\n
    '''
def getPluspServRecTrans():
    '''returns MboRemote\n\n
    getPluspServRecTrans()\n
    '''
def setPluspServRecTrans():
    '''returns None\n\n
    setPluspServRecTrans(final MboRemote pluspServRecTransOwner)\n
    '''
def ():
    '''returns PlusPWorkorderUtil\n\n
    (final Mbo mbo)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def save():
    '''returns None\n\n
    save(final String s)\n
    '''
def canAddEditFeesCharges():
    '''returns boolean\n\n
    canAddEditFeesCharges()\n
    '''
def getPriceTotals():
    '''returns MboRemote\n\n
    getPriceTotals()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def recalculatePrices():
    '''returns None\n\n
    recalculatePrices(final MboRemote mboRemote)\n
    '''
def canPropagateKey():
    '''returns boolean\n\n
    canPropagateKey()\n
    '''
def warnAssociatedWithBillBatch():
    '''returns boolean\n\n
    warnAssociatedWithBillBatch(final String ek)\n
    '''
def copyPlanFeeChargeToGBTransSet():
    '''returns None\n\n
    copyPlanFeeChargeToGBTransSet(final MboSetRemote mboSetRemote)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long n)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def calculateTotals():
    '''returns None\n\n
    calculateTotals(final MboRemote mboRemote, final boolean b)\n
    '''
def initQuote():
    '''returns None\n\n
    initQuote()\n
    initQuote(final String quoteRelatedFieldFlags)\n
    '''
def copyQuoteFields():
    '''returns None\n\n
    copyQuoteFields()\n
    copyQuoteFields(final String str)\n
    '''
def setModifyPSFlags():
    '''returns None\n\n
    setModifyPSFlags()\n
    '''
def removePS():
    '''returns boolean\n\n
    removePS(final String s, final String s2)\n
    '''
def getCurrentBillLines():
    '''returns MboSetRemote\n\n
    getCurrentBillLines()\n
    '''
def duplicateExtraMbos():
    '''returns None\n\n
    duplicateExtraMbos(final MboRemote mboRemote)\n
    '''
def applyWOQuote():
    '''returns None\n\n
    applyWOQuote(final MboRemote mboRemote)\n
    applyWOQuote(final MboRemote mboRemote, final String s)\n
    '''
def applyWOQuoteTotals():
    '''returns None\n\n
    applyWOQuoteTotals(final MboRemote mboRemote)\n
    '''
def applyWOMinimum():
    '''returns None\n\n
    applyWOMinimum(final MboRemote mboRemote)\n
    '''
def applyWOInclude():
    '''returns None\n\n
    applyWOInclude(final MboRemote mboRemote)\n
    '''
def getSumMboSet():
    '''returns double\n\n
    getSumMboSet(final MboSetRemote mboSetRemote, final String s, final boolean b)\n
    '''
def populateToBeBilledTr():
    '''returns None\n\n
    populateToBeBilledTr(final MboRemote mboRemote)\n
    '''
def addToBeBilled():
    '''returns None\n\n
    addToBeBilled(final MboRemote mboRemote)\n
    '''
def addToBeBilledTr():
    '''returns None\n\n
    addToBeBilledTr(final MboRemote mboRemote, final String val, final MboRemote mboRemote2)\n
    '''
def deleteToBeBilledAndTr():
    '''returns None\n\n
    deleteToBeBilledAndTr(final MboRemote mboRemote)\n
    '''
def undeleteToBeBilledAndTr():
    '''returns None\n\n
    undeleteToBeBilledAndTr(final MboRemote mboRemote)\n
    '''
def isWoInAnyBillBatch():
    '''returns boolean\n\n
    isWoInAnyBillBatch()\n
    '''
def addBillLineTr():
    '''returns None\n\n
    addBillLineTr(final MboRemote mboRemote, final MboRemote mboRemote2)\n
    '''
def createTransactions():
    '''returns None\n\n
    createTransactions(final MboRemote mboRemote, final String s, final MboRemote mboRemote2)\n
    '''
def copyIntServItemsToServRecTransSet():
    '''returns None\n\n
    copyIntServItemsToServRecTransSet(final MboSetRemote mboSetRemote)\n
    '''
def copyPlanIntServItemsToServRecTransSet():
    '''returns None\n\n
    copyPlanIntServItemsToServRecTransSet(final MboSetRemote mboSetRemote)\n
    '''
def updateServicesListPrice():
    '''returns None\n\n
    updateServicesListPrice()\n
    '''
def validateObjectChangeForServices():
    '''returns None\n\n
    validateObjectChangeForServices()\n
    '''
def hasHoldBillLines():
    '''returns MboSetRemote\n\n
    hasHoldBillLines()\n
    '''
def openMultiplePriceEstimatesDialog():
    '''returns boolean\n\n
    openMultiplePriceEstimatesDialog()\n
    '''
def isStatusValidForCustomerPriceEstimate():
    '''returns boolean\n\n
    isStatusValidForCustomerPriceEstimate()\n
    '''
def getValidStatusToCreateBill():
    '''returns HashSet<String>\n\n
    getValidStatusToCreateBill()\n
    '''
def validateOpenBillBatch():
    '''returns int\n\n
    validateOpenBillBatch()\n
    '''
