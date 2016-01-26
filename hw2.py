#!/usr/bin/python  

import cobra
import cobra.test
import os

model=cobra.test.create_test_model("ecoli")

# Add NADH-, NADPH-consuming reactions to model #
# cobrapy.readthedocs.org

### Problem 1 ###


### Problem 2 ###

# Modify objectives then optimize.
# check FBA tutrial of cobrapy tutorial 

### Problem 3 ###

# http://cobrapy.readthedocs.org/en/0.2.1/03_single_deletion.html

# single_deletion_growth_dict: A dictionary that provides the growth rate 
# information for single gene knock outs. This can speed up simulations 
# because nonviable single deletion strains imply that all double deletion
# strains will also be nonviable.

print "Problem 3: \n"
