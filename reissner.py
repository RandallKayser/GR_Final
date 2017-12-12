import numpy as np
import matplotlib.pyplot as pp
import scipy as sp
import sys
oom_num = 10
tau_init = 0
mass = float(sys.argv[1])
charge = float(sys.argv[2])
energy = 1.0
ll = 0.0
r_init = (1.0) * (mass + np.sqrt(mass**2 + charge**2))
rlist = []
for n in xrange(oom_num):
    rlist.append([r_init])

tau_step = [10**(-n) for n in xrange(oom_num)]

new_r = 0


def h(r, M, Q):
    return -2.0*M/r + Q**2.0/r**2.0


def f(r, E, L, M, Q):
    return -np.sqrt(np.abs(E**2.0 - (1.0 + h(r, M, Q)) * (1.0 + L**2.0 / r**2.0)))


for n in xrange(len(tau_step)):
    print n
    while rlist[n][-1] > 0.0:
        new_r = rlist[n][-1] + tau_step[n]*f(rlist[n][-1], energy, ll, mass, charge)
        rlist[n].append(new_r)
    print len(rlist[n])*tau_step[n]


print [len(rlist[n])*tau_step[n] for n in xrange(len(tau_step))]

