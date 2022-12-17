def removeProperty():
    '''returns boolean\n\n
    removeProperty(final String propName)\n
    '''
def addProperty():
    '''returns boolean\n\n
    addProperty(final BeanPropertyDefinition def)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final PropertyName name)\n
    '''
def findProperty():
    '''returns BeanPropertyDefinition\n\n
    findProperty(final PropertyName name)\n
    '''
def getClassInfo():
    '''returns AnnotatedClass\n\n
    getClassInfo()\n
    '''
def getObjectIdInfo():
    '''returns ObjectIdInfo\n\n
    getObjectIdInfo()\n
    '''
def findProperties():
    '''returns List<BeanPropertyDefinition>\n\n
    findProperties()\n
    '''
def findJsonValueMethod():
    '''returns AnnotatedMethod\n\n
    findJsonValueMethod()\n
    '''
def findJsonValueAccessor():
    '''returns AnnotatedMember\n\n
    findJsonValueAccessor()\n
    '''
def getIgnoredPropertyNames():
    '''returns Set<String>\n\n
    getIgnoredPropertyNames()\n
    '''
def hasKnownClassAnnotations():
    '''returns boolean\n\n
    hasKnownClassAnnotations()\n
    '''
def getClassAnnotations():
    '''returns Annotations\n\n
    getClassAnnotations()\n
    '''
def bindingsForBeanType():
    '''returns TypeBindings\n\n
    bindingsForBeanType()\n
    '''
def resolveType():
    '''returns JavaType\n\n
    resolveType(final Type jdkType)\n
    '''
def findDefaultConstructor():
    '''returns AnnotatedConstructor\n\n
    findDefaultConstructor()\n
    '''
def findAnySetterAccessor():
    '''returns AnnotatedMember\n\n
    findAnySetterAccessor()\n
    '''
def getConstructors():
    '''returns List<AnnotatedConstructor>\n\n
    getConstructors()\n
    '''
def instantiateBean():
    '''returns Object\n\n
    instantiateBean(final boolean fixAccess)\n
    '''
def findMethod():
    '''returns AnnotatedMethod\n\n
    findMethod(final String name, final Class<?>[] paramTypes)\n
    '''
def findAnyGetter():
    '''returns AnnotatedMember\n\n
    findAnyGetter()\n
    '''
def findBackReferences():
    '''returns List<BeanPropertyDefinition>\n\n
    findBackReferences()\n
    '''
def getFactoryMethods():
    '''returns List<AnnotatedMethod>\n\n
    getFactoryMethods()\n
    '''
def findFactoryMethod():
    '''returns Method\n\n
    findFactoryMethod(final Class<?>... expArgTypes)\n
    '''
def findClassDescription():
    '''returns String\n\n
    findClassDescription()\n
    '''
