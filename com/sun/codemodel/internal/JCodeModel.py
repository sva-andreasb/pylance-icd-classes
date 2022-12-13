def JCodeModel():
    '''public JCodeModel()
    '''
def _package():
    '''public JPackage _package(final String name)
    public JPackage _package()
    '''
def rootPackage():
    '''public final JPackage rootPackage()
    '''
def packages():
    '''public Iterator<JPackage> packages()
    '''
def _class():
    '''public JDefinedClass _class(final String fullyqualifiedName)
    public JDefinedClass _class(final int mods, final String fullyqualifiedName, final ClassType t)
    public JDefinedClass _class(final String fullyqualifiedName, final ClassType t)
    '''
def directClass():
    '''public JClass directClass(final String name)
    '''
def _getClass():
    '''public JDefinedClass _getClass(final String fullyQualifiedName)
    '''
def newAnonymousClass():
    '''public JDefinedClass newAnonymousClass(final JClass baseType)
    '''
def anonymousClass():
    '''public JDefinedClass anonymousClass(final JClass baseType)
    public JDefinedClass anonymousClass(final Class<?> baseType)
    '''
def build():
    '''public void build(final File destDir, final PrintStream status)
    public void build(final File srcDir, final File resourceDir, final PrintStream status)
    public void build(final File destDir)
    public void build(final File srcDir, final File resourceDir)
    public void build(final CodeWriter out)
    public void build(final CodeWriter source, final CodeWriter resource)
    '''
def countArtifacts():
    '''public int countArtifacts()
    '''
def ref():
    '''public JClass ref(final Class<?> clazz)
    public JClass ref(final String fullyQualifiedClassName)
    '''
def _ref():
    '''public JType _ref(final Class<?> c)
    '''
def wildcard():
    '''public JClass wildcard()
    '''
def parseType():
    '''public JType parseType(final String name)
    '''
def TypeNameParser():
    '''public TypeNameParser(final String s)
    '''
def name():
    '''public String name()
    '''
def fullName():
    '''public String fullName()
    '''
def binaryName():
    '''public String binaryName()
    '''
def outer():
    '''public JClass outer()
    '''
def _extends():
    '''public JClass _extends()
    '''
def _implements():
    '''public Iterator<JClass> _implements()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public JClass next()
    '''
def remove():
    '''public void remove()
    '''
def isInterface():
    '''public boolean isInterface()
    '''
def isAbstract():
    '''public boolean isAbstract()
    '''
def getPrimitiveType():
    '''public JPrimitiveType getPrimitiveType()
    '''
def isArray():
    '''public boolean isArray()
    '''
def declare():
    '''public void declare(final JFormatter f)
    '''
def typeParams():
    '''public JTypeVar[] typeParams()
    '''
