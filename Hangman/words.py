import string
import random

def load_words():

	word_list=["happy","hangman","smile","wonderful","love",
	"light","education","school","mountain","beautiful",
	"above","below","after","super","excellent","please",
	"fight","right","today","attend","contain","facebook","youtube","sunday"
	,"student"


	]
	return word_list


def choose_word():

	word_list=load_words()
	secret_word=random.choice(word_list)
	secret_word=secret_word.lower()
	return secret_word
