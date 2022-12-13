def AssetActivityDataManager():
    '''public AssetActivityDataManager()
    '''
def populate():
    '''public boolean populate()
    '''
def populateActivities():
    '''public void populateActivities(final HashMap<String, ArrayList<String>> queryMap)
    '''
def getDateDBSqlString():
    '''public String[] getDateDBSqlString(final int dbType)
    '''
def getOrgQuery():
    '''public String getOrgQuery()
    '''
def populateActivityPropertyDetails():
    '''public void populateActivityPropertyDetails()
    '''
def populateActivityParentFromAsset():
    '''public void populateActivityParentFromAsset(final String uniqueidname)
    '''
def populateActivityDatesFromSkdproject():
    '''public void populateActivityDatesFromSkdproject()
    '''
def getCompleteQueryWhere():
    '''public String getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)
    '''
def getDefaultRestriction():
    '''public String getDefaultRestriction(final String objectName)
    '''
def loadActivity():
    '''public void loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)
    '''
def activityRecordCount():
    '''public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
    '''
def saveActivities():
    '''public void saveActivities(final IlvGeneralActivity activity)
    '''
def applyActivityChange():
    '''public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
    public void applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)
    '''
