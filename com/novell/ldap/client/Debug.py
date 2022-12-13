LDAP_DEBUG = "boolean  false"
all = "String  TraceAll""
rawInput = "String  RawInput""
rawOutput = "String  RawOutput""
referrals = "String  Referrals""
messages = "String  Messages""
apiRequests = "String  APIRequests""
bindSemaphore = "String  BindSemaphore""
controls = "String  Controls""
asn1 = "String  ASN1""
encoding = "String  Encoding""
decoding = "String  Decoding""
connections = "String  Connections""
saslBind = "String  SaslBind""
TLS = "String  TraceTLS""
urlParse = "String  UrlParse""
buffer = "String  DumpBuffer""
objects = "String  DumpObject""
objectHierarchy = "String  DumpObjectHierarchy""
objectConstructors = "String  DumpObjectConstructors""
objectFields = "String  DumpObjectFields""
objectMethods = "String  DumpObjectMethods""
traceInstructions = "String  VMTraceInstructions""
traceMethodCalls = "String  VMTraceMethodCalls""
EventsCalls = "String  EventsTrace""
def trace():
'''public static final boolean trace(final String s)
public static final void trace(final String s, final String s2)
'''
pass
def setTraceStream():
'''public static final void setTraceStream(final PrintStream debugOut)
'''
pass
def setTrace():
'''public static final void setTrace(final String s, final boolean b)
'''
pass
def VMtraceInstructions():
'''public static final boolean VMtraceInstructions()
public static final void VMtraceInstructions(final boolean b)
'''
pass
def VMtraceMethodCalls():
'''public static final boolean VMtraceMethodCalls()
public static void VMtraceMethodCalls(final boolean b)
'''
pass
def totalMemory():
'''public static final long totalMemory()
'''
pass
def freeMemory():
'''public static final long freeMemory()
'''
pass
def dumpObject():
'''public static final boolean dumpObject()
public static final void dumpObject(final Object o)
'''
pass
def setDumpObject():
'''public static final void setDumpObject(final boolean b)
'''
pass
def dumpObjectHierarchy():
'''public static final boolean dumpObjectHierarchy()
'''
pass
def setDumpObjectHierarchy():
'''public static final void setDumpObjectHierarchy(final boolean b)
'''
pass
def dumpObjectConstructors():
'''public static final boolean dumpObjectConstructors()
'''
pass
def setDumpObjectConstructors():
'''public static final void setDumpObjectConstructors(final boolean b)
'''
pass
def dumpObjectFields():
'''public static final boolean dumpObjectFields()
'''
pass
def setDumpObjectFields():
'''public static final void setDumpObjectFields(final boolean b)
'''
pass
def dumpObjectMethods():
'''public static final boolean dumpObjectMethods()
'''
pass
def setDumpObjectMethods():
'''public static final void setDumpObjectMethods(final boolean b)
'''
pass
def dumpBuffer():
'''public static final boolean dumpBuffer()
public static final void dumpBuffer(final String s, final byte[] array, final int n, final int n2)
'''
pass
def setDumpBuffer():
'''public static final void setDumpBuffer(final boolean b)
'''
pass
