#!/Users/sarahvaccaro/anaconda/bin/python    

import pandas as pd
import cobra
import os
from pickle import *
    
def build_draft_strain_specific_models():
    data = pd.read_csv('Klebsiella_pneu.csv',index_col=0)
    
    for o in data.columns:
        missing_genes = data[pd.isnull(data[o])][o].index.tolist()

        # INSERT YOUR MODEL HERE
        model = cobra.io.json.load_json_model('iYL1228.json')
        
        model.name = o
        model.id = o
        
        if len(missing_genes) > 0:
            cobra.manipulation.delete_model_genes(model, missing_genes)
            model.optimize()
            print model, model.solution.f, len(model._trimmed_genes), len(model._trimmed_reactions)
        else:
            model.optimize()
            print model, model.solution.f, 0, 0
        o=o.replace('/','-').replace(' ','')
        
        dump(model, open('models/'+o+'.pickle','wb'))
        
build_draft_strain_specific_models()
