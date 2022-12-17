INITIATEWORKFLOW = "String  \"initiateworkflow\""
INPUTWF = "String  \"inputwf\""
COMPLETEWF = "String  \"completewf\""
LISTASSIGNMENTS = "String  \"listassignments\""
REASSIGNWF = "String  \"reassignwf\""
NEWOROLDWF = "String  \"neworoldwf\""
STOPWF = "String  \"stopwf\""
ACTIVEWF = "String  \"activewf\""
def ():
    '''returns WorkflowDirector\n\n
    (final MXSession s)\n
    '''
def isInteractionDoublePlay():
    '''returns boolean\n\n
    isInteractionDoublePlay()\n
    '''
def getInstance():
    '''returns WFInstanceRemote\n\n
    getInstance()\n
    '''
def getAssignment():
    '''returns WFAssignmentRemote\n\n
    getAssignment()\n
    '''
def getNextApp():
    '''returns String\n\n
    getNextApp()\n
    '''
def getNextAction():
    '''returns String\n\n
    getNextAction()\n
    '''
def getWfSet():
    '''returns MboSetRemote\n\n
    getWfSet()\n
    '''
def setAssignment():
    '''returns None\n\n
    setAssignment(final WFAssignmentRemote remote)\n
    '''
def setInstance():
    '''returns None\n\n
    setInstance(final WFInstanceRemote remote)\n
    '''
def getNextDirectionBody():
    '''returns String\n\n
    getNextDirectionBody()\n
    '''
def getNextDirectionTitle():
    '''returns String\n\n
    getNextDirectionTitle()\n
    '''
def clearDirections():
    '''returns None\n\n
    clearDirections()\n
    '''
def input():
    '''returns None\n\n
    input(final DirectorInput message)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def resetNonUI():
    '''returns None\n\n
    resetNonUI()\n
    '''
def getControlled():
    '''returns MboRemote\n\n
    getControlled()\n
    '''
def setControlled():
    '''returns None\n\n
    setControlled(final MboRemote remote)\n
    '''
def getControlledUniqueKey():
    '''returns long\n\n
    getControlledUniqueKey()\n
    '''
def startInput():
    '''returns None\n\n
    startInput(final String app, final MboRemote target, final DirectorInput message)\n
    '''
def getNextUniqueId():
    '''returns long\n\n
    getNextUniqueId()\n
    '''
def getWorkflowWarnings():
    '''returns MXException[]\n\n
    getWorkflowWarnings()\n
    '''
def addWorkflowWarning():
    '''returns None\n\n
    addWorkflowWarning(final MXException exception)\n
    '''
def isAtInteraction():
    '''returns boolean\n\n
    isAtInteraction()\n
    '''
def getNextTab():
    '''returns String\n\n
    getNextTab()\n
    '''
def setNextTab():
    '''returns None\n\n
    setNextTab(final String nextTab)\n
    '''
def getLaunchProcess():
    '''returns String\n\n
    getLaunchProcess()\n
    '''
def setLaunchProcess():
    '''returns None\n\n
    setLaunchProcess(final String launchProcess)\n
    '''
def setAssignID():
    '''returns None\n\n
    setAssignID(final int assignID)\n
    '''
def setProcessName():
    '''returns None\n\n
    setProcessName(final String valueString)\n
    '''
def doAutoInit():
    '''returns boolean\n\n
    doAutoInit(final MboRemote targetMbo)\n
    '''
def preventAutoInit():
    '''returns None\n\n
    preventAutoInit()\n
    '''
def allowAutoInit():
    '''returns None\n\n
    allowAutoInit()\n
    '''
def clearInteraction():
    '''returns None\n\n
    clearInteraction()\n
    '''
