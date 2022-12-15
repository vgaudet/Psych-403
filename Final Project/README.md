README.md
Author: Gaudet, Vernon
403FIN_P_go_nogo.py

This program is a Go/No-go task. Participants will be presented with colored tiles: blue, yellow and green. Tiles are preceded by a fixation cross. Participants will be instructed to respond to  yellow and blue tiles but to withold responding to green. The majority of trials will present yellow tiles (3/4 chance). This is to habituate responding. Blue and green tile presentations are meant to evoke incorrect responses inferring failure to inhibit responses (1/8 chance each). This is a common experiment paradigm that tests a participant's inhibition and/or decision making capacity. Participants will be prompted for information then shown instructions, then the trials will begin.

Stimuli: blue, yellow and green tiles are meant to be presented for 1 second after 0.5 second red fixation cross. Participant: Participant is meant to press SPACEBAR to respond to specific stimuli as fast as possible. Participants are meant to press SPACEBAR when presented with blue or yellow tiles. Participants are meant to withold(inhibit) response(SPACEBAR) when presented with green tiles. 

Countdown timers are used to present stimuli and other elements due to dropped frames on my system.

The following are recorded for each trial: block number(int), in-block trial number(int), stimulus color(str), color code(int)*, correct response(int)**, subject response(int)***, subject accuracy(int)**** and subject response time(float).

All recorded elements including subject responses are recorded into lists indexed over entire total trial span. Lists are then stored within a dictionary then saved as JSON and CSV files after experiment course is complete. Files are saved to a folder named 'data' in the working directory. If such a folder does not exist, it will be created. Files are saved in the following format: SUBJECTNUMBER-AGE+HANDEDNESS+DATE.CSV or SUBJECTNUMBER-AGE+HANDEDNESS+DATE.JSON.

* correct response is coded as: 0 = No response, 1 = Response(SPACEBAR).
** color codes: 0 = green, 1 = blue, 2 = yellow.
*** subject response is coded as: 0 = No response/SPACEBAR not pressed, 1 = SPACEBAR pressed.
**** subject accuracy is coded as: 0 = Incorrect, 1 = Correct
