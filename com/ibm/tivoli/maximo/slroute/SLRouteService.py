SKDACTIONINFOMAP_SEPARATOR = "String  \"\u00ef¿½\""
def ():
    '''returns DataGroupInformation\n\n
    (final MXServer mxServer)\n
    ()\n
    (final Date workPeriod, final Calendar startCal, final Calendar endCal)\n
    (final String groupname, final String title)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def createSLRBasedOnSKDProject():
    '''returns int\n\n
    createSLRBasedOnSKDProject(final MboRemote skdProj)\n
    '''
def getSKDProjectResources():
    '''returns List<MboSetRemote>\n\n
    getSKDProjectResources(final MboRemote skdProj, final boolean useResourceFilter, final SLRouteServiceCache appCache)\n
    '''
def getSkdProjAssignments():
    '''returns MboSetRemote\n\n
    getSkdProjAssignments(final MboRemote skdProj)\n
    getSkdProjAssignments(final MboRemote skdProj, final Date start, final Date end)\n
    '''
def getCrewAssignments():
    '''returns MboSetRemote\n\n
    getCrewAssignments(final String amcrew, final UserInfo userInfo, final Date start, final Date end, final String orgId, final SLRouteServiceCache appCache)\n
    '''
def getLaborAssignments():
    '''returns MboSetRemote\n\n
    getLaborAssignments(final String labor, final UserInfo userInfo, final Date start, final Date end, final String orgId, final SLRouteServiceCache appCache)\n
    '''
def getSLRouteSet():
    '''returns SLRouteSetRemote\n\n
    getSLRouteSet(final SLRouteRemote slroute)\n
    '''
def applyRoutes():
    '''returns int\n\n
    applyRoutes(final MboRemote slroute)\n
    '''
def getModel():
    '''returns IlvGanttModel\n\n
    getModel(final UserInfo userInfo, final String skdProjID, final boolean addShiftInfo, final SLRouteServiceCache appCache)\n
    '''
def getSKDDD():
    '''returns SKDDD\n\n
    getSKDDD()\n
    '''
def updateTravelTime():
    '''returns String\n\n
    updateTravelTime(final IlvGanttModel model, final String toAssignId, final String fromAssignId, final String fromLocationId, final String toLocationId, final String slrRouteId, final Double duration, final UserInfo userInfo)\n
    '''
def clearSLRTravelTimeData():
    '''returns None\n\n
    clearSLRTravelTimeData(final AssignmentRemote assignment)\n
    '''
def getSLRouteSetFromSelection():
    '''returns SLRouteSetRemote\n\n
    getSLRouteSetFromSelection(final SLRouteRemote slroute)\n
    '''
def getModelNew():
    '''returns IlvGanttModel\n\n
    getModelNew(final UserInfo userInfo, final String rootActivityName, final String rootResourceName, final List<MboSetRemote> resMboSetList, final Date startDate, final Date endDate, final int shiftMargin, final SLRouteServiceCache appCache, final boolean addHierachy, final MboRemote skdProj)\n
    '''
def getModelForResource():
    '''returns IlvGanttModel\n\n
    getModelForResource(final UserInfo userInfo, final String skdProjID, final String resObj, final String resKey, final SLRouteServiceCache appCache)\n
    '''
def clearStaticDataCaches():
    '''returns None\n\n
    clearStaticDataCaches()\n
    '''
def getSLRTravelTimeRecord():
    '''returns SLRTravelTimeSetRemote\n\n
    getSLRTravelTimeRecord(final String toAssignId, final String fromAssignId, final String fromLocationId, final String toLocationId, final long slrRouteId, final UserInfo userInfo)\n
    '''
def refreshModel():
    '''returns List<MXReservation>\n\n
    refreshModel(final IlvGanttModel model, final UserInfo userInfo, final SLRouteServiceCache appCache)\n
    '''
def recalculateTravelTimeForAssigment():
    '''returns None\n\n
    recalculateTravelTimeForAssigment(final MXGanttModel mxModel, final MXActivity fromAssignment, final MXActivity toAssignment, final MXResource resource, final MboRemote project, final UserInfo userInfo)\n
    '''
def notifyLaborOrCrewAssignment():
    '''returns None\n\n
    notifyLaborOrCrewAssignment(final Long assignmentId, final String workOrderNumber)\n
    '''
def notifyAssignmentUpdate():
    '''returns None\n\n
    notifyAssignmentUpdate(final Long assignmentId, final String workOrderNumber, final int operation)\n
    '''
def getResource():
    '''returns MXResource\n\n
    getResource()\n
    '''
def getGroupname():
    '''returns String\n\n
    getGroupname()\n
    '''
