#!/Users/sarahvaccaro/anaconda/bin/python

import re
import cobra
import cobra.test
import libsbml
from cobra import Model, Reaction, Metabolite

ecoli_core=cobra.io.load_matlab_model('ecoli_core_model.mat')

def rename_metabolites():
    get_compartment=re.compile('.*\[([a-z])\].*')

    for metabolite in ecoli_core.metabolites:
        comp = get_compartment.match(metabolite.id)
        id = metabolite.id.replace('[','_').replace(']','')
        metabolite.id = id
        metabolite.compartment = comp.group(1)
    return ecoli_core.metabolites


def add_sink_rxns():
    NADH_sink = Reaction('NADH_sink')
    NADH_sink.lower_bound = 0.
    NADH_sink.upper_bound = 1000.
    NADH_sink.add_metabolites({
            ecoli_core.metabolites.get_by_id('nadh[c]') : -1,
            ecoli_core.metabolites.get_by_id('nad[c]') : 1,
            ecoli_core.metabolites.get_by_id('h[c]') : 1
            })
    NADPH_sink = Reaction('NADPH_sink')
    NADPH_sink.lower_bound = 0.
    NADPH_sink.upper_bound = 1000.
    NADPH_sink.add_metabolites({
            ecoli_core.metabolites.get_by_id('nadph[c]'): -1,
            ecoli_core.metabolites.get_by_id('nadp[c]') : 1,
            ecoli_core.metabolites.get_by_id('h[c]') : 1
            })
    ecoli_core.add_reactions([
            NADH_sink,
            NADPH_sink
            ])
    return ecoli_core

def simulate_model_growth(target):
    tmp_ecoli_core=ecoli_core.copy()
    tmp_ecoli_core.reactions.get_by_id('EX_glc(e)').lower_bound=-1
    tmp_ecoli_core.reactions.get_by_id('EX_glc(e)').upper_bound=-1
    tmp_ecoli_core.reactions.get_by_id('Biomass_Ecoli_core_w_GAM').objective_coefficient=0
    tmp_ecoli_core.reactions.get_by_id(target).upper_bound=1000.
    tmp_ecoli_core.reactions.get_by_id(target).objective_coefficient=1
    rate = tmp_ecoli_core.optimize().f
    print 'Max Rate for %s: %s' % (target, rate)

def simulate_carbon_source(source):
    tmp_ecoli_core=ecoli_core.copy()
    tmp_ecoli_core.reactions.get_by_id('EX_glc(e)').lower_bound=0
    tmp_ecoli_core.reactions.get_by_id(source).lower_bound=-20.
    rate = tmp_ecoli_core.optimize().f
    print 'Growth on %s: %s' % (source, rate)

def simulate_gene_knockout():
    tmp_ecoli_core=ecoli_core.copy()
    max_rate=ecoli_core.optimize().f
    rate, status = cobra.flux_analysis.single_deletion(tmp_ecoli_core)
    for gene in rate:
        if rate[gene]/max_rate <= 0.01:
            print '%s: NO growth' % gene
        elif rate[gene]/max_rate > 0.01:
            print '%s: growth' % gene
        else:
            print '%s: OTHER' % gene

add_sink_rxns()

print '\nPROBLEM 1\n-----------\n'
simulate_model_growth('Biomass_Ecoli_core_w_GAM')
simulate_model_growth('ATPM')
simulate_model_growth('NADH_sink')
simulate_model_growth('NADPH_sink')

print '\nPROBLEM 2\n-----------\n'
simulate_carbon_source('EX_glc(e)')
simulate_carbon_source('EX_succ(e)')
simulate_carbon_source('EX_fru(e)')
simulate_carbon_source('EX_ac(e)')
simulate_carbon_source('EX_pyr(e)')

print '\nPROBLEM 3\n-----------\n'
simulate_gene_knockout()
=======
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
