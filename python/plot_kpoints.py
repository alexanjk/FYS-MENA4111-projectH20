import numpy as np
import matplotlib.pyplot as plt

#filename = input("Please type the path to the filename you want to read: ")
filename = "../data/convergence_kpoints.txt"
energy = []
kpoint = []

with open(filename) as infile:
    infile.readline()
    lines = infile.readlines()
    for i,line in enumerate(lines):
        words = line.split()
        energy.append(float(words[-2]))
        kpoint.append(float(words[-1][:-7]))

energy = np.array(energy)
kpoint = np.array(kpoint)

energy = energy/26 #TOTEN per atom

plt.plot(kpoint,energy,"b-")
plt.plot(kpoint,energy,"bo")
plt.title("Convergence of energy by kpoints")
plt.xlabel("Kpoint density [a.u.]")
plt.ylabel("Total Energy per atom [eV/atom]")
plt.grid()
plt.tight_layout()
plt.savefig("../fig/convergence_kpoints.png")
plt.show()

energy_difference = abs(np.diff(energy))

plt.plot(kpoint[:-1],energy_difference,"b-")
plt.plot(kpoint[:-1],energy_difference,"bo")
plt.title("Convergence of energy by kpoints - difference")
plt.xlabel("Kpoint density [a.u.]")
plt.ylabel("Absolute Total Energy Difference per atom [eV/atom]")
plt.grid()
plt.tight_layout()
plt.savefig("../fig/vaspout_convergence_kpoints_difference.png")
plt.show()
