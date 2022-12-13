def Assignment():
    '''public Assignment(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def calledFromAssignmentManager():
    '''public boolean calledFromAssignmentManager()
    '''
def completeAssignment():
    '''public void completeAssignment(final String status, final Date date)
    public void completeAssignment()
    public void completeAssignment(final boolean completeWO)
    '''
def getLabTransSet():
    '''public LabTransSetRemote getLabTransSet()
    '''
def createLabTrans():
    '''public void createLabTrans(final WORemote ownerWO)
    '''
def getToolTransSet():
    '''public ToolTransSetRemote getToolTransSet()
    '''
def createToolTransCrew():
    '''public void createToolTransCrew(final WORemote ownerWO, final AMCrewRemote crew)
    '''
def completeTheWO():
    '''public void completeTheWO(final WORemote ownerWO)
    '''
def canFinishWO():
    '''public boolean canFinishWO(final WO woMbo)
    '''
def getWPEndDateTime():
    '''public Date getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal, final AvailCalc availCalc)
    '''
def calcFinishDate():
    '''public void calcFinishDate()
    '''
def propagateKeyValue():
    '''public void propagateKeyValue(final String keyName, final String keyValue)
    '''
def startAssignment():
    '''public void startAssignment(final Date startDate)
    '''
def interruptAssignment():
    '''public void interruptAssignment(final Date interruptDate)
    '''
def finishAssignment():
    '''public void finishAssignment(final Date finishDate)
    '''
def getCrewWorkZoneWhere():
    '''public String getCrewWorkZoneWhere(final MboRemote owner)
    public String getCrewWorkZoneWhere(final String assetNum, final String location, final String siteId, final String orgId)
    '''
def getLaborWorkZoneWhere():
    '''public String getLaborWorkZoneWhere(final String assetNum, final String location, final String siteId, final String orgId)
    public String getLaborWorkZoneWhere(final MboRemote owner)
    '''
def countMembers():
    '''public int countMembers()
    '''
def getAvailableLabor():
    '''public MboSetRemote getAvailableLabor()
    '''
def delete():
    '''public void delete()
    '''
def undelete():
    '''public void undelete()
    '''
def modify():
    '''public void modify()
    '''
