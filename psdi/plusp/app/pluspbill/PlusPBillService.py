def ():
    '''returns PlusPBillService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def updateBillBatchStatus():
    '''returns PlusPBillBatchRemote\n\n
    updateBillBatchStatus(@WSMboKey("PLUSPBILLBATCH") final PlusPBillBatchRemote plusPBillBatchRemote, final String s, final String[] array, final boolean b)\n
    '''
def approveBillLines():
    '''returns PlusPBillBatchRemote\n\n
    approveBillLines(@WSMboKey("PLUSPBILLBATCH") final PlusPBillBatchRemote plusPBillBatchRemote, final String s)\n
    '''
def setLastWhereForGroupBy():
    '''returns PlusPBillBatchRemote\n\n
    setLastWhereForGroupBy(final PlusPBillBatchRemote plusPBillBatchRemote, final String anObject, final String val)\n
    '''
def addCopyThread():
    '''returns None\n\n
    addCopyThread(final long l, final ExecutorService value)\n
    '''
def stopCopyThread():
    '''returns None\n\n
    stopCopyThread(final long l, final String value)\n
    '''
def getResetRequestedBy():
    '''returns String\n\n
    getResetRequestedBy(final long l)\n
    '''
def finishBackgroundCopy():
    '''returns ExecutorService\n\n
    finishBackgroundCopy(final long l)\n
    '''
def warnIfValueInBatchGrouped():
    '''returns None\n\n
    warnIfValueInBatchGrouped(final MboValue mboValue, final String anObject)\n
    '''
def billedPriceAdjustment():
    '''returns double\n\n
    billedPriceAdjustment(final double n, final double n2)\n
    '''
def validateOrdersListToCreateBillBatch():
    '''returns None\n\n
    validateOrdersListToCreateBillBatch(final MboSetRemote mboSetRemote)\n
    '''
def validateOrderToCreateBillBatch():
    '''returns None\n\n
    validateOrderToCreateBillBatch(final MboRemote mboRemote)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("PLUSPBILLBATCH") final PlusPBillBatchRemote plusPBillBatchRemote, final String s, final Date date, final String s2)\n
    '''
