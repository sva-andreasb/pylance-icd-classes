PLUGIN_NAME = "String  Console""
def createAppender():
'''public static ConsoleAppender createAppender(Layout<? extends Serializable> layout, final Filter filter, final String targetStr, final String name, final String follow, final String ignore)
public static ConsoleAppender createAppender(Layout<? extends Serializable> layout, final Filter filter, Target target, final String name, final boolean follow, final boolean direct, final boolean ignoreExceptions)
'''
pass
def createDefaultAppenderForLayout():
'''public static ConsoleAppender createDefaultAppenderForLayout(final Layout<? extends Serializable> layout)
'''
pass
def newBuilder():
'''public static <B extends Builder<B>> B newBuilder()
'''
pass
def getTarget():
'''public Target getTarget()
'''
pass
def getDefaultCharset():
'''public Charset getDefaultCharset()
public Charset getDefaultCharset()
'''
pass
def Builder():
'''public Builder()
'''
pass
def setTarget():
'''public B setTarget(final Target aTarget)
'''
pass
def setFollow():
'''public B setFollow(final boolean shouldFollow)
'''
pass
def setDirect():
'''public B setDirect(final boolean shouldDirect)
'''
pass
def build():
'''public ConsoleAppender build()
'''
pass
def SystemErrStream():
'''public SystemErrStream()
'''
pass
def close():
'''public void close()
public void close()
'''
pass
def flush():
'''public void flush()
public void flush()
'''
pass
def write():
'''public void write(final byte[] b)
public void write(final byte[] b, final int off, final int len)
public void write(final int b)
public void write(final byte[] b)
public void write(final byte[] b, final int off, final int len)
public void write(final int b)
'''
pass
def SystemOutStream():
'''public SystemOutStream()
'''
pass
def FactoryData():
'''public FactoryData(final OutputStream os, final String type, final Layout<? extends Serializable> layout)
'''
pass
def createManager():
'''public OutputStreamManager createManager(final String name, final FactoryData data)
'''
pass
