def _extends():
    '''returns JClass\n\n
    _extends(final JClass superClass)\n
    _extends(final Class<?> superClass)\n
    _extends()\n
    '''
def _implements():
    '''returns Iterator<JClass>\n\n
    _implements(final JClass iface)\n
    _implements(final Class<?> iface)\n
    _implements()\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def enumConstant():
    '''returns JEnumConstant\n\n
    enumConstant(final String name)\n
    '''
def fullName():
    '''returns String\n\n
    fullName()\n
    '''
def binaryName():
    '''returns String\n\n
    binaryName()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def field():
    '''returns JFieldVar\n\n
    field(final int mods, final JType type, final String name)\n
    field(final int mods, final Class<?> type, final String name)\n
    field(final int mods, final JType type, final String name, final JExpression init)\n
    field(final int mods, final Class<?> type, final String name, final JExpression init)\n
    '''
def isAnnotationTypeDeclaration():
    '''returns boolean\n\n
    isAnnotationTypeDeclaration()\n
    '''
def _annotationTypeDeclaration():
    '''returns JDefinedClass\n\n
    _annotationTypeDeclaration(final String name)\n
    '''
def _enum():
    '''returns JDefinedClass\n\n
    _enum(final String name)\n
    _enum(final int mods, final String name)\n
    '''
def getClassType():
    '''returns ClassType\n\n
    getClassType()\n
    '''
def removeField():
    '''returns None\n\n
    removeField(final JFieldVar field)\n
    '''
def init():
    '''returns JBlock\n\n
    init()\n
    '''
def constructor():
    '''returns JMethod\n\n
    constructor(final int mods)\n
    '''
def constructors():
    '''returns Iterator<JMethod>\n\n
    constructors()\n
    '''
def getConstructor():
    '''returns JMethod\n\n
    getConstructor(final JType[] argTypes)\n
    '''
def method():
    '''returns JMethod\n\n
    method(final int mods, final JType type, final String name)\n
    method(final int mods, final Class<?> type, final String name)\n
    '''
def methods():
    '''returns Collection<JMethod>\n\n
    methods()\n
    '''
def getMethod():
    '''returns JMethod\n\n
    getMethod(final String name, final JType[] argTypes)\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass()\n
    '''
def isPackage():
    '''returns boolean\n\n
    isPackage()\n
    '''
def getPackage():
    '''returns JPackage\n\n
    getPackage()\n
    '''
def _class():
    '''returns JDefinedClass\n\n
    _class(final int mods, final String name)\n
    _class(final int mods, final String name, final boolean isInterface)\n
    _class(final int mods, final String name, final ClassType classTypeVal)\n
    _class(final String name)\n
    '''
def _interface():
    '''returns JDefinedClass\n\n
    _interface(final int mods, final String name)\n
    _interface(final String name)\n
    '''
def javadoc():
    '''returns JDocComment\n\n
    javadoc()\n
    '''
def hide():
    '''returns None\n\n
    hide()\n
    '''
def isHidden():
    '''returns boolean\n\n
    isHidden()\n
    '''
def outer():
    '''returns JClass\n\n
    outer()\n
    '''
def declare():
    '''returns None\n\n
    declare(final JFormatter f)\n
    '''
def direct():
    '''returns None\n\n
    direct(final String string)\n
    '''
def generify():
    '''returns JTypeVar\n\n
    generify(final String name)\n
    generify(final String name, final Class<?> bound)\n
    generify(final String name, final JClass bound)\n
    '''
def typeParams():
    '''returns JTypeVar[]\n\n
    typeParams()\n
    '''
def annotate():
    '''returns JAnnotationUse\n\n
    annotate(final Class<? extends Annotation> clazz)\n
    annotate(final JClass clazz)\n
    '''
def annotations():
    '''returns Collection<JAnnotationUse>\n\n
    annotations()\n
    '''
def mods():
    '''returns JMods\n\n
    mods()\n
    '''
