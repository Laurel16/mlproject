from distance import haversine

def test_type_of_result():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 48.8609473, 2.3646878
    assert type(haversine(lon1, lat1, lon2, lat2)) is float

