Gaudet, Vernon
# Assignment 8: Level 6: PsychoPy - Response collection and saving data
## PsychoPy keypress exercises
	1. Complete.
	2. If you put event.ClearEvents within the trial loop instead of outside the trial loop, the keypress events will be cleared for every frame or every core clock tick effectively erasing any user input. If you unindent the "if keys" line then there is no check for keypresses during a trial. This causes count not to increase which result in no updates to "resp_time" or "sub_resp" in the case of core timer mode. In frame timer mode, frames will pass and "if keys" will be called before "keys" is defined resulting in a name error. 

## Psychtoolbox keypress exercises
	1. Incomplete. Can't find referenced lines.
	2. Incomplete.
	3. Incomplete.
## Recording data exercises	
	1. Complete.
	2. Complete.
## Save csv exercises
	1. Complete.
## Save JSON exercises
	1. Complete.
## Read JSON exercises
	1. Complete.
	2. Complete.
	3. Complete.
