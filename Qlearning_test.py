import numpy as np
import numpy.random as rand
rand.seed(42)


#interest pointsd in City
X=["A","B","C","D"] #States
A=[0,1,2,3]#Actions
#A=["goA","goB","goC","goD"]#Actions

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
        #should work as reward and not cost.. 
        #we will use something related with time, like 1/t

        old_value=q[currentState][action]
        next_max=np.max(q[nextState])

        q[currentState][action]=(1-alpha)*old_value+alpha*(cnew+gamma*next_max)

        currentState = nextState
        i=i+1

    return q



# Initialize Q-function
qinit = np.zeros((len(A), len(A)))

qnew = qlearning(X, A, P, C, d, 10000, qinit)
print(qnew)

#for each iteration of the learning process
#maybe after reach certain number of epochs its policy becomes greedy
#-> instead of np.choice, we would hvae it searching for themaximum
def qlearningIteration(X, A, P, C, d, qinit, currentState, time):
    q=qinit
    alpha=0.3
    gamma=0.9

    #linalg.norm() nao funcionou..TODO
    total =qnew[currentState][0]+qnew[currentState][1]+qnew[currentState][2]+qnew[currentState][3]
    
    action = np.random.choice(A, 1, p=qnew[currentState]/total)
    print(action)
    
    nextState = action[0]
    
    cnew= 1/time

    old_value=q[currentState][action]
    next_max=np.max(q[nextState])

    q[currentState][action]=(1-alpha)*old_value+alpha*(cnew+gamma*next_max)

    currentState = nextState

    return q


qnew = qlearningIteration(X, A, P, C, d, qinit, 0, 3)
print(qnew)