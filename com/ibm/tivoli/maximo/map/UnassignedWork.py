def ():
    '''returns UnassignedWork\n\n
    ()\n
    '''
def refreshQueryUnassignedWork():
    '''returns JSONObject\n\n
    refreshQueryUnassignedWork(final WebClientSession clientSession, final MapControlAccessor map, final LatLngBounds bounds, final JSONObject params)\n
    '''
def queryUnassignedWork():
    '''returns JSONObject\n\n
    queryUnassignedWork(final WebClientSession clientSession, final MapControlAccessor map, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean defaultStatusFilter, final String extraClause, final boolean isRestrictWorkToDates, final Long projectID)\n
    queryUnassignedWork(final WebClientSession clientSession, final MapDataUtils.PROVIDER mapProvider, final LatLngBounds bounds, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean defaultStatusFilter, final String extraClause, final boolean isRestrictWorkToDates, final Long projectID)\n
    '''
def getUnassignedWhere():
    '''returns String\n\n
    getUnassignedWhere(final UserInfo userInfo, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean isSpatial, final boolean defaultStatusFilter, final String extraClause, final LatLngBounds bounds, final boolean isRestrictWorkToDates, final Long projectID)\n
    '''
def formatUWOWhere():
    '''returns String\n\n
    formatUWOWhere(final LatLngBounds bounds, final String where, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean addRegion)\n
    '''
def queryUnassignedWorkDispatcher():
    '''returns JSONObject\n\n
    queryUnassignedWorkDispatcher(final WebClientSession webClientSession, final MapControlAccessor mapControlAccessor, final MboRemote appMbo, final JSONObject queryData)\n
    '''
