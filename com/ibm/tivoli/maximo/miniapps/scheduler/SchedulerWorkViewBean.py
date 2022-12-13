def initialize():
    '''public void initialize()
    '''
def async_set_compliance():
    '''public boolean async_set_compliance(@MXEventParam("projectid") final String id, @MXEventParam("state") final boolean state)
    '''
def async_reforecast_pm():
    '''public boolean async_reforecast_pm(@MXEventParam("projectid") final String currentProjectId)
    '''
def _cpmcreatelinks():
    '''public JSONObject _cpmcreatelinks(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)
    '''
def _cpmall():
    '''public JSONObject _cpmall(final WebClientSession sess)
    '''
def _cpmselected():
    '''public JSONObject _cpmselected(final WebClientSession sess, @MXEventParam("ids") final String ids, final String values)
    '''
def _cpmfilter():
    '''public JSONObject _cpmfilter(final WebClientSession sess, @MXEventParam("filteredByCriticalPath") final boolean filteredByCriticalPath)
    '''
def REFORECAST():
    '''public JSONObject REFORECAST(final WebClientSession sess, final String actionid, final String params)
    '''
def validatePMsegment():
    '''public void validatePMsegment(final WebClientSession sess, final JSONObject change, final ReplyBuilder reply, final MXGanttModel model, final MXActivity currentActivity)
    '''
def isRepairFacilityEnabled():
    '''public boolean isRepairFacilityEnabled()
    '''
def setupBean():
    '''public void setupBean(final WebClientSession wcs)
    '''
def _refreshSelected():
    '''public JSONObject _refreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)
    '''
def _discardRefreshSelected():
    '''public JSONObject _discardRefreshSelected(final WebClientSession sess, @MXEventParam("ids") final String ids)
    '''
