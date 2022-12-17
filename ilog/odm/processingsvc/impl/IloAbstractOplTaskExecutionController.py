COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloAbstractOplTaskExecutionController\n\n
    (final IloProcessingService ps, final IloExecutionScope scope, final IloTaskConfig config, final IloTaskInputOutput io, final List<IloTaskExecutionController> tasks)\n
    '''
def setOptimizationService():
    '''returns None\n\n
    setOptimizationService(final IloOptimizationService service)\n
    '''
def setup():
    '''returns None\n\n
    setup()\n
    '''
def tearDown():
    '''returns None\n\n
    tearDown()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    '''
def acceptCurrentSolution():
    '''returns None\n\n
    acceptCurrentSolution()\n
    acceptCurrentSolution()\n
    '''
def hasFeasibleSolution():
    '''returns boolean\n\n
    hasFeasibleSolution()\n
    hasFeasibleSolution()\n
    '''
def enginePhaseChanged():
    '''returns None\n\n
    enginePhaseChanged(final IloEnginePhase newPhase)\n
    '''
def progressUpdateHappened():
    '''returns None\n\n
    progressUpdateHappened(final OptimProgressUpdate update)\n
    '''
def getCurrentEnginePhase():
    '''returns IloEnginePhase\n\n
    getCurrentEnginePhase()\n
    '''
def getLastOptimProgressUpdate():
    '''returns OptimProgressUpdate\n\n
    getLastOptimProgressUpdate()\n
    '''
def addOptimProgressObserver():
    '''returns None\n\n
    addOptimProgressObserver(final OptimProgressObserver observer)\n
    '''
def removeOptimProgressObserver():
    '''returns None\n\n
    removeOptimProgressObserver(final OptimProgressObserver observer)\n
    '''
