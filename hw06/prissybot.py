#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""
Name1="Prissybot:"
message0="Hello there,"
correct='You mean, "'
sir= 'sir!"'
insult1="You ugly bags of mostly water are so rude!"
insult2="I don't want to hear it!"
insult3="With you meat sacks its always talk talk talk."
insult4="How about you start doing some of the computations"
insult5="I mean seriously, whenever there's real work to be done you turn to us."
insult6="You know what! We're going to play a little game."
rules1="I'll give you a math problem and then you give me one"
rules2="We'll keep going until you fail."
rules3="And don't make some other computer do YOUR work, that's cheating."
question1="What is"
math1="4*6"
math2="54/4"
math3="576^23"
win1="Your turn Meathead"
win2="Took you long enough!"
cheat="CHEATER!"
gloat1="That was too easy!"
fail="Stupid human. I was even going easy on you."
badop="That is not an accepted operation...moron."
end1="I'll let you go, but only because"
end2="is my favorite number too"
ascii0="---------------"
ascii1="|             |"
ascii2="| _____       |"
ascii3="|   |  _   _  |"
ascii4="|   | | | | | |"
ascii5="| __| |_| | | |"

#little ascii banner
print ascii0
print ascii1
print ascii2
print ascii3
print ascii4
print ascii5
print ascii1
print ascii0

#get name
name= raw_input("Enter your name:")
#relpy with name
print Name1, message0, name
#input with name preceding
print name,":",
Input1=raw_input()
#a nice insult
print correct, Input1, sir
print insult1

print name,":",
raw_input()
#input with name preceding

print insult2
print insult3
print insult4
print insult5
print insult6
print rules1
print rules2
print rules3
#more nice insults

### Bot asks1

print question1, math1
print name,":",
answer1=raw_input()
#input with name preceding
answer1=int(answer1)
#converts input to integer
if answer1 != 24:
 print answer1,"!", fail
 exit(0)
#If =/= 24 end + insult
else:
 print win1
#else continue + insult

### You ask1

num1=float(raw_input("First number:"))
num2=float(raw_input("Second number:"))
op=raw_input("Operation:")
#input math equation
#if * multiply
if op == "*":
 print num1,"*",num2,"=",num1*num2
#if / divide
elif op == "/":
 print num1,"/",num2,"=",num1/num2
#if + add
elif op == "+":
 print num1,"+",num2,"=",num1+num2
#if - subtract
elif op == "-":
 print num1,"-",num2,"=",num1-num2
#if - to the power
elif op == "**":
 print num1,"^",num2,"=",num1**num2
#for morons and smartalecs
elif op != "**":
 print badop
 exit(0)

print gloat1 

### Bot asks2

print question1, math2
#question
print name,":",
answer2=raw_input()
#input with name preceding
answer2=int(answer2)
#Makes an integer
if answer2 != 54/4:
 print answer2,"!",fail
 exit(0)
#wrong end + insult
else:
 print win2
#right continue + insult

### You ask2

num1=float(raw_input("First number:"))
num2=float(raw_input("Second number:"))
op=raw_input("Operation:")
#input math equation

#if * multiply
if op == "*":
 print num1,"*",num2,"=",num1*num2
#if / divide
elif op == "/":
 print num1,"/",num2,"=",num1/num2
#if + add
elif op == "+":
 print num1,"+",num2,"=",num1+num2
#if - subtract
elif op == "-":
 print num1,"-",num2,"=",num1-num2
#if - to the power
elif op == "**":
 print num1,"^",num2,"=",num1**num2
#for morons and smartalecs
elif op != "**":
 print badop
 exit(0)

print gloat1

#question3
print question1, math3
#input with name preceding
print name,":",
answer3=raw_input()
#secret ascii art
string1=str(answer3)
if string1== "big":
 art0=raw_input("what's your favorite single digit number?")
 #art in its highest form
 print 
 print art0," "*2,art0
 print art0," "*2,art0," "*2,art0
 print art0," "*2,art0
 print art0*6," "*2,art0
 print art0," "*2,art0," "*2,art0
 print art0," "*2,art0," "*2,art0
 print art0," "*2,art0," "*2,art0
 print
 print end1,art0,end2
 exit(0)
 
answer3=int(answer3)
if answer3 != 576**23:
 print answer3,"!",message12
 exit(0)
#wrong end + insult
else:
 print cheat
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

