def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def async_set_compliance():
    '''returns boolean\n\n
    async_set_compliance(@MXEventParam("projectid") final String id, @MXEventParam("state") final boolean state)\n
    '''
def async_reforecast_pm():
    '''returns boolean\n\n
    async_reforecast_pm(@MXEventParam("projectid") final String currentProjectId)\n
    '''
def _cpmcreatelinks():
    '''returns JSONObject\n\n
    _cpmcreatelinks(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)\n
    '''
def _cpmall():
    '''returns JSONObject\n\n
    _cpmall(final WebClientSession sess)\n
    '''
def _cpmselected():
    '''returns JSONObject\n\n
    _cpmselected(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)\n
    '''
def _cpmfilter():
    '''returns JSONObject\n\n
    _cpmfilter(final WebClientSession sess, @MXEventParam("filteredByCriticalPath") final boolean filteredByCriticalPath)\n
    '''
def REFORECAST():
    '''returns JSONObject\n\n
    REFORECAST(final WebClientSession sess, final String actionid, final String params)\n
    '''
def validatePMsegment():
    '''returns None\n\n
    validatePMsegment(final WebClientSession sess, final JSONObject change, final ReplyBuilder reply, final MXGanttModel model, final MXActivity currentActivity)\n
    '''
def isRepairFacilityEnabled():
    '''returns boolean\n\n
    isRepairFacilityEnabled()\n
    '''
def setupBean():
    '''returns None\n\n
    setupBean(final WebClientSession wcs)\n
    '''
def _refreshSelected():
    '''returns JSONObject\n\n
    _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)\n
    '''
def _discardRefreshSelected():
    '''returns JSONObject\n\n
    _discardRefreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)\n
    '''
