def getClientEventCtrl():
    '''returns MapControlClientEvent\n\n
    getClientEventCtrl()\n
    '''
def ():
    '''returns MapControl\n\n
    ()\n
    '''
def getWidth():
    '''returns String\n\n
    getWidth()\n
    '''
def isContextPersistent():
    '''returns Boolean\n\n
    isContextPersistent()\n
    '''
def isZoomToDataInput():
    '''returns Boolean\n\n
    isZoomToDataInput()\n
    '''
def isDataSourceDynamic():
    '''returns Boolean\n\n
    isDataSourceDynamic()\n
    '''
def getZoomLevel():
    '''returns String\n\n
    getZoomLevel()\n
    '''
def getFullExtZoomLevel():
    '''returns String\n\n
    getFullExtZoomLevel()\n
    '''
def isMapViewOnly():
    '''returns Boolean\n\n
    isMapViewOnly()\n
    '''
def getInitialX():
    '''returns Double\n\n
    getInitialX()\n
    '''
def getInitialY():
    '''returns Double\n\n
    getInitialY()\n
    '''
def getFullX():
    '''returns Double\n\n
    getFullX()\n
    '''
def getFullY():
    '''returns Double\n\n
    getFullY()\n
    '''
def isMobile():
    '''returns boolean\n\n
    isMobile()\n
    '''
def getHeight():
    '''returns String\n\n
    getHeight()\n
    '''
def getRefreshMapInterval():
    '''returns String\n\n
    getRefreshMapInterval()\n
    '''
def getRouteConfiguration():
    '''returns JSONObject\n\n
    getRouteConfiguration()\n
    '''
def getMapConfiguration():
    '''returns JSONObject\n\n
    getMapConfiguration()\n
    '''
def getPrintTimeout():
    '''returns int\n\n
    getPrintTimeout()\n
    '''
def loadToolsConfiguration():
    '''returns JSONObject\n\n
    loadToolsConfiguration()\n
    '''
def loadGISMapConfiguration():
    '''returns None\n\n
    loadGISMapConfiguration()\n
    '''
def getGoogleMapConfiguration():
    '''returns JSONObject\n\n
    getGoogleMapConfiguration(final MboRemote mbo)\n
    '''
def getBingMapConfiguration():
    '''returns JSONObject\n\n
    getBingMapConfiguration(final MboRemote mbo)\n
    '''
def getSpatialMapConfiguration():
    '''returns JSONObject\n\n
    getSpatialMapConfiguration(final MboRemote mbo)\n
    '''
def loadSpatialMapDefinitions():
    '''returns JSONObject\n\n
    loadSpatialMapDefinitions()\n
    '''
def addSpatialSecureTokenInfo():
    '''returns None\n\n
    addSpatialSecureTokenInfo(final JSONObject mapConf)\n
    '''
def storeUserLocation():
    '''returns int\n\n
    storeUserLocation()\n
    '''
def loadMenuItems():
    '''returns int\n\n
    loadMenuItems()\n
    '''
