==========================
Requirements Documentation
==========================

Chatbot Prototype
=================

**Goal**
    Create a dialogue system that simulates conversation with users. The purpose
    of this program is to act as the back end of a UI. Therefore, it must 
    encorporate elements from a given domain knowledge into its response and 
    actions. As implied, in addition to outputting textual messages as part of a 
    conversation, it must also be able to select appropriate actions and 
    execute them. The decision making process and message outputs should be 
    realistic and paralel their real-life counterparts. Part of this includes
    simulating the individualism and pscyhology of a person.


Design Notes
============

**The decision making process will be stochastic in nature.** Given the goal 
of high fidelity, the implementation should use probablistic algorithms that
will make testing and validation more challenging. 

**There are multiple possible emotional models.** The following are just a list
of the potential dimensional models to represent an individual's personality.

* `Five Factor Model <http://en.wikipedia.org/wiki/Big_five_personality_traits>`_ 
* `HEXACO Model <http://en.wikipedia.org/wiki/HEXACO_model_of_personality_structurek>`_ 
* `Various personality models <http://en.wikipedia.org/wiki/Personality_psychology#Personality_theories>`_ 

  
Use Cases
=========

1. The user asks the chatbot for its name
2. The chatbot responds with its name

1. The user insults the chatbot
2. The chatbot possibly gets upset and refuses to answer future questions.



