def ():
    '''returns ConstructorArgumentValues\n\n
    ()\n
    (final ConstructorArgumentValues other)\n
    '''
def addArgumentValues():
    '''returns None\n\n
    addArgumentValues(final ConstructorArgumentValues other)\n
    '''
def addIndexedArgumentValue():
    '''returns None\n\n
    addIndexedArgumentValue(final int index, final Object value)\n
    addIndexedArgumentValue(final int index, final Object value, final String type)\n
    '''
def getIndexedArgumentValue():
    '''returns ValueHolder\n\n
    getIndexedArgumentValue(final int index, final Class requiredType)\n
    '''
def getIndexedArgumentValues():
    '''returns Map\n\n
    getIndexedArgumentValues()\n
    '''
def addGenericArgumentValue():
    '''returns None\n\n
    addGenericArgumentValue(final Object value)\n
    addGenericArgumentValue(final Object value, final String type)\n
    '''
def getGenericArgumentValue():
    '''returns ValueHolder\n\n
    getGenericArgumentValue(final Class requiredType)\n
    getGenericArgumentValue(final Class requiredType, final Set usedValueHolders)\n
    '''
def getGenericArgumentValues():
    '''returns List\n\n
    getGenericArgumentValues()\n
    '''
def getArgumentValue():
    '''returns ValueHolder\n\n
    getArgumentValue(final int index, final Class requiredType)\n
    getArgumentValue(final int index, final Class requiredType, final Set usedValueHolders)\n
    '''
def getArgumentCount():
    '''returns int\n\n
    getArgumentCount()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def setType():
    '''returns None\n\n
    setType(final String type)\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
