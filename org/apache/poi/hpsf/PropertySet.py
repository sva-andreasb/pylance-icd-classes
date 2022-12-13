OS_WIN16 = "int  0"
OS_MACINTOSH = "int  1"
OS_WIN32 = "int  2"
def PropertySet():
    '''    public PropertySet()
    public PropertySet(final InputStream stream)
    public PropertySet(final byte[] stream, final int offset, final int length)
    public PropertySet(final byte[] stream)
    public PropertySet(final PropertySet ps)
    '''
def getByteOrder():
    '''    public int getByteOrder()
    '''
def setByteOrder():
    '''    public void setByteOrder(final int byteOrder)
    '''
def getFormat():
    '''    public int getFormat()
    '''
def setFormat():
    '''    public void setFormat(final int format)
    '''
def getOSVersion():
    '''    public int getOSVersion()
    '''
def setOSVersion():
    '''    public void setOSVersion(final int osVersion)
    '''
def getClassID():
    '''    public ClassID getClassID()
    '''
def setClassID():
    '''    public void setClassID(final ClassID classID)
    '''
def getSectionCount():
    '''    public int getSectionCount()
    '''
def getSections():
    '''    public List<Section> getSections()
    '''
def addSection():
    '''    public void addSection(final Section section)
    '''
def clearSections():
    '''    public void clearSections()
    '''
def getPropertySetIDMap():
    '''    public PropertyIDMap getPropertySetIDMap()
    '''
def isPropertySetStream():
    '''    public static boolean isPropertySetStream(final InputStream stream)
    public static boolean isPropertySetStream(final byte[] src, final int offset, final int length)
    '''
def write():
    '''    public void write(final OutputStream out)
    public void write(final DirectoryEntry dir, final String name)
    '''
def toInputStream():
    '''    public InputStream toInputStream()
    '''
def getPropertyStringValue():
    '''    public static String getPropertyStringValue(final Object propertyValue)
    '''
def isSummaryInformation():
    '''    public boolean isSummaryInformation()
    '''
def isDocumentSummaryInformation():
    '''    public boolean isDocumentSummaryInformation()
    '''
def getProperties():
    '''    public Property[] getProperties()
    '''
def wasNull():
    '''    public boolean wasNull()
    '''
def getFirstSection():
    '''    public Section getFirstSection()
    '''
def getSingleSection():
    '''    public Section getSingleSection()
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
