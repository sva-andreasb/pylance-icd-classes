def registerSubtypes():
    '''returns None\n\n
    registerSubtypes(final NamedType... types)\n
    registerSubtypes(final Class<?>... classes)\n
    registerSubtypes(final Collection<Class<?>> subtypes)\n
    '''
def collectAndResolveSubtypesByClass():
    '''returns Collection<NamedType>\n\n
    collectAndResolveSubtypesByClass(final MapperConfig<?> config, final AnnotatedMember property, final JavaType baseType)\n
    collectAndResolveSubtypesByClass(final MapperConfig<?> config, final AnnotatedClass type)\n
    '''
def collectAndResolveSubtypesByTypeId():
    '''returns Collection<NamedType>\n\n
    collectAndResolveSubtypesByTypeId(final MapperConfig<?> config, final AnnotatedMember property, final JavaType baseType)\n
    collectAndResolveSubtypesByTypeId(final MapperConfig<?> config, final AnnotatedClass baseType)\n
    '''
