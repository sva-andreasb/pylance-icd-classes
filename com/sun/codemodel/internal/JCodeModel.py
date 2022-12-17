def ():
    '''returns TypeNameParser\n\n
    ()\n
    (final String s)\n
    '''
def _package():
    '''returns JPackage\n\n
    _package(final String name)\n
    _package()\n
    '''
def packages():
    '''returns Iterator<JPackage>\n\n
    packages()\n
    '''
def _class():
    '''returns JDefinedClass\n\n
    _class(final String fullyqualifiedName)\n
    _class(final int mods, final String fullyqualifiedName, final ClassType t)\n
    _class(final String fullyqualifiedName, final ClassType t)\n
    '''
def directClass():
    '''returns JClass\n\n
    directClass(final String name)\n
    '''
def _getClass():
    '''returns JDefinedClass\n\n
    _getClass(final String fullyQualifiedName)\n
    '''
def newAnonymousClass():
    '''returns JDefinedClass\n\n
    newAnonymousClass(final JClass baseType)\n
    '''
def anonymousClass():
    '''returns JDefinedClass\n\n
    anonymousClass(final JClass baseType)\n
    anonymousClass(final Class<?> baseType)\n
    '''
def build():
    '''returns None\n\n
    build(final File destDir, final PrintStream status)\n
    build(final File srcDir, final File resourceDir, final PrintStream status)\n
    build(final File destDir)\n
    build(final File srcDir, final File resourceDir)\n
    build(final CodeWriter out)\n
    build(final CodeWriter source, final CodeWriter resource)\n
    '''
def countArtifacts():
    '''returns int\n\n
    countArtifacts()\n
    '''
def ref():
    '''returns JClass\n\n
    ref(final Class<?> clazz)\n
    ref(final String fullyQualifiedClassName)\n
    '''
def _ref():
    '''returns JType\n\n
    _ref(final Class<?> c)\n
    '''
def wildcard():
    '''returns JClass\n\n
    wildcard()\n
    '''
def parseType():
    '''returns JType\n\n
    parseType(final String name)\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def fullName():
    '''returns String\n\n
    fullName()\n
    '''
def binaryName():
    '''returns String\n\n
    binaryName()\n
    '''
def outer():
    '''returns JClass\n\n
    outer()\n
    '''
def _extends():
    '''returns JClass\n\n
    _extends()\n
    '''
def _implements():
    '''returns Iterator<JClass>\n\n
    _implements()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns JClass\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def getPrimitiveType():
    '''returns JPrimitiveType\n\n
    getPrimitiveType()\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray()\n
    '''
def declare():
    '''returns None\n\n
    declare(final JFormatter f)\n
    '''
def typeParams():
    '''returns JTypeVar[]\n\n
    typeParams()\n
    '''
