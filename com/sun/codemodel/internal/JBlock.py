def JBlock():
    '''    public JBlock()
    public JBlock(final boolean bracesRequired, final boolean indentRequired)
    '''
def getContents():
    '''    public List<Object> getContents()
    '''
def pos():
    '''    public int pos()
    public int pos(final int newPos)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def decl():
    '''    public JVar decl(final JType type, final String name)
    public JVar decl(final JType type, final String name, final JExpression init)
    public JVar decl(final int mods, final JType type, final String name, final JExpression init)
    '''
def assign():
    '''    public JBlock assign(final JAssignmentTarget lhs, final JExpression exp)
    '''
def assignPlus():
    '''    public JBlock assignPlus(final JAssignmentTarget lhs, final JExpression exp)
    '''
def invoke():
    '''    public JInvocation invoke(final JExpression expr, final String method)
    public JInvocation invoke(final JExpression expr, final JMethod method)
    public JInvocation invoke(final String method)
    public JInvocation invoke(final JMethod method)
    '''
def staticInvoke():
    '''    public JInvocation staticInvoke(final JClass type, final String method)
    '''
def add():
    '''    public JBlock add(final JStatement s)
    '''
def _if():
    '''    public JConditional _if(final JExpression expr)
    '''
def _for():
    '''    public JForLoop _for()
    '''
def _while():
    '''    public JWhileLoop _while(final JExpression test)
    '''
def _switch():
    '''    public JSwitch _switch(final JExpression test)
    '''
def _do():
    '''    public JDoLoop _do(final JExpression test)
    '''
def _try():
    '''    public JTryBlock _try()
    '''
def _return():
    '''    public void _return()
    public void _return(final JExpression exp)
    '''
def _throw():
    '''    public void _throw(final JExpression exp)
    '''
def _break():
    '''    public void _break()
    public void _break(final JLabel label)
    '''
def label():
    '''    public JLabel label(final String name)
    '''
def _continue():
    '''    public void _continue(final JLabel label)
    public void _continue()
    '''
def block():
    '''    public JBlock block()
    '''
def directStatement():
    '''    public JStatement directStatement(final String source)
    '''
def state():
    '''    public void state(final JFormatter f)
    public void state(final JFormatter f)
    '''
def generate():
    '''    public void generate(final JFormatter f)
    '''
def forEach():
    '''    public JForEach forEach(final JType varType, final String name, final JExpression collection)
    '''
