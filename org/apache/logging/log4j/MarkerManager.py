def clear():
    '''    public static void clear()
    '''
def exists():
    '''    public static boolean exists(final String key)
    '''
def getMarker():
    '''    public static Marker getMarker(final String name)
    public static Marker getMarker(final String name, final String parent)
    public static Marker getMarker(final String name, final Marker parent)
    '''
def Log4jMarker():
    '''    public Log4jMarker(final String name)
    '''
def addParents():
    '''    public synchronized Marker addParents(final Marker... parentMarkers)
    '''
def remove():
    '''    public synchronized boolean remove(final Marker parent)
    '''
def setParents():
    '''    public Marker setParents(final Marker... markers)
    '''
def getName():
    '''    public String getName()
    '''
def getParents():
    '''    public Marker[] getParents()
    '''
def hasParents():
    '''    public boolean hasParents()
    '''
def isInstanceOf():
    '''    public boolean isInstanceOf(final Marker marker)
    public boolean isInstanceOf(final String markerName)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def toString():
    '''    public String toString()
    '''
def formatTo():
    '''    public void formatTo(final StringBuilder sb)
    '''
