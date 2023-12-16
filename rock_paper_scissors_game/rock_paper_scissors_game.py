# create a dictonary for store the image
dict={
  "Rock":"🤛",
  "Paper":"📄",
  "Scissor":"✂️"
}
import random
list=["Rock","Paper","Scissor"]
play_again=0
match_count=0
tie_match_count=0
#create a dictionary for total numers of player win
MatchDict={
  "You_Win":0,
  "Second_User_Win":0
}
while(play_again!="No"):
  my_choice=input("Choose any one of Rock,Paper,Scissor:")
  if( play_again!="No"):
     print("My Move: ",my_choice,dict[my_choice],)
     match_count+=1 
  num=random.randint(0,2)
  second_value=list[num]
  if(play_again!="No"):
     print("Second User Move: ",second_value,dict[second_value])
     print("...........   Result is   ..............")
  if (my_choice==second_value):
    print("Matich is Tie")
    tie_match_count+=1
    print("\n")
    play_again=input("You want to Play Again Yes or No:")
  elif(my_choice=="Rock"):
     if(second_value=="Paper"):
          print("You Lose: ",dict[my_choice])
          # print("second User Win: ",dict[second_value])
          MatchDict["Second_User_Win"]+=1
          print("\n")
          play_again=input("You want to Play Again Yes or No:")
     elif(second_value=="Scissor"):
          print("You win: ",dict[my_choice])
          # print("second User Loose: ",dict[second_value])
          MatchDict["You_Win"]+=1
          print("\n")
          play_again=input("You want to Play Again Yes or No:")
  elif(my_choice=="Paper"): 
    if(second_value=="Rock"):
          print("You Win: ",dict[my_choice])
          # print("second User Loose: ",dict[second_value])
          MatchDict["You_Win"]+=1
          play_again=input("You want to Play Again Yes or No:")
          print("\n")
    elif(second_value=="Scissor"):
          print("You Lose: ",dict[my_choice])
          # print("second User Win: ",dict[second_value])
          MatchDict["Second_User_Win"]+=1
          print("\n")
          play_again=input("You want to Play Again Yes or No:") 
  elif(my_choice=="Scissor"):
    if(second_value=="Paper"):
          print("You Win: ",dict[my_choice])
          # print("second User Loose: ",dict[second_value])
          MatchDict["You_Win"]+=1
          print("\n")
          play_again=input("You want to Play Again Yes or No:")
    elif(second_value=="Rock"):
          print("You Lose: ",dict[my_choice])
          # print("second User Win: ",dict[second_value])
          MatchDict["Second_User_Win"]+=1
          print("\n")
          play_again=input("You want to Play Again Yes or No:")
print("\n")
print("Total Number of Matches: ",match_count)
print("Number of Tie Matches: ",tie_match_count)
print("You Win:",MatchDict["You_Win"],"matches")
print("Second User Win: ",MatchDict["Second_User_Win"],"matches")
print("\n")
if (MatchDict["You_Win"]>MatchDict["Second_User_Win"]):
  print("Congratulation You Win The Game")
elif(MatchDict["You_Win"]==MatchDict["Second_User_Win"]):
  print("Game is tie")
else:
  print("You Lost The Game")
  