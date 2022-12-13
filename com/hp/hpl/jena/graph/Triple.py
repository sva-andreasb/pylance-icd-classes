def Triple():
    '''public Triple(final Node s, final Node p, final Node o)
    '''
def toString():
    '''public String toString()
    public String toString(final PrefixMapping pm)
    '''
def getSubject():
    '''public final Node getSubject()
    '''
def getPredicate():
    '''public final Node getPredicate()
    '''
def getObject():
    '''public final Node getObject()
    '''
def getMatchSubject():
    '''public Node getMatchSubject()
    '''
def getMatchPredicate():
    '''public Node getMatchPredicate()
    '''
def getMatchObject():
    '''public Node getMatchObject()
    '''
def asTriple():
    '''public Triple asTriple()
    '''
def isConcrete():
    '''public boolean isConcrete()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def sameAs():
    '''public boolean sameAs(final Node s, final Node p, final Node o)
    '''
def matches():
    '''public boolean matches(final Triple other)
    public boolean matches(final Node s, final Node p, final Node o)
    '''
def subjectMatches():
    '''public boolean subjectMatches(final Node s)
    '''
def predicateMatches():
    '''public boolean predicateMatches(final Node p)
    '''
def objectMatches():
    '''public boolean objectMatches(final Node o)
    '''
def hashCode():
    '''public int hashCode()
    public static int hashCode(final Node s, final Node p, final Node o)
    '''
def create():
    '''public static Triple create(final Node s, final Node p, final Node o)
    '''
def createMatch():
    '''public static Triple createMatch(final Node s, final Node p, final Node o)
    '''
def map1():
    '''public Node map1(final Triple t)
    public Node map1(final Triple t)
    public Node map1(final Triple t)
    '''
def filterOn():
    '''public final Filter<Triple> filterOn(final Triple t)
    public Filter<Triple> filterOn(final Node n)
    public Filter<Triple> filterOn(final Node n)
    public Filter<Triple> filterOn(final Node n)
    '''
def getField():
    '''public Node getField(final Triple t)
    public Node getField(final Triple t)
    public Node getField(final Triple t)
    '''
def accept():
    '''public boolean accept(final Triple x)
    public boolean accept(final Triple x)
    public boolean accept(final Triple x)
    '''
