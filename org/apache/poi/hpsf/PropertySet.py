OS_WIN16 = "int  0"
OS_MACINTOSH = "int  1"
OS_WIN32 = "int  2"
def PropertySet():
'''public PropertySet()
public PropertySet(final InputStream stream)
public PropertySet(final byte[] stream, final int offset, final int length)
public PropertySet(final byte[] stream)
public PropertySet(final PropertySet ps)
'''
pass
def getByteOrder():
'''public int getByteOrder()
'''
pass
def setByteOrder():
'''public void setByteOrder(final int byteOrder)
'''
pass
def getFormat():
'''public int getFormat()
'''
pass
def setFormat():
'''public void setFormat(final int format)
'''
pass
def getOSVersion():
'''public int getOSVersion()
'''
pass
def setOSVersion():
'''public void setOSVersion(final int osVersion)
'''
pass
def getClassID():
'''public ClassID getClassID()
'''
pass
def setClassID():
'''public void setClassID(final ClassID classID)
'''
pass
def getSectionCount():
'''public int getSectionCount()
'''
pass
def getSections():
'''public List<Section> getSections()
'''
pass
def addSection():
'''public void addSection(final Section section)
'''
pass
def clearSections():
'''public void clearSections()
'''
pass
def getPropertySetIDMap():
'''public PropertyIDMap getPropertySetIDMap()
'''
pass
def isPropertySetStream():
'''public static boolean isPropertySetStream(final InputStream stream)
public static boolean isPropertySetStream(final byte[] src, final int offset, final int length)
'''
pass
def write():
'''public void write(final OutputStream out)
public void write(final DirectoryEntry dir, final String name)
'''
pass
def toInputStream():
'''public InputStream toInputStream()
'''
pass
def getPropertyStringValue():
'''public static String getPropertyStringValue(final Object propertyValue)
'''
pass
def isSummaryInformation():
'''public boolean isSummaryInformation()
'''
pass
def isDocumentSummaryInformation():
'''public boolean isDocumentSummaryInformation()
'''
pass
def getProperties():
'''public Property[] getProperties()
'''
pass
def wasNull():
'''public boolean wasNull()
'''
pass
def getFirstSection():
'''public Section getFirstSection()
'''
pass
def getSingleSection():
'''public Section getSingleSection()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def toString():
'''public String toString()
'''
pass
