import wavelib
import numpy as np
from numpy.testing import assert_array_equal

def test_edge_trigger():
    signal = \
        np.array([   -8.,  188.,  312.,  324.,  196.,    8., -184., -316., -332.,
                   -196.,   -8.,  188.,  316.,  328.,  196.,    8., -188., -320.,
                   -328., -200.,   -4.,  188.,  316.,  324.,  200.,    8., -188.,
                   -316., -332., -200.,   -8.,  188.,  312.,  328.,  196.,    4.,
                   -192., -316., -332., -200.,   -8.,  188.,  312.,  328.,  200.,
                      8., -184., -320., -328., -200. ])
    assert_array_equal(
        wavelib.edge_trigger(signal, cursor=0, noise_threshold=10),
        np.array([ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 1, 0, 0, 0, 0 ])
    )
    
def test_trigger_count():
    trigger = np.array([ 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1 ])
    assert_array_equal(
        wavelib.trigger_count(trigger),
        np.array([ 0., 0.5, 1, 1.25, 1.50, 1.75, 2, 2.25, 2.5, 2.75, 3 ])
    )
