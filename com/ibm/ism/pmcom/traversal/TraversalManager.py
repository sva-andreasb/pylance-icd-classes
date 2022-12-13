TM_FLAG_NONE = "int 0"
TM_FLAG_IGNORE_ERRORS = "int 1"
TM_FLAG_RUN_ASYNCHRONOUSLY = "int 2"
TM_FLAG_QUEUEABLE_JOB = "int 4"
TM_FLAG_IA_DUP_CHECK = "int 8"
def getInstance():
'''public static synchronized TraversalManager getInstance()
'''
pass
def getQueuedJobs():
'''public ConcurrentLinkedQueue<Controller> getQueuedJobs()
'''
pass
def isJobQueued():
'''public boolean isJobQueued(final String jobName)
'''
pass
def getQueuedJobCount():
'''public int getQueuedJobCount()
'''
pass
def Traverse():
'''public List<TraversalState> Traverse(final MboRemote startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
public List<TraversalState> Traverse(final Iterator<MboRemote> startNodesIterator, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
public List<TraversalState> Traverse(final String jobName, final MboRemote startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
public List<TraversalState> Traverse(final MboSetRemote startNodes, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
public List<TraversalState> Traverse(final String jobName, final MboSetRemote startNodes, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
public List<TraversalState> Traverse(final Collection<MboRemote> startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
public List<TraversalState> Traverse(final String jobName, final Object startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
'''
pass
def Process():
'''public List<TraversalState> Process(final String jobName, final Object startNode, final ITraversableScope traverseScope, final ITraversableAction traverseAction, final int flags)
'''
pass
def dumpThreadStates():
'''public void dumpThreadStates()
'''
pass
def uncaughtException():
'''public void uncaughtException(final Thread t, final Throwable e)
'''
pass
def waitForFinish():
'''public void waitForFinish()
'''
pass
def Controller():
'''public Controller(final String jobGuid, final String jobName, final ITraversableScope controlScope, final ITraversableAction action, final boolean stopOnFailure, final int flags)
'''
pass
def isSatisfied():
'''public boolean isSatisfied()
'''
pass
def getWorkQueueSize():
'''public int getWorkQueueSize()
'''
pass
def getVisited():
'''public ConcurrentHashMap<String, String> getVisited()
'''
pass
def submitJobWork():
'''public void submitJobWork(final Object jobWork)
'''
pass
def submitNewWork():
'''public void submitNewWork(final MboRemote node)
public void submitNewWork(final Collection<MboRemote> collection)
public void submitNewWork(final mboSetContainer newWork)
public void submitNewWork(final Iterator<MboRemote> newWork)
'''
pass
def getMaxAllowedWorkers():
'''public int getMaxAllowedWorkers()
'''
pass
def getJobGuid():
'''public String getJobGuid()
'''
pass
def setJobGuid():
'''public void setJobGuid(final String jobGuid)
'''
pass
def getControlScope():
'''public ITraversableScope getControlScope()
'''
pass
def setControlScope():
'''public void setControlScope(final ITraversableScope controlScope)
'''
pass
def getAction():
'''public ITraversableAction getAction()
'''
pass
def getWorkItem():
'''public void getWorkItem(final int threadsPerJob, final Worker worker, final boolean doCheck)
'''
pass
def setAction():
'''public void setAction(final ITraversableAction action)
'''
pass
def getWorkerCount():
'''public int getWorkerCount()
'''
pass
def getMaxWorkers():
'''public int getMaxWorkers()
'''
pass
def getLastStartTime():
'''public long getLastStartTime()
'''
pass
def addWorker():
'''public void addWorker(final Worker worker)
'''
pass
def removeWorker():
'''public void removeWorker(final Worker worker)
'''
pass
def addFailedState():
'''public void addFailedState(final TraversalState state)
'''
pass
def isCancelled():
'''public boolean isCancelled()
'''
pass
def getStartNode():
'''public MboRemote getStartNode()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def Worker():
'''public Worker(final ThreadGroup group)
'''
pass
def activateWorker():
'''public void activateWorker()
'''
pass
def getRunTime():
'''public long getRunTime()
'''
pass
def getWorkerId():
'''public String getWorkerId()
'''
pass
def dumpMyStack():
'''public void dumpMyStack()
'''
pass
