def ():
    '''returns AsyncProcess\n\n
    (final MboServerInterface ms)\n
    (final Enumeration enums, final UserInfo ui, final Mbo param, final String notifyEmail)\n
    (final MboSetRemote mboset, final Mbo param, final String notifyEmail)\n
    '''
def execute():
    '''returns None\n\n
    execute(final MboRemote mbo)\n
    '''
def createCompletionOrder():
    '''returns Vector<String>\n\n
    createCompletionOrder(Vector<String> completionorder, final String nextWO, final Hashtable htChildren, final Hashtable htTasks)\n
    '''
def setLatestPMDueDate():
    '''returns None\n\n
    setLatestPMDueDate(final String pmnum, final String siteid, final Date dueDate)\n
    '''
def getLatestPMDueDate():
    '''returns Date\n\n
    getLatestPMDueDate(final String pmnum, final String siteid)\n
    '''
def setPMWOCancelUserListResponse():
    '''returns None\n\n
    setPMWOCancelUserListResponse(final boolean response)\n
    '''
def setReportParameterData():
    '''returns None\n\n
    setReportParameterData(final ReportParameterData data)\n
    '''
def createFileFromStream():
    '''returns None\n\n
    createFileFromStream(final File file, final InputStream inputStream)\n
    '''
def setFailedWOChangeStatusRecord():
    '''returns None\n\n
    setFailedWOChangeStatusRecord(final long workorderid)\n
    '''
def getFailedWOChangeStatusRecord():
    '''returns ArrayList<Long>\n\n
    getFailedWOChangeStatusRecord()\n
    '''
def clearFailedWOChangeStatusRecord():
    '''returns None\n\n
    clearFailedWOChangeStatusRecord()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
