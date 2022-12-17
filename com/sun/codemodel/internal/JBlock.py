def ():
    '''returns JBlock\n\n
    ()\n
    (final boolean bracesRequired, final boolean indentRequired)\n
    '''
def getContents():
    '''returns List<Object>\n\n
    getContents()\n
    '''
def pos():
    '''returns int\n\n
    pos()\n
    pos(final int newPos)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def decl():
    '''returns JVar\n\n
    decl(final JType type, final String name)\n
    decl(final JType type, final String name, final JExpression init)\n
    decl(final int mods, final JType type, final String name, final JExpression init)\n
    '''
def assign():
    '''returns JBlock\n\n
    assign(final JAssignmentTarget lhs, final JExpression exp)\n
    '''
def assignPlus():
    '''returns JBlock\n\n
    assignPlus(final JAssignmentTarget lhs, final JExpression exp)\n
    '''
def invoke():
    '''returns JInvocation\n\n
    invoke(final JExpression expr, final String method)\n
    invoke(final JExpression expr, final JMethod method)\n
    invoke(final String method)\n
    invoke(final JMethod method)\n
    '''
def staticInvoke():
    '''returns JInvocation\n\n
    staticInvoke(final JClass type, final String method)\n
    '''
def add():
    '''returns JBlock\n\n
    add(final JStatement s)\n
    '''
def _if():
    '''returns JConditional\n\n
    _if(final JExpression expr)\n
    '''
def _for():
    '''returns JForLoop\n\n
    _for()\n
    '''
def _while():
    '''returns JWhileLoop\n\n
    _while(final JExpression test)\n
    '''
def _switch():
    '''returns JSwitch\n\n
    _switch(final JExpression test)\n
    '''
def _do():
    '''returns JDoLoop\n\n
    _do(final JExpression test)\n
    '''
def _try():
    '''returns JTryBlock\n\n
    _try()\n
    '''
def _return():
    '''returns None\n\n
    _return()\n
    _return(final JExpression exp)\n
    '''
def _throw():
    '''returns None\n\n
    _throw(final JExpression exp)\n
    '''
def _break():
    '''returns None\n\n
    _break()\n
    _break(final JLabel label)\n
    '''
def label():
    '''returns JLabel\n\n
    label(final String name)\n
    '''
def _continue():
    '''returns None\n\n
    _continue(final JLabel label)\n
    _continue()\n
    '''
def block():
    '''returns JBlock\n\n
    block()\n
    '''
def directStatement():
    '''returns JStatement\n\n
    directStatement(final String source)\n
    '''
def state():
    '''returns None\n\n
    state(final JFormatter f)\n
    state(final JFormatter f)\n
    '''
def generate():
    '''returns None\n\n
    generate(final JFormatter f)\n
    '''
def forEach():
    '''returns JForEach\n\n
    forEach(final JType varType, final String name, final JExpression collection)\n
    '''
