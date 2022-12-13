INITIATEWORKFLOW = "String  \"initiateworkflow\""
INPUTWF = "String  \"inputwf\""
COMPLETEWF = "String  \"completewf\""
LISTASSIGNMENTS = "String  \"listassignments\""
REASSIGNWF = "String  \"reassignwf\""
NEWOROLDWF = "String  \"neworoldwf\""
STOPWF = "String  \"stopwf\""
ACTIVEWF = "String  \"activewf\""
def WorkflowDirector():
    '''public WorkflowDirector(final MXSession s)
    '''
def isInteractionDoublePlay():
    '''public boolean isInteractionDoublePlay()
    '''
def getInstance():
    '''public WFInstanceRemote getInstance()
    '''
def getAssignment():
    '''public WFAssignmentRemote getAssignment()
    '''
def getNextApp():
    '''public String getNextApp()
    '''
def getNextAction():
    '''public String getNextAction()
    '''
def getWfSet():
    '''public MboSetRemote getWfSet()
    '''
def setAssignment():
    '''public void setAssignment(final WFAssignmentRemote remote)
    '''
def setInstance():
    '''public void setInstance(final WFInstanceRemote remote)
    '''
def getNextDirectionBody():
    '''public String getNextDirectionBody()
    '''
def getNextDirectionTitle():
    '''public String getNextDirectionTitle()
    '''
def clearDirections():
    '''public void clearDirections()
    '''
def input():
    '''public void input(final DirectorInput message)
    '''
def reset():
    '''public void reset()
    '''
def resetNonUI():
    '''public void resetNonUI()
    '''
def getControlled():
    '''public MboRemote getControlled()
    '''
def setControlled():
    '''public void setControlled(final MboRemote remote)
    '''
def getControlledUniqueKey():
    '''public long getControlledUniqueKey()
    '''
def startInput():
    '''public void startInput(final String app, final MboRemote target, final DirectorInput message)
    '''
def getNextUniqueId():
    '''public long getNextUniqueId()
    '''
def getWorkflowWarnings():
    '''public MXException[] getWorkflowWarnings()
    '''
def addWorkflowWarning():
    '''public void addWorkflowWarning(final MXException exception)
    '''
def isAtInteraction():
    '''public boolean isAtInteraction()
    '''
def getNextTab():
    '''public String getNextTab()
    '''
def setNextTab():
    '''public void setNextTab(final String nextTab)
    '''
def getLaunchProcess():
    '''public String getLaunchProcess()
    '''
def setLaunchProcess():
    '''public void setLaunchProcess(final String launchProcess)
    '''
def setAssignID():
    '''public void setAssignID(final int assignID)
    '''
def setProcessName():
    '''public void setProcessName(final String valueString)
    '''
def doAutoInit():
    '''public boolean doAutoInit(final MboRemote targetMbo)
    '''
def preventAutoInit():
    '''public void preventAutoInit()
    '''
def allowAutoInit():
    '''public void allowAutoInit()
    '''
def clearInteraction():
    '''public void clearInteraction()
    '''
