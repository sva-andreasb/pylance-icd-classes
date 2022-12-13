def AbstractTaskCommand():
'''public AbstractTaskCommand(final TaskCommandMetadata inMetadata)
public AbstractTaskCommand(final CommandData commandData)
'''
pass
def getCurrentStep():
'''public CommandStep getCurrentStep(final int operation)
public CommandStep getCurrentStep(final int operation, final String stepName)
'''
pass
def setCurrentStep():
'''public void setCurrentStep(final AbstractCommandStep newCurrentStep)
'''
pass
def getCurrentStepIndex():
'''public int getCurrentStepIndex()
'''
pass
def setCurrentStepIndex():
'''public void setCurrentStepIndex(final int index)
'''
pass
def listCommandSteps():
'''public String[] listCommandSteps()
'''
pass
def nextStep():
'''public final CommandStep nextStep()
'''
pass
def previousStep():
'''public final CommandStep previousStep()
'''
pass
def hasNextStep():
'''public final boolean hasNextStep()
'''
pass
def hasPreviousStep():
'''public final boolean hasPreviousStep()
'''
pass
def gotoStep():
'''public final CommandStep gotoStep(final String stepName)
'''
pass
def getCommandStep():
'''public CommandStep getCommandStep(final String stepName)
'''
pass
def getTaskCommandData():
'''public final TaskCommandData getTaskCommandData()
'''
pass
def getTaskCommandMetadata():
'''public final TaskCommandMetadata getTaskCommandMetadata()
'''
pass
def addStep():
'''public void addStep(final AbstractCommandStep step, final int index)
'''
pass
def resetCommandData():
'''public void resetCommandData(final CommandData cmdData)
'''
pass
def validate():
'''public void validate()
'''
pass
def processTaskParameters():
'''public void processTaskParameters()
'''
pass
def commandParamsModified():
'''public void commandParamsModified()
'''
pass
def execute():
'''public void execute()
'''
pass
def run():
'''public Object run()
'''
pass
def getTaskCommandResult():
'''public TaskCommandResult getTaskCommandResult()
'''
pass
def listAllStepParamsData():
'''public void listAllStepParamsData()
'''
pass
