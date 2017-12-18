import matplotlib.pyplot as pp

myfile = open("output.txt", 'r')

taudata =  [i.strip() for i in myfile.readlines()]
print taudata
taudata = [i.split(", ") for i in taudata]

charges = sorted([float(taudata[i][1]) / 1.47e6 for i in xrange(len(taudata))])
tau = sorted([float(taudata[i][-1]) / 83374725.0 for i in xrange(len(taudata))])

pp.plot(charges, tau, 'r-')
pp.axis([-0.1,1.1, .9, 1.5])
pp.title("Proper time for Radial Plunge onto Charged Black Hole")
pp.xlabel("Q/M")
pp.ylabel("Proper Time to Hit Singularity; units of Schwartzschild Prediction")
pp.savefig("Schwartzschild_Comparison.png")
pp.show()
