def getInstance():
    '''public static Region getInstance(final String id)
    public static Region getInstance(final int code)
    '''
def getAvailable():
    '''public static Set<Region> getAvailable(final RegionType type)
    '''
def getContainingRegion():
    '''public Region getContainingRegion()
    public Region getContainingRegion(final RegionType type)
    '''
def getContainedRegions():
    '''public Set<Region> getContainedRegions()
    public Set<Region> getContainedRegions(final RegionType type)
    '''
def getPreferredValues():
    '''public List<Region> getPreferredValues()
    '''
def contains():
    '''public boolean contains(final Region other)
    '''
def toString():
    '''public String toString()
    '''
def getNumericCode():
    '''public int getNumericCode()
    '''
def getType():
    '''public RegionType getType()
    '''
def compareTo():
    '''public int compareTo(final Region other)
    '''
