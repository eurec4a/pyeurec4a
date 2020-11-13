# EUREC4A python tools

This package aims to be a small collection of useful tools for the analysis of EUREC4A. There has been some discussion if this package should exist at all, because it might lead to a lock-in into python regarding the ease of use of EUREC4A-data and also many of the tools we are developing and using should not be EUREC4A exclusive. Thus, at least for now, we try to keep this package fairly minimal.

## usage

The package provides a few function to obtain data from the eurec4a field campaign, use it as follows:

```ipython
In [1]: import eurec4a
```

### obtaining informations about flights and segments

```ipython
In [2]: flightinfo = eurec4a.get_flight_segments()

In [3]: flightinfo["HALO"]["HALO-0119"]["takeoff"]
Out[3]: datetime.datetime(2020, 1, 19, 9, 34, 25)
```

### obtaining general campaign metadata

```ipython
In [4]: meta = eurec4a.get_meta()

In [5]: meta["ATR42"]["color"]
Out[5]: '#f7c96b'
```

### accessing public datasets via the intake data catalog

```ipython
In [6]: cat = eurec4a.get_intake_catalog()

In [7]: cat.radiosondes.ronbrown.to_dask()
Out[7]:
<xarray.Dataset>
Dimensions:      (alt: 3100, nv: 2, sounding: 329)
Coordinates:
  * alt          (alt) int16 0 10 20 30 40 50 ... 30950 30960 30970 30980 30990
    flight_time  (sounding, alt) datetime64[ns] dask.array<chunksize=(83, 775), meta=np.ndarray>
    lat          (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    lon          (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    sounding_id  (sounding) |S1000 dask.array<chunksize=(165,), meta=np.ndarray>
Dimensions without coordinates: nv, sounding
Data variables:
    N_gps        (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    N_ptu        (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    alt_bnds     (alt, nv) int16 dask.array<chunksize=(3100, 2), meta=np.ndarray>
    ascent_flag  (sounding) int16 dask.array<chunksize=(329,), meta=np.ndarray>
    dp           (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    dz           (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    launch_time  (sounding) datetime64[ns] dask.array<chunksize=(329,), meta=np.ndarray>
    m_gps        (sounding, alt) int16 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    m_ptu        (sounding, alt) int16 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    mr           (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    p            (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    platform_id  (sounding) int16 dask.array<chunksize=(329,), meta=np.ndarray>
    q            (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    rh           (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    ta           (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    theta        (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    u            (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    v            (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    wdir         (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
    wspd         (sounding, alt) float32 dask.array<chunksize=(83, 1550), meta=np.ndarray>
Attributes:
    Conventions:      CF-1.7
    acknowledgement:  The MPI-M is listed as the institute of first contact. ...
    campaign_id:      EUREC4A
    created_on:       Fri Jun 26 11:12:20 2020
    created_with:     batch_interpolate_soundings.py with its last modificati...
    doi:              10.25326/62
    featureType:      trajectory
    instrument:       Radiosonde RS41-SGP by Vaisala
    instrument_id:    Vaisala-RS
    platform_id:      RonBrown
    references:       Stephan et al. (2020): Ship- and island-based atmospher...
    title:            EUREC4A level 2 sounding data
    version:          v2.2.0
```
