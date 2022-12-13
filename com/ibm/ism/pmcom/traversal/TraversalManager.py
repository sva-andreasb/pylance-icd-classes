TM_FLAG_NONE = "int  0"
TM_FLAG_IGNORE_ERRORS = "int  1"
TM_FLAG_RUN_ASYNCHRONOUSLY = "int  2"
TM_FLAG_QUEUEABLE_JOB = "int  4"
TM_FLAG_IA_DUP_CHECK = "int  8"
def getInstance():
    '''    public static synchronized TraversalManager getInstance()
    '''
def getQueuedJobs():
    '''    public ConcurrentLinkedQueue<Controller> getQueuedJobs()
    '''
def isJobQueued():
    '''    public boolean isJobQueued(final String jobName)
    '''
def getQueuedJobCount():
    '''    public int getQueuedJobCount()
    '''
def Traverse():
    '''    public List<TraversalState> Traverse(final MboRemote startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    public List<TraversalState> Traverse(final Iterator<MboRemote> startNodesIterator, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    public List<TraversalState> Traverse(final String jobName, final MboRemote startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    public List<TraversalState> Traverse(final MboSetRemote startNodes, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    public List<TraversalState> Traverse(final String jobName, final MboSetRemote startNodes, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    public List<TraversalState> Traverse(final Collection<MboRemote> startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    public List<TraversalState> Traverse(final String jobName, final Object startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    '''
def Process():
    '''    public List<TraversalState> Process(final String jobName, final Object startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
    '''
def dumpThreadStates():
    '''    public void dumpThreadStates()
    '''
def uncaughtException():
    '''    public void uncaughtException(final Thread t, final Throwable e)
    '''
def waitForFinish():
    '''    public void waitForFinish()
    '''
def Controller():
    '''    public Controller(final String jobGuid, final String jobName, final ITraversableScope controlScope, final ITraversableAction action, final boolean stopOnFailure, final int flags)
    '''
def isSatisfied():
    '''    public boolean isSatisfied()
    '''
def getWorkQueueSize():
    '''    public int getWorkQueueSize()
    '''
def getVisited():
    '''    public ConcurrentHashMap<String, String> getVisited()
    '''
def submitJobWork():
    '''    public void submitJobWork(final Object jobWork)
    '''
def submitNewWork():
    '''    public void submitNewWork(final MboRemote node)
    public void submitNewWork(final Collection<MboRemote> collection)
    public void submitNewWork(final mboSetContainer newWork)
    public void submitNewWork(final Iterator<MboRemote> newWork)
    '''
def getMaxAllowedWorkers():
    '''    public int getMaxAllowedWorkers()
    '''
def getJobGuid():
    '''    public String getJobGuid()
    '''
def setJobGuid():
    '''    public void setJobGuid(final String jobGuid)
    '''
def getControlScope():
    '''    public ITraversableScope getControlScope()
    '''
def setControlScope():
    '''    public void setControlScope(final ITraversableScope controlScope)
    '''
def getAction():
    '''    public ITraversableAction getAction()
    '''
def getWorkItem():
    '''    public void getWorkItem(final int threadsPerJob, final Worker worker, final boolean doCheck)
    '''
def setAction():
    '''    public void setAction(final ITraversableAction action)
    '''
def getWorkerCount():
    '''    public int getWorkerCount()
    '''
def getMaxWorkers():
    '''    public int getMaxWorkers()
    '''
def getLastStartTime():
    '''    public long getLastStartTime()
    '''
def addWorker():
    '''    public void addWorker(final Worker worker)
    '''
def removeWorker():
    '''    public void removeWorker(final Worker worker)
    '''
def addFailedState():
    '''    public void addFailedState(final TraversalState state)
    '''
def isCancelled():
    '''    public boolean isCancelled()
    '''
def getStartNode():
    '''    public MboRemote getStartNode()
    '''
def run():
    '''    public void run()
    public void run()
    '''
def Worker():
    '''    public Worker(final ThreadGroup group)
    '''
def activateWorker():
    '''    public void activateWorker()
    '''
def getRunTime():
    '''    public long getRunTime()
    '''
def getWorkerId():
    '''    public String getWorkerId()
    '''
def dumpMyStack():
    '''    public void dumpMyStack()
    '''
