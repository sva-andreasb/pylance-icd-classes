SKDACTIONINFOMAP_SEPARATOR = "String  \"\u00ef¿½\""
def SLRouteService():
    '''public SLRouteService(final MXServer mxServer)
    '''
def init():
    '''public void init()
    '''
def destroy():
    '''public void destroy()
    '''
def createSLRBasedOnSKDProject():
    '''public int createSLRBasedOnSKDProject(final MboRemote skdProj)
    '''
def getSKDProjectResources():
    '''public List<MboSetRemote> getSKDProjectResources(final MboRemote skdProj, final boolean useResourceFilter, final SLRouteServiceCache appCache)
    '''
def getSkdProjAssignments():
    '''public MboSetRemote getSkdProjAssignments(final MboRemote skdProj)
    public MboSetRemote getSkdProjAssignments(final MboRemote skdProj, final Date start, final Date end)
    '''
def getCrewAssignments():
    '''public MboSetRemote getCrewAssignments(final String amcrew, final UserInfo userInfo, final Date start, final Date end, final String orgId, final SLRouteServiceCache appCache)
    '''
def getLaborAssignments():
    '''public MboSetRemote getLaborAssignments(final String labor, final UserInfo userInfo, final Date start, final Date end, final String orgId, final SLRouteServiceCache appCache)
    '''
def getSLRouteSet():
    '''public SLRouteSetRemote getSLRouteSet(final SLRouteRemote slroute)
    '''
def applyRoutes():
    '''public int applyRoutes(final MboRemote slroute)
    '''
def getModel():
    '''public IlvGanttModel getModel(final UserInfo userInfo, final String skdProjID, final boolean addShiftInfo, final SLRouteServiceCache appCache)
    '''
def getSKDDD():
    '''public SKDDD getSKDDD()
    '''
def getActionTitle():
    '''public HashMap<String, HashMap<String, SKDActionInfo>> getActionTitle(final UserInfo userInfo, final HashMap<String, HashMap<String, SKDActionInfo>> actionInfo, final String useWith)
    public HashMap<String, HashMap<String, SKDActionInfo>> getActionTitle(final UserInfo userInfo, final HashMap<String, HashMap<String, SKDActionInfo>> actionInfo)
    '''
def updateTravelTime():
    '''public String updateTravelTime(final IlvGanttModel model, final String toAssignId, final String fromAssignId, final String fromLocationId, final String toLocationId, final String slrRouteId, final Double duration, final UserInfo userInfo)
    '''
def clearSLRTravelTimeData():
    '''public void clearSLRTravelTimeData(final AssignmentRemote assignment)
    '''
def getSLRouteSetFromSelection():
    '''public SLRouteSetRemote getSLRouteSetFromSelection(final SLRouteRemote slroute)
    '''
def getModelNew():
    '''public IlvGanttModel getModelNew(final UserInfo userInfo, final String rootActivityName, final String rootResourceName, final List<MboSetRemote> resMboSetList, final Date startDate, final Date endDate, final int shiftMargin, final SLRouteServiceCache appCache, final boolean addHierachy, final MboRemote skdProj)
    '''
def getModelForResource():
    '''public IlvGanttModel getModelForResource(final UserInfo userInfo, final String skdProjID, final String resObj, final String resKey, final SLRouteServiceCache appCache)
    '''
def clearStaticDataCaches():
    '''public void clearStaticDataCaches()
    '''
def getSLRTravelTimeRecord():
    '''public SLRTravelTimeSetRemote getSLRTravelTimeRecord(final String toAssignId, final String fromAssignId, final String fromLocationId, final String toLocationId, final long slrRouteId, final UserInfo userInfo)
    '''
def refreshModel():
    '''public List<MXReservation> refreshModel(final IlvGanttModel model, final UserInfo userInfo, final SLRouteServiceCache appCache)
    '''
def recalculateTravelTimeForAssigment():
    '''public void recalculateTravelTimeForAssigment(final MXGanttModel mxModel, final MXActivity fromAssignment, final MXActivity toAssignment, final MXResource resource, final MboRemote project, final UserInfo userInfo)
    '''
def notifyLaborOrCrewAssignment():
    '''public void notifyLaborOrCrewAssignment(final Long assignmentId, final String workOrderNumber)
    '''
def notifyAssignmentUpdate():
    '''public void notifyAssignmentUpdate(final Long assignmentId, final String workOrderNumber, final int operation)
    '''
def join():
    '''public static String join(final String attribute, final List<? extends MboRemote> mboList, final String delim, final boolean isString)
    '''
def ShiftInformation():
    '''public ShiftInformation()
    public ShiftInformation(final Date workPeriod, final Calendar startCal, final Calendar endCal)
    '''
def DataGroupInformation():
    '''public DataGroupInformation(final String groupname, final String title)
    '''
def getResource():
    '''public MXResource getResource()
    '''
def getGroupname():
    '''public String getGroupname()
    '''
