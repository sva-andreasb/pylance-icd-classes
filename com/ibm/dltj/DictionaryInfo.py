VIEWABLE_DEFAULT = "boolean  false"
PROPER_CASE_DEFAULT = "boolean  false"
LOWER_CASE_DEFAULT = "boolean  false"
DLT_REL_COMPAT_V53 = "int  5300"
DLT_REL_COMPAT_V60 = "int  6000"
DLT_REL_COMPAT_V61 = "int  6100"
DLT_REL_COMPAT_V70 = "int  7000"
RELEASE_COMPAT_DEFAULT = "int  6100"
LATIN1 = "String  Latin1""
def DictionaryInfo():
'''public DictionaryInfo()
public DictionaryInfo(final long n, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5, final String s)
public DictionaryInfo(final long n, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5, final String s, final boolean b6, final boolean b7, final boolean b8)
public DictionaryInfo(final long version, final boolean isEditable, final boolean isMinimizable, final boolean isMinimized, final boolean isDeterministic, final boolean isReversed, final String copyrightStatement, final boolean isProperCase, final boolean isLowerCase, final boolean isViewable, final int releaseCompatibility)
'''
pass
def clear():
'''public synchronized void clear()
'''
pass
def getLanguages():
'''public synchronized String[] getLanguages()
'''
pass
def getLanguagesSet():
'''public synchronized Set getLanguagesSet()
'''
pass
def getLocales():
'''public synchronized Locale[] getLocales()
'''
pass
def getFunctions():
'''public synchronized Integer[] getFunctions(final String key)
'''
pass
def hasFunction():
'''public boolean hasFunction(final int value)
'''
pass
def getCopyrightStatement():
'''public synchronized String getCopyrightStatement()
'''
pass
def setCopyrightStatement():
'''public void setCopyrightStatement(final String copyrightStatement)
'''
pass
def getHeaderLength():
'''public synchronized long getHeaderLength()
'''
pass
def isBigEndian():
'''public synchronized boolean isBigEndian()
'''
pass
def isDeterministic():
'''public synchronized boolean isDeterministic()
'''
pass
def isEditable():
'''public boolean isEditable()
'''
pass
def setNotEditable():
'''public void setNotEditable()
'''
pass
def setNotViewable():
'''public void setNotViewable()
'''
pass
def isMinimizable():
'''public synchronized boolean isMinimizable()
'''
pass
def isMinimized():
'''public synchronized boolean isMinimized()
'''
pass
def isReversed():
'''public synchronized boolean isReversed()
'''
pass
def getLangToTypesMap():
'''public synchronized TreeMap getLangToTypesMap()
'''
pass
def getLast_modified():
'''public synchronized int getLast_modified()
'''
pass
def getNumberOfLanguages():
'''public synchronized long getNumberOfLanguages()
'''
pass
def getNumberOfLinks():
'''public synchronized long getNumberOfLinks()
'''
pass
def getNumberOfGlosses():
'''public synchronized long getNumberOfGlosses()
'''
pass
def getNumberOfPools():
'''public synchronized long getNumberOfPools()
'''
pass
def getNumberOfStates():
'''public synchronized long getNumberOfStates()
'''
pass
def getVersion():
'''public long getVersion()
'''
pass
def setVersion():
'''public void setVersion(final int n)
'''
pass
def getVersionStr():
'''public synchronized String getVersionStr()
'''
pass
def getReleaseCompatibility():
'''public int getReleaseCompatibility()
'''
pass
def isProperCase():
'''public boolean isProperCase()
'''
pass
def isLowerCase():
'''public boolean isLowerCase()
'''
pass
def isViewable():
'''public boolean isViewable()
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def setDescription():
'''public void setDescription(final String description)
'''
pass
def addType():
'''public synchronized void addType(final String s, final int n)
'''
pass
def mergeCopyright():
'''public synchronized void mergeCopyright(final String str)
'''
pass
def getGlossCompatibilityLevel():
'''public static int getGlossCompatibilityLevel(final int n)
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def toString():
'''public String toString()
'''
pass
