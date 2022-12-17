TYPE_ARRAY_LIST = "int  1"
TYPE_HASH_MAP = "int  2"
TYPE_LINKED_HASH_MAP = "int  3"
def ():
    '''returns StdTypeConstructor\n\n
    (final BeanDescription beanDesc, final MapperConfig<?> config)\n
    (final AnnotatedWithParams base, final int t)\n
    '''
def constructValueInstantiator():
    '''returns ValueInstantiator\n\n
    constructValueInstantiator(final DeserializationContext ctxt)\n
    '''
def setDefaultCreator():
    '''returns None\n\n
    setDefaultCreator(final AnnotatedWithParams creator)\n
    '''
def addStringCreator():
    '''returns None\n\n
    addStringCreator(final AnnotatedWithParams creator, final boolean explicit)\n
    '''
def addIntCreator():
    '''returns None\n\n
    addIntCreator(final AnnotatedWithParams creator, final boolean explicit)\n
    '''
def addLongCreator():
    '''returns None\n\n
    addLongCreator(final AnnotatedWithParams creator, final boolean explicit)\n
    '''
def addDoubleCreator():
    '''returns None\n\n
    addDoubleCreator(final AnnotatedWithParams creator, final boolean explicit)\n
    '''
def addBooleanCreator():
    '''returns None\n\n
    addBooleanCreator(final AnnotatedWithParams creator, final boolean explicit)\n
    '''
def addDelegatingCreator():
    '''returns None\n\n
    addDelegatingCreator(final AnnotatedWithParams creator, final boolean explicit, final SettableBeanProperty[] injectables, final int delegateeIndex)\n
    '''
def addPropertyCreator():
    '''returns None\n\n
    addPropertyCreator(final AnnotatedWithParams creator, final boolean explicit, final SettableBeanProperty[] properties)\n
    '''
def hasDefaultCreator():
    '''returns boolean\n\n
    hasDefaultCreator()\n
    '''
def hasDelegatingCreator():
    '''returns boolean\n\n
    hasDelegatingCreator()\n
    '''
def hasPropertyBasedCreator():
    '''returns boolean\n\n
    hasPropertyBasedCreator()\n
    '''
def getParameterCount():
    '''returns int\n\n
    getParameterCount()\n
    '''
def getParameterType():
    '''returns JavaType\n\n
    getParameterType(final int index)\n
    '''
def getGenericParameterType():
    '''returns Type\n\n
    getGenericParameterType(final int index)\n
    '''
def call():
    '''returns Object\n\n
    call()\n
    call(final Object[] args)\n
    '''
def call1():
    '''returns Object\n\n
    call1(final Object arg)\n
    '''
def getMember():
    '''returns Member\n\n
    getMember()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object pojo, final Object value)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final Object pojo)\n
    '''
def withAnnotations():
    '''returns Annotated\n\n
    withAnnotations(final AnnotationMap fallback)\n
    '''
def getAnnotated():
    '''returns AnnotatedElement\n\n
    getAnnotated()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getType():
    '''returns JavaType\n\n
    getType()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
