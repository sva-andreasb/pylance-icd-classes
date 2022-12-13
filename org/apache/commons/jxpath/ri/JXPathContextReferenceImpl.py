USE_SOFT_CACHE = "boolean  true"
def JXPathContextReferenceImpl():
    '''public JXPathContextReferenceImpl(final JXPathContext parentContext, final Object contextBean, final Pointer contextPointer)
    '''
def compare():
    '''public int compare(final Object a, final Object b)
    '''
def addNodePointerFactory():
    '''public static void addNodePointerFactory(final NodePointerFactory factory)
    '''
def getNodePointerFactories():
    '''public static NodePointerFactory[] getNodePointerFactories()
    '''
def getValue():
    '''public Object getValue(final String xpath)
    public Object getValue(final String xpath, final Expression expr)
    public Object getValue(final String xpath, final Class requiredType)
    public Object getValue(final String xpath, final Expression expr, final Class requiredType)
    '''
def iterate():
    '''public Iterator iterate(final String xpath)
    public Iterator iterate(final String xpath, final Expression expr)
    '''
def getPointer():
    '''public Pointer getPointer(final String xpath)
    public Pointer getPointer(final String xpath, final Expression expr)
    '''
def setValue():
    '''public void setValue(final String xpath, final Object value)
    public void setValue(final String xpath, final Expression expr, final Object value)
    '''
def createPath():
    '''public Pointer createPath(final String xpath)
    public Pointer createPath(final String xpath, final Expression expr)
    '''
def createPathAndSetValue():
    '''public Pointer createPathAndSetValue(final String xpath, final Object value)
    public Pointer createPathAndSetValue(final String xpath, final Expression expr, final Object value)
    '''
def iteratePointers():
    '''public Iterator iteratePointers(final String xpath)
    public Iterator iteratePointers(final String xpath, final Expression expr)
    '''
def removePath():
    '''public void removePath(final String xpath)
    public void removePath(final String xpath, final Expression expr)
    '''
def removeAll():
    '''public void removeAll(final String xpath)
    public void removeAll(final String xpath, final Expression expr)
    '''
def getRelativeContext():
    '''public JXPathContext getRelativeContext(final Pointer pointer)
    '''
def getContextPointer():
    '''public synchronized Pointer getContextPointer()
    '''
def getAbsoluteRootContext():
    '''public EvalContext getAbsoluteRootContext()
    '''
def getVariablePointer():
    '''public NodePointer getVariablePointer(final QName name)
    '''
def getFunction():
    '''public Function getFunction(final QName functionName, final Object[] parameters)
    '''
def allocateConditionally():
    '''public static Object allocateConditionally(final String className, final String existenceCheckClassName)
    '''
