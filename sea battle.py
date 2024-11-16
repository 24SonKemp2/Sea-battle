import turtle , random, time 
turtle.speed(9)
t = time.localtime(time.time())
localtime = time.asctime(t)
s =  time.asctime(t)
s.split()
a = str(s[11])
b = str(s[12])
hour = a + b
hour = int(hour)
turtle.hideturtle()
turtle.speed(9)
hodpl = []
name = input("Введите свое имя ")
if hour > 6 and hour <= 9 :
  turtle.bgcolor('#6d7aff')
elif hour > 9 and hour <= 12:
  turtle.bgcolor('#6da0ff')
elif hour > 12 and hour <= 15:
  turtle.bgcolor('#6dc6ff')
elif hour > 15 and hour <= 18:
  turtle.bgcolor('#1a808f')
elif hour > 18 and hour <= 21:
  turtle.bgcolor('#6da0ff')
elif hour > 21 and hour <= 0:
  turtle.bgcolor('#19408a')
elif hour > 0 and hour <= 3:
  turtle.bgcolor('#05108a')
elif hour > 3 and hour <= 6:
  turtle.bgcolor('#0f0057')
def tosdp ():
  turtle.penup()
  turtle.right(90)
  turtle.forward(7 )
  turtle.left(90) 
  turtle.pendown()
def tosdp2 ():
  turtle.penup()
  turtle.right(90)
  turtle.forward(10)
  turtle.left(90) 
  turtle.fd(25)
  turtle.pendown()
def frs():
  tosdp2()
  turtle.pensize(2)
  turtle.fd(80)
  turtle.left(45)
  turtle.fd(17)
  turtle.left(137.2)
  turtle.fd(116)
  turtle.left(135)
  turtle.fd(11)
  turtle.left(42)
  turtle.fd(15)
  turtle.penup()
  turtle.back(15)
  turtle.right(42)
  turtle.bk(15)
  turtle.pendown()
  turtle.right(225)
  turtle.penup()
  turtle.fd(8)
  turtle.left(270)
  turtle.fd(10)
  turtle.pendown()
  turtle.fd(40)
  turtle.right(90)
  turtle.fd(10)
  turtle.penup()
  turtle.bk(10)
  turtle.left(90)
  turtle.bk(40)
  turtle.right(90)
  turtle.pendown()
  turtle.fd(10)
  turtle.right(270)
  turtle.penup()
  turtle.fd(60)
  turtle.right(273)
  turtle.pendown()
  turtle.fd(3)
  turtle.left(90)
  turtle.fd(8)
  turtle.right(90)
  turtle.fd(3)
  turtle.right(30)
  turtle.fd(6)
  turtle.right(60)
  turtle.fd(13)
  turtle.right(40)
  turtle.fd(6)
  turtle.right(50)
  turtle.fd(3)
  turtle.left(270)
  turtle.fd(3)
  turtle.right(270)
  turtle.fd(3)
  turtle.penup()
  turtle.bk(3)
  turtle.left(90)
  turtle.bk(3)
  turtle.right(270)
  turtle.fd(3)
  turtle.left(40)
  turtle.fd(1)
  turtle.right(120)
  turtle.fd(4)
  turtle.pendown()
  turtle.fd(10)
  for i in range (72):
    turtle.fd(0.1)
    turtle.right(5)
  turtle.penup()
  for i in range(36):
    turtle.fd(0.1)
    turtle.right(5)
  turtle.pendown()
  turtle.fd(7)
bp = 0
pp = 0
korkorp = []
def trs():
  turtle.pensize(2)
  tosdp()
  turtle.pencolor("black")
  turtle.left(90)
  for i in range(18):
    turtle.forward(0.5)
    turtle.right(360/72)
  turtle.fd(68)
  for i in range(18):
    turtle.forward(0.5)
    turtle.right(360/72)
  turtle.right(90)
  turtle.fd(79)
  turtle.pencolor("black")
  turtle.right(90)
  turtle.penup()
  for i in range(18):
    turtle.forward(0.5)
    turtle.right(360/72)
  turtle.fd(51)
  turtle.pendown()
  turtle.left(90)
  turtle.fd(7)
  turtle.left(90)
  turtle.fd(11)
  turtle.left(12.75)
  turtle.fd(15)
  turtle.left(77.25)
  turtle.fd(3)
def sh():
  turtle.pencolor("black")
  tosdp()
  turtle.pensize(2)
  turtle.hideturtle()
  turtle.forward(4)
  turtle.back(8)
  turtle.forward(12)
  turtle.left(45)
  turtle.forward(11.2)
  turtle.left(135)
  turtle.forward(28)
  turtle.left(135)
  turtle.forward(11.2)
  turtle.back(11.2)
  turtle.left(135)
  turtle.forward(6)
  turtle.right(90)
  turtle.forward(14)
  turtle.right(90)
  turtle.forward(6)
  turtle.back(6)
  turtle.right(90)
  turtle.forward(5)
  turtle.seth(90)
  turtle.forward(7)
  for i in range(3):
    turtle.left(90)
    turtle.forward(4)
def udh ():
  turtle.pencolor("black")
  tosdp()
  turtle.pensize(2)
  turtle.forward(32)
  turtle.left(58.95)
  turtle.fd(17-1.5)
  turtle.left(180-51.10)
  turtle.fd(38)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(16)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(28)
  turtle.left(180-57.55)
  turtle.fd(8)
  turtle.seth(90)
  turtle.fd(6)
def ddh ():
  turtle.pencolor("black")
  tosdp()
  turtle.pensize(2)
  turtle.forward(32)
  turtle.left(58.95)
  turtle.fd(17-1.5)
  turtle.left(180-51.10)
  turtle.fd(38)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(16)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(28)
  turtle.left(180-57.55)
  turtle.fd(8)
  turtle.seth(270)
  turtle.fd(6)
  
def ldh ():
  turtle.pencolor("black")
  tosdp()
  turtle.pensize(2)
  turtle.forward(32)
  turtle.left(58.95)
  turtle.fd(17-1.5)
  turtle.left(180-51.10)
  turtle.fd(38)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(16)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(28)
  turtle.left(180-57.55)
  turtle.fd(8)
  turtle.seth(180)
  turtle.fd(6)
  
def rdh ():
  turtle.pencolor("black")
  tosdp()
  turtle.pensize(2)
  turtle.forward(32)
  turtle.left(58.95)
  turtle.fd(17-1.5)
  turtle.left(180-51.10)
  turtle.fd(38)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(16)
  turtle.right(95.3)
  turtle.fd(6)
  turtle.right(84.7)
  turtle.fd(28)
  turtle.left(180-57.55)
  turtle.fd(8)
  turtle.seth(180)
  turtle.fd(6)
  

def whitex ():
  
  turtle.pensize(3)
  turtle.color("white")
  turtle.seth(315)
  turtle.forward(10)
  turtle.back(20)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(10)
  turtle.back(20)
  turtle.forward(10)

def redx():
  turtle.pensize(3)
  turtle.color("red")
  turtle.seth(315)
  turtle.forward(10)
  turtle.back(20)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(10)
  turtle.back(20)
  turtle.forward(10)
if hour > 0 and hour < 4:
  turtle.bgcolor('#090067')
elif hour > 5 and hour < 12:
  turtle.bgcolor('#6ac5ff')
elif hour > 13 and hour < 17:
  turtle.bgcolor('#4f56a3')
else:
  turtle.bgcolor('#464c90')
neispkl = [11,12,13,14,15,16,17,18
,19,110,21,22,23,24,25,26,27,28,29,210,31,32,33,34,35,36,37,38,39,310,41,42,43,44,45,46,47,48,49,410,51,52,53,54,55,56,57,58,59,510,61,62,63,64,65,66,67,68,69,610,71,72,73,74,75,76,77,78,79,710,81,82,83,84,85,86,87,88,89,810,91,92,93,94,95,96,97,98,99,910,101,102,103,104,105,106,107,108,109,1010]
def make1 ():
  turtle.pensize(5)
  turtle.penup() 
  turtle.setpos(-340,-126)
  turtle.pendown()
  turtle.left(90)
  turtle.forward(340)
  turtle.right(90)
  turtle.forward(340)
  turtle.right(90)
  turtle.forward(340)
  turtle.right(90)
  turtle.forward(340)
  turtle.right(90)
  xcor = -340 
  for i in range (10):
    xcor = xcor + 34
    turtle.penup()
    turtle.setpos(xcor,-126)
    turtle.pendown()
    turtle.forward(340)
  ycor = -160
  turtle.right(90)
  for i in range(10):
    ycor = ycor + 34
    turtle.penup()
    turtle.setpos(-340,ycor)
    turtle.pendown()
    turtle.forward(340)
  turtle.left(90)
  turtle.pensize(5)
  turtle.penup()
  turtle.setpos(20,-126)
  turtle.pendown()
  turtle.right(90)
  turtle.forward(340)
  turtle.left(90)
  turtle.forward(340)
  turtle.left(90)
  turtle.forward(340)
  turtle.left(90)
  turtle.forward(340)
  turtle.right(180)
  xcor = 20
  for i in range (10):
    xcor = xcor + 34
    turtle.penup()
    turtle.setpos(xcor,-126)
    turtle.pendown()
    turtle.forward(340)
  ycor = -126
  turtle.right(90)
  for i in range(10):
    ycor = ycor + 34
    turtle.penup()
    turtle.setpos(20,ycor)
    turtle.pendown()
    turtle.forward(340)
  ycor = 191
  
  for i in range (1,11):
    turtle.penup()
    turtle.setpos(7,ycor)
    turtle.pendown()
    turtle.write(i)
    ycor = ycor - 34
  xcor = 37
  for i in range (1,11):
    turtle.penup()
    turtle.setpos(xcor,225)
    turtle.pendown()
    if i == 1:
      turtle.write("а")
    elif i == 2:
      turtle.write("б")
    elif i == 3:
      turtle.write("в")
    elif i == 4:
      turtle.write("г")
    elif i == 5:
      turtle.write("д")
    elif i == 6:
      turtle.write("е")
    elif i == 7:
      turtle.write("ж")
    elif i == 8:
      turtle.write("з")
    elif i == 9:
      turtle.write("и")
    elif i == 10:
      turtle.write("к")
    xcor = xcor + 34
  xcor = -323
  for i in range (1,11):
    turtle.penup()
    turtle.setpos(xcor,225)
    turtle.pendown()
    if i == 1:
      turtle.write("а")
    elif i == 2:
      turtle.write("б")
    elif i == 3:
      turtle.write("в")
    elif i == 4:
      turtle.write("г")
    elif i == 5:
      turtle.write("д")
    elif i == 6:
      turtle.write("е")
    elif i == 7:
      turtle.write("ж")
    elif i == 8:
      turtle.write("з")
    elif i == 9:
      turtle.write("и")
    elif i == 10:
      turtle.write("к")
    xcor = xcor + 34
