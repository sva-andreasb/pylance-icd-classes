def CronTaskManager():
'''public CronTaskManager()
public CronTaskManager(final MXServer mxServer)
'''
pass
def configFromProperties():
'''public void configFromProperties()
'''
pass
def configure():
'''public synchronized void configure(final Properties configData)
'''
pass
def config():
'''public synchronized void config(final Properties configData)
'''
pass
def suspendCrontasks():
'''public void suspendCrontasks()
'''
pass
def resumeCrontasks():
'''public synchronized void resumeCrontasks()
'''
pass
def isReadyForAdminMode():
'''public boolean isReadyForAdminMode()
'''
pass
def activeCronThreads():
'''public Enumeration activeCronThreads()
'''
pass
def loadCrontask():
'''public void loadCrontask(final String taskName, final String instanceName, final String className)
'''
pass
def initialzeCronTaskInfo():
'''public synchronized boolean initialzeCronTaskInfo(final String taskName, final String instanceName)
'''
pass
def insertFirstRowIntoTask():
'''public synchronized void insertFirstRowIntoTask(final String task)
'''
pass
def updateLastEnd():
'''public synchronized int updateLastEnd(final CronTask cron, final String taskName, final String instanceName)
'''
pass
def updateTaskInfoByAnotherServer():
'''public synchronized int updateTaskInfoByAnotherServer(final CronTask cron, final String taskName, final String instanceName)
'''
pass
def getLastTaskInfo():
'''public synchronized Date[] getLastTaskInfo(final CronTask cron, final String taskName, final String instanceName)
'''
pass
def getLastRunTime():
'''public synchronized Date getLastRunTime(final CronTask cron, final String taskName, final String instanceName)
'''
pass
def init():
'''public synchronized void init()
'''
pass
def destroy():
'''public synchronized void destroy()
'''
pass
def shutdown():
'''public synchronized void shutdown()
'''
pass
def isShutdown():
'''public synchronized boolean isShutdown()
'''
pass
def add():
'''public synchronized void add(final CronTask newTask, final String taskName, final String instanceName)
'''
pass
def remove():
'''public synchronized void remove(final CronTask task, final String taskName, final String instanceName)
'''
pass
def get():
'''public synchronized CronTask get(final String name, final String instanceName)
'''
pass
def isSleeping():
'''public synchronized boolean isSleeping(final String taskName, final String instanceName)
'''
pass
def restart():
'''public void restart()
'''
pass
def handleAutoRemoval():
'''public void handleAutoRemoval(final CronTask cronTask)
'''
pass
def getInstanceMbo():
'''public CrontaskInstanceRemote getInstanceMbo(final String taskName, final String instanceName)
'''
pass
def deactivate():
'''public void deactivate(final String taskName, final String instName)
public void deactivate(final String key)
'''
pass
def activate():
'''public void activate(final CrontaskInstanceRemote inst)
'''
pass
def runTenantsChanged():
'''public void runTenantsChanged()
'''
pass
def logSql():
'''public void logSql(final String sql, final Connection con)
'''
pass
def setLastKPICronTaskRun():
'''public void setLastKPICronTaskRun()
'''
pass
def getLastKPICronTaskRun():
'''public Date getLastKPICronTaskRun()
'''
pass
def eventValidate():
'''public boolean eventValidate(final EventMessage em)
'''
pass
def preSaveEventAction():
'''public void preSaveEventAction(final EventMessage em)
'''
pass
def eventAction():
'''public void eventAction(final EventMessage em)
'''
pass
def postCommitEventAction():
'''public void postCommitEventAction(final EventMessage em)
'''
pass
def markShutdown():
'''public void markShutdown()
'''
pass
def isMarkedForShutDown():
'''public boolean isMarkedForShutDown()
'''
pass
def startTask():
'''public void startTask()
'''
pass
def run():
'''public void run()
public void run()
public void run()
public void run()
'''
pass
def MonitorThread():
'''public MonitorThread(final CronTaskManager cm)
'''
pass
def removeDeadSessions():
'''public void removeDeadSessions()
'''
pass
def removeDeadTenantSessions():
'''public void removeDeadTenantSessions()
'''
pass
def printTaskSchedulerInfo():
'''public void printTaskSchedulerInfo()
'''
pass
def CronIncrementThread():
'''public CronIncrementThread()
'''
pass
