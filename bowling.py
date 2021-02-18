########################
### CODE CHALLENGE #####
########################

# Requirements:
# Create a program in your choice of language that can calculate the score of a full round of bowling, based on user inputs and the following rules:



# Strike

# If you knock down all 10 pins in the first shot of a frame, you get a strike.
# How to score: A strike earns 10 points plus the sum of your next two shots.



# Spare

# If you knock down all 10 pins using both shots of a frame, you get a spare.
# How to score: A spare earns 10 points plus the sum of your next one-shot.



# Open Frame

# If you do not knock down all 10 pins using both shots of your frame (9 or fewer pins knocked down), you have an open frame.
# How to score: An open frame only earns the current of pins knocked down.



# The 10th Frame

# If you roll a strike in the first shot of the 10th frame, you get 2 more shots.
# If you roll a spare in the first two shots of the 10th frame, you get 1 more shot.
# If you leave the 10th frame open after two shots, the game is over and you do not get an additional shot.

# How to Score: The score for the 10th frame is the total current of pins knocked down in the 10th frame.

class Scoreboard:
    """
    Contains methods to calculate the final score.
    """
    def __init__(self, frames, shots, score):
        self.frames = frames
        self.shots = shots
        self.score = score

    # Method for testing outcomes in unittest
    def throw(self, pins):
        self.shots.append(pins)

    # Check if strike
    def is_strike(self, shot_index):
        return self.shots[shot_index] == 10
    
    # Check if spare
    def is_spare(self, shot_index):
        return self.shots[shot_index] + self.shots[shot_index + 1] == 10

    # Get score
    def get_final_score(self):
        shot_index = 0

        # Extract shots from frames
        for frame in self.frames:
            for shot in frame.shots:
                self.shots.append(shot)
        
        # Iterate through shots, calculating spares and strikes accordingly
        for i in range(10):
            if self.is_strike(shot_index):
                self.score += 10 + self.shots[shot_index + 1] + self.shots[shot_index + 2]
                shot_index += 1
            elif self.is_spare(shot_index):
                self.score += 10 + self.shots[shot_index + 2]
                shot_index += 2
            else:
                self.score += self.shots[shot_index] + self.shots[shot_index + 1]
                shot_index += 2

        return self.score
    
    def __repr__(self):  
        return "Frames:% s Total Score:% s" % (self.frames, self.score) 


class Frame:
    """
    Class to keep track of each frame.
    """
    def __init__(self, shots):
        self.shots = shots

    def __repr__(self):  
        return "Frame:% s" % (self.shots) 



######################
######## Run #########
######################

# Variables
scoreboard = Scoreboard(frames = [], shots = [], score = 0)
frame = Frame(shots = [])

# Iterator that prompts user to input each individual score
while len(scoreboard.frames) < 9:
    try:
        # Input for pins, only accepts integers
        pins = int(input('Enter the number of pins hit for shot {} '.format(len(frame.shots) + 1) + 'of frame {} '.format(len(scoreboard.frames) + 1)))

        # Make a throw
        if not 0 <= pins <= 10:
            print('Please enter an amount between 0 and 10.')
        else:
            if len(frame.shots) == 0:
                if pins == 10:
                    frame.shots.append(pins)
                    scoreboard.frames.append(frame)
                    frame = Frame(shots = [])
                    print(scoreboard.frames)
                    
                else:
                    frame.shots.append(pins)

            else:
                if frame.shots[0] + pins <= 10:
                    frame.shots.append(pins)
                else:
                    print('Too many pins entered on second shot, please try again.')
        

        # Add frame to scoreboard
        if len(frame.shots) == 2:
            scoreboard.frames.append(frame)
            frame = Frame(shots = [])
            print(scoreboard.frames)



    except ValueError:
        print('Please enter a valid number.')

else:
    i = 0
    while i < 4:
        pins = int(input('Enter the number of pins hit for shot {} '.format(len(frame.shots) + 1) + 'of frame {} '.format(len(scoreboard.frames) + 1)))

        # Make a throw
        if not 0 <= pins <= 10:
            print('Please enter an amount between 0 and 10.')

        else:
            frame.shots.append(pins)
            print(scoreboard.frames)
            i = i + 1
            if len(frame.shots) == 2:
                if frame.shots[0] + frame.shots[1] >= 10:
                    i = i + 1
                else:
                    i = i + 2

    else:
        scoreboard.frames.append(frame)  
        print("Your final score: ", scoreboard.get_final_score())
