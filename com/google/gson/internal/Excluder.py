def ():
    '''returns Excluder\n\n
    ()\n
    '''
def withVersion():
    '''returns Excluder\n\n
    withVersion(final double ignoreVersionsAfter)\n
    '''
def withModifiers():
    '''returns Excluder\n\n
    withModifiers(final int... modifiers)\n
    '''
def disableInnerClassSerialization():
    '''returns Excluder\n\n
    disableInnerClassSerialization()\n
    '''
def excludeFieldsWithoutExposeAnnotation():
    '''returns Excluder\n\n
    excludeFieldsWithoutExposeAnnotation()\n
    '''
def withExclusionStrategy():
    '''returns Excluder\n\n
    withExclusionStrategy(final ExclusionStrategy exclusionStrategy, final boolean serialization, final boolean deserialization)\n
    '''
def read():
    '''returns T\n\n
    read(final JsonReader in)\n
    '''
def write():
    '''returns None\n\n
    write(final JsonWriter out, final T value)\n
    '''
def excludeField():
    '''returns boolean\n\n
    excludeField(final Field field, final boolean serialize)\n
    '''
def excludeClass():
    '''returns boolean\n\n
    excludeClass(final Class<?> clazz, final boolean serialize)\n
    '''
