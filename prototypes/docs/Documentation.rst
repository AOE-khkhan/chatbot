Documentation 

Classes List

	Conversation 
	Chatbot
	User
	Profile
	PersonalityModel
	EmotionModel
	User
	Parser
	Interpreter
	ActionSelector
	ResponseGenerator
	WorkingMemory (conversation context)
	ChatbotManager
	Reasoning System


Parser:

	Returns a parsed string.

Interpreter:
	
	Object that interprets inputs and updates the state of its arguments


ActionSelector Class:

	Wrapper for Response Generator 

	But also a manager for actions accomplished including logging the action history.

ResponseGenerator
	
	Object that generates text based on the information

WorkingMemory (ConverstaionContext)

	Represnts the working memory during conversation. 
	
	Information that acts as input to the ActionSelector

	Should have a default set of attributes that form the basis of a mental
	model of a conversation. Unfortunately, no such information could be found
	in official literature. Therefore, the program will have to use a novel
	set of attributes with much room for improvement.

	Short term memory that keeps track of information related to the immediate
	conversation. Dynamic states such as the topic of conversation should 
	be represented as lists, with the most recent conversation being the last
	one.

	Named entities
	Topics of conversation
	User information


PersonalityModel

	A dimensional structure to model human emotion.
	The interface allows for operations on the axes that reprsent human emotion.

Profile
	"""
		Digital representation of an individual

		Emotion model is mutable whereas the personality model and the profile attributes aren't
	""""

	Age
	gender

	** future
		race
		religion
		family
		political views
		property
		hobbies
		interests

** Sources:
	Google Search: Basic Personal Information
	Popular Demographics 
	Socialogical cateogrization
	Forms of Discrimination 


Chatbot

	Personality Model
	Profile
	Initial Emotional model
	Role

Reasoning System:
	Infers implicit information such as logical entailments and extracting
	goals.  


Resources:

Dialogics - talkworks.wikidot.com
 
