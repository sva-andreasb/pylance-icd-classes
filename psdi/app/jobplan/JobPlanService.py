def JobPlanService():
    '''    public JobPlanService()
    public JobPlanService(final MXServer mxServer)
    '''
def getValidJobPlansForOrgAndSite():
    '''    public MboSetRemote getValidJobPlansForOrgAndSite(final UserInfo userInfo, final String orgid, final String siteid)
    '''
def getMultiSiteJobPlan():
    '''    public MboSetRemote getMultiSiteJobPlan(final UserInfo userInfo, final String jpnum, final String orgid, final String siteid)
    public MboSetRemote getMultiSiteJobPlan(final UserInfo userInfo, final String jpnum, final String revisionNum, final String orgid, final String siteid)
    '''
def changeStatus():
    '''    public void changeStatus(@WSMboKey("JOBPLAN") final JobPlanRemote jobplan, final String status, final Date date, final String memo)
    '''
