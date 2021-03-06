import numpy as np
import matplotlib.pyplot as plt

#filename = input("Please type the path to the filename you want to read: ")
filename = "../data/convergence_energy.txt"
energy = []
cutoff = []

with open(filename) as infile:
    infile.readline()
    lines = infile.readlines()
    for i,line in enumerate(lines):
        words = line.split()
        energy.append(float(words[-2]))
        cutoff.append(float(words[-1][:-7]))

energy = np.array(energy)
cutoff = np.array(cutoff)

energy = energy/26 #TOTEN per atom

plt.plot(cutoff,energy,"b-")
plt.plot(cutoff,energy,"bo")
plt.title("Convergence of energy by energy cutoff")
plt.xlabel("Cutoff Energy [eV]")
plt.ylabel("Total Energy per atom [eV/atom]")
plt.grid()
plt.tight_layout()
plt.savefig("../fig/convergence_energy.png")
plt.show()

energy_difference = abs(np.diff(energy))

plt.plot(cutoff[:-1],energy_difference,"b-")
plt.plot(cutoff[:-1],energy_difference,"bo")
plt.title("Convergence of energy by energy cutoff - difference")
plt.xlabel("Cutoff Energy [eV]")
plt.ylabel("Absolute Total Energy Difference per atom [eV/atom]")
plt.grid()
plt.tight_layout()
plt.savefig("../fig/convergence_energy_difference.png")
plt.show()
