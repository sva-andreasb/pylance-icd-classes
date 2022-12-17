AUTOINITACTIVE = "String  \"AutoInitActive\""
def ():
    '''returns WFProcess\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def findIncomingActions():
    '''returns List<WFAction>\n\n
    findIncomingActions(final int nodeID)\n
    '''
def getNextActionNum():
    '''returns int\n\n
    getNextActionNum()\n
    '''
def setNextActionNum():
    '''returns None\n\n
    setNextActionNum(final int actionID)\n
    '''
def findNode():
    '''returns WFNode\n\n
    findNode(final int nodeID)\n
    '''
def validateWorkflow():
    '''returns Vector<MXException>\n\n
    validateWorkflow()\n
    validateWorkflow(final Hashtable<String, String> hinfo)\n
    '''
def buildSubProcessList():
    '''returns None\n\n
    buildSubProcessList(final Hashtable<String, String> h)\n
    '''
def hasPositiveStop():
    '''returns boolean\n\n
    hasPositiveStop()\n
    '''
def hasNegativeStop():
    '''returns boolean\n\n
    hasNegativeStop()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long modifier)\n
    '''
def enableProcess():
    '''returns boolean\n\n
    enableProcess()\n
    '''
def makeProcessActive():
    '''returns None\n\n
    makeProcessActive()\n
    '''
def initiateWorkflow():
    '''returns WFInstanceRemote\n\n
    initiateWorkflow(final MboRemote targetMbo, final String memo)\n
    '''
def validateProcess():
    '''returns boolean\n\n
    validateProcess()\n
    '''
def deactivateProcess():
    '''returns None\n\n
    deactivateProcess()\n
    '''
def createRevision():
    '''returns MboRemote\n\n
    createRevision()\n
    '''
def disableProcess():
    '''returns None\n\n
    disableProcess()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def resynchronize():
    '''returns None\n\n
    resynchronize()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def needAppSupport():
    '''returns boolean\n\n
    needAppSupport()\n
    '''
def makeAutoInitiate():
    '''returns None\n\n
    makeAutoInitiate()\n
    '''
def clearAutoInitiate():
    '''returns None\n\n
    clearAutoInitiate()\n
    '''
def nextNoteUID():
    '''returns int\n\n
    nextNoteUID()\n
    '''
def updatePointedTo():
    '''returns None\n\n
    updatePointedTo(final Integer wasMemberNodeID, final Integer nowMemberNodeID)\n
    '''
def addNodePointedTo():
    '''returns None\n\n
    addNodePointedTo(final Mbo pointedToNode)\n
    '''
def createPointedToList():
    '''returns String\n\n
    createPointedToList(final int nodeID)\n
    '''
def getNextNodePoint():
    '''returns Point\n\n
    getNextNodePoint()\n
    '''
def getNodeAt():
    '''returns MboRemote\n\n
    getNodeAt(final int x, final int y)\n
    '''
def setDeletableFlag():
    '''returns None\n\n
    setDeletableFlag(final boolean flag)\n
    '''
