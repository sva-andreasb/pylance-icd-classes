def StdValueInstantiator():
    '''public StdValueInstantiator(final DeserializationConfig config, final Class<?> valueType)
    public StdValueInstantiator(final DeserializationConfig config, final JavaType valueType)
    '''
def configureFromObjectSettings():
    '''public void configureFromObjectSettings(final AnnotatedWithParams defaultCreator, final AnnotatedWithParams delegateCreator, final JavaType delegateType, final SettableBeanProperty[] delegateArgs, final AnnotatedWithParams withArgsCreator, final SettableBeanProperty[] constructorArgs)
    '''
def configureFromArraySettings():
    '''public void configureFromArraySettings(final AnnotatedWithParams arrayDelegateCreator, final JavaType arrayDelegateType, final SettableBeanProperty[] arrayDelegateArgs)
    '''
def configureFromStringCreator():
    '''public void configureFromStringCreator(final AnnotatedWithParams creator)
    '''
def configureFromIntCreator():
    '''public void configureFromIntCreator(final AnnotatedWithParams creator)
    '''
def configureFromLongCreator():
    '''public void configureFromLongCreator(final AnnotatedWithParams creator)
    '''
def configureFromDoubleCreator():
    '''public void configureFromDoubleCreator(final AnnotatedWithParams creator)
    '''
def configureFromBooleanCreator():
    '''public void configureFromBooleanCreator(final AnnotatedWithParams creator)
    '''
def configureIncompleteParameter():
    '''public void configureIncompleteParameter(final AnnotatedParameter parameter)
    '''
def getValueTypeDesc():
    '''public String getValueTypeDesc()
    '''
def canCreateFromString():
    '''public boolean canCreateFromString()
    '''
def canCreateFromInt():
    '''public boolean canCreateFromInt()
    '''
def canCreateFromLong():
    '''public boolean canCreateFromLong()
    '''
def canCreateFromDouble():
    '''public boolean canCreateFromDouble()
    '''
def canCreateFromBoolean():
    '''public boolean canCreateFromBoolean()
    '''
def canCreateUsingDefault():
    '''public boolean canCreateUsingDefault()
    '''
def canCreateUsingDelegate():
    '''public boolean canCreateUsingDelegate()
    '''
def canCreateUsingArrayDelegate():
    '''public boolean canCreateUsingArrayDelegate()
    '''
def canCreateFromObjectWith():
    '''public boolean canCreateFromObjectWith()
    '''
def canInstantiate():
    '''public boolean canInstantiate()
    '''
def getDelegateType():
    '''public JavaType getDelegateType(final DeserializationConfig config)
    '''
def getArrayDelegateType():
    '''public JavaType getArrayDelegateType(final DeserializationConfig config)
    '''
def getFromObjectArguments():
    '''public SettableBeanProperty[] getFromObjectArguments(final DeserializationConfig config)
    '''
def createUsingDefault():
    '''public Object createUsingDefault(final DeserializationContext ctxt)
    '''
def createFromObjectWith():
    '''public Object createFromObjectWith(final DeserializationContext ctxt, final Object[] args)
    '''
def createUsingDelegate():
    '''public Object createUsingDelegate(final DeserializationContext ctxt, final Object delegate)
    '''
def createUsingArrayDelegate():
    '''public Object createUsingArrayDelegate(final DeserializationContext ctxt, final Object delegate)
    '''
def createFromString():
    '''public Object createFromString(final DeserializationContext ctxt, final String value)
    '''
def createFromInt():
    '''public Object createFromInt(final DeserializationContext ctxt, final int value)
    '''
def createFromLong():
    '''public Object createFromLong(final DeserializationContext ctxt, final long value)
    '''
def createFromDouble():
    '''public Object createFromDouble(final DeserializationContext ctxt, final double value)
    '''
def createFromBoolean():
    '''public Object createFromBoolean(final DeserializationContext ctxt, final boolean value)
    '''
def getDelegateCreator():
    '''public AnnotatedWithParams getDelegateCreator()
    '''
def getArrayDelegateCreator():
    '''public AnnotatedWithParams getArrayDelegateCreator()
    '''
def getDefaultCreator():
    '''public AnnotatedWithParams getDefaultCreator()
    '''
def getWithArgsCreator():
    '''public AnnotatedWithParams getWithArgsCreator()
    '''
def getIncompleteParameter():
    '''public AnnotatedParameter getIncompleteParameter()
    '''
