def ConfigurationScheduler():
    '''public ConfigurationScheduler()
    public ConfigurationScheduler(final String name)
    '''
def start():
    '''public void start()
    '''
def stop():
    '''public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def isExecutorServiceSet():
    '''public boolean isExecutorServiceSet()
    '''
def incrementScheduledItems():
    '''public void incrementScheduledItems()
    '''
def decrementScheduledItems():
    '''public void decrementScheduledItems()
    '''
def schedule():
    '''public <V> ScheduledFuture<V> schedule(final Callable<V> callable, final long delay, final TimeUnit unit)
    '''
def nextFireInterval():
    '''public long nextFireInterval(final Date fireDate)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def CronRunnable():
    '''public CronRunnable(final Runnable runnable, final CronExpression cronExpression)
    '''
def setScheduledFuture():
    '''public void setScheduledFuture(final CronScheduledFuture<?> future)
    '''
def run():
    '''public void run()
    '''
