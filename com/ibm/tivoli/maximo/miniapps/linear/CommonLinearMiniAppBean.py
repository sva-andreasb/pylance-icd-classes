LINEARASSET_MSG_GROUP = "String  \"linearasset\""
def getDataListener():
    '''returns DataBeanListener\n\n
    getDataListener()\n
    '''
def updateFromToMeasure():
    '''returns String\n\n
    updateFromToMeasure()\n
    '''
def label():
    '''returns String\n\n
    label(final String key)\n
    label(final String key, final String group)\n
    '''
def getBaseImageUrl():
    '''returns String\n\n
    getBaseImageUrl()\n
    '''
def getLinearUrl():
    '''returns String\n\n
    getLinearUrl(final String miniAppsDir)\n
    '''
def filterCss():
    '''returns String\n\n
    filterCss(final String css, final MiniAppControl control)\n
    '''
def send_client_treegrid_refresh():
    '''returns None\n\n
    send_client_treegrid_refresh(final String data)\n
    '''
def send_client_treegrid_from_to_measure():
    '''returns None\n\n
    send_client_treegrid_from_to_measure()\n
    '''
def send_client_treegrid_reset():
    '''returns None\n\n
    send_client_treegrid_reset()\n
    '''
def send_client_remove_treegrid():
    '''returns None\n\n
    send_client_remove_treegrid()\n
    '''
def send_client_visibility_grid():
    '''returns None\n\n
    send_client_visibility_grid(final String data)\n
    '''
def sendEventToTreeGrid():
    '''returns None\n\n
    sendEventToTreeGrid(final String eventId, final String eventArg)\n
    '''
def get_calculatedMeasure():
    '''returns JSONObject\n\n
    get_calculatedMeasure(final WebClientSession wcs, @MXEventParam("linearObjTargetInfo") final JSONObject linearObjTargetInfo)\n
    '''
def isMboLinkedToFeatureClass():
    '''returns JSONObject\n\n
    isMboLinkedToFeatureClass(final WebClientSession wcs)\n
    '''
def get_i18n_MaxMsg_label():
    '''returns JSONObject\n\n
    get_i18n_MaxMsg_label(@MXEventParam("msgKey") final String msgKey, @MXEventParam("msgGroup") final String msgGroup)\n
    '''
def return_mapProvider_type():
    '''returns JSONObject\n\n
    return_mapProvider_type(final WebClientSession sess)\n
    '''
def getCurrentMapProvider():
    '''returns String\n\n
    getCurrentMapProvider(final UserInfo userInfo)\n
    '''
