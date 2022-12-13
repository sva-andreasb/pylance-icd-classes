AUTOINITACTIVE = "String  \"AutoInitActive\""
def WFProcess():
    '''    public WFProcess(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def initRelationship():
    '''    public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def add():
    '''    public void add()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def findIncomingActions():
    '''    public List<WFAction> findIncomingActions(final int nodeID)
    '''
def getNextActionNum():
    '''    public int getNextActionNum()
    '''
def setNextActionNum():
    '''    public void setNextActionNum(final int actionID)
    '''
def findNode():
    '''    public WFNode findNode(final int nodeID)
    '''
def validateWorkflow():
    '''    public Vector validateWorkflow()
    public Vector<MXException> validateWorkflow(final Hashtable<String, String> hinfo)
    '''
def buildSubProcessList():
    '''    public void buildSubProcessList(final Hashtable<String, String> h)
    '''
def hasPositiveStop():
    '''    public boolean hasPositiveStop()
    '''
def hasNegativeStop():
    '''    public boolean hasNegativeStop()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def delete():
    '''    public void delete(final long modifier)
    '''
def enableProcess():
    '''    public boolean enableProcess()
    '''
def makeProcessActive():
    '''    public void makeProcessActive()
    '''
def initiateWorkflow():
    '''    public WFInstanceRemote initiateWorkflow(final MboRemote targetMbo, final String memo)
    '''
def validateProcess():
    '''    public boolean validateProcess()
    '''
def deactivateProcess():
    '''    public void deactivateProcess()
    '''
def createRevision():
    '''    public MboRemote createRevision()
    '''
def disableProcess():
    '''    public void disableProcess()
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def resynchronize():
    '''    public void resynchronize()
    '''
def getValidateOrder():
    '''    public String[] getValidateOrder()
    '''
def needAppSupport():
    '''    public boolean needAppSupport()
    '''
def makeAutoInitiate():
    '''    public void makeAutoInitiate()
    '''
def clearAutoInitiate():
    '''    public void clearAutoInitiate()
    '''
def nextNoteUID():
    '''    public int nextNoteUID()
    '''
def updatePointedTo():
    '''    public void updatePointedTo(final Integer wasMemberNodeID, final Integer nowMemberNodeID)
    '''
def addNodePointedTo():
    '''    public void addNodePointedTo(final Mbo pointedToNode)
    '''
def createPointedToList():
    '''    public String createPointedToList(final int nodeID)
    '''
def getNextNodePoint():
    '''    public Point getNextNodePoint()
    '''
def getNodeAt():
    '''    public MboRemote getNodeAt(final int x, final int y)
    '''
def setDeletableFlag():
    '''    public void setDeletableFlag(final boolean flag)
    '''
