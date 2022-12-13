CACHEKEY_ASSIGNMENTACTIVITYMAP = "String  \"WOActivityDataManager-assignmentmap\""
CACHEKEY_COSTTYPEDATA_LOADED = "String  \"WOActivityDataManager-CostTypeDataLoaded\""
CACHEKEY_COSTTYPEDATA = "String  \"WOActivityDataManager-CostTypeData\""
CACHEKEY_WOMBOMAP = "String  \"WOActivityDataManager-WOMboMap\""
CACHEKEY_ASSSIGNMENTMBOMAP = "String  \"WOActivityDataManager-AssignmentMboMap\""
CACHEKEY_GROUPINFOSET = "String  \"WOActivityDataManager-groupInfoSet\""
CACHEKEY_WOWEATHERALERT = "String  \"WOActivityDataManager-WOWeatherAlertData\""
CACHEKEY_WORKLOG = "String  \"WOActivityDataManager-WorkLogData\""
CACHEKEY_CREWTYPEWORKZONE = "String  \"WOActivityDataManager-CrewTypeWorkZoneData\""
CACHEKEY_CRAFTWORKZONE = "String  \"WOActivityDataManager-CraftWorkZoneData\""
CACHEKEY_ASSIGNREPLOC = "String  \"WOActivityDataManager-AssignRepLocData\""
def WOActivityDataManager():
    '''    public WOActivityDataManager()
    '''
def initializeActivity():
    '''    public void initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    '''
def initializeActivityChildren():
    '''    public void initializeActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    '''
def loadActivity():
    '''    public void loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)
    public void loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)
    '''
def calculateHours():
    '''    public double calculateHours(final Date date1, final Date date2)
    '''
def getWOClassRestriction():
    '''    public String getWOClassRestriction(final String objectName)
    '''
def getDefaultRestriction():
    '''    public String getDefaultRestriction(final String objectName)
    '''
def getCompleteQueryWhere():
    '''    public String getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)
    '''
def activityRecordCount():
    '''    public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
    '''
def populateActivities():
    '''    public void populateActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def loadAdditionalActivities():
    '''    public void loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def loadWorkAndNonWorkActivities():
    '''    public void loadWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def populateActivityPropertyDetails():
    '''    public void populateActivityPropertyDetails()
    '''
def applyActivityChange():
    '''    public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
    public void applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)
    '''
def applyScenarioChange():
    '''    public void applyScenarioChange(final MboRemote activity, final MboRemote parentactivity, final MXTransaction txn)
    public void applyScenarioChange(final MboRemote activity, final MboRemote parentactivity, final String ids, final MXTransaction txn)
    '''
def sortActivityChildren():
    '''    public List<IlvActivity> sortActivityChildren(final IlvActivity activity, final String objectName, final MXGanttModel model)
    '''
def linkChildDummyNode():
    '''    public List<IlvActivity> linkChildDummyNode(final MXActivity activity, final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def saveActivities():
    '''    public void saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)
    '''
def applyAssignmentChanges():
    '''    public void applyAssignmentChanges(final IlvGeneralActivity activity, final MXTransaction txn)
    '''
def getModifiedActivityChildren():
    '''    public List<IlvActivity> getModifiedActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)
    '''
def loadCrewWorkAndNonWorkActivities():
    '''    public void loadCrewWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def loadCostTypeReservations():
    '''    public void loadCostTypeReservations(final MXGanttModel model, final SKDAppService.ActivityData activityData)
    '''
def populateActivityParentFromAsset():
    '''    public void populateActivityParentFromAsset(final String objectname, final String uniqueidname)
    '''
def populateActivityParentFromLocation():
    '''    public void populateActivityParentFromLocation(final String objectname, final String uniqueidname)
    '''
def isAVIATIONMROLicensePresent():
    '''    public static boolean isAVIATIONMROLicensePresent()
    '''
def setPLUSAReservation():
    '''    public void setPLUSAReservation(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MboRemote asstMbo)
    '''
def compare():
    '''    public int compare(final IlvActivity a01, final IlvActivity a02)
    '''
