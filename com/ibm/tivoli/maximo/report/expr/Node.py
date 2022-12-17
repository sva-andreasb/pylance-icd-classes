Any = "int  -1"
Root = "int  1"
Literal = "int  2"
Quoted = "int  3"
Number = "int  4"
Group = "int  5"
GroupSeparator = "int  6"
Operand = "int  7"
def ():
    '''returns Node\n\n
    (final int type)\n
    (final int type, final String value)\n
    (final Node parent, final int type, final String value)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final Node node)\n
    '''
def removeChild():
    '''returns None\n\n
    removeChild(final Node node)\n
    '''
def nextSibling():
    '''returns Node\n\n
    nextSibling()\n
    '''
def prevSibling():
    '''returns Node\n\n
    prevSibling()\n
    '''
def dump():
    '''returns None\n\n
    dump(final PrintStream writer)\n
    dump(final PrintWriter writer)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def toFormattedString():
    '''returns String\n\n
    toFormattedString()\n
    toFormattedString(final ToStringVisitor.Transformer transformer)\n
    '''
def toFormattedStringChildrenOnly():
    '''returns String\n\n
    toFormattedStringChildrenOnly()\n
    toFormattedStringChildrenOnly(final ToStringVisitor.Transformer transformer)\n
    '''
def child():
    '''returns Node\n\n
    child(final int i)\n
    '''
def find():
    '''returns Collector\n\n
    find(final Collector c)\n
    '''
def addChildren():
    '''returns None\n\n
    addChildren(final List<Node> children2)\n
    '''
def last():
    '''returns Node\n\n
    last()\n
    '''
