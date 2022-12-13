def isAnonymous():
    '''public final boolean isAnonymous()
    '''
def _extends():
    '''public JDefinedClass _extends(final JClass superClass)
    public JDefinedClass _extends(final Class<?> superClass)
    public JClass _extends()
    '''
def _implements():
    '''public JDefinedClass _implements(final JClass iface)
    public JDefinedClass _implements(final Class<?> iface)
    public Iterator<JClass> _implements()
    '''
def name():
    '''public String name()
    '''
def enumConstant():
    '''public JEnumConstant enumConstant(final String name)
    '''
def fullName():
    '''public String fullName()
    '''
def binaryName():
    '''public String binaryName()
    '''
def isInterface():
    '''public boolean isInterface()
    '''
def isAbstract():
    '''public boolean isAbstract()
    '''
def field():
    '''public JFieldVar field(final int mods, final JType type, final String name)
    public JFieldVar field(final int mods, final Class<?> type, final String name)
    public JFieldVar field(final int mods, final JType type, final String name, final JExpression init)
    public JFieldVar field(final int mods, final Class<?> type, final String name, final JExpression init)
    '''
def isAnnotationTypeDeclaration():
    '''public boolean isAnnotationTypeDeclaration()
    '''
def _annotationTypeDeclaration():
    '''public JDefinedClass _annotationTypeDeclaration(final String name)
    '''
def _enum():
    '''public JDefinedClass _enum(final String name)
    public JDefinedClass _enum(final int mods, final String name)
    '''
def getClassType():
    '''public ClassType getClassType()
    '''
def fields():
    '''public Map<String, JFieldVar> fields()
    '''
def removeField():
    '''public void removeField(final JFieldVar field)
    '''
def init():
    '''public JBlock init()
    '''
def constructor():
    '''public JMethod constructor(final int mods)
    '''
def constructors():
    '''public Iterator<JMethod> constructors()
    '''
def getConstructor():
    '''public JMethod getConstructor(final JType[] argTypes)
    '''
def method():
    '''public JMethod method(final int mods, final JType type, final String name)
    public JMethod method(final int mods, final Class<?> type, final String name)
    '''
def methods():
    '''public Collection<JMethod> methods()
    '''
def getMethod():
    '''public JMethod getMethod(final String name, final JType[] argTypes)
    '''
def isClass():
    '''public boolean isClass()
    '''
def isPackage():
    '''public boolean isPackage()
    '''
def getPackage():
    '''public JPackage getPackage()
    '''
def _class():
    '''public JDefinedClass _class(final int mods, final String name)
    public JDefinedClass _class(final int mods, final String name, final boolean isInterface)
    public JDefinedClass _class(final int mods, final String name, final ClassType classTypeVal)
    public JDefinedClass _class(final String name)
    '''
def _interface():
    '''public JDefinedClass _interface(final int mods, final String name)
    public JDefinedClass _interface(final String name)
    '''
def javadoc():
    '''public JDocComment javadoc()
    '''
def hide():
    '''public void hide()
    '''
def isHidden():
    '''public boolean isHidden()
    '''
def classes():
    '''public final Iterator<JDefinedClass> classes()
    '''
def listClasses():
    '''public final JClass[] listClasses()
    '''
def outer():
    '''public JClass outer()
    '''
def declare():
    '''public void declare(final JFormatter f)
    '''
def direct():
    '''public void direct(final String string)
    '''
def _package():
    '''public final JPackage _package()
    '''
def parentContainer():
    '''public final JClassContainer parentContainer()
    '''
def generify():
    '''public JTypeVar generify(final String name)
    public JTypeVar generify(final String name, final Class<?> bound)
    public JTypeVar generify(final String name, final JClass bound)
    '''
def typeParams():
    '''public JTypeVar[] typeParams()
    '''
def annotate():
    '''public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
    public JAnnotationUse annotate(final JClass clazz)
    '''
def annotate2():
    '''public <W extends JAnnotationWriter> W annotate2(final Class<W> clazz)
    '''
def annotations():
    '''public Collection<JAnnotationUse> annotations()
    '''
def mods():
    '''public JMods mods()
    '''
