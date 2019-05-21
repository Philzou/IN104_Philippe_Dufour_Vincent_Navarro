

import random
from minimax_time import minimax_alphabeta


class Node:
    def __init__(self, children = None, value = None):
        self.children = children or []
        self.value = value


    def evaluate(self):
        assert self.value is not None, 'This node has no value'
        return self.value
            
    def get_children(self):
        return self.children
        
    
    def tostring(self, l):
        if len(self.children)>0:
            string = '' 
            for child in self.children:
                string += ('\n' + '  '*l +'|-- ' + child.tostring(l+1))
        else:
            string = str(self.value)
        return string
    
    def __str__(self):
        return self.tostring(0)


def get_random_tree(maximize = True, max_depth = 5):
    ''' Construit un arbre dont le resultat de minimax est connu (selon si la racine est un noeud maximisant ou pas).
        Retourne le noeud racine de l'arbre et le score correspondant '''
    score = random.randint(-10,10) # on fixe le score qu'aura le noeud racine
    
    def make_children(parent, parent_score, maximize, max_depth, children_min=0, children_max= 4):
        ''' instancie recursivement des noeuds enfants, de telle manière que le parent ait le score indiqué '''
        # on tire au sort le nombre d'enfants qu'aura parent, sauf si max_dpth est a 0 auquel cas on ne creera aucun enfant
        n = random.randrange(children_min,children_max) if max_depth>0 else 0
        if n>0:  
            children = []
            index_of_child_with_parent_score = random.randrange(n) # on choisit quel sera l'enfant qui transmettra son score a son parent
            for k in range(n):
                # on crée n enfants
                child = Node()
                if k==index_of_child_with_parent_score:
                    child_score = parent_score
                elif maximize:
                    child_score = random.randint(-10, parent_score) 
                else:
                    child_score = random.randint(parent_score, 10)
                children.append(child)
                make_children(child, child_score, not maximize, max_depth-1) # auxquels on crée des noeuds enfants recursivement
            parent.children = children                
        else: 
            # si parent ne doit avoir aucun enfant, alors c'est une feuille de l'arbre et il faut lui attribuer une valeur
            parent.value = parent_score
        
    root = Node() # création de la racine
    make_children(root, score, maximize, max_depth, 3,5) # on impose à la racine d'avoir un minimum d'enfants
    
    return root, score

#---------------------------------
def get_test_tree1():
    '''Arbre dont le score est 10 lorsquue la racine est maximisant
    Issu de la vidéo https://www.youtube.com/watch?v=J1GoI5WHBto&t=13m11s'''
    n1 = Node(value = 10)
    n2 = Node(value = 11)
    n3 = Node(value = 9)
    n4 = Node(value = 12)
    n5 = Node(value = 14)
    n6 = Node(value = 15)
    n7 = Node(value = 13)
    n8 = Node(value = 14)
    n9 = Node(value = 5)
    n10= Node(value = 2)
    n11 = Node(value = 4)
    n12 = Node(value = 1)
    n13 = Node(value = 3)
    n14 = Node(value = 22)
    n15 = Node(value = 20)
    n16 = Node(value = 21)

    n21 = Node(children = [n1,n2])
    n22 = Node(children = [n3,n4])
    n23 = Node(children = [n5,n6])
    n24 = Node(children = [n7,n8])
    n25 = Node(children = [n9,n10])
    n26 = Node(children = [n11,n12])
    n27 = Node(children = [n13,n14])
    n28 = Node(children = [n15,n16])

    n31 = Node(children = [n21,n22])
    n32 = Node(children = [n23,n24])
    n33 = Node(children = [n25,n26])
    n34 = Node(children = [n27,n28])

    n41 = Node(children = [n31,n32])
    n42 = Node(children = [n33,n34])

    root = Node(children = [n41,n42])
    return root


def test(root, solution, maximize):
    ''' Test si minimax appliqué à root renvoie bien la solution '''
    result = minimax_alphabeta(root, 10, maximize = maximize)
    if not result==solution:
        print(str.format("Error lors du test (maximize = {:b}) sur l'arbre : ", maximize))
        print(root)
        print('minimax returned : ', result)
        print('but the solution was : ', solution)
        raise Exception()
        
        
if __name__=='__main__':
    test(get_test_tree1(), 10, maximize = True)
    K = 10
    for k in range(K):
        maximize = k%2==0
        root, truth = get_random_tree(maximize = maximize, max_depth = random.randint(4,6))
        test(root, truth, maximize=maximize)
    
    print(str(K+1)+" tests passed succesfully")

