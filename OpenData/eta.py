'''EXERCISE:

Question 1)We can see the effect of the pseudorapidity to the mearsuremtet resolution 
looking to the number of events and the shape of the histogram. Events with high 
pseudorapidity might interact with other matter than hit the barrel causing inaccuracy 
to the measurement. Thus the probability of events with the same measurement are more
distributed around the mean value. However, with low pseudorapidity the particles that
hit the detector can be measured more accurately. This makes the histogram look thinner
because more events with the same value can be measured.


Question 2)The results show the mean value around 91,2 Gev and the analysis of how pseudorapidity
affects the measurements are according to the theory.

Question 3)We can see in the picture 'etas.pdf' that when we decrease the range of pseudorapidity 
that is out of analysis, i.e. increasing cond2(small etas) and decreasing cond1(large etas), 
the number of events grow rapidly. If we look into each histogram, it's clear that the orange shape
(small etas) looks more and more like the blue one (high etas) as the range of eta gets bigger. It 
gets thiner following the reason explained in question 1.

'''
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit


dataset = pd.read_csv('Zmumu_Run2011A_masses.csv')
#print('The amount of all events = %d' % len(dataset))
#print (dataset.head())
plt.figure()
i=1
cond1=1.67
cond2=0.30
while i <=4 :
	
	large_etas = dataset[(np.absolute(dataset.eta1) > cond1) & (np.absolute(dataset.eta2) > cond1)]
	small_etas = dataset[(np.absolute(dataset.eta1) < cond2) & (np.absolute(dataset.eta2) < cond2)]

	#print('\n' *2)

	
	#print('The amount of events where the pseudorapidity of both muons has been large = %d' %len(large_etas))
	#print('The amount of events where the pseudorapidity of both muons has been small = %d' %len(small_etas))
	plt.subplot(2, 2, i)
	invariant_mass = small_etas['M']
	axes = plt.gca()
	axes.set_ylim([0,200])
	if i>=3:
		plt.xlabel('Invariant mass [GeV]')
	if i%2 != 0:
		plt.ylabel('Number of events per bin')
	if i==1:
		plt.title('Histograms of invariant masses')
	plt.hist(invariant_mass, bins=120, range=(60,120),alpha=0.9, label='Low Eta <%.2f'%cond2)

	invariant_mass = large_etas['M']
	plt.hist(invariant_mass, bins=120, range=(60,120),alpha=0.7, label='High Eta >%.2f'%cond1)

	plt.legend (loc='upper right')
	cond1=cond1-0.15
	cond2=cond2+0.15
	i+=1

plt.savefig('etas.pdf')# figure with 4 histograms with diferent intervals of etas
#plt.show()

plt.figure()
invariant_mass = dataset['M']
bin_heights, bin_borders, _ = plt.hist(invariant_mass, bins=500, range=(60,120))

bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2



#Question 4)
def BW(E,M,T,a,b,A):
	# T is the decay width, A is the height of Breit-Weigner, a is the slope and b is the linear coefficient.
	
	g=np.sqrt(M**2*(M**2+T**2))
	K=(2*M*T*g*np.sqrt(2))/(np.pi*np.sqrt(M**2+g))
	return a*E+b+A*K/((E**2-M**2)**2+(T*M)**2)

popt,pcov=curve_fit(BW, bin_centers, bin_heights,p0=[85.,2.,0.,0.,1000])

plt.plot(bin_centers,BW(bin_centers, *popt), label='fit')
plt.ylabel('Number of events per bin')
plt.title('Histogram of invariant masses')
plt.xlabel('Invariant mass [GeV]')
#print(popt) printind the paramters of the fit
#print(pcov) printing the matrix of covariance

plt.savefig('fit.pdf')
#plt.show()


#Question 5)
T,unc_T =popt[1],pcov[1][1]  #decay width and its variance (matrix's of covariance diagonal)
h=6.58211928e-25   # reduced Planck's constant in Gev*s
t=h/T   #lifetime
unc_t=np.sqrt((h/T**2)**2*unc_T*2)  #lifetime's uncertainty 
print('The lifetime of the Z boson is (%g +- %g)s '%(t,unc_t))


#The lifetime of the Z boson is (1.6135e-25 +- 2.70962e-27)s 