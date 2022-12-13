PLUGIN_NAME = "String  RollingFile""
def stop():
'''public boolean stop(final long timeout, final TimeUnit timeUnit)
'''
pass
def append():
'''public void append(final LogEvent event)
'''
pass
def getFileName():
'''public String getFileName()
public String getFileName()
'''
pass
def getFilePattern():
'''public String getFilePattern()
public String getFilePattern()
'''
pass
def getTriggeringPolicy():
'''public <T extends TriggeringPolicy> T getTriggeringPolicy()
'''
pass
def createAppender():
'''public static <B extends Builder<B>> RollingFileAppender createAppender(final String fileName, final String filePattern, final String append, final String name, final String bufferedIO, final String bufferSizeStr, final String immediateFlush, final TriggeringPolicy policy, final RolloverStrategy strategy, final Layout<? extends Serializable> layout, final Filter filter, final String ignore, final String advertise, final String advertiseUri, final Configuration config)
'''
pass
def newBuilder():
'''public static <B extends Builder<B>> B newBuilder()
'''
pass
def Builder():
'''public Builder()
'''
pass
def build():
'''public RollingFileAppender build()
'''
pass
def getAdvertiseUri():
'''public String getAdvertiseUri()
'''
pass
def isAdvertise():
'''public boolean isAdvertise()
'''
pass
def isAppend():
'''public boolean isAppend()
'''
pass
def isCreateOnDemand():
'''public boolean isCreateOnDemand()
'''
pass
def isLocking():
'''public boolean isLocking()
'''
pass
def getFilePermissions():
'''public String getFilePermissions()
'''
pass
def getFileOwner():
'''public String getFileOwner()
'''
pass
def getFileGroup():
'''public String getFileGroup()
'''
pass
def withAdvertise():
'''public B withAdvertise(final boolean advertise)
'''
pass
def withAdvertiseUri():
'''public B withAdvertiseUri(final String advertiseUri)
'''
pass
def withAppend():
'''public B withAppend(final boolean append)
'''
pass
def withFileName():
'''public B withFileName(final String fileName)
'''
pass
def withCreateOnDemand():
'''public B withCreateOnDemand(final boolean createOnDemand)
'''
pass
def withLocking():
'''public B withLocking(final boolean locking)
'''
pass
def getPolicy():
'''public TriggeringPolicy getPolicy()
'''
pass
def getStrategy():
'''public RolloverStrategy getStrategy()
'''
pass
def withFilePattern():
'''public B withFilePattern(final String filePattern)
'''
pass
def withPolicy():
'''public B withPolicy(final TriggeringPolicy policy)
'''
pass
def withStrategy():
'''public B withStrategy(final RolloverStrategy strategy)
'''
pass
def withFilePermissions():
'''public B withFilePermissions(final String filePermissions)
'''
pass
def withFileOwner():
'''public B withFileOwner(final String fileOwner)
'''
pass
def withFileGroup():
'''public B withFileGroup(final String fileGroup)
'''
pass
