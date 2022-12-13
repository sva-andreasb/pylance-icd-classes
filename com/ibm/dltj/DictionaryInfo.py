VIEWABLE_DEFAULT = "boolean  false"
PROPER_CASE_DEFAULT = "boolean  false"
LOWER_CASE_DEFAULT = "boolean  false"
DLT_REL_COMPAT_V53 = "int  5300"
DLT_REL_COMPAT_V60 = "int  6000"
DLT_REL_COMPAT_V61 = "int  6100"
DLT_REL_COMPAT_V70 = "int  7000"
RELEASE_COMPAT_DEFAULT = "int  6100"
LATIN1 = "String  \"Latin1\""
def DictionaryInfo():
    '''    public DictionaryInfo()
    public DictionaryInfo(final long n, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5, final String s)
    public DictionaryInfo(final long n, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5, final String s, final boolean b6, final boolean b7, final boolean b8)
    public DictionaryInfo(final long version, final boolean isEditable, final boolean isMinimizable, final boolean isMinimized, final boolean isDeterministic, final boolean isReversed, final String copyrightStatement, final boolean isProperCase, final boolean isLowerCase, final boolean isViewable, final int releaseCompatibility)
    '''
def clear():
    '''    public synchronized void clear()
    '''
def getLanguages():
    '''    public synchronized String[] getLanguages()
    '''
def getLanguagesSet():
    '''    public synchronized Set getLanguagesSet()
    '''
def getLocales():
    '''    public synchronized Locale[] getLocales()
    '''
def getFunctions():
    '''    public synchronized Integer[] getFunctions(final String key)
    '''
def hasFunction():
    '''    public boolean hasFunction(final int value)
    '''
def getCopyrightStatement():
    '''    public synchronized String getCopyrightStatement()
    '''
def setCopyrightStatement():
    '''    public void setCopyrightStatement(final String copyrightStatement)
    '''
def getHeaderLength():
    '''    public synchronized long getHeaderLength()
    '''
def isBigEndian():
    '''    public synchronized boolean isBigEndian()
    '''
def isDeterministic():
    '''    public synchronized boolean isDeterministic()
    '''
def isEditable():
    '''    public boolean isEditable()
    '''
def setNotEditable():
    '''    public void setNotEditable()
    '''
def setNotViewable():
    '''    public void setNotViewable()
    '''
def isMinimizable():
    '''    public synchronized boolean isMinimizable()
    '''
def isMinimized():
    '''    public synchronized boolean isMinimized()
    '''
def isReversed():
    '''    public synchronized boolean isReversed()
    '''
def getLangToTypesMap():
    '''    public synchronized TreeMap getLangToTypesMap()
    '''
def getLast_modified():
    '''    public synchronized int getLast_modified()
    '''
def getNumberOfLanguages():
    '''    public synchronized long getNumberOfLanguages()
    '''
def getNumberOfLinks():
    '''    public synchronized long getNumberOfLinks()
    '''
def getNumberOfGlosses():
    '''    public synchronized long getNumberOfGlosses()
    '''
def getNumberOfPools():
    '''    public synchronized long getNumberOfPools()
    '''
def getNumberOfStates():
    '''    public synchronized long getNumberOfStates()
    '''
def getVersion():
    '''    public long getVersion()
    '''
def setVersion():
    '''    public void setVersion(final int n)
    '''
def getVersionStr():
    '''    public synchronized String getVersionStr()
    '''
def getReleaseCompatibility():
    '''    public int getReleaseCompatibility()
    '''
def isProperCase():
    '''    public boolean isProperCase()
    '''
def isLowerCase():
    '''    public boolean isLowerCase()
    '''
def isViewable():
    '''    public boolean isViewable()
    '''
def getDescription():
    '''    public String getDescription()
    '''
def setDescription():
    '''    public void setDescription(final String description)
    '''
def addType():
    '''    public synchronized void addType(final String s, final int n)
    '''
def mergeCopyright():
    '''    public synchronized void mergeCopyright(final String str)
    '''
def getGlossCompatibilityLevel():
    '''    public static int getGlossCompatibilityLevel(final int n)
    '''
def clone():
    '''    public Object clone()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def toString():
    '''    public String toString()
    '''
