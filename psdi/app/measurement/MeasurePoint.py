GENERATING_WORK = "String  \"MEASUREPOINT.GeneratingWork\""
def MeasurePoint():
    '''    public MeasurePoint(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def initFieldFlagsOnMbo():
    '''    public void initFieldFlagsOnMbo(final String attrName)
    '''
def appValidate():
    '''    public void appValidate()
    '''
def add():
    '''    public void add()
    '''
def generateAutoKey():
    '''    public void generateAutoKey()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def getJobPlanOrPMToGenWO():
    '''    public Object getJobPlanOrPMToGenWO()
    '''
def getJobPlanOrPMToGenWOForGaugeMeter():
    '''    public Object getJobPlanOrPMToGenWOForGaugeMeter()
    '''
def getJobPlanOrPMToGenWOForCharacteristicMeter():
    '''    public Object getJobPlanOrPMToGenWOForCharacteristicMeter()
    public Object getJobPlanOrPMToGenWOForCharacteristicMeter(final MboRemote measurement)
    '''
def generateWorkOrder():
    '''    public void generateWorkOrder(final Date effectiveDate, final String memo, final boolean actionsAsCriteria)
    public void generateWorkOrder(final Date effectiveDate, final String memo, final boolean actionsAsCriteria, final MboRemote measurement)
    '''
def generateWorkOrderForCharacteristicMeter():
    '''    public void generateWorkOrderForCharacteristicMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria)
    public void generateWorkOrderForCharacteristicMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria, final MboRemote measurement)
    '''
def generateWorkOrderForGaugeMeter():
    '''    public void generateWorkOrderForGaugeMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria)
    public void generateWorkOrderForGaugeMeter(final Date effectiveDate, final String memo, final boolean actionsAsCriteria, final MboRemote measurement)
    '''
def genWOAndPointWOFromPM():
    '''    public void genWOAndPointWOFromPM(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String pmnum, final int priority)
    public void genWOAndPointWOFromPM(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String pmnum, int priority, final MboRemote measurement)
    '''
def genWOAndPointWOFromJobPlan():
    '''    public void genWOAndPointWOFromJobPlan(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String jpnum, final int priority)
    public void genWOAndPointWOFromJobPlan(final Date effectiveDate, final String memo, final boolean useActionLimitCriteria, final String jpnum, int priority, final MboRemote measurement)
    '''
def getDeployedMeter():
    '''    public MboRemote getDeployedMeter()
    '''
def getDeployedMeterForUpdate():
    '''    public MboRemote getDeployedMeterForUpdate()
    '''
def updateMeterOnMeasureDeletion():
    '''    public void updateMeterOnMeasureDeletion()
    '''
def save():
    '''    public void save()
    '''
def setMoveAssetFlag():
    '''    public void setMoveAssetFlag(final boolean flag)
    '''
def isChangeByUserWhenSetFromLookup():
    '''    public boolean isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)
    '''
