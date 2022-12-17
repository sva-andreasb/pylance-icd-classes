def ():
    '''returns JndiTemplate\n\n
    ()\n
    (final Properties environment)\n
    '''
def setEnvironment():
    '''returns None\n\n
    setEnvironment(final Properties environment)\n
    '''
def getEnvironment():
    '''returns Properties\n\n
    getEnvironment()\n
    '''
def execute():
    '''returns Object\n\n
    execute(final JndiCallback contextCallback)\n
    '''
def lookup():
    '''returns Object\n\n
    lookup(final String name)\n
    lookup(final String name, final Class requiredType)\n
    '''
def doInContext():
    '''returns Object\n\n
    doInContext(final Context ctx)\n
    doInContext(final Context ctx)\n
    doInContext(final Context ctx)\n
    doInContext(final Context ctx)\n
    '''
def bind():
    '''returns None\n\n
    bind(final String name, final Object object)\n
    '''
def rebind():
    '''returns None\n\n
    rebind(final String name, final Object object)\n
    '''
def unbind():
    '''returns None\n\n
    unbind(final String name)\n
    '''
