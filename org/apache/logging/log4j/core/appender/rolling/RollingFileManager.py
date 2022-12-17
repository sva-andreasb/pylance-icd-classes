def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def addRolloverListener():
    '''returns None\n\n
    addRolloverListener(final RolloverListener listener)\n
    '''
def removeRolloverListener():
    '''returns None\n\n
    removeRolloverListener(final RolloverListener listener)\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def isDirectWrite():
    '''returns boolean\n\n
    isDirectWrite()\n
    '''
def getFileExtension():
    '''returns FileExtension\n\n
    getFileExtension()\n
    '''
def isRenameEmptyFiles():
    '''returns boolean\n\n
    isRenameEmptyFiles()\n
    '''
def setRenameEmptyFiles():
    '''returns None\n\n
    setRenameEmptyFiles(final boolean renameEmptyFiles)\n
    '''
def getFileSize():
    '''returns long\n\n
    getFileSize()\n
    '''
def getFileTime():
    '''returns long\n\n
    getFileTime()\n
    '''
def releaseSub():
    '''returns boolean\n\n
    releaseSub(final long timeout, final TimeUnit timeUnit)\n
    '''
def getPatternProcessor():
    '''returns PatternProcessor\n\n
    getPatternProcessor()\n
    '''
def setTriggeringPolicy():
    '''returns None\n\n
    setTriggeringPolicy(final TriggeringPolicy triggeringPolicy)\n
    '''
def setRolloverStrategy():
    '''returns None\n\n
    setRolloverStrategy(final RolloverStrategy rolloverStrategy)\n
    '''
def setPatternProcessor():
    '''returns None\n\n
    setPatternProcessor(final PatternProcessor patternProcessor)\n
    '''
def getRolloverStrategy():
    '''returns RolloverStrategy\n\n
    getRolloverStrategy()\n
    getRolloverStrategy()\n
    '''
def updateData():
    '''returns None\n\n
    updateData(final Object data)\n
    '''
def ():
    '''returns FactoryData\n\n
    (final Action act, final RollingFileManager manager)\n
    (final String fileName, final String pattern, final boolean append, final boolean bufferedIO, final TriggeringPolicy policy, final RolloverStrategy strategy, final String advertiseURI, final Layout<? extends Serializable> layout, final int bufferSize, final boolean immediateFlush, final boolean createOnDemand, final String filePermissions, final String fileOwner, final String fileGroup, final Configuration configuration)\n
    '''
def execute():
    '''returns boolean\n\n
    execute()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isComplete():
    '''returns boolean\n\n
    isComplete()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getTriggeringPolicy():
    '''returns TriggeringPolicy\n\n
    getTriggeringPolicy()\n
    '''
def getPattern():
    '''returns String\n\n
    getPattern()\n
    '''
def createManager():
    '''returns RollingFileManager\n\n
    createManager(final String name, final FactoryData data)\n
    '''
def remainingCapacity():
    '''returns int\n\n
    remainingCapacity()\n
    '''
def add():
    '''returns boolean\n\n
    add(final Runnable runnable)\n
    '''
def put():
    '''returns None\n\n
    put(final Runnable runnable)\n
    '''
def offer():
    '''returns boolean\n\n
    offer(final Runnable runnable, final long timeout, final TimeUnit timeUnit)\n
    '''
def addAll():
    '''returns boolean\n\n
    addAll(final Collection<? extends Runnable> collection)\n
    '''