make1()
turtle.pencolor("black")
turtle.speed(9)
def odk ():
  global defolt
  global y
  if defolt == "да":
    if y == 1:
      odf = "а1"
    elif y == 2:
      odf = "а3"
    elif y == 3:
      odf = "а5"
    else:
      odf = "а7"
  else:
    odf = input("Введите координаты для однопалубника")
  if odf == "a1":
    odf = 11
  elif odf == "a2":
    odf = 12
  elif odf == "a3":
    odf = 13
  elif odf == "a4":
    odf = 14
  elif odf == "a5":
    odf = 15
  elif odf == "a6":
    odf = 16
  elif odf == "a7":
    odf = 17
  elif odf == "a8":
    odf = 18
  elif odf == "a9":
    odf = 19
  elif odf == "a10":
    odf = 110
  elif odf == "b1":
    odf = 21
  elif odf == "b2":
    odf = 22
  elif odf == "b3":
    odf = 23
  elif odf == "b4":
    odf = 24
  elif odf == "b5":
    odf = 25
  elif odf == "b6":
    odf = 26
  elif odf == "b7":
    odf = 27
  elif odf == "b8":
    odf = 28
  elif odf == "b9":
    odf = 29
  elif odf == "b10":
    odf = 210
  elif odf == "c1":
    odf = 31
  elif odf == "c2":
    odf = 32
  elif odf == "c3":
    odf = 33
  elif odf == "c4":
    odf = 34
  elif odf == "c5":
    odf = 35
  elif odf == "c6":
    odf = 36
  elif odf == "c7":
    odf = 37
  elif odf == "c8":
    odf = 38
  elif odf == "c9":
    odf = 39
  elif odf == "c10":
    odf = 310
  elif odf == "d1":
    odf = 41
  elif odf == "d2":
    odf = 42
  elif odf == "d3":
    odf = 43
  elif odf == "d4":
    odf = 44
  elif odf == "d5":
    odf = 45
  elif odf == "d6":
    odf = 46
  elif odf == "d7":
    odf = 47
  elif odf == "d8":
    odf = 48
  elif odf == "d9":
    odf = 49
  elif odf == "d10":
    odf = 410
  elif odf == "e1":
    odf = 51
  elif odf == "e2":
    odf = 52
  elif odf == "eз":
    odf = 53
  elif odf == "e4":
    odf = 54
  elif odf == "e5":
    odf = 55
  elif odf == "e6":
    odf = 56
  elif odf == "e7":
    odf = 57
  elif odf == "e8":
    odf = 58
  elif odf == "e9":
    odf = 59
  elif odf == "e10":
    odf = 510 
  elif odf == "f1":
    odf = 61
  elif odf == "f2":
    odf = 62
  elif odf == "f3":
    odf = 63
  elif odf == "f4":
    odf = 64
  elif odf == "f5":
    odf = 65
  elif odf == "f6":
    odf = 66
  elif odf == "f7":
    odf = 67
  elif odf == "f8":
    odf = 68
  elif odf == "f9":
    odf = 69
  elif odf == "f10":
    odf = 610 
  elif odf == "g1":
    odf = 71
  elif odf == "g2":
    odf = 72
  elif odf == "g3":
    odf = 73
  elif odf == "g4":
    odf = 74
  elif odf == "g5":
    odf = 75
  elif odf == "g6":
    odf = 76
  elif odf == "g7":
    odf = 77
  elif odf == "g8":
    odf = 78
  elif odf == "g9":
    odf = 79
  elif odf == "g10":
    odf = 710 
  elif odf == "h1":
    odf = 81
  elif odf == "h2":
    odf = 82
  elif odf == "h3":
    odf = 83
  elif odf == "h4":
    odf = 84
  elif odf == "h5":
    odf = 85
  elif odf == "h6":
    odf = 86
  elif odf == "h7":
    odf = 87
  elif odf == "h8":
    odf = 88
  elif odf == "h9":
    odf = 89
  elif odf == "h10":
    odf = 810  
  elif odf == "i1":
    odf = 91
  elif odf == "i2":
    odf = 92
  elif odf == "i3":
    odf = 93
  elif odf == "i4":
    odf = 94
  elif odf == "i5":
    odf = 95
  elif odf == "i6":
    odf = 96
  elif odf == "i7":
    odf = 97
  elif odf == "i8":
    odf = 98
  elif odf == "i9":
    odf = 99
  elif odf == "i10":
    odf = 910
  elif odf == "j1":
    odf = 101
  elif odf == "j2":
    odf = 102
  elif odf == "j3":
    odf = 103
  elif odf == "j4":
    odf = 104
  elif odf == "j5":
    odf = 105
  elif odf == "j6":
    odf = 106
  elif odf == "j7":
    odf = 107
  elif odf == "j8":
    odf = 108
  elif odf == "j9":
    odf = 109
  elif odf == "j10":
    odf = 1010
  #second line
  peensize = 2
  r = 4
  if odf == 12:
    turtle.penup()
    turtle.setpos(-323,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 22:
    turtle.penup()
    turtle.setpos(-289,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 32:
    turtle.penup()
    turtle.setpos(-255,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 42:
    turtle.penup()
    turtle.setpos(-221,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 52:
    turtle.penup()
    turtle.setpos(-187,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 62:
    turtle.penup()
    turtle.setpos(-153,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 72:
    turtle.penup()
    turtle.setpos(-119,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 82:
    turtle.penup()
    turtle.setpos(-85,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 92:
    turtle.penup()
    turtle.setpos(-51,157)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 102:
    turtle.penup()
    turtle.setpos(-17,157)
    turtle.pendown()
    turtle.pensize(peensize)
    
  #first line
  elif odf == 11:
    turtle.penup()
    turtle.setpos(-323,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 21:
    turtle.penup()
    turtle.setpos(-289,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 31:
    turtle.penup()
    turtle.setpos(-255,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 41:
    turtle.penup()
    turtle.setpos(-221,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 51:
    turtle.penup()
    turtle.setpos(-187,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 61:
    turtle.penup()
    turtle.setpos(-153,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 71:
    turtle.penup()
    turtle.setpos(-119,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 81:
    turtle.penup()
    turtle.setpos(-85,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 91:
    turtle.penup()
    turtle.setpos(-51,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 101:
    turtle.penup()
    turtle.setpos(-17,191)
    turtle.pendown()
    turtle.pensize(peensize)
    
  #third line
  elif odf == 13:
    turtle.penup()
    turtle.setpos(-323,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 23:
    turtle.penup()
    turtle.setpos(-289,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 33:
    turtle.penup()
    turtle.setpos(-255,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 43:
    turtle.penup()
    turtle.setpos(-221,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 53:
    turtle.penup()
    turtle.setpos(-187,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 63:
    turtle.penup()
    turtle.setpos(-153,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 73:
    turtle.penup()
    turtle.setpos(-119,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 83:
    turtle.penup()
    turtle.setpos(-85,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 93:
    turtle.penup()
    turtle.setpos(-51,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 103:
    turtle.penup()
    turtle.setpos(-17,123)
    turtle.pendown()
    turtle.pensize(peensize)
    
  #fourth line
  elif odf == 14:
    turtle.penup()
    turtle.setpos(-323,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 24:
    turtle.penup()
    turtle.setpos(-289,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 34:
    turtle.penup()
    turtle.setpos(-255,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 44:
    turtle.penup()
    turtle.setpos(-221,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 54:
    turtle.penup()
    turtle.setpos(-187,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 64:
    turtle.penup()
    turtle.setpos(-153,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 74:
    turtle.penup()
    turtle.setpos(-119,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 84:
    turtle.penup()
    turtle.setpos(-85,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 94:
    turtle.penup()
    turtle.setpos(-51,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 104:
    turtle.penup()
    turtle.setpos(-17,89)
    turtle.pendown()
    turtle.pensize(peensize)
    
  #fifth line
  elif odf == 15:
    turtle.penup()
    turtle.setpos(-323,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 25:
    turtle.penup()
    turtle.setpos(-289,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 35:
    turtle.penup()
    turtle.setpos(-255,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 45:
    turtle.penup()
    turtle.setpos(-221,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 55:
    turtle.penup()
    turtle.setpos(-187,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 65:
    turtle.penup()
    turtle.setpos(-153,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 75:
    turtle.penup()
    turtle.setpos(-119,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 85:
    turtle.penup()
    turtle.setpos(-85,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 95:
    turtle.penup()
    turtle.setpos(-51,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 105:
    turtle.penup()
    turtle.setpos(-17,54)
    turtle.pendown()
    turtle.pensize(peensize)
    
  #sixth line
  elif odf == 16:
    turtle.penup()
    turtle.setpos(-323,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 26:
    turtle.penup()
    turtle.setpos(-289,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 36:
    turtle.penup()
    turtle.setpos(-255,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 46:
    turtle.penup()
    turtle.setpos(-221,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 56:
    turtle.penup()
    turtle.setpos(-187,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 66:
    turtle.penup()
    turtle.setpos(-153,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 76:
    turtle.penup()
    turtle.setpos(-119,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 86:
    turtle.penup()
    turtle.setpos(-85,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 96:
    turtle.penup()
    turtle.setpos(-51,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 106:
    turtle.penup()
    turtle.setpos(-17,20)
    turtle.pendown()
    turtle.pensize(peensize)
    
  #seventh line
  elif odf == 17:
    turtle.penup()
    turtle.setpos(-323,-14)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 27:
    turtle.penup()
    turtle.setpos(-289,-14)
    turtle.pendown()
    turtle.pensize(peensize)
    
  elif odf == 37:
    turtle.penup()
    turtle.setpos(-255,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 47:
    turtle.penup()
    turtle.setpos(-221,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 57:
    turtle.penup()
    turtle.setpos(-187,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 67:
    turtle.penup()
    turtle.setpos(-153,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 77:
    turtle.penup()
    turtle.setpos(-119,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 87:
    turtle.penup()
    turtle.setpos(-85,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 97:
    turtle.penup()
    turtle.setpos(-51,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 107:
    turtle.penup()
    turtle.setpos(-17,-14)
    turtle.pendown()
    turtle.pensize(peensize)
  #eighth line
  elif odf == 18:
    turtle.penup()
    turtle.setpos(-323,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 28:
    turtle.penup()
    turtle.setpos(-289,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 38:
    turtle.penup()
    turtle.setpos(-255,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 48:
    turtle.penup()
    turtle.setpos(-221,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 58:
    turtle.penup()
    turtle.setpos(-187,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 68:
    turtle.penup()
    turtle.setpos(-153,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 78:
    turtle.penup()
    turtle.setpos(-119,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 88:
    turtle.penup()
    turtle.setpos(-85,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 98:
    turtle.penup()
    turtle.setpos(-51,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 108:
    turtle.penup()
    turtle.setpos(-17,-48)
    turtle.pendown()
    turtle.pensize(peensize)
  #nineth line
  elif odf == 19:
    turtle.penup()
    turtle.setpos(-323,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 29:
    turtle.penup()
    turtle.setpos(-289,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 39:
    turtle.penup()
    turtle.setpos(-255,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 49:
    turtle.penup()
    turtle.setpos(-221,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 59:
    turtle.penup()
    turtle.setpos(-187,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 69:
    turtle.penup()
    turtle.setpos(-153,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 79:
    turtle.penup()
    turtle.setpos(-119,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 89:
    turtle.penup()
    turtle.setpos(-85,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 99:
    turtle.penup()
    turtle.setpos(-51,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 109:
    turtle.penup()
    turtle.setpos(-17,-85)
    turtle.pendown()
    turtle.pensize(peensize)
  #tenth line
  elif odf == 110:
    turtle.penup()
    turtle.setpos(-323,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 210:
    turtle.penup()
    turtle.setpos(-289,-120)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 310:
    turtle.penup()
    turtle.setpos(-255,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 410:
    turtle.penup()
    turtle.setpos(-221,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 510:
    turtle.penup()
    turtle.setpos(-187,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 610:
    turtle.penup()
    turtle.setpos(-153,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 710:
    turtle.penup()
    turtle.setpos(-119,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 810:
    turtle.penup()
    turtle.setpos(-85,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 910:
    turtle.penup()
    turtle.setpos(-51,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  elif odf == 1010:
    turtle.penup()
    turtle.setpos(-17,-120)
    turtle.pendown()
    turtle.pensize(peensize)
  korkorp.append(odf)
  sh()
  

def twk():
  oy = 196
  ty = 162
  thy = 128
  fy = 94
  fiy = 60
  sy =  26
  sey = -8
  ey = -42
  ny = -76
  tey = -110
  global defolt
  global y
  if defolt == "да":
    if y == 1:
      odf = "c1"
    elif y == 2:
      odf = "c4"
    elif y == 3:
      odf = "c7"
  else:
    odf = input("Введите координаты для двухпалубника")
  if odf == "a1":
    odf = 11
  elif odf == "a2":
    odf = 12
  elif odf == "a3":
    odf = 13
  elif odf == "a4":
    odf = 14
  elif odf == "a5":
    odf = 15
  elif odf == "a6":
    odf = 16
  elif odf == "a7":
    odf = 17
  elif odf == "a8":
    odf = 18
  elif odf == "a9":
    odf = 19
  elif odf == "a10":
    odf = 110
  elif odf == "b1":
    odf = 21
  elif odf == "b2":
    odf = 22
  elif odf == "b3":
    odf = 23
  elif odf == "b4":
    odf = 24
  elif odf == "b5":
    odf = 25
  elif odf == "b6":
    odf = 26
  elif odf == "b7":
    odf = 27
  elif odf == "b8":
    odf = 28
  elif odf == "b9":
    odf = 29
  elif odf == "b10":
    odf = 210
  elif odf == "c1":
    odf = 31
  elif odf == "c2":
    odf = 32
  elif odf == "c3":
    odf = 33
  elif odf == "c4":
    odf = 34
  elif odf == "c5":
    odf = 35
  elif odf == "c6":
    odf = 36
  elif odf == "c7":
    odf = 37
  elif odf == "c8":
    odf = 38
  elif odf == "c9":
    odf = 39
  elif odf == "c10":
    odf = 310
  elif odf == "d1":
    odf = 41
  elif odf == "d2":
    odf = 42
  elif odf == "d3":
    odf = 43
  elif odf == "d4":
    odf = 44
  elif odf == "d5":
    odf = 45
  elif odf == "d6":
    odf = 46
  elif odf == "d7":
    odf = 47
  elif odf == "d8":
    odf = 48
  elif odf == "d9":
    odf = 49
  elif odf == "d10":
    odf = 410
  elif odf == "e1":
    odf = 51
  elif odf == "e2":
    odf = 52
  elif odf == "e3":
    odf = 53
  elif odf == "e4":
    odf = 54
  elif odf == "e5":
    odf = 55
  elif odf == "e6":
    odf = 56
  elif odf == "e7":
    odf = 57
  elif odf == "e8":
    odf = 58
  elif odf == "e9":
    odf = 59
  elif odf == "e10":
    odf = 510 
  elif odf == "f1":
    odf = 61
  elif odf == "f2":
    odf = 62
  elif odf == "f3":
    odf = 63
  elif odf == "f4":
    odf = 64
  elif odf == "f5":
    odf = 65
  elif odf == "f6":
    odf = 66
  elif odf == "f7":
    odf = 67
  elif odf == "f8":
    odf = 68
  elif odf == "f9":
    odf = 69
  elif odf == "f10":
    odf = 610 
  elif odf == "g1":
    odf = 71
  elif odf == "g2":
    odf = 72
  elif odf == "g3":
    odf = 73
  elif odf == "g4":
    odf = 74
  elif odf == "g5":
    odf = 75
  elif odf == "g6":
    odf = 76
  elif odf == "g7":
    odf = 77
  elif odf == "g8":
    odf = 78
  elif odf == "g9":
    odf = 79
  elif odf == "g10":
    odf = 710 
  elif odf == "h1":
    odf = 81
  elif odf == "h2":
    odf = 82
  elif odf == "h3":
    odf = 83
  elif odf == "h4":
    odf = 84
  elif odf == "h5":
    odf = 85
  elif odf == "h6":
    odf = 86
  elif odf == "h7":
    odf = 87
  elif odf == "h8":
    odf = 88
  elif odf == "h9":
    odf = 89
  elif odf == "h10":
    odf = 810  
  elif odf == "i1":
    odf = 91
  elif odf == "i2":
    odf = 92
  elif odf == "i3":
    odf = 93
  elif odf == "i4":
    odf = 94
  elif odf == "i5":
    odf = 95
  elif odf == "i6":
    odf = 96
  elif odf == "i7":
    odf = 97
  elif odf == "i8":
    odf = 98
  elif odf == "i9":
    odf = 99
  elif odf == "i10":
    odf = 910
  elif odf == "j1":
    odf = 101
  elif odf == "j2":
    odf = 102
  elif odf == "j3":
    odf = 103
  elif odf == "j4":
    odf = 104
  elif odf == "j5":
    odf = 105
  elif odf == "j6":
    odf = 106
  elif odf == "j7":
    odf = 107
  elif odf == "j8":
    odf = 108
  elif odf == "j9":
    odf = 109
  elif odf == "j10":
    odf = 1010
  left = [odf - 10]
  right = [odf + 10]
  up = [odf - 1]
  down = [odf + 1]
  if odf == 12:
    turtle.penup()
    turtle.setpos(-323,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 22:
    turtle.penup()
    turtle.setpos(-289,ty)
    turtle.pendown()
    turtle.pensize(15)
  
  elif odf == 32:
    turtle.penup()
    turtle.setpos(-255,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 42:
    turtle.penup()
    turtle.setpos(-221,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 52:
    turtle.penup()
    turtle.setpos(-187,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 62:
    turtle.penup()
    turtle.setpos(-153,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 72:
    turtle.penup()
    turtle.setpos(-119,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 82:
    turtle.penup()
    turtle.setpos(-85,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 92:
    turtle.penup()
    turtle.setpos(-51,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 102:
    turtle.penup()
    turtle.setpos(-17,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  #first line
  elif odf == 11:
    turtle.penup()
    turtle.setpos(-323,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 21:
    turtle.penup()
    turtle.setpos(-289,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 31:
    turtle.penup()
    turtle.setpos(-255,oy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 41:
    turtle.penup()
    turtle.setpos(-221,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 51:
    turtle.penup()
    turtle.setpos(-187,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 61:
    turtle.penup()
    turtle.setpos(-153,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 71:
    turtle.penup()
    turtle.setpos(-119,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 81:
    turtle.penup()
    turtle.setpos(-85,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 91:
    turtle.penup()
    turtle.setpos(-51,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 101:
    turtle.penup()
    turtle.setpos(-17,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  #third line
  elif odf == 13:
    turtle.penup()
    turtle.setpos(-323,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 23:
    turtle.penup()
    turtle.setpos(-289,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 33:
    turtle.penup()
    turtle.setpos(-255,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 43:
    turtle.penup()
    turtle.setpos(-221,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 53:
    turtle.penup()
    turtle.setpos(-187,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 63:
    turtle.penup()
    turtle.setpos(-153,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 73:
    turtle.penup()
    turtle.setpos(-119,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 83:
    turtle.penup()
    turtle.setpos(-85,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 93:
    turtle.penup()
    turtle.setpos(-51,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 103:
    turtle.penup()
    turtle.setpos(-17,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fourth line
  elif odf == 14:
    turtle.penup()
    turtle.setpos(-323,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 24:
    turtle.penup()
    turtle.setpos(-289,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 34:
    turtle.penup()
    turtle.setpos(-255, fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 44:
    turtle.penup()
    turtle.setpos(-221,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 54:
    turtle.penup()
    turtle.setpos(-187,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 64:
    turtle.penup()
    turtle.setpos(-153,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 74:
    turtle.penup()
    turtle.setpos(-119,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 84:
    turtle.penup()
    turtle.setpos(-85,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 94:
    turtle.penup()
    turtle.setpos(-51,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 104:
    turtle.penup()
    turtle.setpos(-17,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fifth line
  elif odf == 15:
    turtle.penup()
    turtle.setpos(-323,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 25:
    turtle.penup()
    turtle.setpos(-289,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 35:
    turtle.penup()
    turtle.setpos(-255,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 45:
    turtle.penup()
    turtle.setpos(-221,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 55:
    turtle.penup()
    turtle.setpos(-187,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 65:
    turtle.penup()
    turtle.setpos(-153,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 75:
    turtle.penup()
    turtle.setpos(-119,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 85:
    turtle.penup()
    turtle.setpos(-85,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 95:
    turtle.penup()
    turtle.setpos(-51,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 105:
    turtle.penup()
    turtle.setpos(-17,fiy)
    turtle.pendown()
    turtle.pensize(15)
  #sixth line
  elif odf == 16:
    turtle.penup()
    turtle.setpos(-323,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 26:
    turtle.penup()
    turtle.setpos(-289,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 36:
    turtle.penup()
    turtle.setpos(-255,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 46:
    turtle.penup()
    turtle.setpos(-221,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 56:
    turtle.penup()
    turtle.setpos(-187,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 66:
    turtle.penup()
    turtle.setpos(-153,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 76:
    turtle.penup()
    turtle.setpos(-119,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 86:
    turtle.penup()
    turtle.setpos(-85,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 96:
    turtle.penup()
    turtle.setpos(-51,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 106:
    turtle.penup()
    turtle.setpos(-17,sy)
    turtle.pendown()
    turtle.pensize(15)
  #seventh line
  elif odf == 17:
    turtle.penup()
    turtle.setpos(-323,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 27:
    turtle.penup()
    turtle.setpos(-289,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 37:
    turtle.penup()
    turtle.setpos(-255,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 47:
    turtle.penup()
    turtle.setpos(-221,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 57:
    turtle.penup()
    turtle.setpos(-187,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 67:
    turtle.penup()
    turtle.setpos(-153,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 77:
    turtle.penup()
    turtle.setpos(-119,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 87:
    turtle.penup()
    turtle.setpos(-85,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 97:
    turtle.penup()
    turtle.setpos(-51,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 107:
    turtle.penup()
    turtle.setpos(-17,sey)
    turtle.pendown()
    turtle.pensize(15)
  #eighth line
  elif odf == 18:
    turtle.penup()
    turtle.setpos(-323,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 28:
    turtle.penup()
    turtle.setpos(-289,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 38:
    turtle.penup()
    turtle.setpos(-255,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 48:
    turtle.penup()
    turtle.setpos(-221,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 58:
    turtle.penup()
    turtle.setpos(-187,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 68:
    turtle.penup()
    turtle.setpos(-153,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 78:
    turtle.penup()
    turtle.setpos(-119,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 88:
    turtle.penup()
    turtle.setpos(-85,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 98:
    turtle.penup()
    turtle.setpos(-51,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 108:
    turtle.penup()
    turtle.setpos(-17,ey)
    turtle.pendown()
    turtle.pensize(15)
  #nineth line
  elif odf == 19:
    turtle.penup()
    turtle.setpos(-323,ny)
    turtle.pendown()
    turtle.pensize(15) 
  elif odf == 29:
    turtle.penup()
    turtle.setpos(-289,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 39:
    turtle.penup()
    turtle.setpos(-255,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 49:
    turtle.penup()
    turtle.setpos(-221,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 59:
    turtle.penup()
    turtle.setpos(-187,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 69:
    turtle.penup()
    turtle.setpos(-153,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 79:
    turtle.penup()
    turtle.setpos(-119,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 89:
    turtle.penup()
    turtle.setpos(-85,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 99:
    turtle.penup()
    turtle.setpos(-51,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 109:
    turtle.penup()
    turtle.setpos(-17,ny)
    turtle.pendown()
    turtle.pensize(15)
  #tenth line
  elif odf == 110:
    turtle.penup()
    turtle.setpos(-323,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 210:
    turtle.penup()
    turtle.setpos(-289,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 310:
    turtle.penup()
    turtle.setpos(-255,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 410:
    turtle.penup()
    turtle.setpos(-221,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 510:
    turtle.penup()
    turtle.setpos(-187,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 610:
    turtle.penup()
    turtle.setpos(-153,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 710:
    turtle.penup()
    turtle.setpos(-119,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 810:
    turtle.penup()
    turtle.setpos(-85,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 910:
    turtle.penup()
    turtle.setpos(-51,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 1010:
    turtle.penup()
    turtle.setpos(-17,tey)
    turtle.pendown()
    turtle.pensize(15)
  korkorp.append(odf)
  if defolt == "default":
    napr = "d"
  else:
    napr = input()
  if napr == "l":
    turtle.seth(0) 
    ldh()
    korkorp.append(left[0])
  elif napr == "r":
    turtle.seth(180)
    rdh()
    korkorp.append(right[0])
  elif napr == "d":
    turtle.seth(270)
    ddh()
    korkorp.append(down[0])
  elif napr == "u":
    udh()
    turtle.forward(34) 
    korkorp.append(up[0])
def thk () :
  oy = 196
  ty = 162
  thy = 128
  fy = 94
  fiy = 60
  sy =  26
  sey = -8
  ey = -42
  ny = -76
  ty = -110
  global defolt
  global y
  if defolt == "да":
    if y == 1:
      odf = "e1"
    elif y == 2:
      odf = "e5"
  else:
    odf = input("Введите координаты для трехпалубника")
  if odf == "a1":
    odf = 11
  elif odf == "a2":
    odf = 12
  elif odf == "a3":
    odf = 13
  elif odf == "a4":
    odf = 14
  elif odf == "a5":
    odf = 15
  elif odf == "a6":
    odf = 16
  elif odf == "a7":
    odf = 17
  elif odf == "a8":
    odf = 18
  elif odf == "a9":
    odf = 19
  elif odf == "a10":
    odf = 110
  elif odf == "b1":
    odf = 21
  elif odf == "b2":
    odf = 22
  elif odf == "b3":
    odf = 23
  elif odf == "b4":
    odf = 24
  elif odf == "b5":
    odf = 25
  elif odf == "b6":
    odf = 26
  elif odf == "b7":
    odf = 27
  elif odf == "b8":
    odf = 28
  elif odf == "b9":
    odf = 29
  elif odf == "b10":
    odf = 210
  elif odf == "c1":
    odf = 31
  elif odf == "c2":
    odf = 32
  elif odf == "c3":
    odf = 33
  elif odf == "c4":
    odf = 34
  elif odf == "c5":
    odf = 35
  elif odf == "b6":
    odf = 36
  elif odf == "c7":
    odf = 37
  elif odf == "c8":
    odf = 38
  elif odf == "c9":
    odf = 39
  elif odf == "c10":
    odf = 310
  elif odf == "d1":
    odf = 41
  elif odf == "d2":
    odf = 42
  elif odf == "d3":
    odf = 43
  elif odf == "d4":
    odf = 44
  elif odf == "d5":
    odf = 45
  elif odf == "d6":
    odf = 46
  elif odf == "d7":
    odf = 47
  elif odf == "d8":
    odf = 48
  elif odf == "d9":
    odf = 49
  elif odf == "d10":
    odf = 410
  elif odf == "e1":
    odf = 51
  elif odf == "e2":
    odf = 52
  elif odf == "e3":
    odf = 53
  elif odf == "e4":
    odf = 54
  elif odf == "e5":
    odf = 55
  elif odf == "e6":
    odf = 56
  elif odf == "e7":
    odf = 57
  elif odf == "e8":
    odf = 58
  elif odf == "e9":
    odf = 59
  elif odf == "e10":
    odf = 510 
  elif odf == "f1":
    odf = 61
  elif odf == "f2":
    odf = 62
  elif odf == "f3":
    odf = 63
  elif odf == "f4":
    odf = 64
  elif odf == "f5":
    odf = 65
  elif odf == "f6":
    odf = 66
  elif odf == "f7":
    odf = 67
  elif odf == "f8":
    odf = 68
  elif odf == "f9":
    odf = 69
  elif odf == "f10":
    odf = 610 
  elif odf == "g1":
    odf = 71
  elif odf == "g2":
    odf = 72
  elif odf == "g3":
    odf = 73
  elif odf == "g4":
    odf = 74
  elif odf == "g5":
    odf = 75
  elif odf == "g6":
    odf = 76
  elif odf == "g7":
    odf = 77
  elif odf == "g8":
    odf = 78
  elif odf == "g9":
    odf = 79
  elif odf == "g10":
    odf = 710 
  elif odf == "h1":
    odf = 81
  elif odf == "h2":
    odf = 82
  elif odf == "h3":
    odf = 83
  elif odf == "h4":
    odf = 84
  elif odf == "h5":
    odf = 85
  elif odf == "h6":
    odf = 86
  elif odf == "h7":
    odf = 87
  elif odf == "h8":
    odf = 88
  elif odf == "h9":
    odf = 89
  elif odf == "h10":
    odf = 810  
  elif odf == "i1":
    odf = 91
  elif odf == "i2":
    odf = 92
  elif odf == "i3":
    odf = 93
  elif odf == "i4":
    odf = 94
  elif odf == "i5":
    odf = 95
  elif odf == "i6":
    odf = 96
  elif odf == "i7":
    odf = 97
  elif odf == "i8":
    odf = 98
  elif odf == "i9":
    odf = 99
  elif odf == "i10":
    odf = 910
  elif odf == "j1":
    odf = 101
  elif odf == "j2":
    odf = 102
  elif odf == "j3":
    odf = 103
  elif odf == "j4":
    odf = 104
  elif odf == "j5":
    odf = 105
  elif odf == "j6":
    odf = 106
  elif odf == "j7":
    odf = 107
  elif odf == "j8":
    odf = 108
  elif odf == "j9":
    odf = 109
  elif odf == "j10":
    odf = 1010
  left = [odf - 10, odf - 20]
  right = [odf + 10,odf + 20]
  up = [odf - 1,odf - 2]
  down = [odf + 1,odf + 2]
  if odf == 12:
    turtle.penup()
    turtle.setpos(-323,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 22:
    turtle.penup()
    turtle.setpos(-289,ty)
    turtle.pendown()
    turtle.pensize(15)
  
  elif odf == 32:
    turtle.penup()
    turtle.setpos(-255,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 42:
    turtle.penup()
    turtle.setpos(-221,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 52:
    turtle.penup()
    turtle.setpos(-187,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 62:
    turtle.penup()
    turtle.setpos(-153,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 72:
    turtle.penup()
    turtle.setpos(-119,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 82:
    turtle.penup()
    turtle.setpos(-85,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 92:
    turtle.penup()
    turtle.setpos(-51,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 102:
    turtle.penup()
    turtle.setpos(-17,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  #first line
  elif odf == 11:
    turtle.penup()
    turtle.setpos(-323,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 21:
    turtle.penup()
    turtle.setpos(-289,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 31:
    turtle.penup()
    turtle.setpos(-255,oy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 41:
    turtle.penup()
    turtle.setpos(-221,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 51:
    turtle.penup()
    turtle.setpos(-187,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 61:
    turtle.penup()
    turtle.setpos(-153,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 71:
    turtle.penup()
    turtle.setpos(-119,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 81:
    turtle.penup()
    turtle.setpos(-85,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 91:
    turtle.penup()
    turtle.setpos(-51,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 101:
    turtle.penup()
    turtle.setpos(-17,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  #third line
  elif odf == 13:
    turtle.penup()
    turtle.setpos(-323,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 23:
    turtle.penup()
    turtle.setpos(-289,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 33:
    turtle.penup()
    turtle.setpos(-255,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 43:
    turtle.penup()
    turtle.setpos(-221,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 53:
    turtle.penup()
    turtle.setpos(-187,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 63:
    turtle.penup()
    turtle.setpos(-153,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 73:
    turtle.penup()
    turtle.setpos(-119,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 83:
    turtle.penup()
    turtle.setpos(-85,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 93:
    turtle.penup()
    turtle.setpos(-51,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 103:
    turtle.penup()
    turtle.setpos(-17,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fourth line
  elif odf == 14:
    turtle.penup()
    turtle.setpos(-323,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 24:
    turtle.penup()
    turtle.setpos(-289,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 34:
    turtle.penup()
    turtle.setpos(-255, fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 44:
    turtle.penup()
    turtle.setpos(-221,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 54:
    turtle.penup()
    turtle.setpos(-187,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 64:
    turtle.penup()
    turtle.setpos(-153,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 74:
    turtle.penup()
    turtle.setpos(-119,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 84:
    turtle.penup()
    turtle.setpos(-85,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 94:
    turtle.penup()
    turtle.setpos(-51,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 104:
    turtle.penup()
    turtle.setpos(-17,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fifth line
  elif odf == 15:
    turtle.penup()
    turtle.setpos(-323,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 25:
    turtle.penup()
    turtle.setpos(-289,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 35:
    turtle.penup()
    turtle.setpos(-255,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 45:
    turtle.penup()
    turtle.setpos(-221,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 55:
    turtle.penup()
    turtle.setpos(-187,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 65:
    turtle.penup()
    turtle.setpos(-153,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 75:
    turtle.penup()
    turtle.setpos(-119,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 85:
    turtle.penup()
    turtle.setpos(-85,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 95:
    turtle.penup()
    turtle.setpos(-51,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 105:
    turtle.penup()
    turtle.setpos(-17,fiy)
    turtle.pendown()
    turtle.pensize(15)
  #sixth line
  elif odf == 16:
    turtle.penup()
    turtle.setpos(-323,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 26:
    turtle.penup()
    turtle.setpos(-289,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 36:
    turtle.penup()
    turtle.setpos(-255,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 46:
    turtle.penup()
    turtle.setpos(-221,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 56:
    turtle.penup()
    turtle.setpos(-187,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 66:
    turtle.penup()
    turtle.setpos(-153,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 76:
    turtle.penup()
    turtle.setpos(-119,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 86:
    turtle.penup()
    turtle.setpos(-85,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 96:
    turtle.penup()
    turtle.setpos(-51,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 106:
    turtle.penup()
    turtle.setpos(-17,sy)
    turtle.pendown()
    turtle.pensize(15)
  #seventh line
  elif odf == 17:
    turtle.penup()
    turtle.setpos(-323,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 27:
    turtle.penup()
    turtle.setpos(-289,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 37:
    turtle.penup()
    turtle.setpos(-255,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 47:
    turtle.penup()
    turtle.setpos(-221,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 57:
    turtle.penup()
    turtle.setpos(-187,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 67:
    turtle.penup()
    turtle.setpos(-153,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 77:
    turtle.penup()
    turtle.setpos(-119,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 87:
    turtle.penup()
    turtle.setpos(-85,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 97:
    turtle.penup()
    turtle.setpos(-51,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 107:
    turtle.penup()
    turtle.setpos(-17,sey)
    turtle.pendown()
    turtle.pensize(15)
  #eighth line
  elif odf == 18:
    turtle.penup()
    turtle.setpos(-323,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 28:
    turtle.penup()
    turtle.setpos(-289,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 38:
    turtle.penup()
    turtle.setpos(-255,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 48:
    turtle.penup()
    turtle.setpos(-221,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 58:
    turtle.penup()
    turtle.setpos(-187,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 68:
    turtle.penup()
    turtle.setpos(-153,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 78:
    turtle.penup()
    turtle.setpos(-119,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 88:
    turtle.penup()
    turtle.setpos(-85,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 98:
    turtle.penup()
    turtle.setpos(-51,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 108:
    turtle.penup()
    turtle.setpos(-17,ey)
    turtle.pendown()
    turtle.pensize(15)
  #nineth line
  elif odf == 19:
    turtle.penup()
    turtle.setpos(-323,ny)
    turtle.pendown()
    turtle.pensize(15) 
  elif odf == 29:
    turtle.penup()
    turtle.setpos(-289,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 39:
    turtle.penup()
    turtle.setpos(-255,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 49:
    turtle.penup()
    turtle.setpos(-221,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 59:
    turtle.penup()
    turtle.setpos(-187,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 69:
    turtle.penup()
    turtle.setpos(-153,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 79:
    turtle.penup()
    turtle.setpos(-119,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 89:
    turtle.penup()
    turtle.setpos(-85,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 99:
    turtle.penup()
    turtle.setpos(-51,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 109:
    turtle.penup()
    turtle.setpos(-17,ny)
    turtle.pendown()
    turtle.pensize(15)
  #tenth line
  elif odf == 110:
    turtle.penup()
    turtle.setpos(-323,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 210:
    turtle.penup()
    turtle.setpos(-289,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 310:
    turtle.penup()
    turtle.setpos(-255,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 410:
    turtle.penup()
    turtle.setpos(-221,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 510:
    turtle.penup()
    turtle.setpos(-187,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 610:
    turtle.penup()
    turtle.setpos(-153,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 710:
    turtle.penup()
    turtle.setpos(-119,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 810:
    turtle.penup()
    turtle.setpos(-85,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 910:
    turtle.penup()
    turtle.setpos(-51,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 1010:
    turtle.penup()
    turtle.setpos(-17,tey)
    turtle.pendown()
    turtle.pensize(15)
  korkorp.append(odf)
  if defolt == "default":
    napr = "d"
  else:
    napr = input()
  if napr == "l":
    turtle.seth(0) 
    trs()
    korkorp.append(left[0])
    korkorp.append(left[1])
  elif napr == "r":
    turtle.seth(180)
    trs()
    korkorp.append(right[0])
    korkorp.append(right[1])
  elif napr == "d":
    turtle.seth(270)
    trs()
    korkorp.append(down[0])
    korkorp.append(down[1])
  elif napr == "u":
    turtle.seth(90)
    trs()
    korkorp.append(up[0])
    korkorp.append(up[1])
    
def fk():
  oy = 196
  ty = 162
  thy = 128
  fy = 94
  fiy = 60
  sy =  26
  sey = -8
  ey = -42
  ny = -76
  ty = -110
  global defolt
  if defolt == "да":
    odf = "g1"
  else:
    odf = input("Введите координаты для четырехпалубника")
  if odf == "a1":
    odf = 11
  elif odf == "a2":
    odf = 12
  elif odf == "a3":
    odf = 13
  elif odf == "a4":
    odf = 14
  elif odf == "a5":
    odf = 15
  elif odf == "a6":
    odf = 16
  elif odf == "a7":
    odf = 17
  elif odf == "a8":
    odf = 18
  elif odf == "a9":
    odf = 19
  elif odf == "a10":
    odf = 110
  elif odf == "b1":
    odf = 21
  elif odf == "b2":
    odf = 22
  elif odf == "b3":
    odf = 23
  elif odf == "b4":
    odf = 24
  elif odf == "b5":
    odf = 25
  elif odf == "b6":
    odf = 26
  elif odf == "b7":
    odf = 27
  elif odf == "b8":
    odf = 28
  elif odf == "b9":
    odf = 29
  elif odf == "b10":
    odf = 210
  elif odf == "c1":
    odf = 31
  elif odf == "c2":
    odf = 32
  elif odf == "c3":
    odf = 33
  elif odf == "c4":
    odf = 34
  elif odf == "c5":
    odf = 35
  elif odf == "b6":
    odf = 36
  elif odf == "c7":
    odf = 37
  elif odf == "c8":
    odf = 38
  elif odf == "c9":
    odf = 39
  elif odf == "c10":
    odf = 310
  elif odf == "d1":
    odf = 41
  elif odf == "d2":
    odf = 42
  elif odf == "d3":
    odf = 43
  elif odf == "d4":
    odf = 44
  elif odf == "d5":
    odf = 45
  elif odf == "d6":
    odf = 46
  elif odf == "d7":
    odf = 47
  elif odf == "d8":
    odf = 48
  elif odf == "d9":
    odf = 49
  elif odf == "d10":
    odf = 410
  elif odf == "e1":
    odf = 51
  elif odf == "e2":
    odf = 52
  elif odf == "e3":
    odf = 53
  elif odf == "e4":
    odf = 54
  elif odf == "e5":
    odf = 55
  elif odf == "e6":
    odf = 56
  elif odf == "e7":
    odf = 57
  elif odf == "e8":
    odf = 58
  elif odf == "e9":
    odf = 59
  elif odf == "e10":
    odf = 510 
  elif odf == "f1":
    odf = 61
  elif odf == "f2":
    odf = 62
  elif odf == "f3":
    odf = 63
  elif odf == "f4":
    odf = 64
  elif odf == "f5":
    odf = 65
  elif odf == "f6":
    odf = 66
  elif odf == "f7":
    odf = 67
  elif odf == "f8":
    odf = 68
  elif odf == "f9":
    odf = 69
  elif odf == "f10":
    odf = 610 
  elif odf == "g1":
    odf = 71
  elif odf == "g2":
    odf = 72
  elif odf == "g3":
    odf = 73
  elif odf == "g4":
    odf = 74
  elif odf == "g5":
    odf = 75
  elif odf == "g6":
    odf = 76
  elif odf == "g7":
    odf = 77
  elif odf == "g8":
    odf = 78
  elif odf == "g9":
    odf = 79
  elif odf == "g10":
    odf = 710 
  elif odf == "h1":
    odf = 81
  elif odf == "h2":
    odf = 82
  elif odf == "h3":
    odf = 83
  elif odf == "h4":
    odf = 84
  elif odf == "h5":
    odf = 85
  elif odf == "h6":
    odf = 86
  elif odf == "h7":
    odf = 87
  elif odf == "h8":
    odf = 88
  elif odf == "h9":
    odf = 89
  elif odf == "h10":
    odf = 810  
  elif odf == "i1":
    odf = 91
  elif odf == "i2":
    odf = 92
  elif odf == "i3":
    odf = 93
  elif odf == "i4":
    odf = 94
  elif odf == "i5":
    odf = 95
  elif odf == "i6":
    odf = 96
  elif odf == "i7":
    odf = 97
  elif odf == "i8":
    odf = 98
  elif odf == "i9":
    odf = 99
  elif odf == "i10":
    odf = 910
  elif odf == "j1":
    odf = 101
  elif odf == "j2":
    odf = 102
  elif odf == "j3":
    odf = 103
  elif odf == "j4":
    odf = 104
  elif odf == "j5":
    odf = 105
  elif odf == "j6":
    odf = 106
  elif odf == "j7":
    odf = 107
  elif odf == "j8":
    odf = 108
  elif odf == "j9":
    odf = 109
  elif odf == "j10":
    odf = 1010
  left = [odf - 10,odf - 20 , odf - 30]
  right = [odf + 10,odf + 20 , odf + 30]
  up = [odf - 1,odf - 2 , odf - 3]
  down = [odf + 1,odf + 2 , odf + 3]
  if odf == 12:
    turtle.penup()
    turtle.setpos(-323,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 22:
    turtle.penup()
    turtle.setpos(-289,ty)
    turtle.pendown()
    turtle.pensize(15)
  
  elif odf == 32:
    turtle.penup()
    turtle.setpos(-255,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 42:
    turtle.penup()
    turtle.setpos(-221,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 52:
    turtle.penup()
    turtle.setpos(-187,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 62:
    turtle.penup()
    turtle.setpos(-153,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 72:
    turtle.penup()
    turtle.setpos(-119,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 82:
    turtle.penup()
    turtle.setpos(-85,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 92:
    turtle.penup()
    turtle.setpos(-51,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 102:
    turtle.penup()
    turtle.setpos(-17,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  #first line
  elif odf == 11:
    turtle.penup()
    turtle.setpos(-323,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 21:
    turtle.penup()
    turtle.setpos(-289,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 31:
    turtle.penup()
    turtle.setpos(-255,oy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 41:
    turtle.penup()
    turtle.setpos(-221,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 51:
    turtle.penup()
    turtle.setpos(-187,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 61:
    turtle.penup()
    turtle.setpos(-153,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 71:
    turtle.penup()
    turtle.setpos(-119,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 81:
    turtle.penup()
    turtle.setpos(-85,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 91:
    turtle.penup()
    turtle.setpos(-51,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 101:
    turtle.penup()
    turtle.setpos(-17,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  #third line
  elif odf == 13:
    turtle.penup()
    turtle.setpos(-323,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 23:
    turtle.penup()
    turtle.setpos(-289,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 33:
    turtle.penup()
    turtle.setpos(-255,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 43:
    turtle.penup()
    turtle.setpos(-221,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 53:
    turtle.penup()
    turtle.setpos(-187,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 63:
    turtle.penup()
    turtle.setpos(-153,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 73:
    turtle.penup()
    turtle.setpos(-119,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 83:
    turtle.penup()
    turtle.setpos(-85,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 93:
    turtle.penup()
    turtle.setpos(-51,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 103:
    turtle.penup()
    turtle.setpos(-17,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fourth line
  elif odf == 14:
    turtle.penup()
    turtle.setpos(-323,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 24:
    turtle.penup()
    turtle.setpos(-289,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 34:
    turtle.penup()
    turtle.setpos(-255, fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 44:
    turtle.penup()
    turtle.setpos(-221,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 54:
    turtle.penup()
    turtle.setpos(-187,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 64:
    turtle.penup()
    turtle.setpos(-153,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 74:
    turtle.penup()
    turtle.setpos(-119,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 84:
    turtle.penup()
    turtle.setpos(-85,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 94:
    turtle.penup()
    turtle.setpos(-51,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 104:
    turtle.penup()
    turtle.setpos(-17,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fifth line
  elif odf == 15:
    turtle.penup()
    turtle.setpos(-323,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 25:
    turtle.penup()
    turtle.setpos(-289,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 35:
    turtle.penup()
    turtle.setpos(-255,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 45:
    turtle.penup()
    turtle.setpos(-221,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 55:
    turtle.penup()
    turtle.setpos(-187,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 65:
    turtle.penup()
    turtle.setpos(-153,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 75:
    turtle.penup()
    turtle.setpos(-119,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 85:
    turtle.penup()
    turtle.setpos(-85,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 95:
    turtle.penup()
    turtle.setpos(-51,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 105:
    turtle.penup()
    turtle.setpos(-17,fiy)
    turtle.pendown()
    turtle.pensize(15)
  #sixth line
  elif odf == 16:
    turtle.penup()
    turtle.setpos(-323,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 26:
    turtle.penup()
    turtle.setpos(-289,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 36:
    turtle.penup()
    turtle.setpos(-255,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 46:
    turtle.penup()
    turtle.setpos(-221,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 56:
    turtle.penup()
    turtle.setpos(-187,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 66:
    turtle.penup()
    turtle.setpos(-153,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 76:
    turtle.penup()
    turtle.setpos(-119,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 86:
    turtle.penup()
    turtle.setpos(-85,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 96:
    turtle.penup()
    turtle.setpos(-51,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 106:
    turtle.penup()
    turtle.setpos(-17,sy)
    turtle.pendown()
    turtle.pensize(15)
  #seventh line
  elif odf == 17:
    turtle.penup()
    turtle.setpos(-323,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 27:
    turtle.penup()
    turtle.setpos(-289,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 37:
    turtle.penup()
    turtle.setpos(-255,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 47:
    turtle.penup()
    turtle.setpos(-221,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 57:
    turtle.penup()
    turtle.setpos(-187,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 67:
    turtle.penup()
    turtle.setpos(-153,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 77:
    turtle.penup()
    turtle.setpos(-119,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 87:
    turtle.penup()
    turtle.setpos(-85,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 97:
    turtle.penup()
    turtle.setpos(-51,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 107:
    turtle.penup()
    turtle.setpos(-17,sey)
    turtle.pendown()
    turtle.pensize(15)
  #eighth line
  elif odf == 18:
    turtle.penup()
    turtle.setpos(-323,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 28:
    turtle.penup()
    turtle.setpos(-289,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 38:
    turtle.penup()
    turtle.setpos(-255,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 48:
    turtle.penup()
    turtle.setpos(-221,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 58:
    turtle.penup()
    turtle.setpos(-187,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 68:
    turtle.penup()
    turtle.setpos(-153,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 78:
    turtle.penup()
    turtle.setpos(-119,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 88:
    turtle.penup()
    turtle.setpos(-85,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 98:
    turtle.penup()
    turtle.setpos(-51,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 108:
    turtle.penup()
    turtle.setpos(-17,ey)
    turtle.pendown()
    turtle.pensize(15)
  #nineth line
  elif odf == 19:
    turtle.penup()
    turtle.setpos(-323,ny)
    turtle.pendown()
    turtle.pensize(15) 
  elif odf == 29:
    turtle.penup()
    turtle.setpos(-289,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 39:
    turtle.penup()
    turtle.setpos(-255,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 49:
    turtle.penup()
    turtle.setpos(-221,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 59:
    turtle.penup()
    turtle.setpos(-187,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 69:
    turtle.penup()
    turtle.setpos(-153,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 79:
    turtle.penup()
    turtle.setpos(-119,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 89:
    turtle.penup()
    turtle.setpos(-85,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 99:
    turtle.penup()
    turtle.setpos(-51,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 109:
    turtle.penup()
    turtle.setpos(-17,ny)
    turtle.pendown()
    turtle.pensize(15)
  #tenth line
  elif odf == 110:
    turtle.penup()
    turtle.setpos(-323,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 210:
    turtle.penup()
    turtle.setpos(-289,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 310:
    turtle.penup()
    turtle.setpos(-255,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 410:
    turtle.penup()
    turtle.setpos(-221,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 510:
    turtle.penup()
    turtle.setpos(-187,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 610:
    turtle.penup()
    turtle.setpos(-153,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 710:
    turtle.penup()
    turtle.setpos(-119,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 810:
    turtle.penup()
    turtle.setpos(-85,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 910:
    turtle.penup()
    turtle.setpos(-51,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 1010:
    turtle.penup()
    turtle.setpos(-17,tey)
    turtle.pendown()
    turtle.pensize(15)
  korkorp.append(odf)
  if defolt == "да":
    napr = "d"
  else:
    napr = input()
  if napr == "l":
    turtle.seth(0) 
    frs()
    korkorp.append(left[0])
    korkorp.append(left[1])
    korkorp.append(left[2])
  elif napr == "r":
    turtle.seth(180)
    frs()
    korkorp.append(right[0])
    korkorp.append(right[1])
    korkorp.append(right[2])
  elif napr == "d":
    turtle.seth(270)
    frs()
    korkorp.append(down[0])
    korkorp.append(down[1])
    korkorp.append(down[2])
  elif napr == "u":
    turtle.seth(90)
    frs()
    korkorp.append(up[0])
    korkorp.append(up[1])
    korkorp.append(up[2])
  
defolt = input("Классическкая расстановка ?")
y = 1
for i in range(4):
  odk()
  y = y + 1
y = 1
for i in range(3):
  twk()
  y = y + 1
y = 1
for i in range (2):
  thk()
  y = y + 1

fk()
turtle.speed(9)
korkorbot = []
hodb = []
while True:
  a = random.choice(neispkl)
  hodb.append(a)
  if a == 21 or a == 31 or a == 41 or a == 51 or a == 61 or a == 71 or a == 81 or a == 91 :
    if a - 10 in neispkl and a + 10 in neispkl and a + 1 in neispkl and a + 9 in neispkl and a - 11 in neispkl:
      neispkl.remove(a)
      korkorbot.append(a)
  elif a == 12 or a == 13 or a == 14 or a == 15 or a == 16 or a == 17 or a == 18 or a == 19:
    if a + 10 in neispkl and a - 1 in neispkl and a + 1 in neispkl and a + 11 in neispkl and a + 9 in neispkl:
      neispkl.remove(a)
      korkorbot.append(a)
  elif a == 102 or a == 103 or a == 104 or a == 105 or a == 106 or a == 106 or a == 107 or a == 108 or a == 109:
    if a - 1 in neispkl and a + 1 in neispkl and a - 10 in neispkl and a - 11 in neispkl and a - 9 in neispkl:
      neispkl.remove(a)
      korkorbot.append(a)
  elif a == 11 or a == 101 or a == 1010 or a == 110:
    if a == 11:
      if a + 10 in neispkl and a + 1 in neispkl and a + 9 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)
    elif a == 1010:
       if 109 in neispkl and 810 in neispkl and 89 in neispkl:
         neispkl.remove(a)
         korkorbot.append(a)
    elif a == 101:
       if a - 10 in neispkl and a + 1 in neispkl and 92 in neispkl:
         neispkl.remove(a)
         korkorbot.append(a)
    else:
      if 19 in neispkl and 210 in neispkl and 29 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)
         
  elif a == 210 or a == 310 or a == 410 or a == 510 or a == 610 or a == 710 or a == 810 or a == 910:
    if a == 210:
      if 110 in neispkl and 310 in neispkl and 29 in neispkl and 19 in neispkl and 39 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)
    elif a == 310 :
      if 210 in neispkl and 410 in neispkl and 39 in neispkl and 29 in neispkl and 49 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)
    elif a == 410:
      if 310 in neispkl and 510 in neispkl and 49 in neispkl and 39 in neispkl and 59 in neispkl :
        neispkl.remove(a)
        korkorbot.append(a)
    elif a == 510:
      if 410 in neispkl and 610 in neispkl and 59 in neispkl and 49 in neispkl and 69 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)
    elif a == 610:
      if 510 in neispkl and 710 in neispkl and 69 in neispkl and 59 in neispkl and 79 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)
    elif a == 710 :
      if 610 in neispkl and 810 in neispkl and 79 in neispkl and 69 in neispkl and 89 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a)   
    elif a == 810 :
      if 710 in neispkl and 910 in neispkl and 89 in neispkl and 79 in neispkl and 99 in neispkl:
        neispkl.remove(a)
        korkorbot.append(a) 
    elif a == 910:
      if 810 in neispkl and 1010 in neispkl and 99 in neispkl and 89 in neispkl and 109 in neispkl: 
        neispkl.remove(a)
        korkorbot.append(a)
  else:
    if a + 10 in neispkl and a - 10 in neispkl and a + 1 in neispkl and a - 1 in neispkl and a + 11 in neispkl and a - 11 in neispkl and a + 9 in neispkl and a - 9 in neispkl :
      neispkl.remove(a)
      korkorbot.append(a)
  if len(korkorbot) == 4:
    break 
while True :
  a = random.choice(neispkl)
  if  a == 21 or a == 31 or a == 41 or a == 51 or a == 61 or a == 71 or a == 81 or a == 91 :
    if a - 10 in neispkl and a + 10 in neispkl and a - 1 in neispkl and a + 20 in neispkl and a + 9 in neispkl and a - 11 in neispkl and a + 19 in neispkl:
      korkorbot.append(a)
      korkorbot.append(a + 10)
      neispkl.remove(a)
      neispkl.remove(a + 10)
  elif a == 210 or a == 310  or a == 410 or a == 510 or a == 610 or a == 710 or a == 810 or a == 910:
    if a == 210:
      if 110 in neispkl and 310 in neispkl and 410 in neispkl and 19 in neispkl and 49 in neispkl and 29 in neispkl and 39 in neispkl:
        korkorbot.append(a)
        korkorbot.append(310)
        neispkl.remove(a)
        neispkl.remove(310)
    elif a == 310:
      if 210 in neispkl and 410 in neispkl and 510 in neispkl and 39 in neispkl and 49 in neispkl and 29 in neispkl and 59 in neispkl:
        korkorbot.append(a)
        korkorbot.append(410)
        neispkl.remove(a)
        neispkl.remove(410)
    elif a == 410:
      if 310 in neispkl and 510 in neispkl  and 610 in neispkl and 49 in neispkl and 59 in neispkl and 39 in neispkl and 69 in neispkl:
        korkorbot.append(a)
        korkorbot.append(510)
        neispkl.remove(a)
        neispkl.remove(510)
    elif a == 510:
      if 410 in neispkl and 610 in neispkl   and 710 in neispkl and 59 in neispkl and 69 in neispkl and 49 in neispkl and 79 in neispkl:
        korkorbot.append(a)
        korkorbot.append(610)
        neispkl.remove(a)
        neispkl.remove(610)
    elif a == 610:
      if 510 in neispkl and 710 in neispkl and 810 in neispkl and 59 in neispkl and 69 in neispkl and 79 in neispkl and 89 in neispkl:
        korkorbot.append(a)
        korkorbot.append(710)
        neispkl.remove(a)
        neispkl.remove(710)
    elif a == 710:
      if 610 in neispkl and 810 in neispkl and 910 in neispkl and 69 in neispkl and 79 in neispkl and 89 in neispkl and 99 in neispkl:
        korkorbot.append(a)
        korkorbot.append(810)
        neispkl.remove(a)
        neispkl.remove(810)
    elif a == 810:
      if 710 in neispkl and 910 in neispkl and 1010 in neispkl and 79 in neispkl and 89 in neispkl and 99 in neispkl and 109 in neispkl:
        korkorbot.append(a)
        korkorbot.append(910)
        neispkl.remove(a)
        neispkl.remove(910)   
  else:
    if  a + 10 in neispkl and a - 10 in neispkl and a - 1 in neispkl and a + 1 in neispkl and a + 9 in neispkl and a + 11 in neispkl and a + 20 in neispkl and a - 9 in neispkl and a - 11 in neispkl and a + 21 in neispkl and a + 19 in neispkl:
      neispkl.remove(a)
      neispkl.remove(a + 10)
      korkorbot.append(a)
      korkorbot.append(a + 10)
  if len(korkorbot) == 10:
    time.sleep(2)
    break
while True:
  a = random.choice(neispkl)
  #ungles
  if a == 11 or a == 101 or a == 18 or a == 108:
    if a == 11 and 12 in neispkl and 13 in neispkl:
      if 21 in neispkl and 22 in neispkl and 23 in neispkl and 24 in neispkl and 14 in neispkl:
        neispkl.remove(11)
        neispkl.remove(12)
        neispkl.remove(13)
        korkorbot.append(11)
        korkorbot.append(12) 
        korkorbot.append(13)
    elif a == 101 and 102 in neispkl and 103 in neispkl:
      if 91 in neispkl and 92 in neispkl and 93 in neispkl and 94 in neispkl and 104 in neispkl:
        neispkl.remove(101)
        neispkl.remove(102)
        neispkl.remove(103)
        korkorbot.append(101)
        korkorbot.append(102) 
        korkorbot.append(103)
    elif a == 18 and 19 in neispkl and 110 in neispkl:
      if 17 in neispkl and 27 in neispkl and 28 in neispkl and 29 in neispkl and 210 in neispkl:
        neispkl.remove(18)
        neispkl.remove(19)
        neispkl.remove(110)
        korkorbot.append(18)
        korkorbot.append(19) 
        korkorbot.append(110)
    elif a ==108 and 109 in neispkl and 1010 in neispkl:
      if 107 in neispkl and 97 in neispkl and 98 in neispkl and 99 in neispkl and 910 in neispkl:
        neispkl.remove(108)
        neispkl.remove(109)
        neispkl.remove(1010)
        korkorbot.append(108)
        korkorbot.append(109) 
        korkorbot.append(1010)
  elif a == 12 or a == 13 or a == 14 or a == 15 or a == 16 :
    if a - 1 in neispkl and a + 1 in neispkl and a + 2 in neispkl and a + 3 in neispkl and a + 9 in neispkl and a + 10 in neispkl and a + 11 in neispkl and a + 12 in neispkl and a + 13 in neispkl:
      neispkl.remove(a)
      neispkl.remove(a+1)
      neispkl.remove(a+2)
      korkorbot.append(a)
      korkorbot.append(a+1)
      korkorbot.append(a+2)
  elif a == 102 or a == 103 or a == 104 or a == 105 or a == 106:
    if - 1 in neispkl and a + 1 in neispkl and a + 2 in neispkl and a + 3 in neispkl and a - 11 in neispkl and a - 10 in niespkl and a - 9 in neispkl and a - 8 in neispkl and a - 7 in neispkl:
      neispkl.remove(a)
      neispkl.remove(a+1)
      neispkl.remove(a+2)
      korkorbot.append(a)
      korkorbot.append(a+1)
      korkorbot.append(a+2)
  elif a == 21 or a == 31 or a == 41 or a == 51 or a == 61 or a == 71 or a == 81 or a == 91:
    if a - 10 in neispkl and a + 10 in neispkl and a + 1 in neispkl and a + 2 in neispkl and a + 3 in neispkl and a - 9 in neispkl and a - 8 in neispkl and  a - 7 in neispkl and a + 11 in neispkl and a + 12 in neispkl and a + 13 in neispkl:
      neispkl.remove(a)
      neispkl.remove(a+1)
      neispkl.remove(a+2)
      korkorbot.append(a)
      korkorbot.append(a+1)
      korkorbot.append(a+2)
  elif a == 28 or a == 38 or a == 48 or a == 58 or a == 68 or a == 78 or a == 88 or a == 98:
    if a - 11 in neispkl and a - 1 in neispkl and a + 9 in neispkl and a - 10 in neispkl and a + 10 in neispkl and a - 9 in neispkl and a + 1 in neispkl and a + 11 in neispkl and a - 8 in neispkl and a + 2 in neispkl and a + 12 in neispkl :
      neispkl.remove(a)
      neispkl.remove(a+1)
      neispkl.remove(a+2)
      korkorbot.append(a)
      korkorbot.append(a+1)
      korkorbot.append(a+2)
        
  else:
    if a - 11 in neispkl and a - 1 in neispkl and a + 9 in neispkl and a - 10 in neispkl and a + 10 in neispkl and a - 9 in neispkl and a + 1 in neispkl and a + 11 in neispkl and a - 8 in neispkl and a + 2 in neispkl and a + 12 in neispkl and a - 7 in neispkl and a + 3 in neispkl and a + 13 in neispkl:
      neispkl.remove(a)
      neispkl.remove(a + 1)
      neispkl.remove(a + 2)
      korkorbot.append(a)
      korkorbot.append(a + 1) 
      korkorbot.append(a + 2)
  if len(korkorbot) == 16:
    break
  
while True:
  a = random.choice(neispkl)
  if a + 10 in neispkl and a + 20 in neispkl and a + 30 in neispkl and a - 10 in neispkl and a + 40 in neispkl and a + 1 in neispkl and a - 1 in neispkl and a + 11 in neispkl and a + 9 in neispkl and a + 19 in neispkl and a + 21 in neispkl and a + 31 in neispkl and a + 29 in neispkl:
    
    neispkl.remove(a)
    neispkl.remove(a + 10)
    neispkl.remove(a + 20)
    neispkl.remove(a + 30)
    korkorbot.append(a)
    korkorbot.append(a + 10)    
    korkorbot.append(a + 20)    
    korkorbot.append(a + 30) 
  if len(korkorbot) == 20:
    break
pp = 0
bp = 0
turtle.pensize(5)
neispkl = [11,12,13,14,15,16,17,18,19,110,21,22,23,24,25,26,27,28,29,210,31,32,33,34,35,36,37,38,39,310,41,42,43,44,45,46,47,48,49,410,51,52,53,54,55,56,57,58,59,510,61,62,63,64,65,66,67,68,69,610,71,72,73,74,75,76,77,78,79,710,81,82,83,84,85,86,87,88,89,810,91,92,93,94,95,96,97,98,99,910,101,102,103,104,105,106,107,108,109,1010]
def hodbot ():
  global bp
  oy = 196
  ty = 162
  thy = 128
  fy = 94 
  fiy = 60
  sy =  26
  sey = -8
  ey = -42
  ny = -76
  tey = -110
  odf = random.choice(neispkl)
  neispkl.remove(odf)
  if odf == 12:
    turtle.penup()
    turtle.setpos(-323,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 22:
    turtle.penup()
    turtle.setpos(-289,ty)
    turtle.pendown()
    turtle.pensize(15)
  
  elif odf == 32:
    turtle.penup()
    turtle.setpos(-255,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 42:
    turtle.penup()
    turtle.setpos(-221,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 52:
    turtle.penup()
    turtle.setpos(-187,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 62:
    turtle.penup()
    turtle.setpos(-153,ty)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 72:
    turtle.penup()
    turtle.setpos(-119,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 82:
    turtle.penup()
    turtle.setpos(-85,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 92:
    turtle.penup()
    turtle.setpos(-51,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 102:
    turtle.penup()
    turtle.setpos(-17,ty)
    turtle.pendown()
    turtle.pensize(15)
    
  #first line
  elif odf == 11:
    turtle.penup()
    turtle.setpos(-323,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 21:
    turtle.penup()
    turtle.setpos(-289,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 31:
    turtle.penup()
    turtle.setpos(-255,oy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 41:
    turtle.penup()
    turtle.setpos(-221,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 51:
    turtle.penup()
    turtle.setpos(-187,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 61:
    turtle.penup()
    turtle.setpos(-153,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 71:
    turtle.penup()
    turtle.setpos(-119,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 81:
    turtle.penup()
    turtle.setpos(-85,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 91:
    turtle.penup()
    turtle.setpos(-51,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 101:
    turtle.penup()
    turtle.setpos(-17,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  #third line
  elif odf == 13:
    turtle.penup()
    turtle.setpos(-323,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 23:
    turtle.penup()
    turtle.setpos(-289,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 33:
    turtle.penup()
    turtle.setpos(-255,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 43:
    turtle.penup()
    turtle.setpos(-221,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 53:
    turtle.penup()
    turtle.setpos(-187,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 63:
    turtle.penup()
    turtle.setpos(-153,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 73:
    turtle.penup()
    turtle.setpos(-119,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 83:
    turtle.penup()
    turtle.setpos(-85,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 93:
    turtle.penup()
    turtle.setpos(-51,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 103:
    turtle.penup()
    turtle.setpos(-17,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fourth line
  elif odf == 14:
    turtle.penup()
    turtle.setpos(-323,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 24:
    turtle.penup()
    turtle.setpos(-289,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 34:
    turtle.penup()
    turtle.setpos(-255, fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 44:
    turtle.penup()
    turtle.setpos(-221,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 54:
    turtle.penup()
    turtle.setpos(-187,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 64:
    turtle.penup()
    turtle.setpos(-153,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 74:
    turtle.penup()
    turtle.setpos(-119,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 84:
    turtle.penup()
    turtle.setpos(-85,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 94:
    turtle.penup()
    turtle.setpos(-51,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 104:
    turtle.penup()
    turtle.setpos(-17,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fifth line
  elif odf == 15:
    turtle.penup()
    turtle.setpos(-323,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 25:
    turtle.penup()
    turtle.setpos(-289,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 35:
    turtle.penup()
    turtle.setpos(-255,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 45:
    turtle.penup()
    turtle.setpos(-221,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 55:
    turtle.penup()
    turtle.setpos(-187,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 65:
    turtle.penup()
    turtle.setpos(-153,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 75:
    turtle.penup()
    turtle.setpos(-119,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 85:
    turtle.penup()
    turtle.setpos(-85,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 95:
    turtle.penup()
    turtle.setpos(-51,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 105:
    turtle.penup()
    turtle.setpos(-17,fiy)
    turtle.pendown()
    turtle.pensize(15)
  #sixth line
  elif odf == 16:
    turtle.penup()
    turtle.setpos(-323,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 26:
    turtle.penup()
    turtle.setpos(-289,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 36:
    turtle.penup()
    turtle.setpos(-255,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 46:
    turtle.penup()
    turtle.setpos(-221,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 56:
    turtle.penup()
    turtle.setpos(-187,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 66:
    turtle.penup()
    turtle.setpos(-153,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 76:
    turtle.penup()
    turtle.setpos(-119,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 86:
    turtle.penup()
    turtle.setpos(-85,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 96:
    turtle.penup()
    turtle.setpos(-51,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 106:
    turtle.penup()
    turtle.setpos(-17,sy)
    turtle.pendown()
    turtle.pensize(15)
  #seventh line
  elif odf == 17:
    turtle.penup()
    turtle.setpos(-323,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 27:
    turtle.penup()
    turtle.setpos(-289,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 37:
    turtle.penup()
    turtle.setpos(-255,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 47:
    turtle.penup()
    turtle.setpos(-221,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 57:
    turtle.penup()
    turtle.setpos(-187,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 67:
    turtle.penup()
    turtle.setpos(-153,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 77:
    turtle.penup()
    turtle.setpos(-119,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 87:
    turtle.penup()
    turtle.setpos(-85,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 97:
    turtle.penup()
    turtle.setpos(-51,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 107:
    turtle.penup()
    turtle.setpos(-17,sey)
    turtle.pendown()
    turtle.pensize(15)
  #eighth line
  elif odf == 18:
    turtle.penup()
    turtle.setpos(-323,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 28:
    turtle.penup()
    turtle.setpos(-289,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 38:
    turtle.penup()
    turtle.setpos(-255,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 48:
    turtle.penup()
    turtle.setpos(-221,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 58:
    turtle.penup()
    turtle.setpos(-187,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 68:
    turtle.penup()
    turtle.setpos(-153,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 78:
    turtle.penup()
    turtle.setpos(-119,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 88:
    turtle.penup()
    turtle.setpos(-85,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 98:
    turtle.penup()
    turtle.setpos(-51,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 108:
    turtle.penup()
    turtle.setpos(-17,ey)
    turtle.pendown()
    turtle.pensize(15)
  #nineth line
  elif odf == 19:
    turtle.penup()
    turtle.setpos(-323,ny)
    turtle.pendown()
    turtle.pensize(15) 
  elif odf == 29:
    turtle.penup()
    turtle.setpos(-289,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 39:
    turtle.penup()
    turtle.setpos(-255,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 49:
    turtle.penup()
    turtle.setpos(-221,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 59:
    turtle.penup()
    turtle.setpos(-187,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 69:
    turtle.penup()
    turtle.setpos(-153,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 79:
    turtle.penup()
    turtle.setpos(-119,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 89:
    turtle.penup()
    turtle.setpos(-85,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 99:
    turtle.penup()
    turtle.setpos(-51,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 109:
    turtle.penup()
    turtle.setpos(-17,ny)
    turtle.pendown()
    turtle.pensize(15)
  #tenth line
  elif odf == 110:
    turtle.penup()
    turtle.setpos(-323,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 210:
    turtle.penup()
    turtle.setpos(-289,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 310:
    turtle.penup()
    turtle.setpos(-255,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 410:
    turtle.penup()
    turtle.setpos(-221,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 510:
    turtle.penup()
    turtle.setpos(-187,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 610:
    turtle.penup()
    turtle.setpos(-153,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 710:
    turtle.penup()
    turtle.setpos(-119,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 810:
    turtle.penup()
    turtle.setpos(-85,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 910:
    turtle.penup()
    turtle.setpos(-51,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 1010:
    turtle.penup()
    turtle.setpos(-17,tey)
    turtle.pendown()
    turtle.pensize(15)
  if odf in korkorp:
    redx()
    bp = bp + 1
  elif odf == 31 or odf == 34 or odf == 37 or odf == 74 :
    if defolt == "default":
      redx()
      bp = bp + 1
  elif odf in korkorp:
    redx()
    bp = bp + 1
  else:
    whitex()
sds = False
dss = False
tss = False
fss = False
isphod = []
if name == "moder":
  print(korkorbot)
def sigmapoddef(x,y):
  turtle.penup()
  turtle.setpos(x,y)
  turtle.pendown()
  turtle.pensize(15)
def hodp ():
  global hodpl
  global sds
  global dss
  global tss
  global fss
  global pp
  oy = 196
  ty = 162
  thy = 128
  fy = 94
  fiy = 60
  sy =  26
  sey = -8
  ey = -42
  ny = -76
  tey = -110
  odf = input()
  hodpl.append(odf)
  if odf == "a1":
    odf = 11
  elif odf == "a2":
    odf = 12
  elif odf == "a3":
    odf = 13
  elif odf == "a4":
    odf = 14
  elif odf == "a5":
    odf = 15
  elif odf == "a6":
    odf = 16
  elif odf == "a7":
    odf = 17
  elif odf == "a8":
    odf = 18
  elif odf == "a9":
    odf = 19
  elif odf == "a10":
    odf = 110
  elif odf == "b1":
    odf = 21
  elif odf == "b2":
    odf = 22
  elif odf == "b3":
    odf = 23
  elif odf == "b4":
    odf = 24
  elif odf == "b5":
    odf = 25
  elif odf == "b6":
    odf = 26
  elif odf == "b7":
    odf = 27
  elif odf == "b8":
    odf = 28
  elif odf == "b9":
    odf = 29
  elif odf == "b10":
    odf = 210
  elif odf == "c1":
    odf = 31
  elif odf == "c2":
    odf = 32
  elif odf == "c3":
    odf = 33
  elif odf == "c4":
    odf = 34
  elif odf == "c5":
    odf = 35
  elif odf == "c6":
    odf = 36
  elif odf == "c7":
    odf = 37
  elif odf == "c8":
    odf = 38
  elif odf == "c9":
    odf = 39
  elif odf == "c10":
    odf = 310
  elif odf == "d1":
    odf = 41
  elif odf == "d2":
    odf = 42
  elif odf == "d3":
    odf = 43
  elif odf == "d4":
    odf = 44
  elif odf == "d5":
    odf = 45
  elif odf == "d6":
    odf = 46
  elif odf == "d7":
    odf = 47
  elif odf == "d8":
    odf = 48
  elif odf == "d9":
    odf = 49
  elif odf == "d10":
    odf = 410
  elif odf == "e1":
    odf = 51
  elif odf == "e2":
    odf = 52
  elif odf == "e3":
    odf = 53
  elif odf == "e4":
    odf = 54
  elif odf == "e5":
    odf = 55
  elif odf == "e6":
    odf = 56
  elif odf == "e7":
    odf = 57
  elif odf == "e8":
    odf = 58
  elif odf == "e9":
    odf = 59
  elif odf == "e10":
    odf = 510 
  elif odf == "f1":
    odf = 61
  elif odf == "f2":
    odf = 62
  elif odf == "f3":
    odf = 63
  elif odf == "f4":
    odf = 64
  elif odf == "f5":
    odf = 65
  elif odf == "f6":
    odf = 66
  elif odf == "f7":
    odf = 67
  elif odf == "f8":
    odf = 68
  elif odf == "f9":
    odf = 69
  elif odf == "f10":
    odf = 610 
  elif odf == "g1":
    odf = 71
  elif odf == "g2":
    odf = 72
  elif odf == "g3":
    odf = 73
  elif odf == "g4":
    odf = 74
  elif odf == "g5":
    odf = 75
  elif odf == "g6":
    odf = 76
  elif odf == "g7":
    odf = 77
  elif odf == "g8":
    odf = 78
  elif odf == "g9":
    odf = 79
  elif odf == "g10":
    odf = 710 
  elif odf == "h1":
    odf = 81
  elif odf == "h2":
    odf = 82
  elif odf == "h3":
    odf = 83
  elif odf == "h4":
    odf = 84
  elif odf == "h5":
    odf = 85
  elif odf == "h6":
    odf = 86
  elif odf == "h7":
    odf = 87
  elif odf == "h8":
    odf = 88
  elif odf == "h9":
    odf = 89
  elif odf == "h10":
    odf = 810  
  elif odf == "i1":
    odf = 91
  elif odf == "i2":
    odf = 92
  elif odf == "i3":
    odf = 93
  elif odf == "i4":
    odf = 94
  elif odf == "i5":
    odf = 95
  elif odf == "i6":
    odf = 96
  elif odf == "i7":
    odf = 97
  elif odf == "i8":
    odf = 98
  elif odf == "i9":
    odf = 99
  elif odf == "i10":
    odf = 910
  elif odf == "j1":
    odf = 101
  elif odf == "j2":
    odf = 102
  elif odf == "j3":
    odf = 103
  elif odf == "j4":
    odf = 104
  elif odf == "j5":
    odf = 105
  elif odf == "j6":
    odf = 106
  elif odf == "j7":
    odf = 107
  elif odf == "j8":
    odf = 108
  elif odf == "j9":
    odf = 109
  elif odf == "j10":
    odf = 1010
  if odf == 12:
    sigmapoddef(37,ty)
  elif odf == 22:
    sigmapoddef(71,ty)
  elif odf == 32:
    sigmapoddef(105,ty)
  elif odf == 42:
    sigmapoddef(139,ty)
  elif odf == 52:
    sigmapoddef(173,ty)
  elif odf == 62:
    sigmapoddef(207,ty)
  elif odf == 72:
    sigmapoddef(241,ty)
  elif odf == 82:
    sigmapoddef(275,ty)
  elif odf == 92:
    sigmapoddef(309,ty)
  elif odf == 102:
    sigmapoddef(343,ty)
  #first line
  elif odf == 11:
    turtle.penup()
    turtle.setpos(37,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 21:
    turtle.penup()
    turtle.setpos(71,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 31:
    turtle.penup()
    turtle.setpos(105,oy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 41:
    turtle.penup()
    turtle.setpos(139,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 51:
    turtle.penup()
    turtle.setpos(173,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 61:
    turtle.penup()
    turtle.setpos(207,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 71:
    turtle.penup()
    turtle.setpos(241,oy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 81:
    turtle.penup()
    turtle.setpos(275,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 91:
    turtle.penup()
    turtle.setpos(309,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 101:
    turtle.penup()
    turtle.setpos(343,oy)
    turtle.pendown()
    turtle.pensize(15)
    
  #third line
  elif odf == 13:
    turtle.penup()
    turtle.setpos(37,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 23:
    turtle.penup()
    turtle.setpos(71,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 33:
    turtle.penup()
    turtle.setpos(105,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 43:
    turtle.penup()
    turtle.setpos(139,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 53:
    turtle.penup()
    turtle.setpos(173,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 63:
    turtle.penup()
    turtle.setpos(207,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 73:
    turtle.penup()
    turtle.setpos(241,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 83:
    turtle.penup()
    turtle.setpos(275,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 93:
    turtle.penup()
    turtle.setpos(309,thy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 103:
    turtle.penup()
    turtle.setpos(343,thy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fourth line
  elif odf == 14:
    turtle.penup()
    turtle.setpos(37,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 24:
    turtle.penup()
    turtle.setpos(71,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 34:
    turtle.penup()
    turtle.setpos(105,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 44:
    turtle.penup()
    turtle.setpos(139,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 54:
    turtle.penup()
    turtle.setpos(173,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 64:
    turtle.penup()
    turtle.setpos(207,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 74:
    turtle.penup()
    turtle.setpos(241,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 84:
    turtle.penup()
    turtle.setpos(275,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  elif odf == 94:
    turtle.penup()
    turtle.setpos(309,fy)
    turtle.pendown()
    turtle.pensize(15)
   
  elif odf == 104:
    turtle.penup()
    turtle.setpos(343,fy)
    turtle.pendown()
    turtle.pensize(15)
    
  #fifth line
  elif odf == 15:
    turtle.penup()
    turtle.setpos(37,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 25:
    turtle.penup()
    turtle.setpos(71,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 35:
    turtle.penup()
    turtle.setpos(105,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 45:
    turtle.penup()
    turtle.setpos(139,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 55:
    turtle.penup()
    turtle.setpos(173,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 65:
    turtle.penup()
    turtle.setpos(207,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 75:
    turtle.penup()
    turtle.setpos(241,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 85:
    turtle.penup()
    turtle.setpos(275,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 95:
    turtle.penup()
    turtle.setpos(309,fiy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 105:
    turtle.penup()
    turtle.setpos(343,fiy)
    turtle.pendown()
    turtle.pensize(15)
  #sixth line
  elif odf == 16:
    turtle.penup()
    turtle.setpos(37,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 26:
    turtle.penup()
    turtle.setpos(71,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 36:
    turtle.penup()
    turtle.setpos(105,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 46:
    turtle.penup()
    turtle.setpos(139,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 56:
    turtle.penup()
    turtle.setpos(173,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 66:
    turtle.penup()
    turtle.setpos(207,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 76:
    turtle.penup()
    turtle.setpos(241,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 86:
    turtle.penup()
    turtle.setpos(275,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 96:
    turtle.penup()
    turtle.setpos(309,sy)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 106:
    turtle.penup()
    turtle.setpos(343,sy)
    turtle.pendown()
    turtle.pensize(15)
  #seventh line
  elif odf == 17:
    turtle.penup()
    turtle.setpos(37,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 27:
    turtle.penup()
    turtle.setpos(71,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 37:
    turtle.penup()
    turtle.setpos(105,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 47:
    turtle.penup()
    turtle.setpos(139,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 57:
    turtle.penup()
    turtle.setpos(173,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 67:
    turtle.penup()
    turtle.setpos(207,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 77:
    turtle.penup()
    turtle.setpos(241,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 87:
    turtle.penup()
    turtle.setpos(275,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 97:
    turtle.penup()
    turtle.setpos(309,sey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 107:
    turtle.penup()
    turtle.setpos(343,sey)
    turtle.pendown()
    turtle.pensize(15)
  #eighth line
  elif odf == 18:
    turtle.penup()
    turtle.setpos(37,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 28:
    turtle.penup()
    turtle.setpos(71,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 38:
    turtle.penup()
    turtle.setpos(105,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 48:
    turtle.penup()
    turtle.setpos(139,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 58:
    turtle.penup()
    turtle.setpos(173, ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 68:
    turtle.penup()
    turtle.setpos(207,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 78:
    turtle.penup()
    turtle.setpos(241,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 88:
    turtle.penup()
    turtle.setpos(275,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 98:
    turtle.penup()
    turtle.setpos(309,ey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 108:
    turtle.penup()
    turtle.setpos(343,ey)
    turtle.pendown()
    turtle.pensize(15)
  #nineth line
  elif odf == 19:
    turtle.penup()
    turtle.setpos(37,ny)
    turtle.pendown()
    turtle.pensize(15) 
  elif odf == 29:
    turtle.penup()
    turtle.setpos(71,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 39:
    turtle.penup()
    turtle.setpos(105,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 49:
    turtle.penup()
    turtle.setpos(139,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 59:
    turtle.penup()
    turtle.setpos(173,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 69:
    turtle.penup()
    turtle.setpos(207,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 79:
    turtle.penup()
    turtle.setpos(241,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 89:
    turtle.penup()
    turtle.setpos(275,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 99:
    turtle.penup()
    turtle.setpos(309,ny)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 109:
    turtle.penup()
    turtle.setpos(343,ny)
    turtle.pendown()
    turtle.pensize(15)
  #tenth line
  elif odf == 110:
    turtle.penup()
    turtle.setpos(37,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 210:
    turtle.penup()
    turtle.setpos(71, tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 310:
    turtle.penup()
    turtle.setpos(105,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 410:
    turtle.penup()
    turtle.setpos(139,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 510:
    turtle.penup()
    turtle.setpos(173,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 610:
    turtle.penup()
    turtle.setpos(207,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 710:
    turtle.penup()
    turtle.setpos(241,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 810:
    turtle.penup()
    turtle.setpos(275,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 910:
    turtle.penup()
    turtle.setpos(309,tey)
    turtle.pendown()
    turtle.pensize(15)
  elif odf == 1010:
    turtle.penup()
    turtle.setpos(343,tey)
    turtle.pendown()
    turtle.pensize(15)
  global defolt
  global isphod
  if odf not in isphod:
    if odf in korkorbot:
      a = korkorbot.index(odf)
      redx()
      pp = pp + 1
      isphod.append(odf)
    else:
      whitex()
  else:
    redx()
if " " in name :
  namew = name + " - are  winners" 
else:
  namew = name + " - winner"
pp = 0
bp = 0
while True:
  hodp ()
  strr = str(pp) + "     " + str(bp)
  turtle.title(strr)
  if pp == 20:
    turtle.penup()
    turtle.setpos(-17,250)
    turtle.pendown()
    turtle.write(namew)
    break
  hodbot()
  if bp == 20:
    turtle.penup()
    turtle.setpos(-17,250)
    turtle.pendown()
    turtle.write("win - bot")
    break

