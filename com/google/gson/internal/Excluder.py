def Excluder():
    '''public Excluder()
    '''
def withVersion():
    '''public Excluder withVersion(final double ignoreVersionsAfter)
    '''
def withModifiers():
    '''public Excluder withModifiers(final int... modifiers)
    '''
def disableInnerClassSerialization():
    '''public Excluder disableInnerClassSerialization()
    '''
def excludeFieldsWithoutExposeAnnotation():
    '''public Excluder excludeFieldsWithoutExposeAnnotation()
    '''
def withExclusionStrategy():
    '''public Excluder withExclusionStrategy(final ExclusionStrategy exclusionStrategy, final boolean serialization, final boolean deserialization)
    '''
def create():
    '''public <T> TypeAdapter<T> create(final Gson gson, final TypeToken<T> type)
    '''
def read():
    '''public T read(final JsonReader in)
    '''
def write():
    '''public void write(final JsonWriter out, final T value)
    '''
def excludeField():
    '''public boolean excludeField(final Field field, final boolean serialize)
    '''
def excludeClass():
    '''public boolean excludeClass(final Class<?> clazz, final boolean serialize)
    '''
