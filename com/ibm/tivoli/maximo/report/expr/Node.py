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
pass
def addChild():
'''public void addChild(final Node node)
'''
pass
def removeChild():
'''public void removeChild(final Node node)
'''
pass
def nextSibling():
'''public Node nextSibling()
'''
pass
def prevSibling():
'''public Node prevSibling()
'''
pass
def dump():
'''public void dump(final PrintStream writer)
public void dump(final PrintWriter writer)
'''
pass
def toString():
'''public String toString()
'''
pass
def toFormattedString():
'''public String toFormattedString()
public String toFormattedString(final ToStringVisitor.Transformer transformer)
'''
pass
def toFormattedStringChildrenOnly():
'''public String toFormattedStringChildrenOnly()
public String toFormattedStringChildrenOnly(final ToStringVisitor.Transformer transformer)
'''
pass
def child():
'''public Node child(final int i)
'''
pass
def find():
'''public Collector find(final Collector c)
'''
pass
def addChildren():
'''public void addChildren(final List<Node> children2)
'''
pass
def last():
'''public Node last()
'''
pass
