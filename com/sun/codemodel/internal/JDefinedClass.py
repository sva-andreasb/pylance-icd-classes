def isAnonymous():
'''public final boolean isAnonymous()
'''
pass
def _extends():
'''public JDefinedClass _extends(final JClass superClass)
public JDefinedClass _extends(final Class<?> superClass)
public JClass _extends()
'''
pass
def _implements():
'''public JDefinedClass _implements(final JClass iface)
public JDefinedClass _implements(final Class<?> iface)
public Iterator<JClass> _implements()
'''
pass
def name():
'''public String name()
'''
pass
def enumConstant():
'''public JEnumConstant enumConstant(final String name)
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
def isInterface():
'''public boolean isInterface()
'''
pass
def isAbstract():
'''public boolean isAbstract()
'''
pass
def field():
'''public JFieldVar field(final int mods, final JType type, final String name)
public JFieldVar field(final int mods, final Class<?> type, final String name)
public JFieldVar field(final int mods, final JType type, final String name, final JExpression init)
public JFieldVar field(final int mods, final Class<?> type, final String name, final JExpression init)
'''
pass
def isAnnotationTypeDeclaration():
'''public boolean isAnnotationTypeDeclaration()
'''
pass
def _annotationTypeDeclaration():
'''public JDefinedClass _annotationTypeDeclaration(final String name)
'''
pass
def _enum():
'''public JDefinedClass _enum(final String name)
public JDefinedClass _enum(final int mods, final String name)
'''
pass
def getClassType():
'''public ClassType getClassType()
'''
pass
def fields():
'''public Map<String, JFieldVar> fields()
'''
pass
def removeField():
'''public void removeField(final JFieldVar field)
'''
pass
def init():
'''public JBlock init()
'''
pass
def constructor():
'''public JMethod constructor(final int mods)
'''
pass
def constructors():
'''public Iterator<JMethod> constructors()
'''
pass
def getConstructor():
'''public JMethod getConstructor(final JType[] argTypes)
'''
pass
def method():
'''public JMethod method(final int mods, final JType type, final String name)
public JMethod method(final int mods, final Class<?> type, final String name)
'''
pass
def methods():
'''public Collection<JMethod> methods()
'''
pass
def getMethod():
'''public JMethod getMethod(final String name, final JType[] argTypes)
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
def _interface():
'''public JDefinedClass _interface(final int mods, final String name)
public JDefinedClass _interface(final String name)
'''
pass
def javadoc():
'''public JDocComment javadoc()
'''
pass
def hide():
'''public void hide()
'''
pass
def isHidden():
'''public boolean isHidden()
'''
pass
def classes():
'''public final Iterator<JDefinedClass> classes()
'''
pass
def listClasses():
'''public final JClass[] listClasses()
'''
pass
def outer():
'''public JClass outer()
'''
pass
def declare():
'''public void declare(final JFormatter f)
'''
pass
def direct():
'''public void direct(final String string)
'''
pass
def _package():
'''public final JPackage _package()
'''
pass
def parentContainer():
'''public final JClassContainer parentContainer()
'''
pass
def generify():
'''public JTypeVar generify(final String name)
public JTypeVar generify(final String name, final Class<?> bound)
public JTypeVar generify(final String name, final JClass bound)
'''
pass
def typeParams():
'''public JTypeVar[] typeParams()
'''
pass
def annotate():
'''public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
public JAnnotationUse annotate(final JClass clazz)
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
def mods():
'''public JMods mods()
'''
pass
