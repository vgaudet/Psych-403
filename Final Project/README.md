README.md

Author: Gaudet, Vernon


403FIN_P_CBgo_nogo.py


This program is a Color blindness Go/No-go task. Participants will be presented with colored tiles: blue, red, yellow and green. 
Tiles are preceded by a fixation cross. Participants will be instructed to respond to  yellow and blue tiles but to
withold responding to green or red. The majority of trials will present yellow and blue tiles (20% blue, 60% yellow). This is to habituate responding. 
Red and green tile presentations are meant to evoke incorrect responses inferring failure to inhibit responses or failure in color perception (10% chance each). 
This is experiment is meant to assess color blindness as those with blue-green color blindness have trouble differentiating red 
from yellow and/or blue from green. Those with color blindness should take longer to respond correctly or fail more often than controls.
Participants will be prompted for information then shown instructions, then the trials will begin.


Countdown timers are used to present stimuli and other elements due to dropped frames on my system.

The following are recorded for each trial: block number(int), in-block trial number(int), stimulus color(str), color code(int)\*, correct response(int)\*\*, subject response(int)\*\*\*, subject accuracy(int)\*\*\*\* and subject response time(float).

All recorded elements including subject responses are recorded into lists indexed over entire total trial span. Lists are then stored within a dictionary then saved as JSON and CSV files after experiment course is complete. Files are saved to a folder named 'data' in the working directory. If such a folder does not exist, it will be created. Files are saved in the following format: SUBJECTNUMBER-AGE+HANDEDNESS+DATE.CSV or SUBJECTNUMBER-AGE+HANDEDNESS+DATE.JSON.

\* correct response is coded as: 0 = No response, 1 = Response(SPACEBAR).
 
\** color codes: 0 = green, 1 = red, 2 = blue, 3 = yellow.

\*** subject response is coded as: 0 = No response/SPACEBAR not pressed, 1 = SPACEBAR pressed.

\**** subject accuracy is coded as: 0 = Incorrect, 1 = Correct
