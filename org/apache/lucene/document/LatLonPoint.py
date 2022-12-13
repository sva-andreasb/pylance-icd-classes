BYTES = "int  4"
def setLocationValue():
    '''public void setLocationValue(final double latitude, final double longitude)
    '''
def LatLonPoint():
    '''public LatLonPoint(final String name, final double latitude, final double longitude)
    '''
def toString():
    '''public String toString()
    '''
def newBoxQuery():
    '''public static Query newBoxQuery(final String field, final double minLatitude, final double maxLatitude, double minLongitude, final double maxLongitude)
    '''
def newDistanceQuery():
    '''public static Query newDistanceQuery(final String field, final double latitude, final double longitude, final double radiusMeters)
    '''
def newPolygonQuery():
    '''public static Query newPolygonQuery(final String field, final Polygon... polygons)
    '''
def newDistanceFeatureQuery():
    '''public static Query newDistanceFeatureQuery(final String field, final float weight, final double originLat, final double originLon, final double pivotDistanceMeters)
    '''
