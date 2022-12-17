def ():
    '''returns ApNavigator\n\n
    (final ProcessingEnvironment env)\n
    '''
def visitDeclared():
    '''returns TypeMirror\n\n
    visitDeclared(final DeclaredType t, final TypeElement sup)\n
    '''
def visitTypeVariable():
    '''returns TypeMirror\n\n
    visitTypeVariable(final TypeVariable t, final TypeElement typeElement)\n
    '''
def visitArray():
    '''returns TypeMirror\n\n
    visitArray(final ArrayType t, final TypeElement typeElement)\n
    '''
def visitWildcard():
    '''returns TypeMirror\n\n
    visitWildcard(final WildcardType t, final TypeElement typeElement)\n
    '''
def getSuperClass():
    '''returns TypeElement\n\n
    getSuperClass(final TypeElement typeElement)\n
    '''
def getBaseClass():
    '''returns TypeMirror\n\n
    getBaseClass(final TypeMirror type, final TypeElement sup)\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName(final TypeElement t)\n
    '''
def getTypeName():
    '''returns String\n\n
    getTypeName(final TypeMirror typeMirror)\n
    '''
def getClassShortName():
    '''returns String\n\n
    getClassShortName(final TypeElement t)\n
    '''
def getDeclaredFields():
    '''returns Collection<VariableElement>\n\n
    getDeclaredFields(final TypeElement typeElement)\n
    '''
def getDeclaredField():
    '''returns VariableElement\n\n
    getDeclaredField(final TypeElement clazz, final String fieldName)\n
    '''
def getDeclaredMethods():
    '''returns Collection<ExecutableElement>\n\n
    getDeclaredMethods(final TypeElement typeElement)\n
    '''
def getDeclaringClassForField():
    '''returns TypeElement\n\n
    getDeclaringClassForField(final VariableElement f)\n
    '''
def getDeclaringClassForMethod():
    '''returns TypeElement\n\n
    getDeclaringClassForMethod(final ExecutableElement m)\n
    '''
def getFieldType():
    '''returns TypeMirror\n\n
    getFieldType(final VariableElement f)\n
    '''
def getFieldName():
    '''returns String\n\n
    getFieldName(final VariableElement f)\n
    '''
def getMethodName():
    '''returns String\n\n
    getMethodName(final ExecutableElement m)\n
    '''
def getReturnType():
    '''returns TypeMirror\n\n
    getReturnType(final ExecutableElement m)\n
    '''
def getMethodParameters():
    '''returns TypeMirror[]\n\n
    getMethodParameters(final ExecutableElement m)\n
    '''
def isStaticMethod():
    '''returns boolean\n\n
    isStaticMethod(final ExecutableElement m)\n
    '''
def isFinalMethod():
    '''returns boolean\n\n
    isFinalMethod(final ExecutableElement m)\n
    '''
def isSubClassOf():
    '''returns boolean\n\n
    isSubClassOf(final TypeMirror sub, final TypeMirror sup)\n
    '''
def ref():
    '''returns TypeMirror\n\n
    ref(final Class c)\n
    '''
def use():
    '''returns TypeMirror\n\n
    use(final TypeElement t)\n
    '''
def asDecl():
    '''returns TypeElement\n\n
    asDecl(TypeMirror m)\n
    asDecl(final Class c)\n
    '''
def erasure():
    '''returns TypeMirror\n\n
    erasure(TypeMirror t)\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract(final TypeElement clazz)\n
    '''
def isFinal():
    '''returns boolean\n\n
    isFinal(final TypeElement clazz)\n
    '''
def getEnumConstants():
    '''returns VariableElement[]\n\n
    getEnumConstants(final TypeElement clazz)\n
    '''
def getVoidType():
    '''returns TypeMirror\n\n
    getVoidType()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName(final TypeElement clazz)\n
    '''
def loadObjectFactory():
    '''returns TypeElement\n\n
    loadObjectFactory(final TypeElement referencePoint, final String packageName)\n
    '''
def isBridgeMethod():
    '''returns boolean\n\n
    isBridgeMethod(final ExecutableElement method)\n
    '''
def isOverriding():
    '''returns boolean\n\n
    isOverriding(final ExecutableElement method, TypeElement base)\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface(final TypeElement clazz)\n
    '''
def isTransient():
    '''returns boolean\n\n
    isTransient(final VariableElement f)\n
    '''
def isInnerClass():
    '''returns boolean\n\n
    isInnerClass(final TypeElement clazz)\n
    '''
def isSameType():
    '''returns boolean\n\n
    isSameType(final TypeMirror t1, final TypeMirror t2)\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray(final TypeMirror type)\n
    '''
def isArrayButNotByteArray():
    '''returns boolean\n\n
    isArrayButNotByteArray(final TypeMirror t)\n
    '''
def getComponentType():
    '''returns TypeMirror\n\n
    getComponentType(final TypeMirror t)\n
    '''
def getTypeArgument():
    '''returns TypeMirror\n\n
    getTypeArgument(final TypeMirror typeMirror, final int i)\n
    '''
def isParameterizedType():
    '''returns boolean\n\n
    isParameterizedType(final TypeMirror typeMirror)\n
    '''
def isPrimitive():
    '''returns boolean\n\n
    isPrimitive(final TypeMirror t)\n
    '''
def getPrimitive():
    '''returns TypeMirror\n\n
    getPrimitive(final Class primitiveType)\n
    '''
def getClassLocation():
    '''returns Location\n\n
    getClassLocation(final TypeElement typeElement)\n
    '''
def getFieldLocation():
    '''returns Location\n\n
    getFieldLocation(final VariableElement variableElement)\n
    '''
def getMethodLocation():
    '''returns Location\n\n
    getMethodLocation(final ExecutableElement executableElement)\n
    '''
def hasDefaultConstructor():
    '''returns boolean\n\n
    hasDefaultConstructor(final TypeElement t)\n
    '''
def isStaticField():
    '''returns boolean\n\n
    isStaticField(final VariableElement f)\n
    '''
def isPublicMethod():
    '''returns boolean\n\n
    isPublicMethod(final ExecutableElement m)\n
    '''
def isPublicField():
    '''returns boolean\n\n
    isPublicField(final VariableElement f)\n
    '''
def isEnum():
    '''returns boolean\n\n
    isEnum(final TypeElement t)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getKind():
    '''returns TypeKind\n\n
    getKind()\n
    '''
