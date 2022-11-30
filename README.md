# AbacoStack-Game
game instruction in readme.txt



![image](https://user-images.githubusercontent.com/70949118/161392424-561ba01f-abcc-477a-ae59-9685327807ea.png)


You have a structure formed by three side by side stacks that are limited in size. For this game we will limit our stacks to three elements each. For the explanation we will initially limit ourselves to three stacks with a depth of three. You can see above in the picture a physical example with 4 stacks of depth 3.

Back to our explanation, above these three stacks, you have a list of five positions from 0 to 4. The first stack is aligned with position 1; stack 2 with position 2, and stack 3 with position 3. Positions 0 and 4 don't have a stack aligned with them.

See this figure below to have a better idea about how this structure looks.  
<pre>
0 1 2 3 4  
. . . . .  
  . . .  
  . . .  
  . . .  
<\pre>
The structure is filled with nine beads: 3 As, 3 Bs and 3 Cs, representing 3 colours. Initially the structure looks like this with the 3 stacks each filled with either all As, Bs, or Cs.  
<pre>
0 1 2 3 4  
. . . . .  
  A B C  
  A B C  
  A B C  
<\pre>
The structure always has 9 beads. The beads can move one position at a time to an empty position. An empty position is represented by a "." here.
For example from the initial configuration, one can pop a bead from the first stack and switch it with the top bead in the second stack in the follow series of moves:  
<pre>
0 1 2 3 4  
. . . . .  
  A B C   
  A B C  
  A B C  

0 1 2 3 4  
. A . . .  
  . B C  
  A B C  
  A B C  

0 1 2 3 4  
A . . . .  
  . B C  
  A B C 
  A B C

0 1 2 3 4
A . B . .
  . . C 
  A B C 
  A B C

0 1 2 3 4
A B . . .
  . . C 
  A B C 
  A B C
 

0 1 2 3 4
A . . . .
  B . C 
  A B C 
  A B C


0 1 2 3 4
. A . . .
  B . C 
  A B C 
  A B C

0 1 2 3 4
. . A . .
  B . C 
  A B C 
  A B C

0 1 2 3 4
. . . . .
  B A C 
  A B C 
  A B C
<\pre>  
The game consists of getting a random configuration card and doing the minimum numbers of moves to change the beads of the AbacoStack to that given configuration.

For example, you get the following card:

 |A A C|
 |B C A|
 |C B B|
You need to move the beads one by one to get

from                to
0 1 2 3 4        0 1 2 3 4
. . . . .        . . . . .
  A B C            A A C
  A B C            B C A
  A B C            C B B
The game is played by a user, not the computer. The computer would generate a random configuration card and the user would have to solve the game by indicating the moves to do in order to change the configuration from the initial one to the one indicated on the card.

The moves are indicated by the following input pair ij where i is a digit and j a character like the following:
1u means stack 1 upward move
1d means stack 1 downward move
2u means stack 2 upward move
2d means stack 2 downward move
3u means stack 3 upward move
3d means stack 3 downward move
0r means position 0 right move
1r and 1l mean position 1 right move and left move respectively
2r and 2l mean position 2 right move and left move respectively
3r and 3l mean position 3 right move and left move respectively
4l means position 4 left move
