def ():
    '''returns ConfigurationMonitor\n\n
    (final ConfigurationScheduler scheduler)\n
    (final long lastModifiedMillis, final Watcher watcher)\n
    '''
def checkFiles():
    '''returns None\n\n
    checkFiles()\n
    '''
def getId():
    '''returns UUID\n\n
    getId()\n
    '''
def getIntervalSeconds():
    '''returns int\n\n
    getIntervalSeconds()\n
    '''
def hasEventListeners():
    '''returns boolean\n\n
    hasEventListeners()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    reset(final File file)\n
    reset(final Source source)\n
    '''
def setIntervalSeconds():
    '''returns None\n\n
    setIntervalSeconds(final int intervalSeconds)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns boolean\n\n
    stop(final long timeout, final TimeUnit timeUnit)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def unwatch():
    '''returns None\n\n
    unwatch(final Source source)\n
    '''
def unwatchFile():
    '''returns None\n\n
    unwatchFile(final File file)\n
    '''
def watch():
    '''returns None\n\n
    watch(final Source source, final Watcher watcher)\n
    '''
def watchFile():
    '''returns None\n\n
    watchFile(final File file, final FileWatcher fileWatcher)\n
    '''
def getWatcher():
    '''returns Watcher\n\n
    getWatcher()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
