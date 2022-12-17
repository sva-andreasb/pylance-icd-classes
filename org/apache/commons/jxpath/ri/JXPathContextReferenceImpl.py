USE_SOFT_CACHE = "boolean  true"
def ():
    '''returns JXPathContextReferenceImpl\n\n
    (final JXPathContext parentContext, final Object contextBean, final Pointer contextPointer)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object a, final Object b)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final String xpath)\n
    getValue(final String xpath, final Expression expr)\n
    getValue(final String xpath, final Class requiredType)\n
    getValue(final String xpath, final Expression expr, final Class requiredType)\n
    '''
def iterate():
    '''returns Iterator\n\n
    iterate(final String xpath)\n
    iterate(final String xpath, final Expression expr)\n
    '''
def getPointer():
    '''returns Pointer\n\n
    getPointer(final String xpath)\n
    getPointer(final String xpath, final Expression expr)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String xpath, final Object value)\n
    setValue(final String xpath, final Expression expr, final Object value)\n
    '''
def createPath():
    '''returns Pointer\n\n
    createPath(final String xpath)\n
    createPath(final String xpath, final Expression expr)\n
    '''
def createPathAndSetValue():
    '''returns Pointer\n\n
    createPathAndSetValue(final String xpath, final Object value)\n
    createPathAndSetValue(final String xpath, final Expression expr, final Object value)\n
    '''
def iteratePointers():
    '''returns Iterator\n\n
    iteratePointers(final String xpath)\n
    iteratePointers(final String xpath, final Expression expr)\n
    '''
def removePath():
    '''returns None\n\n
    removePath(final String xpath)\n
    removePath(final String xpath, final Expression expr)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll(final String xpath)\n
    removeAll(final String xpath, final Expression expr)\n
    '''
def getRelativeContext():
    '''returns JXPathContext\n\n
    getRelativeContext(final Pointer pointer)\n
    '''
def getAbsoluteRootContext():
    '''returns EvalContext\n\n
    getAbsoluteRootContext()\n
    '''
def getVariablePointer():
    '''returns NodePointer\n\n
    getVariablePointer(final QName name)\n
    '''
def getFunction():
    '''returns Function\n\n
    getFunction(final QName functionName, final Object[] parameters)\n
    '''
