def ():
    '''returns SimpleMixInResolver\n\n
    (final ClassIntrospector.MixInResolver overrides)\n
    '''
def withOverrides():
    '''returns SimpleMixInResolver\n\n
    withOverrides(final ClassIntrospector.MixInResolver overrides)\n
    '''
def withoutLocalDefinitions():
    '''returns SimpleMixInResolver\n\n
    withoutLocalDefinitions()\n
    '''
def setLocalDefinitions():
    '''returns None\n\n
    setLocalDefinitions(final Map<Class<?>, Class<?>> sourceMixins)\n
    '''
def addLocalDefinition():
    '''returns None\n\n
    addLocalDefinition(final Class<?> target, final Class<?> mixinSource)\n
    '''
def copy():
    '''returns SimpleMixInResolver\n\n
    copy()\n
    '''
def localSize():
    '''returns int\n\n
    localSize()\n
    '''
