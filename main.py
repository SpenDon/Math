import sys
global col, bit, fnum, double, neg, pop
file = open("test.sad", "r")
bit = 0
close = False
double = False
neg = False
pop = False
op = False
func = False
fnum = 0
funcl = {}
ln = 0
col = 0
def error(text):
  print(f'ERROR (Line {str(ln)}, column {str(col)})')
  print(f'{str(ln)}, {str(col)}: {text}')
  print("For language reference, go to github.com/Spencer")
  sys.exit()
def interpret(text):
  global col, bit, fnum, double, neg, pop, close
  col = 0
  for char in text:
      col += 1
      if char == "{":
        if close != False and close != "curl":
          error("Unclosed bracket")
        double = True
        pass
      elif char == "(":
        if close != False and close != "par":
          error("Unclosed bracket")
        neg = True
        pass
      elif char == "[":
        if close != False and close != "brac":
          error("Unclosed bracket")
        pop = True
        pass
      elif char == "/":
        if close != False and close != "line":
          error("Unclosed bracket")
        op = True
        pass
      elif char in ("t", "T"):
        bit += 1000
      elif char in ("m", "M"):
        bit += 1000000
      elif char in ("b", "B"):
        bit += 1000000000
      elif char in ("r", "R"):
        bit += 1000000000000
      elif char in ("q", "Q"):
        bit += 1000000000000000
      elif char in ("g", "G"):
        bit += int("1" + ("0" * 100))
      elif char in ("p", "P"):
        bit += int("1" + ("0" * 100000))
      elif char in ("e", "E"):
        bit *= 69420
      elif char in ("f", "F"):
        fnum += 1
        if fnum == 1:
          print("Respects have been payed, comrade")
        elif fnum == 2:
          print("Lots of respect, comrade")
        elif fnum == 3:
          print("Okay, thanks?")
        elif fnum > 3:
          error("Respect Overload")
      elif char in ("a", "A"):
        print("amogus 69 " * 1000)
      elif char in ("-", "+", "|"):
        if double == True:
          if char == "-":
            bit -= 1
            bit *= 2
          elif char == "+":
            bit += 1
            bit *= 2
          elif char == "|":
            bit *= 2
          close = "curl"
          double = False
        elif neg == True:
          if char == "-":
            bit -= 1
            bit = -bit
          elif char == "+":
            bit += 1
            bit = -bit
          elif char == "|":
            bit = -bit
          close = "par"
          neg = False
        elif pop == True:
          if char == "-":
            bit -= 1
            print(bit)
            bit = 0
          elif char == "+":
            bit += 1
            print(bit)
            bit = 0
          elif char == "|":
            print(bit)
            bit = 0
          close = "brac"
          pop = False
        elif op == True:
          if char == "-":
            bit -= 1
          elif char == "+":
            bit += 1
          # Why does this condition exist
          # You're a psycho if you type "/|\"
          # That does nothing, weirdo
          elif char == "|":
            pass
          close = "line"
          op = False
        else:
          error("Unexpected operator")
      elif char in ("}", ")", "]", "\\"):
        if close != False:
          if close == "curl" and char == "}":
            close = False
            pass
          elif close == "par" and char == ")":
            close = False
            pass
          elif close == "brac" and char == "]":
            close = False
            pass
          elif close == "line" and char == "\\":
            close = False
            pass
          else:
            error("Incorrect closing brackets")
        else:
          error("Unexpected closing bracket")
      elif char == " ":
        pass
      else:
        if char in funcl.keys():
          interpret(funcl[char])
        else:
          error("Unknown character")
for line in file.readlines():
  ln += 1
  line = line.strip()
  if line.startswith("def"):
    cnum = -1
    named = False
    tbn = False
    for dchar in line:
      cnum += 1
      if dchar in ("d", "e", "f", "D", "E", "F") and cnum < 3:
        pass
      elif dchar == " ":
        pass
      elif dchar == ">":
        if named == False:
          tbn = True
        elif tbn == True:
          error("Function must be named")
  else:
    interpret(line)