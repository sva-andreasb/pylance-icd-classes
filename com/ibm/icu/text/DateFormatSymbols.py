FORMAT = "int  0"
STANDALONE = "int  1"
NUMERIC = "int  2"
DT_CONTEXT_COUNT = "int  3"
ABBREVIATED = "int  0"
WIDE = "int  1"
NARROW = "int  2"
SHORT = "int  3"
DT_WIDTH_COUNT = "int  4"
def DateFormatSymbols():
    '''    public DateFormatSymbols()
    public DateFormatSymbols(final Locale locale)
    public DateFormatSymbols(final ULocale locale)
    public DateFormatSymbols(final Calendar cal, final Locale locale)
    public DateFormatSymbols(final Calendar cal, final ULocale locale)
    public DateFormatSymbols(final Class<? extends Calendar> calendarClass, final Locale locale)
    public DateFormatSymbols(final Class<? extends Calendar> calendarClass, final ULocale locale)
    public DateFormatSymbols(final ResourceBundle bundle, final Locale locale)
    public DateFormatSymbols(final ResourceBundle bundle, final ULocale locale)
    '''
def getInstance():
    '''    public static DateFormatSymbols getInstance()
    public static DateFormatSymbols getInstance(final Locale locale)
    public static DateFormatSymbols getInstance(final ULocale locale)
    '''
def getAvailableLocales():
    '''    public static Locale[] getAvailableLocales()
    '''
def getAvailableULocales():
    '''    public static ULocale[] getAvailableULocales()
    '''
def getEras():
    '''    public String[] getEras()
    '''
def setEras():
    '''    public void setEras(final String[] newEras)
    '''
def getEraNames():
    '''    public String[] getEraNames()
    '''
def setEraNames():
    '''    public void setEraNames(final String[] newEraNames)
    '''
def getNarrowEras():
    '''    public String[] getNarrowEras()
    '''
def setNarrowEras():
    '''    public void setNarrowEras(final String[] newNarrowEras)
    '''
def getMonths():
    '''    public String[] getMonths()
    public String[] getMonths(final int context, final int width)
    '''
def setMonths():
    '''    public void setMonths(final String[] newMonths)
    public void setMonths(final String[] newMonths, final int context, final int width)
    '''
def getShortMonths():
    '''    public String[] getShortMonths()
    '''
def setShortMonths():
    '''    public void setShortMonths(final String[] newShortMonths)
    '''
def getWeekdays():
    '''    public String[] getWeekdays()
    public String[] getWeekdays(final int context, final int width)
    '''
def setWeekdays():
    '''    public void setWeekdays(final String[] newWeekdays, final int context, final int width)
    public void setWeekdays(final String[] newWeekdays)
    '''
def getShortWeekdays():
    '''    public String[] getShortWeekdays()
    '''
def setShortWeekdays():
    '''    public void setShortWeekdays(final String[] newAbbrevWeekdays)
    '''
def getQuarters():
    '''    public String[] getQuarters(final int context, final int width)
    '''
def setQuarters():
    '''    public void setQuarters(final String[] newQuarters, final int context, final int width)
    '''
def getYearNames():
    '''    public String[] getYearNames(final int context, final int width)
    '''
def setYearNames():
    '''    public void setYearNames(final String[] yearNames, final int context, final int width)
    '''
def getZodiacNames():
    '''    public String[] getZodiacNames(final int context, final int width)
    '''
def setZodiacNames():
    '''    public void setZodiacNames(final String[] zodiacNames, final int context, final int width)
    '''
def getLeapMonthPattern():
    '''    public String getLeapMonthPattern(final int context, final int width)
    '''
def setLeapMonthPattern():
    '''    public void setLeapMonthPattern(final String leapMonthPattern, final int context, final int width)
    '''
def getAmPmStrings():
    '''    public String[] getAmPmStrings()
    '''
def setAmPmStrings():
    '''    public void setAmPmStrings(final String[] newAmpms)
    '''
def getTimeSeparatorString():
    '''    public String getTimeSeparatorString()
    '''
def setTimeSeparatorString():
    '''    public void setTimeSeparatorString(final String newTimeSeparator)
    '''
def getZoneStrings():
    '''    public String[][] getZoneStrings()
    '''
def setZoneStrings():
    '''    public void setZoneStrings(final String[][] newZoneStrings)
    '''
def getLocalPatternChars():
    '''    public String getLocalPatternChars()
    '''
def setLocalPatternChars():
    '''    public void setLocalPatternChars(final String newLocalPatternChars)
    '''
def clone():
    '''    public Object clone()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def getDateFormatBundle():
    '''    public static ResourceBundle getDateFormatBundle(final Class<? extends Calendar> calendarClass, final Locale locale)
    public static ResourceBundle getDateFormatBundle(final Class<? extends Calendar> calendarClass, final ULocale locale)
    public static ResourceBundle getDateFormatBundle(final Calendar cal, final Locale locale)
    public static ResourceBundle getDateFormatBundle(final Calendar cal, final ULocale locale)
    '''
def getLocale():
    '''    public final ULocale getLocale(final ULocale.Type type)
    '''
def put():
    '''    public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
    '''
