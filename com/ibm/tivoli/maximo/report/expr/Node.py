Any = "int  -1"
Root = "int  1"
Literal = "int  2"
Quoted = "int  3"
Number = "int  4"
Group = "int  5"
GroupSeparator = "int  6"
Operand = "int  7"
def Node():
    '''public Node(final int type)
    public Node(final int type, final String value)
    public Node(final Node parent, final int type, final String value)
    '''
def addChild():
    '''public void addChild(final Node node)
    '''
def removeChild():
    '''public void removeChild(final Node node)
    '''
def nextSibling():
    '''public Node nextSibling()
    '''
def prevSibling():
    '''public Node prevSibling()
    '''
def dump():
    '''public void dump(final PrintStream writer)
    public void dump(final PrintWriter writer)
    '''
def toString():
    '''public String toString()
    '''
def toFormattedString():
    '''public String toFormattedString()
    public String toFormattedString(final ToStringVisitor.Transformer transformer)
    '''
def toFormattedStringChildrenOnly():
    '''public String toFormattedStringChildrenOnly()
    public String toFormattedStringChildrenOnly(final ToStringVisitor.Transformer transformer)
    '''
def child():
    '''public Node child(final int i)
    '''
def find():
    '''public Collector find(final Collector c)
    '''
def addChildren():
    '''public void addChildren(final List<Node> children2)
    '''
def last():
    '''public Node last()
    '''
