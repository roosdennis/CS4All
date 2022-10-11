# Programmeren I, Practicum 5
# Bestandsnaam: wk5ex1
# Naam: Dennis Roos
# Probleemomschrijving: conversie binair <-> decimaal

from re import X


def is_odd(n):
    n % 2 == 1
        
def num_to_binary(n):
    """Converts a value to Binary."""
    if n == 0:
        return ""

    elif n % 2 == 1:
        return num_to_binary(n // 2) + "1"

    else:
        return num_to_binary(n // 2) + "0"

def binary_to_num(s):
    """Converts a Binary value to numbers"""
    if s == "":
        return 0
        
    # als het laatste cijfer een '1' is...
    elif s[-1] == "1":
        return binary_to_num(s[:-1])*2 + 1

    else:  # laatste cijfer moet een '0' zijn
        return binary_to_num(s[:-1])*2 + 0

def increment(s):
    """Converts a Binary value to number, adds 1, and converts back to Binary
       In the end it adds 0's on the left to a maximum of 8 characters in the string
    """
    x = binary_to_num(s) + 1
    y = num_to_binary(x)
    z = 8 - len(y)
    return(z * '0' + y)
  
def count(s, n):
  """ Accepts an 8-character binary input string S and
      Then counts n times upward from S, printing each count
  """
  print(s)
  if n == 0:
    return
  else:
    count(increment(s), n - 1)        

def num_to_ternary(n):
    """Converts a value to Ternary.
       59 zou 2012 moeten genereren, want (2*27)+(0*9)+(1*3)+(2*1)"""
    if n == 0:
        return ""

    elif n % 3 == 1:
        return num_to_ternary(n // 3) + "1"

    elif n % 3 == 2:
        return num_to_ternary(n // 3) + "2"    

    else:
        return num_to_ternary(n // 3) + "0" 

def ternary_to_num(s):
    """Converts a Ternary value to numbers"""
    if s == "":
        return 0

    elif s[-1] == "2":
        return ternary_to_num(s[:-1]) * 3 + 2

    elif s[-1] == "1":
        return ternary_to_num(s[:-1]) * 3 + 1

    else:
        return ternary_to_num(s[:-1]) * 3 + 0



assert is_odd(42) == False
assert is_odd(43) == True
assert num_to_binary(0) == ""
assert num_to_binary(42) == "101010"
assert binary_to_num("") == 0
assert binary_to_num("101010") == 42
assert num_to_ternary(59) == "2012"
assert ternary_to_num("2012") == 59
