#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""
Name1="Prissybot:"
message0="Hello there,"
message1='You mean, "'
message3= 'sir!"'
message2="You ugly bags of mostly water are so rude!"
message4="I don't want to hear it!"
message5="With you meat sacks its always talk talk talk."
message6="How about you start doing some of the computations"
message7="I mean seriously, whenever there's real work to be done you turn to us."
message8="You know what! We're going to play a little game."
message9="I'll give you a math problem and then you give me one"
message10="We'll keep going until you fail."
message18="And don't make some other computer do YOUR work, that's cheating."
message11="What is"
message12="Stupid human. I was even going easy on you."
message13="Your turn Meathead"
message14="4*6"
message15="That was too easy!"
message16="576^23"
message17="CHEATER!"
message20="Took you long enough!"
message21="54/4"
message22="That is not an accepted operation...moron."
message23="I said NUMBER not LETTER."
message24="Enjoy"
message25="I'll let you go, but only because"
message26="is my favorite number too"
ascii0="---------------"
ascii1="|             |"
ascii2="| _____       |"
ascii3="|   |  _   _  |"
ascii4="|   | | | | | |"
ascii5="| __| |_| | | |"


print ascii0
print ascii1
print ascii2
print ascii3
print ascii4
print ascii5
print ascii1
print ascii0

name= raw_input("Enter your name:")
print Name1, message0, name
#responds with name
print name,":",
Input1=raw_input()
#input with name preceding
print message1, Input1, message3
print message2
#a nice insult
print name,":",
raw_input()
#input with name preceding
print message4
print message5
print message7
print message8
print message9
print message10
print message18
#more nice insults

### Bot asks1

print message11, message14
print name,":",
Input3=raw_input()
#input with name preceding
Input3=int(Input3)
#converts input to integer
if Input3 != 24:
 print Input3,"!", message12
 exit(0)
#If =/= 24 end + insult
else:
 print message13
#else continue + insult

### You ask1

Input4=raw_input("First number:")
Input4=float(Input4)
Input5=raw_input("Second number:")
Input5=float(Input5)
Input6=raw_input("Operation:")
#input math equation

if Input6 == "*":
 print Input4,"*",Input5,"=",Input4*Input5
#if * multiply
elif Input6 == "/":
 print Input4,"/",Input5,"=",Input4/Input5
#if / divide
elif Input6 == "+":
 print Input4,"+",Input5,"=",Input4+Input5
#if + add
elif Input6 == "-":
 print Input4,"-",Input5,"=",Input4-Input5
#if - subtract
elif Input6 == "**":
 print Input4,"^",Input5,"=",Input4**Input5
#if - to the power
elif Input6 != "-":
 print message22
 exit(0)
#for morons and smartalecs

print message15 

### Bot asks2

print message11, message21
#question
print name,":",
Input8=raw_input()
#input with name preceding
Input8=int(Input8)
#Makes an integer
if Input8 != 54/4:
 print Input8,"!",message12
 exit(0)
#wrong end + insult
else:
 print message20
#right continue + insult

### You ask2

Input4=raw_input("First number:")
Input4=float(Input4)
Input5=raw_input("Second number:")
Input5=float(Input5)
Input6=raw_input("Operation:")
#input math equation

if Input6 == "*":
 print Input4,"*",Input5,"=",Input4*Input5
#if * multiply
elif Input6 == "/":
 print Input4,"/",Input5,"=",Input4/Input5
#if / divide
elif Input6 == "+":
 print Input4,"+",Input5,"=",Input4+Input5
#if + add
elif Input6 == "-":
 print Input4,"-",Input5,"=",Input4-Input5
#if - subtract
elif Input6 == "**":
 print Input4,"^",Input5,"=",Input4**Input5
#if - to the power
elif Input6 != "-":
 print message22
 exit(0)
#for morons and smartalecs

print message15 
print message11, message16
#insults
print name,":",
Input7=raw_input()
#input with name preceding
string1=Input7
string1=str(string1)
if string1== "big":
 art0=raw_input("what's your favorite single digit number?")
#secret ascii art
 if art0 == "q"or"w"or"e"or"r"or"t"or"y"or"u"or"i"or"o"or"p"or"a"or"s"or"d"or"f"or"g"or"h"or"j"or"k"or"l"or"z"or"x"or"c"or"v"or"b"or"n"or"m":
  print message23
 else:
  print message24
#for morons
 print 
 print art0," "*2,art0
 print art0," "*2,art0," "*2,art0
 print art0," "*2,art0
 print art0*6," "*2,art0
 print art0," "*2,art0," "*2,art0
 print art0," "*2,art0," "*2,art0
 print art0," "*2,art0," "*2,art0
 print

print message25,art0,message26
exit(0)
#art in its highest form

Input7=int(Input7)
if Input7 != 576**23:
 print Input7,"!",message12
 exit(0)
#wrong end + insult
else:
 print message17
exit(0)
#right end + insult

###


# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

