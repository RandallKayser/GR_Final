
#---------------------------------------------------------
# bhmass, bhcharge in mm with geometric units
# energy is unitless ratio of energy at infinity per mm (geometric units again)
# ll is angular momentum per mm at inifinity
#---------------------------------------------------------


import numpy as np
import matplotlib.pyplot as pp
import scipy as sp
import sys
output_file = open("output.txt", 'a')
oom_num = 6
tau_init = 0

#solar mass bh
bhmass = 1.47e6
bhcharge = float(sys.argv[1])
energy = float(sys.argv[2])
ll = float(sys.argv[3])

# start at 20 r_s
r_init = (25.0) * (2.0 * bhmass)

rlist = []
for n in xrange(oom_num):
    rlist.append([r_init])

tau_step = [r_init * 10**(-n) for n in xrange(oom_num)]

new_r = 0


def h(r, M, Q):
    return -2.0*M/r + Q*Q/(r*r)

#ode for radial component of geodesic equation
def f(r, E, L, M, Q):
    return -np.sqrt(np.abs(E**2.0 - (1.0 + h(r, M, Q)) * (1.0 + L**2.0 / r**2.0)))


for n in xrange(len(tau_step)):
    while rlist[n][-1] > 0.0:
        new_r = rlist[n][-1] + tau_step[n]*f(rlist[n][-1], energy, ll, bhmass, bhcharge)
        rlist[n].append(new_r)
        print new_r
output_string = str(bhmass) + ", " + str(bhcharge) + ", " + str(energy) + ", " + str(ll) + ", "

for i in xrange(len(tau_step)):
    output_string += str(tau_step[i] * len(rlist[i])) + ", "
output_string = output_string[:-2] + "\n"

output_file.write(output_string)
output_file.close()
