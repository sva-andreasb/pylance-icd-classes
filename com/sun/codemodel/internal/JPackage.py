def parentContainer():
'''public JClassContainer parentContainer()
'''
pass
def parent():
'''public JPackage parent()
'''
pass
def isClass():
'''public boolean isClass()
'''
pass
def isPackage():
'''public boolean isPackage()
'''
pass
def getPackage():
'''public JPackage getPackage()
'''
pass
def _class():
'''public JDefinedClass _class(final int mods, final String name)
public JDefinedClass _class(final int mods, final String name, final boolean isInterface)
public JDefinedClass _class(final int mods, final String name, final ClassType classTypeVal)
public JDefinedClass _class(final String name)
'''
pass
def _getClass():
'''public JDefinedClass _getClass(final String name)
'''
pass
def compareTo():
'''public int compareTo(final JPackage that)
'''
pass
def _interface():
'''public JDefinedClass _interface(final int mods, final String name)
public JDefinedClass _interface(final String name)
'''
pass
def _annotationTypeDeclaration():
'''public JDefinedClass _annotationTypeDeclaration(final String name)
'''
pass
def _enum():
'''public JDefinedClass _enum(final String name)
'''
pass
def addResourceFile():
'''public JResourceFile addResourceFile(final JResourceFile rsrc)
'''
pass
def hasResourceFile():
'''public boolean hasResourceFile(final String name)
'''
pass
def propertyFiles():
'''public Iterator<JResourceFile> propertyFiles()
'''
pass
def javadoc():
'''public JDocComment javadoc()
'''
pass
def remove():
'''public void remove(final JClass c)
'''
pass
def ref():
'''public JClass ref(final String name)
'''
pass
def subPackage():
'''public JPackage subPackage(final String pkg)
'''
pass
def classes():
'''public Iterator<JDefinedClass> classes()
'''
pass
def isDefined():
'''public boolean isDefined(final String classLocalName)
'''
pass
def isUnnamed():
'''public final boolean isUnnamed()
'''
pass
def name():
'''public String name()
'''
pass
def owner():
'''public final JCodeModel owner()
'''
pass
def annotate():
'''public JAnnotationUse annotate(final JClass clazz)
public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
'''
pass
def annotate2():
'''public <W extends JAnnotationWriter> W annotate2(final Class<W> clazz)
'''
pass
def annotations():
'''public Collection<JAnnotationUse> annotations()
'''
pass
def declare():
'''public void declare(final JFormatter f)
'''
pass
def generate():
'''public void generate(final JFormatter f)
'''
pass
