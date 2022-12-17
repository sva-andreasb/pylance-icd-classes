def ():
    '''returns AjTypeImpl\n\n
    (final Class<T> fromClass)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getPackage():
    '''returns Package\n\n
    getPackage()\n
    '''
def getModifiers():
    '''returns int\n\n
    getModifiers()\n
    '''
def getJavaClass():
    '''returns Class<T>\n\n
    getJavaClass()\n
    '''
def getGenericSupertype():
    '''returns Type\n\n
    getGenericSupertype()\n
    '''
def getEnclosingMethod():
    '''returns Method\n\n
    getEnclosingMethod()\n
    '''
def getEnclosingConstructor():
    '''returns Constructor\n\n
    getEnclosingConstructor()\n
    '''
def getPerClause():
    '''returns PerClause\n\n
    getPerClause()\n
    '''
def isAnnotationPresent():
    '''returns boolean\n\n
    isAnnotationPresent(final Class<? extends Annotation> annotationType)\n
    '''
def getAnnotations():
    '''returns Annotation[]\n\n
    getAnnotations()\n
    '''
def getDeclaredAnnotations():
    '''returns Annotation[]\n\n
    getDeclaredAnnotations()\n
    '''
def getConstructor():
    '''returns Constructor\n\n
    getConstructor(final AjType<?>... parameterTypes)\n
    '''
def getConstructors():
    '''returns Constructor[]\n\n
    getConstructors()\n
    '''
def getDeclaredConstructor():
    '''returns Constructor\n\n
    getDeclaredConstructor(final AjType<?>... parameterTypes)\n
    '''
def getDeclaredConstructors():
    '''returns Constructor[]\n\n
    getDeclaredConstructors()\n
    '''
def getDeclaredField():
    '''returns Field\n\n
    getDeclaredField(final String name)\n
    '''
def getDeclaredFields():
    '''returns Field[]\n\n
    getDeclaredFields()\n
    '''
def getField():
    '''returns Field\n\n
    getField(final String name)\n
    '''
def getFields():
    '''returns Field[]\n\n
    getFields()\n
    '''
def getDeclaredMethod():
    '''returns Method\n\n
    getDeclaredMethod(final String name, final AjType<?>... parameterTypes)\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod(final String name, final AjType<?>... parameterTypes)\n
    '''
def getDeclaredMethods():
    '''returns Method[]\n\n
    getDeclaredMethods()\n
    '''
def getMethods():
    '''returns Method[]\n\n
    getMethods()\n
    '''
def getDeclaredPointcut():
    '''returns Pointcut\n\n
    getDeclaredPointcut(final String name)\n
    '''
def getPointcut():
    '''returns Pointcut\n\n
    getPointcut(final String name)\n
    '''
def getDeclaredPointcuts():
    '''returns Pointcut[]\n\n
    getDeclaredPointcuts()\n
    '''
def getPointcuts():
    '''returns Pointcut[]\n\n
    getPointcuts()\n
    '''
def getDeclaredAdvice():
    '''returns Advice\n\n
    getDeclaredAdvice(final AdviceKind... ofType)\n
    getDeclaredAdvice(final String name)\n
    '''
def getAdvice():
    '''returns Advice\n\n
    getAdvice(final AdviceKind... ofType)\n
    getAdvice(final String name)\n
    '''
def getDeclaredITDMethod():
    '''returns InterTypeMethodDeclaration\n\n
    getDeclaredITDMethod(final String name, final AjType<?> target, final AjType<?>... parameterTypes)\n
    '''
def getDeclaredITDMethods():
    '''returns InterTypeMethodDeclaration[]\n\n
    getDeclaredITDMethods()\n
    '''
def getITDMethod():
    '''returns InterTypeMethodDeclaration\n\n
    getITDMethod(final String name, final AjType<?> target, final AjType<?>... parameterTypes)\n
    '''
def getITDMethods():
    '''returns InterTypeMethodDeclaration[]\n\n
    getITDMethods()\n
    '''
def getDeclaredITDConstructor():
    '''returns InterTypeConstructorDeclaration\n\n
    getDeclaredITDConstructor(final AjType<?> target, final AjType<?>... parameterTypes)\n
    '''
def getDeclaredITDConstructors():
    '''returns InterTypeConstructorDeclaration[]\n\n
    getDeclaredITDConstructors()\n
    '''
def getITDConstructor():
    '''returns InterTypeConstructorDeclaration\n\n
    getITDConstructor(final AjType<?> target, final AjType<?>... parameterTypes)\n
    '''
def getITDConstructors():
    '''returns InterTypeConstructorDeclaration[]\n\n
    getITDConstructors()\n
    '''
def getDeclaredITDField():
    '''returns InterTypeFieldDeclaration\n\n
    getDeclaredITDField(final String name, final AjType<?> target)\n
    '''
def getDeclaredITDFields():
    '''returns InterTypeFieldDeclaration[]\n\n
    getDeclaredITDFields()\n
    '''
def getITDField():
    '''returns InterTypeFieldDeclaration\n\n
    getITDField(final String name, final AjType<?> target)\n
    '''
def getITDFields():
    '''returns InterTypeFieldDeclaration[]\n\n
    getITDFields()\n
    '''
def getDeclareErrorOrWarnings():
    '''returns DeclareErrorOrWarning[]\n\n
    getDeclareErrorOrWarnings()\n
    '''
def getDeclareSofts():
    '''returns DeclareSoft[]\n\n
    getDeclareSofts()\n
    '''
def getDeclareAnnotations():
    '''returns DeclareAnnotation[]\n\n
    getDeclareAnnotations()\n
    '''
def getDeclarePrecedence():
    '''returns DeclarePrecedence[]\n\n
    getDeclarePrecedence()\n
    '''
def getEnumConstants():
    '''returns T[]\n\n
    getEnumConstants()\n
    '''
def getTypeParameters():
    '''returns TypeVariable<Class<T>>[]\n\n
    getTypeParameters()\n
    '''
def isEnum():
    '''returns boolean\n\n
    isEnum()\n
    '''
def isInstance():
    '''returns boolean\n\n
    isInstance(final Object o)\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def isLocalClass():
    '''returns boolean\n\n
    isLocalClass()\n
    '''
def isMemberClass():
    '''returns boolean\n\n
    isMemberClass()\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray()\n
    '''
def isPrimitive():
    '''returns boolean\n\n
    isPrimitive()\n
    '''
def isAspect():
    '''returns boolean\n\n
    isAspect()\n
    '''
def isMemberAspect():
    '''returns boolean\n\n
    isMemberAspect()\n
    '''
def isPrivileged():
    '''returns boolean\n\n
    isPrivileged()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
