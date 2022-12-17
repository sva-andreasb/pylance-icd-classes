def setClassLoader():
    '''returns None\n\n
    setClassLoader(final ClassLoader aLoader)\n
    '''
def setWorld():
    '''returns None\n\n
    setWorld(final World aWorld)\n
    '''
def getAnnotation():
    '''returns Object\n\n
    getAnnotation(final ResolvedType annotationType, final Object onObject)\n
    '''
def getAnnotationFromClass():
    '''returns Object\n\n
    getAnnotationFromClass(final ResolvedType annotationType, final Class aClass)\n
    '''
def getAnnotationFromMember():
    '''returns Object\n\n
    getAnnotationFromMember(final ResolvedType annotationType, final Member aMember)\n
    '''
def getAnnotationOfType():
    '''returns AnnotationAJ\n\n
    getAnnotationOfType(final UnresolvedType ofType, final Member onMember)\n
    '''
def getAnnotationDefaultValue():
    '''returns String\n\n
    getAnnotationDefaultValue(final Member onMember)\n
    '''
def getAnnotations():
    '''returns ResolvedType[]\n\n
    getAnnotations(final Member onMember)\n
    getAnnotations(final Class forClass, final World inWorld)\n
    '''
def getParameterNames():
    '''returns String[]\n\n
    getParameterNames(final Member forMember)\n
    '''
def getParameterAnnotationTypes():
    '''returns ResolvedType[][]\n\n
    getParameterAnnotationTypes(final Member onMember)\n
    '''
