def ():
    '''returns BasicClassIntrospector\n\n
    ()\n
    '''
def copy():
    '''returns ClassIntrospector\n\n
    copy()\n
    '''
def forSerialization():
    '''returns BasicBeanDescription\n\n
    forSerialization(final SerializationConfig cfg, final JavaType type, final MixInResolver r)\n
    '''
def forDeserialization():
    '''returns BasicBeanDescription\n\n
    forDeserialization(final DeserializationConfig cfg, final JavaType type, final MixInResolver r)\n
    '''
def forDeserializationWithBuilder():
    '''returns BasicBeanDescription\n\n
    forDeserializationWithBuilder(final DeserializationConfig cfg, final JavaType type, final MixInResolver r)\n
    '''
def forCreation():
    '''returns BasicBeanDescription\n\n
    forCreation(final DeserializationConfig cfg, final JavaType type, final MixInResolver r)\n
    '''
def forClassAnnotations():
    '''returns BasicBeanDescription\n\n
    forClassAnnotations(final MapperConfig<?> config, final JavaType type, final MixInResolver r)\n
    '''
def forDirectClassAnnotations():
    '''returns BasicBeanDescription\n\n
    forDirectClassAnnotations(final MapperConfig<?> config, final JavaType type, final MixInResolver r)\n
    '''
