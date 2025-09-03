import pytest
from apps.congestion.models import CongestionRecord
from apps.congestion.services import CongestionService
def test_congestion_model_create():
    ent = CongestionRecord()
    assert ent is not None
    assert ent.validate_congestionrecord()
def test_congestion_model_to_dict():
    ent = CongestionRecord()
    d = ent.to_dict_congestionrecord()
    assert 'status' in d or 'created_at' in d

def test_congestion_core_0():
    svc = CongestionService(config={})
    res = svc.process_congestion_0({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_1():
    svc = CongestionService(config={})
    res = svc.process_congestion_1({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_2():
    svc = CongestionService(config={})
    res = svc.process_congestion_2({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_3():
    svc = CongestionService(config={})
    res = svc.process_congestion_3({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_4():
    svc = CongestionService(config={})
    res = svc.process_congestion_4({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_5():
    svc = CongestionService(config={})
    res = svc.process_congestion_5({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_6():
    svc = CongestionService(config={})
    res = svc.process_congestion_6({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_7():
    svc = CongestionService(config={})
    res = svc.process_congestion_7({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_8():
    svc = CongestionService(config={})
    res = svc.process_congestion_8({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_9():
    svc = CongestionService(config={})
    res = svc.process_congestion_9({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_10():
    svc = CongestionService(config={})
    res = svc.process_congestion_0({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_11():
    svc = CongestionService(config={})
    res = svc.process_congestion_1({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_12():
    svc = CongestionService(config={})
    res = svc.process_congestion_2({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_13():
    svc = CongestionService(config={})
    res = svc.process_congestion_3({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_14():
    svc = CongestionService(config={})
    res = svc.process_congestion_4({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_core_15():
    svc = CongestionService(config={})
    res = svc.process_congestion_5({'value': 10+i, 'user_id':'tester'}, {})
    assert res is not None


def test_congestion_algo_0():
    from apps.congestion.analytics import analytics_congestion_0
    res = analytics_congestion_0([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_1():
    from apps.congestion.analytics import analytics_congestion_1
    res = analytics_congestion_1([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_2():
    from apps.congestion.analytics import analytics_congestion_2
    res = analytics_congestion_2([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_3():
    from apps.congestion.analytics import analytics_congestion_3
    res = analytics_congestion_3([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_4():
    from apps.congestion.analytics import analytics_congestion_4
    res = analytics_congestion_4([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_5():
    from apps.congestion.analytics import analytics_congestion_5
    res = analytics_congestion_5([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_6():
    from apps.congestion.analytics import analytics_congestion_6
    res = analytics_congestion_6([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_7():
    from apps.congestion.analytics import analytics_congestion_7
    res = analytics_congestion_7([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_8():
    from apps.congestion.analytics import analytics_congestion_8
    res = analytics_congestion_8([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_9():
    from apps.congestion.analytics import analytics_congestion_9
    res = analytics_congestion_9([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_10():
    from apps.congestion.analytics import analytics_congestion_0
    res = analytics_congestion_0([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_11():
    from apps.congestion.analytics import analytics_congestion_1
    res = analytics_congestion_1([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_12():
    from apps.congestion.analytics import analytics_congestion_2
    res = analytics_congestion_2([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_13():
    from apps.congestion.analytics import analytics_congestion_3
    res = analytics_congestion_3([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res


def test_congestion_algo_14():
    from apps.congestion.analytics import analytics_congestion_4
    res = analytics_congestion_4([{'value': i*2}])
    assert 'computed' in res or 'mean' in res or 'count' in res