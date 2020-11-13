import eurec4a


def test_flight_segment_availability():
    segments = eurec4a.get_flight_segments()
    assert "HALO" in segments


def test_flight_segment_availability_by_version():
    segments = eurec4a.get_flight_segments("v1.0.1-rc1")
    assert "HALO" in segments


def test_meta_availability():
    meta = eurec4a.get_meta()
    assert "HALO" in meta


def test_inake_catalog_availability():
    cat = eurec4a.get_intake_catalog()
    assert "barbados" in cat
