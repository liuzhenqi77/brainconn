from load_samples import *
import numpy as np
import brainconn as bc


def test_breadthdist():
    x = load_sample(thres=.02)
    r, d = bc.breadthdist(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(r), np.sum(d))
    assert np.sum(r) == 5804
    assert np.sum(d) == 30762


def test_reachdist():
    x = load_sample(thres=.02)
    r, d = bc.reachdist(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(r), np.sum(d))
    assert np.sum(r) == 5804
    assert np.sum(d) == 30762

    bx = bc.binarize(x, copy=False)
    br, bd = bc.reachdist(bx)
    bd[np.where(np.isinf(bd))] = 0
    print(np.sum(br), np.sum(bd))
    assert np.sum(br) == 5804
    assert np.sum(bd) == 30762


def test_distance_bin():
    x = bc.binarize(load_sample(thres=.02), copy=False)
    d = bc.distance_bin(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(d))
    assert np.sum(d) == 30506  # deals with diagonals differently


def test_distance_wei():
    x = load_sample(thres=.02)
    d, e = bc.distance_wei(x)
    d[np.where(np.isinf(d))] = 0
    print(np.sum(d), np.sum(e))

    assert np.allclose(np.sum(d), 155650.1, atol=.01)
    assert np.sum(e) == 30570

def test_charpath():
    x = load_sample(thres=.02)
    d, e = bc.distance_wei(x)
    l, eff, ecc, radius, diameter = bc.charpath(d)

    assert np.any(np.isinf(d))
    assert not np.isnan(radius)
    assert not np.isnan(diameter)