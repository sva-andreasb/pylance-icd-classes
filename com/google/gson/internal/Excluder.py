def Excluder():
'''public Excluder()
'''
pass
def withVersion():
'''public Excluder withVersion(final double ignoreVersionsAfter)
'''
pass
def withModifiers():
'''public Excluder withModifiers(final int... modifiers)
'''
pass
def disableInnerClassSerialization():
'''public Excluder disableInnerClassSerialization()
'''
pass
def excludeFieldsWithoutExposeAnnotation():
'''public Excluder excludeFieldsWithoutExposeAnnotation()
'''
pass
def withExclusionStrategy():
'''public Excluder withExclusionStrategy(final ExclusionStrategy exclusionStrategy, final boolean serialization, final boolean deserialization)
'''
pass
def create():
'''public <T> TypeAdapter<T> create(final Gson gson, final TypeToken<T> type)
'''
pass
def read():
'''public T read(final JsonReader in)
'''
pass
def write():
'''public void write(final JsonWriter out, final T value)
'''
pass
def excludeField():
'''public boolean excludeField(final Field field, final boolean serialize)
'''
pass
def excludeClass():
'''public boolean excludeClass(final Class<?> clazz, final boolean serialize)
'''
pass
