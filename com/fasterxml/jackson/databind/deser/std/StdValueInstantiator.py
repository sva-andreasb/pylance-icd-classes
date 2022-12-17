def ():
    '''returns StdValueInstantiator\n\n
    (final DeserializationConfig config, final Class<?> valueType)\n
    (final DeserializationConfig config, final JavaType valueType)\n
    '''
def configureFromObjectSettings():
    '''returns None\n\n
    configureFromObjectSettings(final AnnotatedWithParams defaultCreator, final AnnotatedWithParams delegateCreator, final JavaType delegateType, final SettableBeanProperty[] delegateArgs, final AnnotatedWithParams withArgsCreator, final SettableBeanProperty[] constructorArgs)\n
    '''
def configureFromArraySettings():
    '''returns None\n\n
    configureFromArraySettings(final AnnotatedWithParams arrayDelegateCreator, final JavaType arrayDelegateType, final SettableBeanProperty[] arrayDelegateArgs)\n
    '''
def configureFromStringCreator():
    '''returns None\n\n
    configureFromStringCreator(final AnnotatedWithParams creator)\n
    '''
def configureFromIntCreator():
    '''returns None\n\n
    configureFromIntCreator(final AnnotatedWithParams creator)\n
    '''
def configureFromLongCreator():
    '''returns None\n\n
    configureFromLongCreator(final AnnotatedWithParams creator)\n
    '''
def configureFromDoubleCreator():
    '''returns None\n\n
    configureFromDoubleCreator(final AnnotatedWithParams creator)\n
    '''
def configureFromBooleanCreator():
    '''returns None\n\n
    configureFromBooleanCreator(final AnnotatedWithParams creator)\n
    '''
def configureIncompleteParameter():
    '''returns None\n\n
    configureIncompleteParameter(final AnnotatedParameter parameter)\n
    '''
def getValueTypeDesc():
    '''returns String\n\n
    getValueTypeDesc()\n
    '''
def canCreateFromString():
    '''returns boolean\n\n
    canCreateFromString()\n
    '''
def canCreateFromInt():
    '''returns boolean\n\n
    canCreateFromInt()\n
    '''
def canCreateFromLong():
    '''returns boolean\n\n
    canCreateFromLong()\n
    '''
def canCreateFromDouble():
    '''returns boolean\n\n
    canCreateFromDouble()\n
    '''
def canCreateFromBoolean():
    '''returns boolean\n\n
    canCreateFromBoolean()\n
    '''
def canCreateUsingDefault():
    '''returns boolean\n\n
    canCreateUsingDefault()\n
    '''
def canCreateUsingDelegate():
    '''returns boolean\n\n
    canCreateUsingDelegate()\n
    '''
def canCreateUsingArrayDelegate():
    '''returns boolean\n\n
    canCreateUsingArrayDelegate()\n
    '''
def canCreateFromObjectWith():
    '''returns boolean\n\n
    canCreateFromObjectWith()\n
    '''
def canInstantiate():
    '''returns boolean\n\n
    canInstantiate()\n
    '''
def getDelegateType():
    '''returns JavaType\n\n
    getDelegateType(final DeserializationConfig config)\n
    '''
def getArrayDelegateType():
    '''returns JavaType\n\n
    getArrayDelegateType(final DeserializationConfig config)\n
    '''
def getFromObjectArguments():
    '''returns SettableBeanProperty[]\n\n
    getFromObjectArguments(final DeserializationConfig config)\n
    '''
def createUsingDefault():
    '''returns Object\n\n
    createUsingDefault(final DeserializationContext ctxt)\n
    '''
def createFromObjectWith():
    '''returns Object\n\n
    createFromObjectWith(final DeserializationContext ctxt, final Object[] args)\n
    '''
def createUsingDelegate():
    '''returns Object\n\n
    createUsingDelegate(final DeserializationContext ctxt, final Object delegate)\n
    '''
def createUsingArrayDelegate():
    '''returns Object\n\n
    createUsingArrayDelegate(final DeserializationContext ctxt, final Object delegate)\n
    '''
def createFromString():
    '''returns Object\n\n
    createFromString(final DeserializationContext ctxt, final String value)\n
    '''
def createFromInt():
    '''returns Object\n\n
    createFromInt(final DeserializationContext ctxt, final int value)\n
    '''
def createFromLong():
    '''returns Object\n\n
    createFromLong(final DeserializationContext ctxt, final long value)\n
    '''
def createFromDouble():
    '''returns Object\n\n
    createFromDouble(final DeserializationContext ctxt, final double value)\n
    '''
def createFromBoolean():
    '''returns Object\n\n
    createFromBoolean(final DeserializationContext ctxt, final boolean value)\n
    '''
def getDelegateCreator():
    '''returns AnnotatedWithParams\n\n
    getDelegateCreator()\n
    '''
def getArrayDelegateCreator():
    '''returns AnnotatedWithParams\n\n
    getArrayDelegateCreator()\n
    '''
def getDefaultCreator():
    '''returns AnnotatedWithParams\n\n
    getDefaultCreator()\n
    '''
def getWithArgsCreator():
    '''returns AnnotatedWithParams\n\n
    getWithArgsCreator()\n
    '''
def getIncompleteParameter():
    '''returns AnnotatedParameter\n\n
    getIncompleteParameter()\n
    '''
