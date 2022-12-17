def parentContainer():
    '''returns JClassContainer\n\n
    parentContainer()\n
    '''
def parent():
    '''returns JPackage\n\n
    parent()\n
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
def _getClass():
    '''returns JDefinedClass\n\n
    _getClass(final String name)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final JPackage that)\n
    '''
def _interface():
    '''returns JDefinedClass\n\n
    _interface(final int mods, final String name)\n
    _interface(final String name)\n
    '''
def _annotationTypeDeclaration():
    '''returns JDefinedClass\n\n
    _annotationTypeDeclaration(final String name)\n
    '''
def _enum():
    '''returns JDefinedClass\n\n
    _enum(final String name)\n
    '''
def addResourceFile():
    '''returns JResourceFile\n\n
    addResourceFile(final JResourceFile rsrc)\n
    '''
def hasResourceFile():
    '''returns boolean\n\n
    hasResourceFile(final String name)\n
    '''
def propertyFiles():
    '''returns Iterator<JResourceFile>\n\n
    propertyFiles()\n
    '''
def javadoc():
    '''returns JDocComment\n\n
    javadoc()\n
    '''
def remove():
    '''returns None\n\n
    remove(final JClass c)\n
    '''
def ref():
    '''returns JClass\n\n
    ref(final String name)\n
    '''
def subPackage():
    '''returns JPackage\n\n
    subPackage(final String pkg)\n
    '''
def classes():
    '''returns Iterator<JDefinedClass>\n\n
    classes()\n
    '''
def isDefined():
    '''returns boolean\n\n
    isDefined(final String classLocalName)\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def annotate():
    '''returns JAnnotationUse\n\n
    annotate(final JClass clazz)\n
    annotate(final Class<? extends Annotation> clazz)\n
    '''
def annotations():
    '''returns Collection<JAnnotationUse>\n\n
    annotations()\n
    '''
def declare():
    '''returns None\n\n
    declare(final JFormatter f)\n
    '''
def generate():
    '''returns None\n\n
    generate(final JFormatter f)\n
    '''
