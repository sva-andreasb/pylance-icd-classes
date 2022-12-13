def CronTaskManager():
    '''public CronTaskManager()
    public CronTaskManager(final MXServer mxServer)
    '''
def configFromProperties():
    '''public void configFromProperties()
    '''
def configure():
    '''public synchronized void configure(final Properties configData)
    '''
def config():
    '''public synchronized void config(final Properties configData)
    '''
def suspendCrontasks():
    '''public void suspendCrontasks()
    '''
def resumeCrontasks():
    '''public synchronized void resumeCrontasks()
    '''
def isReadyForAdminMode():
    '''public boolean isReadyForAdminMode()
    '''
def activeCronThreads():
    '''public Enumeration activeCronThreads()
    '''
def loadCrontask():
    '''public void loadCrontask(final String taskName, final String instanceName, final String className)
    '''
def initialzeCronTaskInfo():
    '''public synchronized boolean initialzeCronTaskInfo(final String taskName, final String instanceName)
    '''
def insertFirstRowIntoTask():
    '''public synchronized void insertFirstRowIntoTask(final String task)
    '''
def updateLastEnd():
    '''public synchronized int updateLastEnd(final CronTask cron, final String taskName, final String instanceName)
    '''
def updateTaskInfoByAnotherServer():
    '''public synchronized int updateTaskInfoByAnotherServer(final CronTask cron, final String taskName, final String instanceName)
    '''
def getLastTaskInfo():
    '''public synchronized Date[] getLastTaskInfo(final CronTask cron, final String taskName, final String instanceName)
    '''
def getLastRunTime():
    '''public synchronized Date getLastRunTime(final CronTask cron, final String taskName, final String instanceName)
    '''
def init():
    '''public synchronized void init()
    '''
def destroy():
    '''public synchronized void destroy()
    '''
def shutdown():
    '''public synchronized void shutdown()
    '''
def isShutdown():
    '''public synchronized boolean isShutdown()
    '''
def add():
    '''public synchronized void add(final CronTask newTask, final String taskName, final String instanceName)
    '''
def remove():
    '''public synchronized void remove(final CronTask task, final String taskName, final String instanceName)
    '''
def get():
    '''public synchronized CronTask get(final String name, final String instanceName)
    '''
def isSleeping():
    '''public synchronized boolean isSleeping(final String taskName, final String instanceName)
    '''
def restart():
    '''public void restart()
    '''
def handleAutoRemoval():
    '''public void handleAutoRemoval(final CronTask cronTask)
    '''
def getInstanceMbo():
    '''public CrontaskInstanceRemote getInstanceMbo(final String taskName, final String instanceName)
    '''
def deactivate():
    '''public void deactivate(final String taskName, final String instName)
    public void deactivate(final String key)
    '''
def activate():
    '''public void activate(final CrontaskInstanceRemote inst)
    '''
def runTenantsChanged():
    '''public void runTenantsChanged()
    '''
def logSql():
    '''public void logSql(final String sql, final Connection con)
    '''
def setLastKPICronTaskRun():
    '''public void setLastKPICronTaskRun()
    '''
def getLastKPICronTaskRun():
    '''public Date getLastKPICronTaskRun()
    '''
def eventValidate():
    '''public boolean eventValidate(final EventMessage em)
    '''
def preSaveEventAction():
    '''public void preSaveEventAction(final EventMessage em)
    '''
def eventAction():
    '''public void eventAction(final EventMessage em)
    '''
def postCommitEventAction():
    '''public void postCommitEventAction(final EventMessage em)
    '''
def markShutdown():
    '''public void markShutdown()
    '''
def isMarkedForShutDown():
    '''public boolean isMarkedForShutDown()
    '''
def startTask():
    '''public void startTask()
    '''
def run():
    '''public void run()
    public void run()
    public void run()
    public void run()
    '''
def MonitorThread():
    '''public MonitorThread(final CronTaskManager cm)
    '''
def removeDeadSessions():
    '''public void removeDeadSessions()
    '''
def removeDeadTenantSessions():
    '''public void removeDeadTenantSessions()
    '''
def printTaskSchedulerInfo():
    '''public void printTaskSchedulerInfo()
    '''
def CronIncrementThread():
    '''public CronIncrementThread()
    '''
