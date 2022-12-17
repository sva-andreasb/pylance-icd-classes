TM_FLAG_NONE = "int  0"
TM_FLAG_IGNORE_ERRORS = "int  1"
TM_FLAG_RUN_ASYNCHRONOUSLY = "int  2"
TM_FLAG_QUEUEABLE_JOB = "int  4"
TM_FLAG_IA_DUP_CHECK = "int  8"
def getQueuedJobs():
    '''returns ConcurrentLinkedQueue<Controller>\n\n
    getQueuedJobs()\n
    '''
def isJobQueued():
    '''returns boolean\n\n
    isJobQueued(final String jobName)\n
    '''
def getQueuedJobCount():
    '''returns int\n\n
    getQueuedJobCount()\n
    '''
def Traverse():
    '''returns List<TraversalState>\n\n
    Traverse(final MboRemote startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    Traverse(final Iterator<MboRemote> startNodesIterator, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    Traverse(final String jobName, final MboRemote startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    Traverse(final MboSetRemote startNodes, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    Traverse(final String jobName, final MboSetRemote startNodes, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    Traverse(final Collection<MboRemote> startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    Traverse(final String jobName, final Object startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    '''
def Process():
    '''returns List<TraversalState>\n\n
    Process(final String jobName, final Object startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)\n
    '''
def dumpThreadStates():
    '''returns None\n\n
    dumpThreadStates()\n
    '''
def uncaughtException():
    '''returns None\n\n
    uncaughtException(final Thread t, final Throwable e)\n
    '''
def waitForFinish():
    '''returns None\n\n
    waitForFinish()\n
    '''
def ():
    '''returns Worker\n\n
    (final String jobGuid, final String jobName, final ITraversableScope controlScope, final ITraversableAction action, final boolean stopOnFailure, final int flags)\n
    (final ThreadGroup group)\n
    '''
def isSatisfied():
    '''returns boolean\n\n
    isSatisfied()\n
    '''
def getWorkQueueSize():
    '''returns int\n\n
    getWorkQueueSize()\n
    '''
def submitJobWork():
    '''returns None\n\n
    submitJobWork(final Object jobWork)\n
    '''
def submitNewWork():
    '''returns None\n\n
    submitNewWork(final MboRemote node)\n
    submitNewWork(final Collection<MboRemote> collection)\n
    submitNewWork(final mboSetContainer newWork)\n
    submitNewWork(final Iterator<MboRemote> newWork)\n
    '''
def getMaxAllowedWorkers():
    '''returns int\n\n
    getMaxAllowedWorkers()\n
    '''
def getJobGuid():
    '''returns String\n\n
    getJobGuid()\n
    '''
def setJobGuid():
    '''returns None\n\n
    setJobGuid(final String jobGuid)\n
    '''
def getControlScope():
    '''returns ITraversableScope\n\n
    getControlScope()\n
    '''
def setControlScope():
    '''returns None\n\n
    setControlScope(final ITraversableScope controlScope)\n
    '''
def getAction():
    '''returns ITraversableAction\n\n
    getAction()\n
    '''
def getWorkItem():
    '''returns None\n\n
    getWorkItem(final int threadsPerJob, final Worker worker, final boolean doCheck)\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final ITraversableAction action)\n
    '''
def getWorkerCount():
    '''returns int\n\n
    getWorkerCount()\n
    '''
def getMaxWorkers():
    '''returns int\n\n
    getMaxWorkers()\n
    '''
def getLastStartTime():
    '''returns long\n\n
    getLastStartTime()\n
    '''
def addWorker():
    '''returns None\n\n
    addWorker(final Worker worker)\n
    '''
def removeWorker():
    '''returns None\n\n
    removeWorker(final Worker worker)\n
    '''
def addFailedState():
    '''returns None\n\n
    addFailedState(final TraversalState state)\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def getStartNode():
    '''returns MboRemote\n\n
    getStartNode()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def activateWorker():
    '''returns None\n\n
    activateWorker()\n
    '''
def getRunTime():
    '''returns long\n\n
    getRunTime()\n
    '''
def getWorkerId():
    '''returns String\n\n
    getWorkerId()\n
    '''
def dumpMyStack():
    '''returns None\n\n
    dumpMyStack()\n
    '''
