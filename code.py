import networkx as nx
from collections import OrderedDict
import matplotlib.pyplot as plt

#Approach - Work In Progress
#Though the following code is work in progress below is my thought process on how to wanted to solve the problem.
# build a DiGraph when ever you see a DEPEND command - this allows me to query in_ and out_ edges so that i know
# which component is depends on others.
# OPTION 1 
#  build a custom graph solution? which can add nodes and extact out_ and in_ edges ?
# OPTION 2
#  use networkx library - i used the library bevause the solution has to be robust and scalable, and need to build in short time.


file1 = open('input.txt', 'r') 
G = nx.DiGraph()
componentsInstalled = []

while True: 
    line = file1.readline()   
    if not line: 
        break
    text = line.split();         
    command = text[0];
    if command == "END":
        print(line);
    elif command == "DEPEND":
        #create a dependency graph
        #use networkx library for it's scalability and robustness
        #add edge as in when we see a line starts with DEPEND <1> <2> <3>
        #<1> depends on both <2> and <3> , hence we will have two edges from (1,2) and (1,3)
        print(line,end='');
        i = 2
        while i < len(text):
            G.add_edge(text[1],text[i])
            i = i+1
    elif command == "INSTALL":
        #install should check the following cases
        #check if there are any out_edges for a given component
        #out_edge == 0 means we can install the component and there is no dependency needed
        #if out_edge has some edges, <2> <3> from the above case 
        #we need to check <2> and <3> are also installed - install them if there' not installed
        #keep a track of installed components in a separate list 'componentsInstalled'
        #check if the key exists, if not append it to the list 

        #TODO: there is still some pending cases which i need to take care of.
        
        print(line,end='')
        if text[1] in componentsInstalled:
            print("\t" + text[1] + " is already installed.")            
        else:
             dependencies = G.out_edges(text[1])
             if not dependencies: # if there are no out_edges means, no dependencies
               componentsInstalled.append(text[1])
             elif text[1] in componentsInstalled:
                  print("\t" + text[1] + " is already installed.")  
             else:
                 componentsInstalled.append(text[1]) 
               
    elif command == "REMOVE":
        #Remove primarily removes a components from the list
        #we need to check if there are any dependencies , before removing an element from the list
        #remove only when there are no dependencies

        #TODO: handled minimal cases , need to query the dependency graph before removing an element from the list
        
        print(line,end='')
        if text[1] in componentsInstalled:
            componentsInstalled.remove(text[1])
        print("\t Remvoing " + text[1])    
    elif command == "LIST":
        #list is pretty straight forward
        #we need to list all the elements in the componentsInstalled
        #simple and easy
        print(line,end='')
        for x in componentsInstalled:
            print("\t" + x)
     
     #Finally close the file 
     #thanks for the opportunity given, this is a really intersting problem.
file1.close() 
