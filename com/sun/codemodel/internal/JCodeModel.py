def JCodeModel():
'''public JCodeModel()
'''
pass
def _package():
'''public JPackage _package(final String name)
public JPackage _package()
'''
pass
def rootPackage():
'''public final JPackage rootPackage()
'''
pass
def packages():
'''public Iterator<JPackage> packages()
'''
pass
def _class():
'''public JDefinedClass _class(final String fullyqualifiedName)
public JDefinedClass _class(final int mods, final String fullyqualifiedName, final ClassType t)
public JDefinedClass _class(final String fullyqualifiedName, final ClassType t)
'''
pass
def directClass():
'''public JClass directClass(final String name)
'''
pass
def _getClass():
'''public JDefinedClass _getClass(final String fullyQualifiedName)
'''
pass
def newAnonymousClass():
'''public JDefinedClass newAnonymousClass(final JClass baseType)
'''
pass
def anonymousClass():
'''public JDefinedClass anonymousClass(final JClass baseType)
public JDefinedClass anonymousClass(final Class<?> baseType)
'''
pass
def build():
'''public void build(final File destDir, final PrintStream status)
public void build(final File srcDir, final File resourceDir, final PrintStream status)
public void build(final File destDir)
public void build(final File srcDir, final File resourceDir)
public void build(final CodeWriter out)
public void build(final CodeWriter source, final CodeWriter resource)
'''
pass
def countArtifacts():
'''public int countArtifacts()
'''
pass
def ref():
'''public JClass ref(final Class<?> clazz)
public JClass ref(final String fullyQualifiedClassName)
'''
pass
def _ref():
'''public JType _ref(final Class<?> c)
'''
pass
def wildcard():
'''public JClass wildcard()
'''
pass
def parseType():
'''public JType parseType(final String name)
'''
pass
def TypeNameParser():
'''public TypeNameParser(final String s)
'''
pass
def name():
'''public String name()
'''
pass
def fullName():
'''public String fullName()
'''
pass
def binaryName():
'''public String binaryName()
'''
pass
def outer():
'''public JClass outer()
'''
pass
def _extends():
'''public JClass _extends()
'''
pass
def _implements():
'''public Iterator<JClass> _implements()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public JClass next()
'''
pass
def remove():
'''public void remove()
'''
pass
def isInterface():
'''public boolean isInterface()
'''
pass
def isAbstract():
'''public boolean isAbstract()
'''
pass
def getPrimitiveType():
'''public JPrimitiveType getPrimitiveType()
'''
pass
def isArray():
'''public boolean isArray()
'''
pass
def declare():
'''public void declare(final JFormatter f)
'''
pass
def typeParams():
'''public JTypeVar[] typeParams()
'''
pass
