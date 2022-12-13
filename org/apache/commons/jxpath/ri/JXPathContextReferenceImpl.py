USE_SOFT_CACHE = "boolean  true"
def JXPathContextReferenceImpl():
'''public JXPathContextReferenceImpl(final JXPathContext parentContext, final Object contextBean, final Pointer contextPointer)
'''
pass
def compare():
'''public int compare(final Object a, final Object b)
'''
pass
def addNodePointerFactory():
'''public static void addNodePointerFactory(final NodePointerFactory factory)
'''
pass
def getNodePointerFactories():
'''public static NodePointerFactory[] getNodePointerFactories()
'''
pass
def getValue():
'''public Object getValue(final String xpath)
public Object getValue(final String xpath, final Expression expr)
public Object getValue(final String xpath, final Class requiredType)
public Object getValue(final String xpath, final Expression expr, final Class requiredType)
'''
pass
def iterate():
'''public Iterator iterate(final String xpath)
public Iterator iterate(final String xpath, final Expression expr)
'''
pass
def getPointer():
'''public Pointer getPointer(final String xpath)
public Pointer getPointer(final String xpath, final Expression expr)
'''
pass
def setValue():
'''public void setValue(final String xpath, final Object value)
public void setValue(final String xpath, final Expression expr, final Object value)
'''
pass
def createPath():
'''public Pointer createPath(final String xpath)
public Pointer createPath(final String xpath, final Expression expr)
'''
pass
def createPathAndSetValue():
'''public Pointer createPathAndSetValue(final String xpath, final Object value)
public Pointer createPathAndSetValue(final String xpath, final Expression expr, final Object value)
'''
pass
def iteratePointers():
'''public Iterator iteratePointers(final String xpath)
public Iterator iteratePointers(final String xpath, final Expression expr)
'''
pass
def removePath():
'''public void removePath(final String xpath)
public void removePath(final String xpath, final Expression expr)
'''
pass
def removeAll():
'''public void removeAll(final String xpath)
public void removeAll(final String xpath, final Expression expr)
'''
pass
def getRelativeContext():
'''public JXPathContext getRelativeContext(final Pointer pointer)
'''
pass
def getContextPointer():
'''public synchronized Pointer getContextPointer()
'''
pass
def getAbsoluteRootContext():
'''public EvalContext getAbsoluteRootContext()
'''
pass
def getVariablePointer():
'''public NodePointer getVariablePointer(final QName name)
'''
pass
def getFunction():
'''public Function getFunction(final QName functionName, final Object[] parameters)
'''
pass
def allocateConditionally():
'''public static Object allocateConditionally(final String className, final String existenceCheckClassName)
'''
pass
