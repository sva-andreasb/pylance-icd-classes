SIDEREAL_DAY = "double  23.93446960027"
SOLAR_DAY = "double  24.065709816"
SYNODIC_MONTH = "double  29.530588853"
SIDEREAL_MONTH = "double  27.32166"
TROPICAL_YEAR = "double  365.242191"
SIDEREAL_YEAR = "double  365.25636"
SECOND_MS = "int  1000"
MINUTE_MS = "int  60000"
HOUR_MS = "int  3600000"
DAY_MS = "long  86400000L"
JULIAN_EPOCH_MS = "long  -210866760000000L"
def ():
    '''returns Horizon\n\n
    ()\n
    (final Date d)\n
    (final long aTime)\n
    (final double longitude, final double latitude)\n
    (final double lat, final double lon)\n
    (final double asc, final double dec)\n
    (final double alt, final double azim)\n
    '''
def setTime():
    '''returns None\n\n
    setTime(final long aTime)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final Date date)\n
    '''
def setJulianDay():
    '''returns None\n\n
    setJulianDay(final double jdn)\n
    '''
def getTime():
    '''returns long\n\n
    getTime()\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    '''
def getJulianDay():
    '''returns double\n\n
    getJulianDay()\n
    '''
def getJulianCentury():
    '''returns double\n\n
    getJulianCentury()\n
    '''
def getGreenwichSidereal():
    '''returns double\n\n
    getGreenwichSidereal()\n
    '''
def getLocalSidereal():
    '''returns double\n\n
    getLocalSidereal()\n
    '''
def eclipticToHorizon():
    '''returns Horizon\n\n
    eclipticToHorizon(final double eclipLong)\n
    '''
def getSunLongitude():
    '''returns double\n\n
    getSunLongitude()\n
    '''
def getSunPosition():
    '''returns Equatorial\n\n
    getSunPosition()\n
    '''
def getSunTime():
    '''returns long\n\n
    getSunTime(final double desired, final boolean next)\n
    getSunTime(final SolarLongitude desired, final boolean next)\n
    '''
def eval():
    '''returns Equatorial\n\n
    eval()\n
    eval()\n
    eval()\n
    eval()\n
    '''
def getSunRiseSet():
    '''returns long\n\n
    getSunRiseSet(final boolean rise)\n
    '''
def getMoonPosition():
    '''returns Equatorial\n\n
    getMoonPosition()\n
    '''
def getMoonAge():
    '''returns double\n\n
    getMoonAge()\n
    '''
def getMoonPhase():
    '''returns double\n\n
    getMoonPhase()\n
    '''
def getMoonTime():
    '''returns long\n\n
    getMoonTime(final double desired, final boolean next)\n
    getMoonTime(final MoonAge desired, final boolean next)\n
    '''
def getMoonRiseSet():
    '''returns long\n\n
    getMoonRiseSet(final boolean rise)\n
    '''
def local():
    '''returns String\n\n
    local(final long localMillis)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    '''
def toHmsString():
    '''returns String\n\n
    toHmsString()\n
    '''
