=======
Actions
=======

Design and implementation
============================

Independent units of actions that an agent can make. Similar to the execution
part of an i/e/o architecture. Represented by conrete action classes.

The core of an action is a function call, 'action function'

The action function takes input such as:
    - conversation context
    - last message 
    - agent personality models 

Actions should be restricted to subsets of the input space. Therefore, there
should be restrictions on when the action function can be called. This is 
limited by validator functions
    - Validator functions should be inherited and instantiated separately
      to be reused. An example of a common validator is a function that does
      a membership check on the text input for a set of valid words.
    - Validators may be chained. In other words, designn should support the 
      addition of multiple validators to a single action definition.
    - There should be a standard for what the requirements are in the comments
      of the the action class.

Actions are meant to be indexed and accessed by an "Action Selector". 
Therefore, actions are should have keywords and category tags.
The main question that has to be asked is "What is used to select an action
from its peers?" This means how can an action selector pick an appropriate 
action. Pattern matching may not be enough in more complex cases where there
are multiple actions that share naive forms of categorization such as keywords.
An ideal action selector would choose an action after understanding its 
outcome. For example, Context and cognitive understanding is crucial for more
advanced forms of behaviour. A very simple case is double negatives. Such a 
situation requries linguistic comprehension of the underlying grammar of the 
sentence to figure out the meaning. Naive pattern matching might yield a
failure to match or fail to figure out the cancellation of double negatives.

The general expectation for an action is to return some kind of response 
as a form of feedback. The message may make the assumption that it is the only
action being executed.


=================
Action Selector
=================

The reasoning system that uses the information processed by the 'interpreter' 
and stored in the 'working memory' modules to select the appropriate action(s).

Design & Implementation 
========================

An action selector goes through the actions and chooses an appropriate action 
based on various methods. The simplest method is to choose an action based on
keywords and then filter them based on their validator function.

If an action selector selects multiple actions, it must be able to combine
the generated response by each action in a comprehensible manner.


Reasearch
=========

Situation Calculas and Event Calculas are both logic formalisms that are used
to model dynamic situations. They can be used to formally represent interactions
between an AI and its environment. Because of its purity, its applications may
be limited in more dynamic environments. There is also a wide gap between the 
theory and actual implmenetation. There is a big difference between the logical
paradigm that such formalisms lend themselves to and the imperative paradigm
actually being used for this project.

Examples of Actions
====================
Input: What is the time?
Desired action: Return the time

Input: What is the color of the sky?
Desired action: Return blue.

Input: Tell me a lie.
Desired action: Circle is a square

Input: Play this song.
Desired action: Open the specified song if in database, othwerise, notify 
user song is not available.

Input: Send me to Reddit.
Desired action: Forward the user to www.reddit.com

Input: Thank you.
Desired action: Understand what user is thanking for, and outputting 
"you're welcome".

Thoughts:
  - Procedurally generate the action definitions.
  - System for confirming that the action is correct.
  - Part of a knowledge base should be common nouns and their ascii pictures.


