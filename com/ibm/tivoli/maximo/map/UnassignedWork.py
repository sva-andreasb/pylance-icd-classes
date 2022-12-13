def UnassignedWork():
    '''    public UnassignedWork()
    '''
def refreshQueryUnassignedWork():
    '''    public JSONObject refreshQueryUnassignedWork(final WebClientSession clientSession, final MapControlAccessor map, final LatLngBounds bounds, final JSONObject params)
    '''
def queryUnassignedWork():
    '''    public JSONObject queryUnassignedWork(final WebClientSession clientSession, final MapControlAccessor map, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean defaultStatusFilter, final String extraClause, final boolean isRestrictWorkToDates, final Long projectID)
    public JSONObject queryUnassignedWork(final WebClientSession clientSession, final MapDataUtils.PROVIDER mapProvider, final LatLngBounds bounds, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean defaultStatusFilter, final String extraClause, final boolean isRestrictWorkToDates, final Long projectID)
    '''
def getUnassignedWhere():
    '''    public String getUnassignedWhere(final UserInfo userInfo, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean isSpatial, final boolean defaultStatusFilter, final String extraClause, final LatLngBounds bounds, final boolean isRestrictWorkToDates, final Long projectID)
    '''
def formatUWOWhere():
    '''    public String formatUWOWhere(final LatLngBounds bounds, final String where, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean addRegion)
    '''
def queryUnassignedWorkDispatcher():
    '''    public JSONObject queryUnassignedWorkDispatcher(final WebClientSession webClientSession, final MapControlAccessor mapControlAccessor, final MboRemote appMbo, final JSONObject queryData)
    '''
