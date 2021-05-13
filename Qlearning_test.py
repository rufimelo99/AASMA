import numpy as np
import numpy.random as rand
rand.seed(42)


#interest pointsd in City
X=["A","B","C","D"] #States
A=["goA","goB","goC","goD"]#Actions

epochs = 0

P_A = np.array([[1,   0,     0,   0], 
                [1,   0,     0,   0], 
                [1,   0,     0,   0],
                [1,   0,     0,   0]])
P_B = np.array([[0,   1,     0,   0], 
                [0,   1,     0,   0], 
                [0,   1,     0,   0],
                [0,   1,     0,   0]])
P_C = np.array([[0,   0,     1,   0], 
                [0,   0,     1,   0], 
                [0,   0,     1,   0],
                [0,   0,     1,   0]])
P_D = np.array([[0,   0,     0,   1], 
                [0,   0,     0,   1], 
                [0,   0,     0,   1],
                [0,   0,     0,   1]])
P=[]
P.append(P_A)
P.append(P_B)
P.append(P_C)
P.append(P_D)
C = np.array([  [0.1,   0.2,     0.4,   0.3], 
                [0.2,   0.1,     0.7,   0.3], 
                [0.4,   0.7,     0.1,   0.4],
                [0.3,   0.3,     0.4,   0.1]])

d=0.1
# States
print('Number of states:', len(X))

# Random state
s = rand.randint(len(X))
print('Random state:', X[s])

# Actions
print('Number of actions:', len(A))

# Random action
a = rand.randint(len(A))
print('Random action:', A[a])

# Transition probabilities
print('Transition probabilities for the selected state/action:')
print(P[a][s, :])

# Cost
print('Cost for the selected state/action:')
print(C[s, a])

# Discount
print('Discount:', d)


def egreedy(state_Qopt,eps):
    a = rnd.randint(state_Qopt.shape[0])
    rand=np.random.random(1)[0]
    choices=[0,1]
    choice=np.random.choice(choices,1,p=[eps,1-eps])
    if choice==0:#pode estar errado
        return a
    else:
        min_value=np.min(state_Qopt)
        mult_occur=0
        count=0
        indice=[]

        for value in state_Qopt:#find argmin and if there is mult_occurences
            if value==min_value:
                mult_occur+=1
                indice.append(count)
            if mult_occur>1:
                indice.append(count) 
            count+=1

        if mult_occur==1:
            a=indice[0]
            return a
        if mult_occur>1:
            a=np.random.choice(indice, 1)
            return a[0]


def qlearning(X, A, P, C, d, n, qinit):
    q=qinit
    alpha=0.3
    gamma=0.9
    i=0


    currentState = rand.randint(len(X))
    while i<n:
        #action = egreedy(Qopt[currentState, :], eps=0.15) ??????
        action = rand.randint(len(A))
        
        nextState = action
        
        cnew= C[currentState, action]
        #should work as reward and not cost.. we could have something like a difference between the "Fuel" and "Time" wasted

        old_value=q[currentState][action]
        next_max=np.max(q[nextState])

        q[currentState][action]=(1-alpha)*old_value+alpha*(cnew+gamma*next_max)

        currentState = nextState
        i=i+1

    return q



# Initialize Q-function
qinit = np.zeros((len(A), len(A)))

qnew = qlearning(X, A, P, C, d, 100000, qinit)
print(qnew)
