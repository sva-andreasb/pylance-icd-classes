def getInstance():
    '''public static CallContextCache getInstance()
    '''
def getCallContext():
    '''public final CallContext getCallContext(final Type returnType, final Type[] parameterTypes, final CallingConvention convention)
    public final CallContext getCallContext(final Type returnType, final Type[] parameterTypes, final CallingConvention convention, final boolean saveErrno)
    public final CallContext getCallContext(final Type returnType, final Type[] parameterTypes, final CallingConvention convention, final boolean saveErrno, final boolean faultProtect)
    '''
def CallContextRef():
    '''public CallContextRef(final Signature signature, final CallContext ctx, final ReferenceQueue<CallContext> queue)
    '''
def Signature():
    '''public Signature(final Type returnType, final Type[] parameterTypes, final CallingConvention convention, final boolean saveErrno, final boolean faultProtect)
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def hashCode():
    '''public int hashCode()
    '''
