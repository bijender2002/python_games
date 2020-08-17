#     #    encript decript game

# def encrypt():
#   message = input("Enter the message you want to encrypt: ")
#   print()
#   ascii_message = [ord(char)+2 for char in message]
#   encrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(encrypt_message))
#   print()


# def decrypt():
#   	message = input("Enter the message you want to decrypt: ")
#   	print()
#   	ascii_message = [ord(char)-2 for char in message]
#   	decrypt_message = [ chr(char) for char in ascii_message]  
#   	print (''.join(decrypt_message))
#   	print()

# while True:
# 	choice = input("What do you want to do?\n \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively! ")
# 	if choice == 'e':
# 		encrypt()
# 	elif choice =='d':
#   		decrypt()    
# 	else:
# 		play_again = input("Do you want to try agian or Do you want to exit? (y/n): ")
# 		if play_again == 'y':
# 			continue
# 		else:
# 			break