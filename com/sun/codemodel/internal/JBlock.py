def JBlock():
'''public JBlock()
public JBlock(final boolean bracesRequired, final boolean indentRequired)
'''
pass
def getContents():
'''public List<Object> getContents()
'''
pass
def pos():
'''public int pos()
public int pos(final int newPos)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def decl():
'''public JVar decl(final JType type, final String name)
public JVar decl(final JType type, final String name, final JExpression init)
public JVar decl(final int mods, final JType type, final String name, final JExpression init)
'''
pass
def assign():
'''public JBlock assign(final JAssignmentTarget lhs, final JExpression exp)
'''
pass
def assignPlus():
'''public JBlock assignPlus(final JAssignmentTarget lhs, final JExpression exp)
'''
pass
def invoke():
'''public JInvocation invoke(final JExpression expr, final String method)
public JInvocation invoke(final JExpression expr, final JMethod method)
public JInvocation invoke(final String method)
public JInvocation invoke(final JMethod method)
'''
pass
def staticInvoke():
'''public JInvocation staticInvoke(final JClass type, final String method)
'''
pass
def add():
'''public JBlock add(final JStatement s)
'''
pass
def _if():
'''public JConditional _if(final JExpression expr)
'''
pass
def _for():
'''public JForLoop _for()
'''
pass
def _while():
'''public JWhileLoop _while(final JExpression test)
'''
pass
def _switch():
'''public JSwitch _switch(final JExpression test)
'''
pass
def _do():
'''public JDoLoop _do(final JExpression test)
'''
pass
def _try():
'''public JTryBlock _try()
'''
pass
def _return():
'''public void _return()
public void _return(final JExpression exp)
'''
pass
def _throw():
'''public void _throw(final JExpression exp)
'''
pass
def _break():
'''public void _break()
public void _break(final JLabel label)
'''
pass
def label():
'''public JLabel label(final String name)
'''
pass
def _continue():
'''public void _continue(final JLabel label)
public void _continue()
'''
pass
def block():
'''public JBlock block()
'''
pass
def directStatement():
'''public JStatement directStatement(final String source)
'''
pass
def state():
'''public void state(final JFormatter f)
public void state(final JFormatter f)
'''
pass
def generate():
'''public void generate(final JFormatter f)
'''
pass
def forEach():
'''public JForEach forEach(final JType varType, final String name, final JExpression collection)
'''
pass
