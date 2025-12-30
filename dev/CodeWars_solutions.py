//solution 1: Even or Odd//
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

//solution 2: convert a number_to_string//
  def number_to_string(num):
    return str(num)

//solution 3: remove string spaces//
def no_space(x):
    return x.replace(" ", "")

//solution 4: vowel count//
def get_count(sentence):
    return sum(1 for c in sentence if c in "aeiou")