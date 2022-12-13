FORMAT = "int 0"
STANDALONE = "int 1"
NUMERIC = "int 2"
DT_CONTEXT_COUNT = "int 3"
ABBREVIATED = "int 0"
WIDE = "int 1"
NARROW = "int 2"
SHORT = "int 3"
DT_WIDTH_COUNT = "int 4"
def DateFormatSymbols():
'''public DateFormatSymbols()
public DateFormatSymbols(final Locale locale)
public DateFormatSymbols(final ULocale locale)
public DateFormatSymbols(final Calendar cal, final Locale locale)
public DateFormatSymbols(final Calendar cal, final ULocale locale)
public DateFormatSymbols(final Class<? extends Calendar> calendarClass, final Locale locale)
public DateFormatSymbols(final Class<? extends Calendar> calendarClass, final ULocale locale)
public DateFormatSymbols(final ResourceBundle bundle, final Locale locale)
public DateFormatSymbols(final ResourceBundle bundle, final ULocale locale)
'''
pass
def getInstance():
'''public static DateFormatSymbols getInstance()
public static DateFormatSymbols getInstance(final Locale locale)
public static DateFormatSymbols getInstance(final ULocale locale)
'''
pass
def getAvailableLocales():
'''public static Locale[] getAvailableLocales()
'''
pass
def getAvailableULocales():
'''public static ULocale[] getAvailableULocales()
'''
pass
def getEras():
'''public String[] getEras()
'''
pass
def setEras():
'''public void setEras(final String[] newEras)
'''
pass
def getEraNames():
'''public String[] getEraNames()
'''
pass
def setEraNames():
'''public void setEraNames(final String[] newEraNames)
'''
pass
def getNarrowEras():
'''public String[] getNarrowEras()
'''
pass
def setNarrowEras():
'''public void setNarrowEras(final String[] newNarrowEras)
'''
pass
def getMonths():
'''public String[] getMonths()
public String[] getMonths(final int context, final int width)
'''
pass
def setMonths():
'''public void setMonths(final String[] newMonths)
public void setMonths(final String[] newMonths, final int context, final int width)
'''
pass
def getShortMonths():
'''public String[] getShortMonths()
'''
pass
def setShortMonths():
'''public void setShortMonths(final String[] newShortMonths)
'''
pass
def getWeekdays():
'''public String[] getWeekdays()
public String[] getWeekdays(final int context, final int width)
'''
pass
def setWeekdays():
'''public void setWeekdays(final String[] newWeekdays, final int context, final int width)
public void setWeekdays(final String[] newWeekdays)
'''
pass
def getShortWeekdays():
'''public String[] getShortWeekdays()
'''
pass
def setShortWeekdays():
'''public void setShortWeekdays(final String[] newAbbrevWeekdays)
'''
pass
def getQuarters():
'''public String[] getQuarters(final int context, final int width)
'''
pass
def setQuarters():
'''public void setQuarters(final String[] newQuarters, final int context, final int width)
'''
pass
def getYearNames():
'''public String[] getYearNames(final int context, final int width)
'''
pass
def setYearNames():
'''public void setYearNames(final String[] yearNames, final int context, final int width)
'''
pass
def getZodiacNames():
'''public String[] getZodiacNames(final int context, final int width)
'''
pass
def setZodiacNames():
'''public void setZodiacNames(final String[] zodiacNames, final int context, final int width)
'''
pass
def getLeapMonthPattern():
'''public String getLeapMonthPattern(final int context, final int width)
'''
pass
def setLeapMonthPattern():
'''public void setLeapMonthPattern(final String leapMonthPattern, final int context, final int width)
'''
pass
def getAmPmStrings():
'''public String[] getAmPmStrings()
'''
pass
def setAmPmStrings():
'''public void setAmPmStrings(final String[] newAmpms)
'''
pass
def getTimeSeparatorString():
'''public String getTimeSeparatorString()
'''
pass
def setTimeSeparatorString():
'''public void setTimeSeparatorString(final String newTimeSeparator)
'''
pass
def getZoneStrings():
'''public String[][] getZoneStrings()
'''
pass
def setZoneStrings():
'''public void setZoneStrings(final String[][] newZoneStrings)
'''
pass
def getLocalPatternChars():
'''public String getLocalPatternChars()
'''
pass
def setLocalPatternChars():
'''public void setLocalPatternChars(final String newLocalPatternChars)
'''
pass
def clone():
'''public Object clone()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def getDateFormatBundle():
'''public static ResourceBundle getDateFormatBundle(final Class<? extends Calendar> calendarClass, final Locale locale)
public static ResourceBundle getDateFormatBundle(final Class<? extends Calendar> calendarClass, final ULocale locale)
public static ResourceBundle getDateFormatBundle(final Calendar cal, final Locale locale)
public static ResourceBundle getDateFormatBundle(final Calendar cal, final ULocale locale)
'''
pass
def getLocale():
'''public final ULocale getLocale(final ULocale.Type type)
'''
pass
def put():
'''public void put(final UResource.Key key, final UResource.Value value, final boolean noFallback)
'''
pass
