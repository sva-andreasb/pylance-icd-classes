WORKORDER = "String  \"WORKORDER\""
PMCOMTYPE = "String  \"PMCOMTYPE\""
WOSTATUS = "String  \"WOSTATUS\""
WORKORDERID = "String  \"WORKORDERID\""
PMCOMBPELINPROG = "String  \"PMCOMBPELINPROG\""
def ():
    '''returns PmComWOService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def notifyBPELStatus():
    '''returns None\n\n
    notifyBPELStatus(final String wonum, final String siteid, final String orgid, final String wostatus)\n
    '''
def startWorkOrder():
    '''returns None\n\n
    startWorkOrder(final String pwonum, final String psiteid, final String wonum, final String siteid, final String activityName)\n
    '''
