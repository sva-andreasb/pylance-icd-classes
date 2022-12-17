def hasFieldAnnotation():
    '''returns boolean\n\n
    hasFieldAnnotation(final Class<? extends Annotation> annotationType, final VariableElement f)\n
    '''
def hasClassAnnotation():
    '''returns boolean\n\n
    hasClassAnnotation(final TypeElement clazz, final Class<? extends Annotation> annotationType)\n
    '''
def getAllFieldAnnotations():
    '''returns Annotation[]\n\n
    getAllFieldAnnotations(final VariableElement field, final Locatable srcPos)\n
    '''
def hasMethodAnnotation():
    '''returns boolean\n\n
    hasMethodAnnotation(final Class<? extends Annotation> a, final ExecutableElement method)\n
    '''
def getAllMethodAnnotations():
    '''returns Annotation[]\n\n
    getAllMethodAnnotations(final ExecutableElement method, final Locatable srcPos)\n
    '''
def getClassValue():
    '''returns TypeMirror\n\n
    getClassValue(final Annotation a, final String name)\n
    '''
def getClassArrayValue():
    '''returns TypeMirror[]\n\n
    getClassArrayValue(final Annotation a, final String name)\n
    '''
