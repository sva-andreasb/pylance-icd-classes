def PlusPBillService():
    '''public PlusPBillService()
    public PlusPBillService(final MXServer mxServer)
    '''
def updateBillBatchStatus():
    '''public PlusPBillBatchRemote updateBillBatchStatus(@WSMboKey("PLUSPBILLBATCH") final PlusPBillBatchRemote plusPBillBatchRemote, final String s, final String[] array, final boolean b)
    '''
def approveBillLines():
    '''public PlusPBillBatchRemote approveBillLines(@WSMboKey("PLUSPBILLBATCH") final PlusPBillBatchRemote plusPBillBatchRemote, final String s)
    '''
def setLastWhereForGroupBy():
    '''public PlusPBillBatchRemote setLastWhereForGroupBy(final PlusPBillBatchRemote plusPBillBatchRemote, final String anObject, final String val)
    '''
def addCopyThread():
    '''public void addCopyThread(final long l, final ExecutorService value)
    '''
def stopCopyThread():
    '''public void stopCopyThread(final long l, final String value)
    '''
def getResetRequestedBy():
    '''public String getResetRequestedBy(final long l)
    '''
def finishBackgroundCopy():
    '''public ExecutorService finishBackgroundCopy(final long l)
    '''
def warnIfValueInBatchGrouped():
    '''public void warnIfValueInBatchGrouped(final MboValue mboValue, final String anObject)
    '''
def billedPriceAdjustment():
    '''public double billedPriceAdjustment(final double n, final double n2)
    '''
def agreementHasOpenBB():
    '''public static boolean agreementHasOpenBB(final String val, final String val2, final UserInfo user)
    '''
def changeMboReadOnlyByAllFieldsReadOnly():
    '''public static void changeMboReadOnlyByAllFieldsReadOnly(final MboRemote mboRemote)
    '''
def validateOrdersListToCreateBillBatch():
    '''public void validateOrdersListToCreateBillBatch(final MboSetRemote mboSetRemote)
    '''
def validateOrderToCreateBillBatch():
    '''public void validateOrderToCreateBillBatch(final MboRemote mboRemote)
    '''
def changeStatus():
    '''public void changeStatus(@WSMboKey("PLUSPBILLBATCH") final PlusPBillBatchRemote plusPBillBatchRemote, final String s, final Date date, final String s2)
    '''
