from numba import njit
import numpy as np


@njit(cache=True)
def compute_transport_multipole_matrix(L: float, K1: float, K2: float) -> np.ndarray:

    R = np.zeros((6, 6))

    R[0, 0] = 1 - (K1 * L ** 2) / 2 + (K1 ** 2 * L ** 4) / 24 - (K1 ** 3 * L ** 6) / 720 + (
            K1 ** 4 * L ** 8) / 40320 - (K1 ** 5 * L ** 10) / 3628800 + (K1 ** 6 * L ** 12) / 479001600
    R[0, 1] = L - (K1 * L ** 3) / 6 + (K1 ** 2 * L ** 5) / 120 - (K1 ** 3 * L ** 7) / 5040 + (
            K1 ** 4 * L ** 9) / 362880 - (K1 ** 5 * L ** 11) / 39916800 + (K1 ** 6 * L ** 13) / 6227020800
    R[0, 5] = 0
    R[1, 0] = -(K1 * L) + (K1 ** 2 * L ** 3) / 6 - (K1 ** 3 * L ** 5) / 120 + (K1 ** 4 * L ** 7) / 5040 - (
            K1 ** 5 * L ** 9) / 362880 + (K1 ** 6 * L ** 11) / 39916800
    R[1, 1] = 1 - (K1 * L ** 2) / 2 + (K1 ** 2 * L ** 4) / 24 - (K1 ** 3 * L ** 6) / 720 + (
            K1 ** 4 * L ** 8) / 40320 - (K1 ** 5 * L ** 10) / 3628800 + (K1 ** 6 * L ** 12) / 479001600
    R[1, 5] = 0
    R[2, 2] = 1 + (K1 * L ** 2) / 2 + (K1 ** 2 * L ** 4) / 24 + (K1 ** 3 * L ** 6) / 720 + (
            K1 ** 4 * L ** 8) / 40320 + (K1 ** 5 * L ** 10) / 3628800 + (K1 ** 6 * L ** 12) / 479001600
    R[2, 3] = L + (K1 * L ** 3) / 6 + (K1 ** 2 * L ** 5) / 120 + (K1 ** 3 * L ** 7) / 5040 + (
            K1 ** 4 * L ** 9) / 362880 + (K1 ** 5 * L ** 11) / 39916800 + (K1 ** 6 * L ** 13) / 6227020800
    R[3, 2] = K1 * L + (K1 ** 2 * L ** 3) / 6 + (K1 ** 3 * L ** 5) / 120 + (K1 ** 4 * L ** 7) / 5040 + (
            K1 ** 5 * L ** 9) / 362880 + (K1 ** 6 * L ** 11) / 39916800
    R[3, 3] = 1 + (K1 * L ** 2) / 2 + (K1 ** 2 * L ** 4) / 24 + (K1 ** 3 * L ** 6) / 720 + (
            K1 ** 4 * L ** 8) / 40320 + (K1 ** 5 * L ** 10) / 3628800 + (K1 ** 6 * L ** 12) / 479001600
    R[4, 4] = 1
    R[5, 5] = 1

    return R


