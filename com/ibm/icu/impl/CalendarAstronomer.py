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
def CalendarAstronomer():
'''public CalendarAstronomer()
public CalendarAstronomer(final Date d)
public CalendarAstronomer(final long aTime)
public CalendarAstronomer(final double longitude, final double latitude)
'''
pass
def setTime():
'''public void setTime(final long aTime)
'''
pass
def setDate():
'''public void setDate(final Date date)
'''
pass
def setJulianDay():
'''public void setJulianDay(final double jdn)
'''
pass
def getTime():
'''public long getTime()
'''
pass
def getDate():
'''public Date getDate()
'''
pass
def getJulianDay():
'''public double getJulianDay()
'''
pass
def getJulianCentury():
'''public double getJulianCentury()
'''
pass
def getGreenwichSidereal():
'''public double getGreenwichSidereal()
'''
pass
def getLocalSidereal():
'''public double getLocalSidereal()
'''
pass
def eclipticToEquatorial():
'''public final Equatorial eclipticToEquatorial(final Ecliptic ecliptic)
public final Equatorial eclipticToEquatorial(final double eclipLong, final double eclipLat)
public final Equatorial eclipticToEquatorial(final double eclipLong)
'''
pass
def eclipticToHorizon():
'''public Horizon eclipticToHorizon(final double eclipLong)
'''
pass
def getSunLongitude():
'''public double getSunLongitude()
'''
pass
def getSunPosition():
'''public Equatorial getSunPosition()
'''
pass
def getSunTime():
'''public long getSunTime(final double desired, final boolean next)
public long getSunTime(final SolarLongitude desired, final boolean next)
'''
pass
def eval():
'''public double eval()
public Equatorial eval()
public double eval()
public Equatorial eval()
'''
pass
def getSunRiseSet():
'''public long getSunRiseSet(final boolean rise)
'''
pass
def getMoonPosition():
'''public Equatorial getMoonPosition()
'''
pass
def getMoonAge():
'''public double getMoonAge()
'''
pass
def getMoonPhase():
'''public double getMoonPhase()
'''
pass
def getMoonTime():
'''public long getMoonTime(final double desired, final boolean next)
public long getMoonTime(final MoonAge desired, final boolean next)
'''
pass
def getMoonRiseSet():
'''public long getMoonRiseSet(final boolean rise)
'''
pass
def local():
'''public String local(final long localMillis)
'''
pass
def Ecliptic():
'''public Ecliptic(final double lat, final double lon)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
'''
pass
def Equatorial():
'''public Equatorial(final double asc, final double dec)
'''
pass
def toHmsString():
'''public String toHmsString()
'''
pass
def Horizon():
'''public Horizon(final double alt, final double azim)
'''
pass
