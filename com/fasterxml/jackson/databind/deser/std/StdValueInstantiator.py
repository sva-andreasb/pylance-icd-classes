def StdValueInstantiator():
'''public StdValueInstantiator(final DeserializationConfig config, final Class<?> valueType)
public StdValueInstantiator(final DeserializationConfig config, final JavaType valueType)
'''
pass
def configureFromObjectSettings():
'''public void configureFromObjectSettings(final AnnotatedWithParams defaultCreator, final AnnotatedWithParams delegateCreator, final JavaType delegateType, final SettableBeanProperty[] delegateArgs, final AnnotatedWithParams withArgsCreator, final SettableBeanProperty[] constructorArgs)
'''
pass
def configureFromArraySettings():
'''public void configureFromArraySettings(final AnnotatedWithParams arrayDelegateCreator, final JavaType arrayDelegateType, final SettableBeanProperty[] arrayDelegateArgs)
'''
pass
def configureFromStringCreator():
'''public void configureFromStringCreator(final AnnotatedWithParams creator)
'''
pass
def configureFromIntCreator():
'''public void configureFromIntCreator(final AnnotatedWithParams creator)
'''
pass
def configureFromLongCreator():
'''public void configureFromLongCreator(final AnnotatedWithParams creator)
'''
pass
def configureFromDoubleCreator():
'''public void configureFromDoubleCreator(final AnnotatedWithParams creator)
'''
pass
def configureFromBooleanCreator():
'''public void configureFromBooleanCreator(final AnnotatedWithParams creator)
'''
pass
def configureIncompleteParameter():
'''public void configureIncompleteParameter(final AnnotatedParameter parameter)
'''
pass
def getValueTypeDesc():
'''public String getValueTypeDesc()
'''
pass
def canCreateFromString():
'''public boolean canCreateFromString()
'''
pass
def canCreateFromInt():
'''public boolean canCreateFromInt()
'''
pass
def canCreateFromLong():
'''public boolean canCreateFromLong()
'''
pass
def canCreateFromDouble():
'''public boolean canCreateFromDouble()
'''
pass
def canCreateFromBoolean():
'''public boolean canCreateFromBoolean()
'''
pass
def canCreateUsingDefault():
'''public boolean canCreateUsingDefault()
'''
pass
def canCreateUsingDelegate():
'''public boolean canCreateUsingDelegate()
'''
pass
def canCreateUsingArrayDelegate():
'''public boolean canCreateUsingArrayDelegate()
'''
pass
def canCreateFromObjectWith():
'''public boolean canCreateFromObjectWith()
'''
pass
def canInstantiate():
'''public boolean canInstantiate()
'''
pass
def getDelegateType():
'''public JavaType getDelegateType(final DeserializationConfig config)
'''
pass
def getArrayDelegateType():
'''public JavaType getArrayDelegateType(final DeserializationConfig config)
'''
pass
def getFromObjectArguments():
'''public SettableBeanProperty[] getFromObjectArguments(final DeserializationConfig config)
'''
pass
def createUsingDefault():
'''public Object createUsingDefault(final DeserializationContext ctxt)
'''
pass
def createFromObjectWith():
'''public Object createFromObjectWith(final DeserializationContext ctxt, final Object[] args)
'''
pass
def createUsingDelegate():
'''public Object createUsingDelegate(final DeserializationContext ctxt, final Object delegate)
'''
pass
def createUsingArrayDelegate():
'''public Object createUsingArrayDelegate(final DeserializationContext ctxt, final Object delegate)
'''
pass
def createFromString():
'''public Object createFromString(final DeserializationContext ctxt, final String value)
'''
pass
def createFromInt():
'''public Object createFromInt(final DeserializationContext ctxt, final int value)
'''
pass
def createFromLong():
'''public Object createFromLong(final DeserializationContext ctxt, final long value)
'''
pass
def createFromDouble():
'''public Object createFromDouble(final DeserializationContext ctxt, final double value)
'''
pass
def createFromBoolean():
'''public Object createFromBoolean(final DeserializationContext ctxt, final boolean value)
'''
pass
def getDelegateCreator():
'''public AnnotatedWithParams getDelegateCreator()
'''
pass
def getArrayDelegateCreator():
'''public AnnotatedWithParams getArrayDelegateCreator()
'''
pass
def getDefaultCreator():
'''public AnnotatedWithParams getDefaultCreator()
'''
pass
def getWithArgsCreator():
'''public AnnotatedWithParams getWithArgsCreator()
'''
pass
def getIncompleteParameter():
'''public AnnotatedParameter getIncompleteParameter()
'''
pass
