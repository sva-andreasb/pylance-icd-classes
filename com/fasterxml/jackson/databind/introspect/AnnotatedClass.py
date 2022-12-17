def resolveType():
    '''returns JavaType\n\n
    resolveType(final Type type)\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def hasAnnotation():
    '''returns boolean\n\n
    hasAnnotation(final Class<?> acls)\n
    '''
def hasOneOf():
    '''returns boolean\n\n
    hasOneOf(final Class<? extends Annotation>[] annoClasses)\n
    '''
def annotations():
    '''returns Iterable<Annotation>\n\n
    annotations()\n
    '''
def getType():
    '''returns JavaType\n\n
    getType()\n
    '''
def getAnnotations():
    '''returns Annotations\n\n
    getAnnotations()\n
    '''
def hasAnnotations():
    '''returns boolean\n\n
    hasAnnotations()\n
    '''
def getDefaultConstructor():
    '''returns AnnotatedConstructor\n\n
    getDefaultConstructor()\n
    '''
def getConstructors():
    '''returns List<AnnotatedConstructor>\n\n
    getConstructors()\n
    '''
def getFactoryMethods():
    '''returns List<AnnotatedMethod>\n\n
    getFactoryMethods()\n
    '''
def getStaticMethods():
    '''returns List<AnnotatedMethod>\n\n
    getStaticMethods()\n
    '''
def memberMethods():
    '''returns Iterable<AnnotatedMethod>\n\n
    memberMethods()\n
    '''
def getMemberMethodCount():
    '''returns int\n\n
    getMemberMethodCount()\n
    '''
def findMethod():
    '''returns AnnotatedMethod\n\n
    findMethod(final String name, final Class<?>[] paramTypes)\n
    '''
def getFieldCount():
    '''returns int\n\n
    getFieldCount()\n
    '''
def fields():
    '''returns Iterable<AnnotatedField>\n\n
    fields()\n
    '''
def isNonStaticInnerClass():
    '''returns boolean\n\n
    isNonStaticInnerClass()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def ():
    '''returns Creators\n\n
    (final AnnotatedConstructor defCtor, final List<AnnotatedConstructor> ctors, final List<AnnotatedMethod> ctorMethods)\n
    '''
