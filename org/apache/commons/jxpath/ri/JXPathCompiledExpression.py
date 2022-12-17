def ():
    '''returns JXPathCompiledExpression\n\n
    (final String xpath, final Expression expression)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final JXPathContext context)\n
    getValue(final JXPathContext context, final Class requiredType)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final JXPathContext context, final Object value)\n
    '''
def createPath():
    '''returns Pointer\n\n
    createPath(final JXPathContext context)\n
    '''
def createPathAndSetValue():
    '''returns Pointer\n\n
    createPathAndSetValue(final JXPathContext context, final Object value)\n
    '''
def iterate():
    '''returns Iterator\n\n
    iterate(final JXPathContext context)\n
    '''
def getPointer():
    '''returns Pointer\n\n
    getPointer(final JXPathContext context, final String xpath)\n
    '''
def iteratePointers():
    '''returns Iterator\n\n
    iteratePointers(final JXPathContext context)\n
    '''
def removePath():
    '''returns None\n\n
    removePath(final JXPathContext context)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll(final JXPathContext context)\n
    '''
