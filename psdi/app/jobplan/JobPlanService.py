def ():
    '''returns JobPlanService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getValidJobPlansForOrgAndSite():
    '''returns MboSetRemote\n\n
    getValidJobPlansForOrgAndSite(final UserInfo userInfo, final String orgid, final String siteid)\n
    '''
def getMultiSiteJobPlan():
    '''returns MboSetRemote\n\n
    getMultiSiteJobPlan(final UserInfo userInfo, final String jpnum, final String orgid, final String siteid)\n
    getMultiSiteJobPlan(final UserInfo userInfo, final String jpnum, final String revisionNum, final String orgid, final String siteid)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("JOBPLAN") final JobPlanRemote jobplan, final String status, final Date date, final String memo)\n
    '''
