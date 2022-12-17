def ():
    '''returns WFAssignment\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def complete():
    '''returns None\n\n
    complete(final String memo)\n
    '''
def inactivate():
    '''returns None\n\n
    inactivate()\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final String memo)\n
    '''
def escalate():
    '''returns None\n\n
    escalate()\n
    escalate(final String memo)\n
    '''
def calcDueDate():
    '''returns Date\n\n
    calcDueDate(final PersonRemote person, final Date startDate)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def wfValidate():
    '''returns None\n\n
    wfValidate(final Vector<MXException> errs)\n
    '''
def getTask():
    '''returns WFTask\n\n
    getTask()\n
    '''
def getWFInstance():
    '''returns WFInstanceRemote\n\n
    getWFInstance()\n
    '''
def getInstance():
    '''returns WFInstance\n\n
    getInstance()\n
    '''
def getNode():
    '''returns WFNodeRemote\n\n
    getNode()\n
    '''
def evaluateAssignmentCondition():
    '''returns boolean\n\n
    evaluateAssignmentCondition()\n
    '''
def generateAssignments():
    '''returns None\n\n
    generateAssignments()\n
    '''
def sendNotification():
    '''returns None\n\n
    sendNotification(final PersonRemote person)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def generateForRole():
    '''returns None\n\n
    generateForRole(final MaxRoleRemote role)\n
    '''
def generateForGroup():
    '''returns None\n\n
    generateForGroup(final PersonGroupRemote group)\n
    '''
def getOriginalPersonForAssignment():
    '''returns PersonRemote\n\n
    getOriginalPersonForAssignment()\n
    '''
def generateForPerson():
    '''returns None\n\n
    generateForPerson(final PersonRemote person)\n
    '''
def activeAssignment():
    '''returns None\n\n
    activeAssignment(final PersonRemote person, final WFAssignmentSet activeSet)\n
    '''
def foundPersonToAssignForRole():
    '''returns boolean\n\n
    foundPersonToAssignForRole()\n
    '''
