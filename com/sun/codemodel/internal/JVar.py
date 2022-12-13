def init():
'''public JVar init(final JExpression init)
'''
pass
def name():
'''public String name()
public void name(final String name)
'''
pass
def type():
'''public JType type()
public JType type(final JType newType)
'''
pass
def mods():
'''public JMods mods()
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
def bind():
'''public void bind(final JFormatter f)
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
def assign():
'''public JExpression assign(final JExpression rhs)
'''
pass
def assignPlus():
'''public JExpression assignPlus(final JExpression rhs)
'''
pass
