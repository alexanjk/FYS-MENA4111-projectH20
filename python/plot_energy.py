import numpy as np
import matplotlib.pyplot as plt

#filename = input("Please type the path to the filename you want to read: ")
filename = "../data/energy-convergence.txt"
energy = []
job = []

with open(filename) as infile:
    infile.readline()
    lines = infile.readlines()
    for i,line in enumerate(lines):
        words = line.split()
        energy.append(float(words[-2]))
        job.append(float(words[-1][:-7]))

energy = np.array(energy)
job = np.array(job)

energy = energy/26
print(energy)

plt.plot(job,energy)
plt.plot(job,energy,"bo")
plt.title("Energy vs. Cutoff Energy")
plt.xlabel("Cutoff Energy [eV?]")
plt.ylabel("Energy per atom [eV]")
plt.grid()
#plt.legend()
plt.show()
