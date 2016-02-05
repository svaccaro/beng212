#!/Users/sarahvaccaro/anaconda/bin/python    

import cobra
import pickle
import os
from sets import Set

dictionary={'Alanine Aspartate Metabolism':'Amino Acid Metabolism','Alanine and Aspartate Metabolism':'Amino Acid Metabolism','Arginine and Proline Metabolism':'Amino Acid Metabolism','Cysteine Metabolism':'Amino Acid Metabolism','Glutamate Metabolism':'Amino Acid Metabolism','Glutamate metabolism':'Amino Acid Metabolism','Glycine and Serine Metabolism':'Amino Acid Metabolism','Glycine, Serine and threonine metabolism':'Amino Acid Metabolism','Histidine Metabolism':'Amino Acid Metabolism','Lysine Metabolism':'Amino Acid Metabolism','Methionine Metabolism':'Amino Acid Metabolism','Phenylalanine Metabolism':'Amino Acid Metabolism','Thiamine Metabolism':'Amino Acid Metabolism','Threonine and Lysine Metabolism':'Amino Acid Metabolism','Tryptophan metabolism':'Amino Acid Metabolism','Tyrosine metabolism':'Amino Acid Metabolism','Tyrosine, Tryptophan, and Phenylalanine Metabolism':'Amino Acid Metabolism','Valine, Leucine, and Isoleucine Metabolism':'Amino Acid Metabolism'}

subsystems=Set()

model = pickle.load(open('models/iYL1228.pickle','rb'))

for rxn in model.reactions:
    if rxn.subsystem in dictionary:
        subsystems.add(dictionary[rxn.subsystem])
    else:
        subsystems.add(rxn.subsystem)

for sub in sorted(subsystems):
    print sub



'''
def collect_reactions(model):
    for reaction in model.reactions:
        if reaction.lower_bound!=0 or reaction.upper_bound!=0:
            sub = reaction.subsystem
            rxn = reaction.id
            if sub in dictionary:
                if rxn in dictionary[sub]:
                    dictionary[sub][rxn]+=1
                else:
                    dictionary[sub][rxn]=1
            else:
                dictionary[sub]={rxn:1}




for subsystem in dictionary:
    subsystems.append(subsystem)
    core_count=0
    pan_count=0
    for rxn in dictionary[subsystem]:
        if dictionary[subsystem][rxn]==model_count:
            core_count+=1
        else:
            pan_count+=1
    core.append(core_count)
    pan.append(pan_count)

subsystems=tuple(subsystems)
core=tuple(core)
pan=tuple(pan)
'''
