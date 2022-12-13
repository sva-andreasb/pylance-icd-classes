def Triple():
'''public Triple(final Node s, final Node p, final Node o)
'''
pass
def toString():
'''public String toString()
public String toString(final PrefixMapping pm)
'''
pass
def getSubject():
'''public final Node getSubject()
'''
pass
def getPredicate():
'''public final Node getPredicate()
'''
pass
def getObject():
'''public final Node getObject()
'''
pass
def getMatchSubject():
'''public Node getMatchSubject()
'''
pass
def getMatchPredicate():
'''public Node getMatchPredicate()
'''
pass
def getMatchObject():
'''public Node getMatchObject()
'''
pass
def asTriple():
'''public Triple asTriple()
'''
pass
def isConcrete():
'''public boolean isConcrete()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def sameAs():
'''public boolean sameAs(final Node s, final Node p, final Node o)
'''
pass
def matches():
'''public boolean matches(final Triple other)
public boolean matches(final Node s, final Node p, final Node o)
'''
pass
def subjectMatches():
'''public boolean subjectMatches(final Node s)
'''
pass
def predicateMatches():
'''public boolean predicateMatches(final Node p)
'''
pass
def objectMatches():
'''public boolean objectMatches(final Node o)
'''
pass
def hashCode():
'''public int hashCode()
public static int hashCode(final Node s, final Node p, final Node o)
'''
pass
def create():
'''public static Triple create(final Node s, final Node p, final Node o)
'''
pass
def createMatch():
'''public static Triple createMatch(final Node s, final Node p, final Node o)
'''
pass
def map1():
'''public Node map1(final Triple t)
public Node map1(final Triple t)
public Node map1(final Triple t)
'''
pass
def filterOn():
'''public final Filter<Triple> filterOn(final Triple t)
public Filter<Triple> filterOn(final Node n)
public Filter<Triple> filterOn(final Node n)
public Filter<Triple> filterOn(final Node n)
'''
pass
def getField():
'''public Node getField(final Triple t)
public Node getField(final Triple t)
public Node getField(final Triple t)
'''
pass
def accept():
'''public boolean accept(final Triple x)
public boolean accept(final Triple x)
public boolean accept(final Triple x)
'''
pass
