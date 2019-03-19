# Gurps Door Assistant
The Gurps Door Assistant consists of two tools. One for generating random doors within the parameters specified and the other is for managing those doors in play.

## Door Generator
This tool allows you specify several parameters and then generate as many unique doors as you wish with the requirements you input. The parameters that can currently be used are: Maximum Technology Level, whether or not extra heavy and vault doors are allowed, whether or not extra heavy and vault level security is allowed, and whether or not doors can have locks. You input how many unique doors you want and then the program generates them using some weighted random decision making. The output gives the doors stats, the security mechanisms stats if applicable, and the locks stats if applicable. A string of these values separated by commas is also printed. This string can be copied directly to the Door Manager tool or saved into your GM notes for later use. It is used to import the doors stats into the Door Manager.

## Door Manager
This program takes a comma separated string from the Door Generator program and allows the user to perform actions on it. These currently include both cutting and crushing attacks against the door, forcing the lock with the forced entry skill, and picking the lock. Critical success and failure rolls are possible. All damage is calculated automatically based on the stats input by the user. Success rolls are calculated in a similar fashion. The doors current HP and DR are tracked throughout the encounter. When the door has been successfully bypassed by any of the available methods, the program prints the results and exits.

## Todo List
* Allow locked doors to also be barred or wedged shut in addition to the latch/bolt
* Add knots in as a security feature and tamper-evident device
* Add the possibility of trapped doors
* Generate a detailed random description of the door
* Create a matching key for each lock with a random description
* Add portcullis type doorways
