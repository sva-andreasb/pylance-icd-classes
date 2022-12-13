TYPE_ARRAY_LIST = "int  1"
TYPE_HASH_MAP = "int  2"
TYPE_LINKED_HASH_MAP = "int  3"
def CreatorCollector():
    '''public CreatorCollector(final BeanDescription beanDesc, final MapperConfig<?> config)
    '''
def constructValueInstantiator():
    '''public ValueInstantiator constructValueInstantiator(final DeserializationContext ctxt)
    '''
def setDefaultCreator():
    '''public void setDefaultCreator(final AnnotatedWithParams creator)
    '''
def addStringCreator():
    '''public void addStringCreator(final AnnotatedWithParams creator, final boolean explicit)
    '''
def addIntCreator():
    '''public void addIntCreator(final AnnotatedWithParams creator, final boolean explicit)
    '''
def addLongCreator():
    '''public void addLongCreator(final AnnotatedWithParams creator, final boolean explicit)
    '''
def addDoubleCreator():
    '''public void addDoubleCreator(final AnnotatedWithParams creator, final boolean explicit)
    '''
def addBooleanCreator():
    '''public void addBooleanCreator(final AnnotatedWithParams creator, final boolean explicit)
    '''
def addDelegatingCreator():
    '''public void addDelegatingCreator(final AnnotatedWithParams creator, final boolean explicit, final SettableBeanProperty[] injectables, final int delegateeIndex)
    '''
def addPropertyCreator():
    '''public void addPropertyCreator(final AnnotatedWithParams creator, final boolean explicit, final SettableBeanProperty[] properties)
    '''
def hasDefaultCreator():
    '''public boolean hasDefaultCreator()
    '''
def hasDelegatingCreator():
    '''public boolean hasDelegatingCreator()
    '''
def hasPropertyBasedCreator():
    '''public boolean hasPropertyBasedCreator()
    '''
def StdTypeConstructor():
    '''public StdTypeConstructor(final AnnotatedWithParams base, final int t)
    '''
def tryToOptimize():
    '''public static AnnotatedWithParams tryToOptimize(final AnnotatedWithParams src)
    '''
def getParameterCount():
    '''public int getParameterCount()
    '''
def getParameterType():
    '''public JavaType getParameterType(final int index)
    '''
def getGenericParameterType():
    '''public Type getGenericParameterType(final int index)
    '''
def call():
    '''public Object call()
    public Object call(final Object[] args)
    '''
def call1():
    '''public Object call1(final Object arg)
    '''
def getMember():
    '''public Member getMember()
    '''
def setValue():
    '''public void setValue(final Object pojo, final Object value)
    '''
def getValue():
    '''public Object getValue(final Object pojo)
    '''
def withAnnotations():
    '''public Annotated withAnnotations(final AnnotationMap fallback)
    '''
def getAnnotated():
    '''public AnnotatedElement getAnnotated()
    '''
def getName():
    '''public String getName()
    '''
def getType():
    '''public JavaType getType()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    '''