def setCurrentSALocation():
    '''returns int\n\n
    setCurrentSALocation()\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def getCurrentState():
    '''returns JSONArray\n\n
    getCurrentState()\n
    '''
def getCurrentRecordData():
    '''returns JSONObject\n\n
    getCurrentRecordData()\n
    '''
def getMainRecordMbo():
    '''returns MboRemote\n\n
    getMainRecordMbo()\n
    '''
def showMaxMessage():
    '''returns int\n\n
    showMaxMessage()\n
    '''
def showErrorsParamObject():
    '''returns int\n\n
    showErrorsParamObject()\n
    '''
def showErrors():
    '''returns int\n\n
    showErrors()\n
    '''
def showDialog():
    '''returns int\n\n
    showDialog()\n
    '''
def showSelectDialog():
    '''returns int\n\n
    showSelectDialog(final WebClientSession webClientSession, final JSONObject jsonObject)\n
    showSelectDialog(final JSONObject jsonObject)\n
    '''
def refreshQueryUnassignedWork():
    '''returns int\n\n
    refreshQueryUnassignedWork()\n
    '''
def queryUnassignedWorkDispatcher():
    '''returns int\n\n
    queryUnassignedWorkDispatcher()\n
    '''
def loadMapTipTemplate():
    '''returns int\n\n
    loadMapTipTemplate()\n
    '''
def loadAttributesFromLinearAttributeTemplate():
    '''returns int\n\n
    loadAttributesFromLinearAttributeTemplate()\n
    '''
def getLinearGraphicsbyWhereClause():
    '''returns int\n\n
    getLinearGraphicsbyWhereClause()\n
    '''
def loadLinearLayerObjectAttributes():
    '''returns int\n\n
    loadLinearLayerObjectAttributes()\n
    '''
def deleteLinearLayerSegmentObjects():
    '''returns int\n\n
    deleteLinearLayerSegmentObjects()\n
    '''
def loadMapTipSummaryTemplate():
    '''returns int\n\n
    loadMapTipSummaryTemplate()\n
    '''
def refreshMarkersPositions():
    '''returns int\n\n
    refreshMarkersPositions()\n
    '''
def createMapCallback():
    '''returns None\n\n
    createMapCallback(final String actionName, final JSONObject data)\n
    '''
def addRecordsToLayer():
    '''returns None\n\n
    addRecordsToLayer(final String layerName, final MboSetRemote mboSet, final boolean cleanOld)\n
    '''
def addEventToMap():
    '''returns None\n\n
    addEventToMap(final String eventName, final JSONObject action)\n
    '''
def removeRecordsFromLayer():
    '''returns None\n\n
    removeRecordsFromLayer(final String layerName, final MboSetRemote mboSet)\n
    '''
def getWeatherAlertsByQueryParams():
    '''returns int\n\n
    getWeatherAlertsByQueryParams()\n
    '''
def getCrewLaborByQueryParams():
    '''returns int\n\n
    getCrewLaborByQueryParams()\n
    '''
def getShowMarkersOnRouteError():
    '''returns int\n\n
    getShowMarkersOnRouteError()\n
    '''
def NOOP():
    '''returns int\n\n
    NOOP()\n
    '''
def clearNextEventData():
    '''returns None\n\n
    clearNextEventData()\n
    '''
def refreshLinearLayers():
    '''returns int\n\n
    refreshLinearLayers()\n
    '''
def getRelationshipLinearObject():
    '''returns MboRemote\n\n
    getRelationshipLinearObject(final MboRemote appMbo, final String objectName, final String relationshipName)\n
    '''
def loadLinearSegments():
    '''returns JSONArray\n\n
    loadLinearSegments(final MboRemote linearLayerMbo, final MboRemote appMbo, final MboRemote relatedAsset, final String mapMeasureUnit)\n
    '''
def userHasMapServiceLayerPermission():
    '''returns boolean\n\n
    userHasMapServiceLayerPermission(final MboRemote mapServiceLayerMbo, final String parent)\n
    '''
def getOpenMapReturnAttribute():
    '''returns String\n\n
    getOpenMapReturnAttribute()\n
    '''
def getOpenMapMbo():
    '''returns String\n\n
    getOpenMapMbo()\n
    '''
def getOriginalApp():
    '''returns String\n\n
    getOriginalApp(final String app)\n
    '''
def getPropagateCloneStatus():
    '''returns boolean\n\n
    getPropagateCloneStatus(final String mapName, final String app)\n
    '''
def pushMapControlClientEventHandler():
    '''returns int\n\n
    pushMapControlClientEventHandler()\n
    '''
def isCurrentMboAddressable():
    '''returns int\n\n
    isCurrentMboAddressable()\n
    '''
def isMboFormattedAddressEditable():
    '''returns boolean\n\n
    isMboFormattedAddressEditable()\n
    '''
def getRecordsFromAppTable():
    '''returns int\n\n
    getRecordsFromAppTable(final String tableId)\n
    '''
def getWOTaskRecords():
    '''returns int\n\n
    getWOTaskRecords()\n
    '''
def getWOMultiAssetLocCIRecords():
    '''returns int\n\n
    getWOMultiAssetLocCIRecords()\n
    '''
