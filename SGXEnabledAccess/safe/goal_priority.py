#!/usr/bin/python3

import sys

lines = sys.stdin.readlines()

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []

lemma = sys.argv[1]

for line in lines:
  num = line.split(':')[0]

  if (lemma == 'two_check_pass_can_not_have_same_global_var_strict_reuse') | (lemma == 'two_update_cannot_write_same_val') | (lemma == 'increasing_update_property') | (lemma == 'is_decreasing_update_possible'):
  # if True
      if (' = ' in line) | (' < '  in line) | ('last(' in line) | ('Lock' in line) | ('Unlock' in line) :
        l1.append(num)
      
      elif "RA_shared_key" in line:
        l2.append(num)
      elif "!KU( senc" in line:
        l3.append(num)
      elif ("!GlobalVar" in line) & ("'1'" in line)   :
        l4.append(num)
      else:
        l6.append(num)

  else:
    exit(0)

ranked = l1 + l2 +  l3 + l4 + l5 + l6 + l7 + l8   
# ranked = l1 + l2 + l3 + l4  

for i in ranked:
  print(i)