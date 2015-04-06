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

Design & Implementation 
========================

An action selector goes through the actions and chooses an appropriate action 
based on various methods. The simplest method is to choose an action based on
keywords and then filter them based on their validator function.

If an action selector selects multiple actions, it must be able to combine
the generated response by each action in a comprehensible manner.
