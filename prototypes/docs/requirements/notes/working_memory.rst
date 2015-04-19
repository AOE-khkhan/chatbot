Working Memory
==============

The 'working memory' stage is an intermediate point in the 'Action pipeline'. 
Its purpose is to hold the interpreted raw input as native information such as
objects of a program's knowledge base. As an example, if an interpreter recieves
a textual input with the word 'dog', then the interpreter might store this 
information as a frame defined as an object from the program's knowldge base
module. 

Design & Implementation 
========================

The basic operations of this class are to get and set the common variables
to be shared between the 'Action class' and the 'Interpreter class'. 

There is a degree of dependence between the other two classes in the pipeline
and this one. If the 'workng memory' has no mechanism for storing an information
that the interpreter thinks is neccesary, then that information cannot be stored
and used by the action class. Alternatively, if the 'working memory' has a 
mechanism that is not supported by the 'action class' it will not be able to 
fully use that information. In other words, the modules have a high level of
cohesion and should also be loosely coupled. Especially since the success of
the program can be evaluated using a real function rather than a binary function
meaning that there is room for non-optimal performance of the program. To 
further support a decoupled design there should be a common core structure that
children of the other two classes ('action' and 'interpreter') can rely on. 

At the absolute minimum, the working memory class should support:
    * recent input (percept):
        * named entities: 
        * subject: 
        * verbs
    * interlocutor
    * goal
    * action_history
    * percept history


* lack of semantic relation information
* dependency on working memory
* confidence interval

