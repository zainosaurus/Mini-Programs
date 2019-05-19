'''  Engineering Economics

	Created by Zain Tahlilkar on Mar. 4/2017

	Formulas for second year course 'Engineering Economics' at McMaster University

(F/P,i,N): Compound Amount Factor
(P/F,i,N): Present Worth Factor
(A/F,i,N): Sinking Fund Factor
(F/A,i,N): Uniform Series Compound Amount Factor
(A/P,i,N,S): Capital Recovery Factor w/ Salvage Value
(P/A,i,N): Series Present Worth Factor
(A/G,i,N): Arithmetic Gradient to Annuity Conversion
(P/A,g,i,N): Geometric Gradient to Present Worth Conversion
i0: Growth Adjusted Interest Rate
'''

# Compound Amount Factor
def F_P(i,N):
	return float((1+i) ** N)

# Present Worth Factor
def P_F(i,N):
	return float(1.0 / F_P(i,N))

#Sinking Fund Factor
def A_F(i,N):
	return float(i / ((1+i)**N - 1))

# Uniform Series Present Worth Factor
def F_A(i,N):
	return float(1.0/A_F(i,N))

# Capital Recovery Factor with SAlvage Value
def A_P(i,N,S):
	return  float(i*(1+i)**N/((1+i)**N-1) + S*A_F(i,N))

#Series Present Worth Factor
def P_A(i,N):
	return float(1.0/A_P(i,N,0))

# Arithmetic Grad to Annuity
def A_G(i,N):
	return float(1.0/i - N/((i+1)**N -1))

# Growth Adjusted Interest Rate
def i0(i,g):
	return  float((1.0+i)/(1+g) - 1)

# Geometric Gradient Series to Present Worth
def P_A_g(g,i,N):
	I = i0(i,g)
	return  float(P_A(I,N)/(1+g))

def pr():
	print "(F/P,i,N): Compound Amount Factor"
	print "(P/F,i,N): Present Worth Factor"
	print "(A/F,i,N): Sinking Fund Factor"
	print "(F/A,i,N): Uniform Series Compound Amount Factor"
	print "(A/P,i,N,S): Capital Recovery Factor w/ Salvage Value"
	print "(P/A,i,N): Series Present Worth Factor"
	print "(A/G,i,N): Arithmetic Gradient to Annuity Conversion"
	print "(P/A,g,i,N): Geometric Gradient to Present Worth Conversion"
	print "i0: Growth Adjusted Interest Rate"

