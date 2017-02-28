def test_pinger_basic():
    from pyping.pinger import main
    routine = main('google.com')
    timings = next(routine)
    assert 60 in timings
    assert 600 in timings
    assert 3600 in timings
    for period, v in timings.items():
        assert v["avg"] > 0
        assert v["tmin"] > 0
        assert v["tmax"] > 0
        assert "ch_v" in v
        assert "losts" in v
        assert "dns_errors" in v
