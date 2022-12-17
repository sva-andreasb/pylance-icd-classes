EXTENDS = "char  '+'"
SUPER = "char  '-'"
INSTANCEOF = "char  '='"
def ():
    '''returns SignatureVisitor\n\n
    (final int api)\n
    '''
def visitFormalTypeParameter():
    '''returns None\n\n
    visitFormalTypeParameter(final String s)\n
    '''
def visitClassBound():
    '''returns SignatureVisitor\n\n
    visitClassBound()\n
    '''
def visitInterfaceBound():
    '''returns SignatureVisitor\n\n
    visitInterfaceBound()\n
    '''
def visitSuperclass():
    '''returns SignatureVisitor\n\n
    visitSuperclass()\n
    '''
def visitInterface():
    '''returns SignatureVisitor\n\n
    visitInterface()\n
    '''
def visitParameterType():
    '''returns SignatureVisitor\n\n
    visitParameterType()\n
    '''
def visitReturnType():
    '''returns SignatureVisitor\n\n
    visitReturnType()\n
    '''
def visitExceptionType():
    '''returns SignatureVisitor\n\n
    visitExceptionType()\n
    '''
def visitBaseType():
    '''returns None\n\n
    visitBaseType(final char c)\n
    '''
def visitTypeVariable():
    '''returns None\n\n
    visitTypeVariable(final String s)\n
    '''
def visitArrayType():
    '''returns SignatureVisitor\n\n
    visitArrayType()\n
    '''
def visitClassType():
    '''returns None\n\n
    visitClassType(final String s)\n
    '''
def visitInnerClassType():
    '''returns None\n\n
    visitInnerClassType(final String s)\n
    '''
def visitTypeArgument():
    '''returns SignatureVisitor\n\n
    visitTypeArgument()\n
    visitTypeArgument(final char c)\n
    '''
def visitEnd():
    '''returns None\n\n
    visitEnd()\n
    '''
