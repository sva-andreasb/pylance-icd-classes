def parentContainer():
    '''public JClassContainer parentContainer()
    '''
def parent():
    '''public JPackage parent()
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
def _getClass():
    '''public JDefinedClass _getClass(final String name)
    '''
def compareTo():
    '''public int compareTo(final JPackage that)
    '''
def _interface():
    '''public JDefinedClass _interface(final int mods, final String name)
    public JDefinedClass _interface(final String name)
    '''
def _annotationTypeDeclaration():
    '''public JDefinedClass _annotationTypeDeclaration(final String name)
    '''
def _enum():
    '''public JDefinedClass _enum(final String name)
    '''
def addResourceFile():
    '''public JResourceFile addResourceFile(final JResourceFile rsrc)
    '''
def hasResourceFile():
    '''public boolean hasResourceFile(final String name)
    '''
def propertyFiles():
    '''public Iterator<JResourceFile> propertyFiles()
    '''
def javadoc():
    '''public JDocComment javadoc()
    '''
def remove():
    '''public void remove(final JClass c)
    '''
def ref():
    '''public JClass ref(final String name)
    '''
def subPackage():
    '''public JPackage subPackage(final String pkg)
    '''
def classes():
    '''public Iterator<JDefinedClass> classes()
    '''
def isDefined():
    '''public boolean isDefined(final String classLocalName)
    '''
def isUnnamed():
    '''public final boolean isUnnamed()
    '''
def name():
    '''public String name()
    '''
def owner():
    '''public final JCodeModel owner()
    '''
def annotate():
    '''public JAnnotationUse annotate(final JClass clazz)
    public JAnnotationUse annotate(final Class<? extends Annotation> clazz)
    '''
def annotate2():
    '''public <W extends JAnnotationWriter> W annotate2(final Class<W> clazz)
    '''
def annotations():
    '''public Collection<JAnnotationUse> annotations()
    '''
def declare():
    '''public void declare(final JFormatter f)
    '''
def generate():
    '''public void generate(final JFormatter f)
    '''
