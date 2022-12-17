def ():
    '''returns JobPlanSet\n\n
    (final MboServerInterface ms)\n
    '''
def setJpLocation():
    '''returns None\n\n
    setJpLocation(final String location)\n
    '''
def getJpLocation():
    '''returns String\n\n
    getJpLocation()\n
    '''
def setJpAsset():
    '''returns None\n\n
    setJpAsset(final String assetnum)\n
    '''
def getJpAsset():
    '''returns String\n\n
    getJpAsset()\n
    '''
def setJpItem():
    '''returns None\n\n
    setJpItem(final String itemnum, final String itemsetid)\n
    '''
def getJpItem():
    '''returns String\n\n
    getJpItem()\n
    '''
def getJpItemSetID():
    '''returns String\n\n
    getJpItemSetID()\n
    '''
def clearUserPref():
    '''returns None\n\n
    clearUserPref()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
    '''
def getValidJobPlansForOrgAndSite():
    '''returns None\n\n
    getValidJobPlansForOrgAndSite(String orgid, String siteid)\n
    '''
def getValidJobPlansForTaskGivenOrgAndSite():
    '''returns None\n\n
    getValidJobPlansForTaskGivenOrgAndSite(final String orgid, final String siteid, final String status, final Integer jobplanid)\n
    getValidJobPlansForTaskGivenOrgAndSite(String orgid, String siteid, final String status, final Long jobplanid)\n
    '''
def getMultiSiteJobPlan():
    '''returns None\n\n
    getMultiSiteJobPlan(String jpnum, String orgid, String siteid)\n
    getMultiSiteJobPlan(String jpnum, final String revisionNum, String orgid, String siteid)\n
    '''
