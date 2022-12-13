TIME = "int  1"
MILLIS = "int  2"
THREAD_NAME = "int  4"
OBJECT = "int  8"
TRACE_NORMAL = "int  15"
TRACE_MINIMAL = "int  9"
def isOn():
'''public static final boolean isOn()
'''
pass
def setMethodTraceThreshold():
'''public static final void setMethodTraceThreshold(final int methodTraceThreshold)
'''
pass
def setTraceLevel():
'''public static final void setTraceLevel(final int n)
'''
pass
def getTraceLevel():
'''public static final int getTraceLevel()
'''
pass
def turnMethodTracingOff():
'''public static final void turnMethodTracingOff()
'''
pass
def turnMethodTracingOn():
'''public static final void turnMethodTracingOn()
'''
pass
def turnTracingOff():
'''public static final void turnTracingOff()
'''
pass
def turnTracingOn():
'''public static final void turnTracingOn()
public static final void turnTracingOn(final int traceLevel)
'''
pass
def setTraceStream():
'''public static final void setTraceStream(final FileWriter out)
public static final void setTraceStream(final PrintWriter trc)
'''
pass
def getTraceStream():
'''public static final PrintWriter getTraceStream()
'''
pass
def setFormat():
'''public static final void setFormat(final int n)
'''
pass
def dataTrace():
'''public static final void dataTrace(final int n, final Object o, final byte[] array)
'''
pass
def dumpCallStack():
'''public static final void dumpCallStack()
'''
pass
def entry():
'''public static final void entry(final int n, final Object o, final String s)
public static final void entry(final int n, final String s, final String s2)
public static final void entry(final Object o, final String s)
public static final void entry(final String s, final String s2)
'''
pass
def exit():
'''public static final void exit(final int n, final Object o, final String s)
public static final void exit(final int n, final String s, final String s2)
public static final void exit(final Object o, final String s)
public static final void exit(final String s, final String s2)
'''
pass
def trace():
'''public static final void trace(final int n, final Object o, final String s)
public static final void trace(final int n, final String s, final String s2)
public static final void trace(final Object o, final String s)
public static final void trace(final String s, final String s2)
'''
pass
