import random

board=[0,1,45,
	   3,4,5,
	   6,7,8]


def game():
	print(board[0],'|',board[1], '|',board[2],)
	print('----------')
	print(  board[3], '|',board[4], '|',board[5],)
	print('----------')
	print( board[6], '|',board[7], '|',board[8], )


while True:

 userinput=int(input("Select a place"))

 if board[userinput] != "x" and board[userinput] !="o":
 	board[userinput] ="x"

 	finding=True
 	while finding:

	 	random.seed()
	 	computer=random.randint(0,8)

	 	if board[computer] != "o" and board[computer] !="x":
	 		board[computer] ="o"
	 		finding= False

 else:
 	print("selected place is taken")
 game()
