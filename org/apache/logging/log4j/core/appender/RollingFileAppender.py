PLUGIN_NAME = "String  \"RollingFile\""
def stop():
    '''public boolean stop(final long timeout, final TimeUnit timeUnit)
    '''
def append():
    '''public void append(final LogEvent event)
    '''
def getFileName():
    '''public String getFileName()
    public String getFileName()
    '''
def getFilePattern():
    '''public String getFilePattern()
    public String getFilePattern()
    '''
def getTriggeringPolicy():
    '''public <T extends TriggeringPolicy> T getTriggeringPolicy()
    '''
def createAppender():
    '''public static <B extends Builder<B>> RollingFileAppender createAppender(final String fileName, final String filePattern, final String append, final String name, final String bufferedIO, final String bufferSizeStr, final String immediateFlush, final TriggeringPolicy policy, final RolloverStrategy strategy, final Layout<? extends Serializable> layout, final Filter filter, final String ignore, final String advertise, final String advertiseUri, final Configuration config)
    '''
def newBuilder():
    '''public static <B extends Builder<B>> B newBuilder()
    '''
def Builder():
    '''public Builder()
    '''
def build():
    '''public RollingFileAppender build()
    '''
def getAdvertiseUri():
    '''public String getAdvertiseUri()
    '''
def isAdvertise():
    '''public boolean isAdvertise()
    '''
def isAppend():
    '''public boolean isAppend()
    '''
def isCreateOnDemand():
    '''public boolean isCreateOnDemand()
    '''
def isLocking():
    '''public boolean isLocking()
    '''
def getFilePermissions():
    '''public String getFilePermissions()
    '''
def getFileOwner():
    '''public String getFileOwner()
    '''
def getFileGroup():
    '''public String getFileGroup()
    '''
def withAdvertise():
    '''public B withAdvertise(final boolean advertise)
    '''
def withAdvertiseUri():
    '''public B withAdvertiseUri(final String advertiseUri)
    '''
def withAppend():
    '''public B withAppend(final boolean append)
    '''
def withFileName():
    '''public B withFileName(final String fileName)
    '''
def withCreateOnDemand():
    '''public B withCreateOnDemand(final boolean createOnDemand)
    '''
def withLocking():
    '''public B withLocking(final boolean locking)
    '''
def getPolicy():
    '''public TriggeringPolicy getPolicy()
    '''
def getStrategy():
    '''public RolloverStrategy getStrategy()
    '''
def withFilePattern():
    '''public B withFilePattern(final String filePattern)
    '''
def withPolicy():
    '''public B withPolicy(final TriggeringPolicy policy)
    '''
def withStrategy():
    '''public B withStrategy(final RolloverStrategy strategy)
    '''
def withFilePermissions():
    '''public B withFilePermissions(final String filePermissions)
    '''
def withFileOwner():
    '''public B withFileOwner(final String fileOwner)
    '''
def withFileGroup():
    '''public B withFileGroup(final String fileGroup)
    '''