@njit(cache=True)
def compute_transport_multipole_tensor(L: float, K1: float, K2: float) -> np.ndarray:

    T = np.zeros((6, 6, 6))

    T[0, 0, 0] = -(K2 * L ** 2) / 2 + (K1 * K2 * L ** 4) / 8 - (11 * K1 ** 2 * K2 * L ** 6) / 720 + (
                43 * K1 ** 3 * K2 * L ** 8) / 40320 - (19 * K1 ** 4 * K2 * L ** 10) / 403200 + (
                             683 * K1 ** 5 * K2 * L ** 12) / 479001600 - (
                             2731 * K1 ** 6 * K2 * L ** 14) / 87178291200
    T[0, 0, 1] = -(K2 * L ** 3) / 3 + (K1 * K2 * L ** 5) / 12 - (K1 ** 2 * K2 * L ** 7) / 120 + (
                17 * K1 ** 3 * K2 * L ** 9) / 36288 - (31 * K1 ** 4 * K2 * L ** 11) / 1814400 + (
                             K1 ** 5 * K2 * L ** 13) / 2280960 - (5461 * K1 ** 6 * K2 * L ** 15) / 653837184000
    T[0, 0, 5] = (K1 * L ** 2) / 2 - (K1 ** 2 * L ** 4) / 12 + (K1 ** 3 * L ** 6) / 240 - (
                K1 ** 4 * L ** 8) / 10080 + (K1 ** 5 * L ** 10) / 725760 - (K1 ** 6 * L ** 12) / 79833600
    T[0, 1, 1] = -(K2 * L ** 4) / 12 + (K1 * K2 * L ** 6) / 72 - (K1 ** 2 * K2 * L ** 8) / 960 + (
                17 * K1 ** 3 * K2 * L ** 10) / 362880 - (31 * K1 ** 4 * K2 * L ** 12) / 21772800 + (
                             K1 ** 5 * K2 * L ** 14) / 31933440 - (5461 * K1 ** 6 * K2 * L ** 16) / 10461394944000
    T[0, 1, 5] = (K1 * L ** 3) / 6 - (K1 ** 2 * L ** 5) / 60 + (K1 ** 3 * L ** 7) / 1680 - (
                K1 ** 4 * L ** 9) / 90720 + (K1 ** 5 * L ** 11) / 7983360 - (K1 ** 6 * L ** 13) / 1037836800
    T[0, 5, 5] = 0
    T[0, 2, 2] = (K2 * L ** 2) / 2 + (K1 * K2 * L ** 4) / 24 + (7 * K1 ** 2 * K2 * L ** 6) / 720 + (
                5 * K1 ** 3 * K2 * L ** 8) / 8064 + (103 * K1 ** 4 * K2 * L ** 10) / 3628800 + (
                             409 * K1 ** 5 * K2 * L ** 12) / 479001600 + (149 * K1 ** 6 * K2 * L ** 14) / 7925299200
    T[0, 2, 3] = (K2 * L ** 3) / 3 + (K1 * K2 * L ** 5) / 20 + (13 * K1 ** 2 * K2 * L ** 7) / 2520 + (
                17 * K1 ** 3 * K2 * L ** 9) / 60480 + (41 * K1 ** 4 * K2 * L ** 11) / 3991680 + (
                             K1 ** 5 * K2 * L ** 13) / 3801600 + (3277 * K1 ** 6 * K2 * L ** 15) / 653837184000
    T[0, 3, 3] = (K2 * L ** 4) / 12 + (K1 * K2 * L ** 6) / 120 + (13 * K1 ** 2 * K2 * L ** 8) / 20160 + (
                17 * K1 ** 3 * K2 * L ** 10) / 604800 + (41 * K1 ** 4 * K2 * L ** 12) / 47900160 + (
                             K1 ** 5 * K2 * L ** 14) / 53222400 + (3277 * K1 ** 6 * K2 * L ** 16) / 10461394944000
    T[1, 0, 0] = -(K2 * L) + (K1 * K2 * L ** 3) / 2 - (11 * K1 ** 2 * K2 * L ** 5) / 120 + (
                43 * K1 ** 3 * K2 * L ** 7) / 5040 - (19 * K1 ** 4 * K2 * L ** 9) / 40320 + (
                             683 * K1 ** 5 * K2 * L ** 11) / 39916800 - (2731 * K1 ** 6 * K2 * L ** 13) / 6227020800
    T[1, 0, 1] = -(K2 * L ** 2) + (5 * K1 * K2 * L ** 4) / 12 - (7 * K1 ** 2 * K2 * L ** 6) / 120 + (
                17 * K1 ** 3 * K2 * L ** 8) / 4032 - (341 * K1 ** 4 * K2 * L ** 10) / 1814400 + (
                             13 * K1 ** 5 * K2 * L ** 12) / 2280960 - (5461 * K1 ** 6 * K2 * L ** 14) / 43589145600
    T[1, 0, 5] = K1 * L - (K1 ** 2 * L ** 3) / 3 + (K1 ** 3 * L ** 5) / 40 - (K1 ** 4 * L ** 7) / 1260 + (
                K1 ** 5 * L ** 9) / 72576 - (K1 ** 6 * L ** 11) / 6652800
    T[1, 1, 1] = -(K2 * L ** 3) / 3 + (K1 * K2 * L ** 5) / 12 - (K1 ** 2 * K2 * L ** 7) / 120 + (
                17 * K1 ** 3 * K2 * L ** 9) / 36288 - (31 * K1 ** 4 * K2 * L ** 11) / 1814400 + (
                             K1 ** 5 * K2 * L ** 13) / 2280960 - (5461 * K1 ** 6 * K2 * L ** 15) / 653837184000
    T[1, 1, 5] = (K1 * L ** 2) / 2 - (K1 ** 2 * L ** 4) / 12 + (K1 ** 3 * L ** 6) / 240 - (
                K1 ** 4 * L ** 8) / 10080 + (K1 ** 5 * L ** 10) / 725760 - (K1 ** 6 * L ** 12) / 79833600
    T[1, 5, 5] = 0
    T[1, 2, 2] = K2 * L + (K1 * K2 * L ** 3) / 6 + (7 * K1 ** 2 * K2 * L ** 5) / 120 + (
                5 * K1 ** 3 * K2 * L ** 7) / 1008 + (103 * K1 ** 4 * K2 * L ** 9) / 362880 + (
                             409 * K1 ** 5 * K2 * L ** 11) / 39916800 + (149 * K1 ** 6 * K2 * L ** 13) / 566092800
    T[1, 2, 3] = K2 * L ** 2 + (K1 * K2 * L ** 4) / 4 + (13 * K1 ** 2 * K2 * L ** 6) / 360 + (
                17 * K1 ** 3 * K2 * L ** 8) / 6720 + (41 * K1 ** 4 * K2 * L ** 10) / 362880 + (
                             13 * K1 ** 5 * K2 * L ** 12) / 3801600 + (3277 * K1 ** 6 * K2 * L ** 14) / 43589145600
    T[1, 3, 3] = (K2 * L ** 3) / 3 + (K1 * K2 * L ** 5) / 20 + (13 * K1 ** 2 * K2 * L ** 7) / 2520 + (
                17 * K1 ** 3 * K2 * L ** 9) / 60480 + (41 * K1 ** 4 * K2 * L ** 11) / 3991680 + (
                             K1 ** 5 * K2 * L ** 13) / 3801600 + (3277 * K1 ** 6 * K2 * L ** 15) / 653837184000
    T[2, 0, 2] = K2 * L ** 2 + (K1 * K2 * L ** 4) / 12 - (K1 ** 2 * K2 * L ** 6) / 120 - (
                K1 ** 3 * K2 * L ** 8) / 6720 + (13 * K1 ** 4 * K2 * L ** 10) / 1814400 + (
                             13 * K1 ** 5 * K2 * L ** 12) / 239500800 - (17 * K1 ** 6 * K2 * L ** 14) / 14529715200
    T[2, 0, 3] = (K2 * L ** 3) / 3 - (K1 * K2 * L ** 5) / 60 - (K1 ** 2 * K2 * L ** 7) / 504 + (
                K1 ** 3 * K2 * L ** 9) / 60480 + (19 * K1 ** 4 * K2 * L ** 11) / 19958400 - (
                             K1 ** 5 * K2 * L ** 13) / 239500800 - (K1 ** 6 * K2 * L ** 15) / 8491392000
    T[2, 1, 2] = (K2 * L ** 3) / 3 + (K1 * K2 * L ** 5) / 20 - (K1 ** 2 * K2 * L ** 7) / 2520 - (
                K1 ** 3 * K2 * L ** 9) / 20160 + (K1 ** 4 * K2 * L ** 11) / 2851200 + (
                             K1 ** 5 * K2 * L ** 13) / 79833600 - (K1 ** 6 * K2 * L ** 15) / 26153487360
    T[2, 1, 3] = (K2 * L ** 4) / 6 + (K1 * K2 * L ** 6) / 180 - (K1 ** 2 * K2 * L ** 8) / 3360 - (
                K1 ** 3 * K2 * L ** 10) / 302400 + (13 * K1 ** 4 * K2 * L ** 12) / 119750400 + (
                             K1 ** 5 * K2 * L ** 14) / 1676505600 - (17 * K1 ** 6 * K2 * L ** 16) / 1743565824000
    T[2, 2, 5] = -(K1 * L ** 2) / 2 - (K1 ** 2 * L ** 4) / 12 - (K1 ** 3 * L ** 6) / 240 - (
                K1 ** 4 * L ** 8) / 10080 - (K1 ** 5 * L ** 10) / 725760 - (K1 ** 6 * L ** 12) / 79833600
    T[2, 3, 5] = -(K1 * L ** 3) / 6 - (K1 ** 2 * L ** 5) / 60 - (K1 ** 3 * L ** 7) / 1680 - (
                K1 ** 4 * L ** 9) / 90720 - (K1 ** 5 * L ** 11) / 7983360 - (K1 ** 6 * L ** 13) / 1037836800
    T[3, 0, 2] = 2 * K2 * L + (K1 * K2 * L ** 3) / 3 - (K1 ** 2 * K2 * L ** 5) / 20 - (
                K1 ** 3 * K2 * L ** 7) / 840 + (13 * K1 ** 4 * K2 * L ** 9) / 181440 + (
                             13 * K1 ** 5 * K2 * L ** 11) / 19958400 - (17 * K1 ** 6 * K2 * L ** 13) / 1037836800
    T[3, 0, 3] = K2 * L ** 2 - (K1 * K2 * L ** 4) / 12 - (K1 ** 2 * K2 * L ** 6) / 72 + (
                K1 ** 3 * K2 * L ** 8) / 6720 + (19 * K1 ** 4 * K2 * L ** 10) / 1814400 - (
                             13 * K1 ** 5 * K2 * L ** 12) / 239500800 - (K1 ** 6 * K2 * L ** 14) / 566092800
    T[3, 1, 2] =  K2 * L ** 2 + (K1 * K2 * L ** 4) / 4 - (
                K1 ** 2 * K2 * L ** 6) / 360 - (K1 ** 3 * K2 * L ** 8) / 2240 + (
                             K1 ** 4 * K2 * L ** 10) / 259200 + (13 * K1 ** 5 * K2 * L ** 12) / 79833600 - (
                             K1 ** 6 * K2 * L ** 14) / 1743565824
    T[3, 1, 3] = (2 * K2 * L ** 3) / 3 + (K1 * K2 * L ** 5) / 30 - (K1 ** 2 * K2 * L ** 7) / 420 - (
                K1 ** 3 * K2 * L ** 9) / 30240 + (13 * K1 ** 4 * K2 * L ** 11) / 9979200 + (
                             K1 ** 5 * K2 * L ** 13) / 119750400 - 1.5600214012912426 * 10 ** -10 * K1 ** 6 * K2 * L ** 15
    T[3, 2, 5] = -(K1 * L) - (K1 ** 2 * L ** 3) / 3 - (K1 ** 3 * L ** 5) / 40 - (K1 ** 4 * L ** 7) / 1260 - (
                K1 ** 5 * L ** 9) / 72576 - (K1 ** 6 * L ** 11) / 6652800
    T[3, 3, 5] = -(K1 * L ** 2) / 2 - (K1 ** 2 * L ** 4) / 12 - (K1 ** 3 * L ** 6) / 240 - (
                K1 ** 4 * L ** 8) / 10080 - (K1 ** 5 * L ** 10) / 725760 - (K1 ** 6 * L ** 12) / 79833600
    return T

