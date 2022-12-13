def AbstractTaskCommand():
    '''    public AbstractTaskCommand(final TaskCommandMetadata inMetadata)
    public AbstractTaskCommand(final CommandData commandData)
    '''
def getCurrentStep():
    '''    public CommandStep getCurrentStep(final int operation)
    public CommandStep getCurrentStep(final int operation, final String stepName)
    '''
def setCurrentStep():
    '''    public void setCurrentStep(final AbstractCommandStep newCurrentStep)
    '''
def getCurrentStepIndex():
    '''    public int getCurrentStepIndex()
    '''
def setCurrentStepIndex():
    '''    public void setCurrentStepIndex(final int index)
    '''
def listCommandSteps():
    '''    public String[] listCommandSteps()
    '''
def nextStep():
    '''    public final CommandStep nextStep()
    '''
def previousStep():
    '''    public final CommandStep previousStep()
    '''
def hasNextStep():
    '''    public final boolean hasNextStep()
    '''
def hasPreviousStep():
    '''    public final boolean hasPreviousStep()
    '''
def gotoStep():
    '''    public final CommandStep gotoStep(final String stepName)
    '''
def getCommandStep():
    '''    public CommandStep getCommandStep(final String stepName)
    '''
def getTaskCommandData():
    '''    public final TaskCommandData getTaskCommandData()
    '''
def getTaskCommandMetadata():
    '''    public final TaskCommandMetadata getTaskCommandMetadata()
    '''
def addStep():
    '''    public void addStep(final AbstractCommandStep step, final int index)
    '''
def resetCommandData():
    '''    public void resetCommandData(final CommandData cmdData)
    '''
def validate():
    '''    public void validate()
    '''
def processTaskParameters():
    '''    public void processTaskParameters()
    '''
def commandParamsModified():
    '''    public void commandParamsModified()
    '''
def execute():
    '''    public void execute()
    '''
def run():
    '''    public Object run()
    '''
def getTaskCommandResult():
    '''    public TaskCommandResult getTaskCommandResult()
    '''
def listAllStepParamsData():
    '''    public void listAllStepParamsData()
    '''
