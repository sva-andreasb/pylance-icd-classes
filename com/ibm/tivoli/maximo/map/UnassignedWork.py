def UnassignedWork():
'''public UnassignedWork()
'''
pass
def refreshQueryUnassignedWork():
'''public JSONObject refreshQueryUnassignedWork(final WebClientSession clientSession, final MapControlAccessor map, final LatLngBounds bounds, final JSONObject params)
'''
pass
def queryUnassignedWork():
'''public JSONObject queryUnassignedWork(final WebClientSession clientSession, final MapControlAccessor map, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean defaultStatusFilter, final String extraClause, final boolean isRestrictWorkToDates, final Long projectID)
public JSONObject queryUnassignedWork(final WebClientSession clientSession, final MapDataUtils.PROVIDER mapProvider, final LatLngBounds bounds, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean defaultStatusFilter, final String extraClause, final boolean isRestrictWorkToDates, final Long projectID)
'''
pass
def getUnassignedWhere():
'''public String getUnassignedWhere(final UserInfo userInfo, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean isSpatial, final boolean defaultStatusFilter, final String extraClause, final LatLngBounds bounds, final boolean isRestrictWorkToDates, final Long projectID)
'''
pass
def formatUWOWhere():
'''public String formatUWOWhere(final LatLngBounds bounds, final String where, final Date schedStart, final Date schedFinish, final Date targetStart, final Date targetFinish, final String status, final String workType, final Integer priority, final boolean addRegion)
'''
pass
def queryUnassignedWorkDispatcher():
'''public JSONObject queryUnassignedWorkDispatcher(final WebClientSession webClientSession, final MapControlAccessor mapControlAccessor, final MboRemote appMbo, final JSONObject queryData)
'''
pass
