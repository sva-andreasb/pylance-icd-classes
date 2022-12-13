LDAP_DEBUG = "boolean  false"
all = "String  \"TraceAll\""
rawInput = "String  \"RawInput\""
rawOutput = "String  \"RawOutput\""
referrals = "String  \"Referrals\""
messages = "String  \"Messages\""
apiRequests = "String  \"APIRequests\""
bindSemaphore = "String  \"BindSemaphore\""
controls = "String  \"Controls\""
asn1 = "String  \"ASN1\""
encoding = "String  \"Encoding\""
decoding = "String  \"Decoding\""
connections = "String  \"Connections\""
saslBind = "String  \"SaslBind\""
TLS = "String  \"TraceTLS\""
urlParse = "String  \"UrlParse\""
buffer = "String  \"DumpBuffer\""
objects = "String  \"DumpObject\""
objectHierarchy = "String  \"DumpObjectHierarchy\""
objectConstructors = "String  \"DumpObjectConstructors\""
objectFields = "String  \"DumpObjectFields\""
objectMethods = "String  \"DumpObjectMethods\""
traceInstructions = "String  \"VMTraceInstructions\""
traceMethodCalls = "String  \"VMTraceMethodCalls\""
EventsCalls = "String  \"EventsTrace\""
def trace():
    '''    public static final boolean trace(final String s)
    public static final void trace(final String s, final String s2)
    '''
def setTraceStream():
    '''    public static final void setTraceStream(final PrintStream debugOut)
    '''
def setTrace():
    '''    public static final void setTrace(final String s, final boolean b)
    '''
def VMtraceInstructions():
    '''    public static final boolean VMtraceInstructions()
    public static final void VMtraceInstructions(final boolean b)
    '''
def VMtraceMethodCalls():
    '''    public static final boolean VMtraceMethodCalls()
    public static void VMtraceMethodCalls(final boolean b)
    '''
def totalMemory():
    '''    public static final long totalMemory()
    '''
def freeMemory():
    '''    public static final long freeMemory()
    '''
def dumpObject():
    '''    public static final boolean dumpObject()
    public static final void dumpObject(final Object o)
    '''
def setDumpObject():
    '''    public static final void setDumpObject(final boolean b)
    '''
def dumpObjectHierarchy():
    '''    public static final boolean dumpObjectHierarchy()
    '''
def setDumpObjectHierarchy():
    '''    public static final void setDumpObjectHierarchy(final boolean b)
    '''
def dumpObjectConstructors():
    '''    public static final boolean dumpObjectConstructors()
    '''
def setDumpObjectConstructors():
    '''    public static final void setDumpObjectConstructors(final boolean b)
    '''
def dumpObjectFields():
    '''    public static final boolean dumpObjectFields()
    '''
def setDumpObjectFields():
    '''    public static final void setDumpObjectFields(final boolean b)
    '''
def dumpObjectMethods():
    '''    public static final boolean dumpObjectMethods()
    '''
def setDumpObjectMethods():
    '''    public static final void setDumpObjectMethods(final boolean b)
    '''
def dumpBuffer():
    '''    public static final boolean dumpBuffer()
    public static final void dumpBuffer(final String s, final byte[] array, final int n, final int n2)
    '''
def setDumpBuffer():
    '''    public static final void setDumpBuffer(final boolean b)
    '''
