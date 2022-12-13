PLUGIN_NAME = "String  \"Console\""
def createAppender():
    '''public static ConsoleAppender createAppender(Layout<? extends Serializable> layout, final Filter filter, final String targetStr, final String name, final String follow, final String ignore)
    public static ConsoleAppender createAppender(Layout<? extends Serializable> layout, final Filter filter, Target target, final String name, final boolean follow, final boolean direct, final boolean ignoreExceptions)
    '''
def createDefaultAppenderForLayout():
    '''public static ConsoleAppender createDefaultAppenderForLayout(final Layout<? extends Serializable> layout)
    '''
def newBuilder():
    '''public static <B extends Builder<B>> B newBuilder()
    '''
def getTarget():
    '''public Target getTarget()
    '''
def getDefaultCharset():
    '''public Charset getDefaultCharset()
    public Charset getDefaultCharset()
    '''
def Builder():
    '''public Builder()
    '''
def setTarget():
    '''public B setTarget(final Target aTarget)
    '''
def setFollow():
    '''public B setFollow(final boolean shouldFollow)
    '''
def setDirect():
    '''public B setDirect(final boolean shouldDirect)
    '''
def build():
    '''public ConsoleAppender build()
    '''
def SystemErrStream():
    '''public SystemErrStream()
    '''
def close():
    '''public void close()
    public void close()
    '''
def flush():
    '''public void flush()
    public void flush()
    '''
def write():
    '''public void write(final byte[] b)
    public void write(final byte[] b, final int off, final int len)
    public void write(final int b)
    public void write(final byte[] b)
    public void write(final byte[] b, final int off, final int len)
    public void write(final int b)
    '''
def SystemOutStream():
    '''public SystemOutStream()
    '''
def FactoryData():
    '''public FactoryData(final OutputStream os, final String type, final Layout<? extends Serializable> layout)
    '''
def createManager():
    '''public OutputStreamManager createManager(final String name, final FactoryData data)
    '''
