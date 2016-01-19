#!/usr/bin/python

from cobra import Model, Reaction, Metabolite

model = Model('core_metabolism')

### Add Metabolites ###

# Cytoplasmic metabolites:

atp_c = Metabolite(
    'atp_c',
    formula='C10H12N5O13P3',
    name='adenosine triphosphate',
    compartment='c'
    )
glc_c = Metabolite(
    'glc_c',
    formula='C6H12O6',
    name='glucose',
    compartment='c'
    )
adp_c = Metabolite(
    'adp_c',
    formula='C10H12N5O10P2',
    name='adenosine diphosphate',
    compartment='c'
    )
g6p_c = Metabolite(
    'g6p_c',
    formula='C6H11O9P',
    name='glucose 6-phosphate',
    compartment='c'
    )
h_c = Metabolite(
    'h_c',
    formula='H',
    name='proton',
    compartment='c'
    )
f6p_c = Metabolite(
    'f6p_c',
    formula='C6H11O9P',
    name='fructose 6-phosphate',
    compartment='c'
    )
fdp_c = Metabolite(
    'fdp_c',
    formula='C6H10O12P2',
    name='fructose 1,6-diphosphate',
    compartment='c'
    )
dhap_c = Metabolite(
    'dhap_c',
    formula='C3H5O6P',
    name='dihydroxyacetone phosphate',
    compartment='c'
    )
g3p_c = Metabolite(
    'g3p_c',
    formula='C3H5O6P',
    name='glyceraldehyde 3-phosphate',
    compartment='c'
    )
nad_c = Metabolite(
    'nad_c',
    formula='C21H26N7O14P2',
    name='nicotinamide adenine dinucleotide (oxidized)',
    compartment='c'
    )
pi_c = Metabolite(
    'pi_c',
    formula='HO4P',
    name='inorganic phosphate',
    compartment='c'
    )
m13dpg_c = Metabolite(
    '13dpg_c',
    formula='C3H4O10P2',
    name='3-phospho-D-glycerol phosphate',
    compartment='c'
    )
nadh_c = Metabolite(
    'nadh_c',
    formula='C21H27N7O14P2',
    name='nicotinamide adenine dinucleotide (reduced)',
    compartment='c'
    )
m3pg_c = Metabolite(
    '3pg_c',
    formula='C3H4O7P',
    name='3-phosphoglycerate',
    compartment='c'
    )
m2pg_c = Metabolite(
    '2pg_c',
    formula='C3H4O7P',
    name='2-phosphoglycerate',
    compartment='c'
    )
pep_c = Metabolite(
    'pep_c',
    formula='C3H2O6P',
    name='phosphoenolpyruvate',
    compartment='c'
    )
h2o_c = Metabolite(
    'h2o_c',
    formula='H2O',
    name='water',
    compartment='c'
    )
pyr_c = Metabolite(
    'pyr_c',
    formula='C3H3O3',
    name='pyruvate',
    compartment='c'
    )
gl6p_c = Metabolite(
    'gl6p_c',
    formula='C6H9O9P',
    name='6-phosphgluconolactone',
    compartment='c'
    )
go6p_c = Metabolite(
    'go6p_c',
    formula='C6H10O10P',
    name='6-phosphogluconate',
    compartment='c'
    )
nadp_c = Metabolite(
    'nadp_c',
    formula='C21H25N7O17P3',
    name='nicotinamide adenine dinucleotide phosphate (oxidized)',
    compartment='c'
    )
nadph_c = Metabolite(
    'nadph_c',
    formula='C21H26N7O17P3',
    name='nicotinamide adenine dinucleotide phosphate (reduced)',
    compartment='c'
    )
ru5p_c = Metabolite(
    'ru5p_c',
    formula='C5H9O8P',
    name='ribulose 5-phosphate',
    compartment='c'
    )
r5p_c = Metabolite(
    'r5p_c',
    formula='C5H9O8P',
    name='ribose 5-phosphate',
    compartment='c'
    )
x5p_c = Metabolite(
    'x5p_c',
    formula='C5H9O8P',
    name='xylulose 5-phosphate',
    compartment='c'
    )
s7p_c = Metabolite(
    's7p_c',
    formula='C7H13O10P',
    name='sedoheptulose 7-phosphate',
    compartment='c'
    )
e4p_c = Metabolite(
    'e4p_c',
    formula='C4H7O7P',
    name='erythrose 4-phosphate',
    compartment='c'
    )
gsh_c = Metabolite(
    'gsh_c',
    formula='C10H17N3O6S',
    name='glutathione',
    compartment='c'
    )
gssg_c = Metabolite(
    'gssg_c',
    formula='C20H32N6O12S2',
    name='glutathione disulfide',
    compartment='c'
    )
co2_c = Metabolite(
    'co2_c',
    formula='CO2',
    name='carbon dioxide',
    compartment='c'
    )
accoa_c = Metabolite(
    'accoa_c',
    formula='C23H38N7O17P3S',
    name='acetyl co-a',
    compartment='c'
    )
oac_c = Metabolite(
    'oac_c',
    formula='C4H2O5',
    name='oxaloacetate',
    compartment='c'
    )
cit_c = Metabolite(
    'cit_c',
    formula='C6H5O7',
    name='citrate',
    compartment='c'
    )
coa_c = Metabolite(
    'coa_c',
    formula='C21H36N7O16P3S',
    name='coenzyme a',
    compartment='c'
    )
cisaco_c = Metabolite(
    'cisaco_c',
    formula='C6H3O6',
    name='cis-aconitate',
    compartment='c'
    )
icit_c = Metabolite(
    'icit_c',
    formula='C6H5O7',
    name='isocitrate',
    compartment='c'
    )
oas_c = Metabolite(
    'oas_c',
    formula='C6H3O7',
    name='oxalosuccinate',
    compartment='c'
    )
akg_c = Metabolite(
    'akg_c',
    formula='C5H4O5',
    name='alpha-ketogluterate',
    compartment='c'
    )
succoa_c = Metabolite(
    'succoa_c',
    formula='C25H39N7O19P3S',
    name='succinyl coa',
    compartment='c'
    )
gdp_c = Metabolite(
    'gdp_c',
    formula='C10H15N5O11P2',
    name='guanosine diphosphate',
    compartment='c'
    )
gtp_c = Metabolite(
    'gtp_c',
    formula='C10H16N5O14P3',
    name='guanosine triphosphate',
    compartment='c'
    )
succ_c = Metabolite(
    'succ_c',
    formula='C4H4O4',
    name='succinate',
    compartment='c'
    )
fad_c = Metabolite(
    'fad_c',
    formula='C27H33N9O15P2',
    name='flavin adenine dinucleotide (oxidized)',
    compartment='c'
    )
fadh2_c = Metabolite(
    'fadh2_c',
    formula='C27H35N9O15P2',
    name='flavin adenine dinucleotide (reduced)',
    compartment='c'
    )
fum_c = Metabolite(
    'fum_c',
    formula='C4H2O4',
    name='fumarate',
    compartment='c'
    )
mal_c = Metabolite(
    'mal_c',
    formula='C4H4O5',
    name='malate',
    compartment='c'
    )

# Extracellular Metabolites:

glc_e = Metabolite(
    'glc_e',
    formula='C6H12O6',
    name='glucose',
    compartment='e'
    )
h_e = Metabolite(
    'h_e',
    formula='H',
    name='proton',
    compartment='e'
    )
h2o_e = Metabolite(
    'h2o_e',
    formula='H2O',
    name='water',
    compartment='e'
    )
pyr_e = Metabolite(
    'pyr_e',
    formula='C3H3O3',
    name='pyruvate',
    compartment='e'
    )
co2_e = Metabolite(
    'co2',
    formula='CO2',
    name='carbon dioxide',
    compartment='e'
    )

### Add Reactions ###

HEX1 = Reaction('HEX1')
HEX1.subsystem = 'Glycolysis'
HEX1.lower_bound = 0.
HEX1.upper_bound = 1000.
HEX1.add_metabolites({
    glc_c: -1.0,
    atp_c: -1.0,
    g6p_c: 1.0,
    adp_c: 1.0,
    h_c: 1.0
    })
PGI = Reaction('PGI')
PGI.subsystem = 'Glycolysis'
PGI.lower_bound = -1000.
PGI.upper_bound = 1000.
PGI.add_metabolites({
    g6p_c: -1.0,
    f6p_c: 1.0
    })
PFK = Reaction('PFK')
PFK.subsystem = 'Glycolysis'
PFK.lower_bound = 0.
PFK.upper_bound = 1000.
PFK.add_metabolites({
    atp_c: -1.0,
    f6p_c: -1.0,
    adp_c: 1.0,
    fdp_c: 1.0,
    h_c: 1.0
    })
FBA = Reaction('FBA')
FBA.subsystem = 'Glycolysis'
FBA.lower_bound = -1000.
FBA.upper_bound = 1000.
FBA.add_metabolites({
    fdp_c: -1.0,
    dhap_c: 1.0,
    g3p_c: 1.0
    })
TPI = Reaction('TPI')
TPI.subsystem = 'Glycolysis'
TPI.lower_bound = -1000.
TPI.upper_bound = 1000.
TPI.add_metabolites({
    dhap_c: -1.0,
    g3p_c: 1.0
    })
GAPD = Reaction('GAPD')
GAPD.subsystem = 'Glycolysis'
GAPD.lower_bound = -1000.
GAPD.upper_bound = 1000.
GAPD.objective_coefficient = 0.
GAPD.add_metabolites({
    g3p_c: -1.0,
    nad_c: -1.0,
    pi_c: -1.0,
    m13dpg_c: 1.0,
    h_c: 1.0,
    nadh_c: 1.0
    })
PGK = Reaction('PGK')
PGK.subsystem = 'Glycolysis'
PGK.lower_bound = -1000.
PGK.upper_bound = 1000.
PGK.add_metabolites({
    m13dpg_c: -1.0,
    adp_c: -1.0,
    m3pg_c: 1.0,
    atp_c: 1.0
    })
PGM = Reaction('PGM')
PGM.subsystem = 'Glycolysis'
PGM.lower_bound = -1000.
PGM.upper_bound = 1000.
PGM.add_metabolites({
    m3pg_c: -1.0,
    m2pg_c: 1.0
    })
ENO = Reaction('ENO')
ENO.subsystem = 'Glycolysis'
ENO.lower_bound = -1000.
ENO.upper_bound = 1000.
ENO.add_metabolites({
    m2pg_c: -1.0,
    h2o_c: 1.0,
    pep_c: 1.0
    })
PYK = Reaction('PYK')
PYK.subsystem = 'Glycolysis'
PYK.lower_bound = 0.
PYK.upper_bound = 1000.
PYK.add_metabolites({
    adp_c: -1.0,
    h_c: -1.0,
    pep_c: -1.0,
    atp_c: 1.0,
    pyr_c: 1.0
    })
G6PDH = Reaction('G6PDH')
G6PDH.subsystem = 'Pentose Phosphate Pathway'
G6PDH.lower_bound = 0.
G6PDH.upper_bound = 1000.
G6PDH.add_metabolites({
    g6p_c: -1.0,
    nadp_c: -1.0,
    gl6p_c: 1.0,
    nadph_c: 1.0,
    h_c: 1.0
    })
GL6PLS = Reaction('GL6PLS')
GL6PLS.subsystem = 'Pentose Phosphate Pathway'
GL6PLS.lower_bound = 0.
GL6PLS.upper_bound = 1000.
GL6PLS.add_metabolites({
    gl6p_c: -1.0,
    h2o_c: -1.0,
    go6p_c: 1.0,
    h_c: 1.0
    })
GO6PDH = Reaction('GO6PDH')
GO6PDH.subsystem = 'Pentose Phosphate Pathway'
GO6PDH.lower_bound = 0.
GO6PDH.upper_bound = 1000.
GO6PDH.add_metabolites({
    go6p_c: -1.0,
    nadp_c: -1.0,
    ru5p_c: 1.0,
    co2_c: 1.0,
    nadph_c: 1.0
    })
RPI = Reaction('RPI')
RPI.subsystem = 'Pentose Phosphate Pathway'
RPI.lower_bound = -1000.
RPI.upper_bound = 1000.
RPI.add_metabolites({
    ru5p_c: -1.0,
    r5p_c: 1.0
    })
RPE = Reaction('RPE')
RPE.subsystem ='Pentose Phosphate Pathway'
RPE.lower_bound= -1000.
RPE.upper_bound = 1000.
RPE.add_metabolites({
    ru5p_c: -1.0,
    x5p_c: 1.0
    })
TK1 = Reaction('TK1')
TK1.subsystem ='Pentose Phosphate Pathway'
TK1.lower_bound= -1000.
TK1.upper_bound = 1000.
TK1.add_metabolites({
    r5p_c: -1.0,
    x5p_c: -1.0,
    g3p_c: 1.0,
    s7p_c: 1.0
    })
TA = Reaction('TA')
TA.subsystem ='Pentose Phosphate Pathway'
TA.lower_bound= -1000.
TA.upper_bound = 1000.
TA.add_metabolites({
    s7p_c: -1.0,
    g3p_c: -1.0,
    e4p_c: 1.0,
    f6p_c: 1.0
    })
TK2 = Reaction('TK2')
TK2.subsystem ='Pentose Phosphate Pathway'
TK2.lower_bound= -1000.
TK2.upper_bound = 1000.
TK2.add_metabolites({
    x5p_c: -1.0,
    e4p_c: -1.0,
    g3p_c: 1.0,
    f6p_c: 1.0
    })
GSR = Reaction('GSR')
GSR.subsystem ='Pentose Phosphate Pathway'
GSR.lower_bound= -1000.
GSR.upper_bound = 1000.
GSR.add_metabolites({
    gssg_c: -1.0,
    nadph_c: -1.0,
    h_c: -1.0,
    gsh_c: 2.0,
    nadp_c: 1.0
    })
PDH = Reaction('PDH')
PDH.subsystem ='TCA Cycle'
PDH.lower_bound= 0.
PDH.upper_bound = 1000.
PDH.add_metabolites({
    pyr_c: -1.0,
    coa_c: -1.0,
    nad_c: -1.0,
    accoa_c: 1.0,
    nadh_c: 1.0,
    co2_c: 1.0
    })
CS = Reaction('CS')
CS.subsystem ='TCA Cycle'
CS.lower_bound= 0.
CS.upper_bound = 1000.
CS.add_metabolites({
    accoa_c: -1.0,
    oac_c: -1.0,
    h2o_c: -1.0,
    cit_c: 1.0,
    coa_c: 1.0,
    h_c: 1.0
    })
ACO1 = Reaction('ACO1')
ACO1.subsystem ='TCA Cycle'
ACO1.lower_bound= -1000.
ACO1.upper_bound = 1000.
ACO1.add_metabolites({
    cit_c: -1.0,
    cisaco_c: 1.0,
    h2o_c: 1.0
    })
ACO2 = Reaction('ACO2')
ACO2.subsystem ='TCA Cycle'
ACO2.lower_bound= -1000.
ACO2.upper_bound = 1000.
ACO2.add_metabolites({
    cisaco_c: -1.0,
    h2o_c: -1.0,
    icit_c: 1.0
    })
ICDH1 = Reaction('ICDH1')
ICDH1.subsystem ='TCA Cycle'
ICDH1.lower_bound= 0.
ICDH1.upper_bound = 1000.
ICDH1.add_metabolites({
    icit_c: -1.0,
    nad_c: -1.0,
    oas_c: 1.0,
    nadh_c: 1.0,
    h_c: 1.0
    })
ICDH2 = Reaction('ICDH2')
ICDH2.subsystem ='TCA Cycle'
ICDH2.lower_bound= 0.
ICDH2.upper_bound = 1000.
ICDH2.add_metabolites({
    oas_c: -1.0,
    h_c: -1.0,
    akg_c: 1.0,
    co2_c: 1.0
    })
AKGDH = Reaction('AKGDH')
AKGDH.subsystem ='TCA Cycle'
AKGDH.lower_bound= 0.
AKGDH.upper_bound = 1000.
AKGDH.add_metabolites({
    akg_c: -1.0,
    nad_c: -1.0,
    coa_c: -1.0,
    succoa_c: 1.0,
    co2_c: 1.0,
    nadh_c: 1.0
    })
SCS = Reaction('SCS')
SCS.subsystem ='TCA Cycle'
SCS.lower_bound= -1000.
SCS.upper_bound = 1000.
SCS.add_metabolites({
    succoa_c: -1.0,
    pi_c: -1.0,
    gdp_c: -1.0,
    h_c: -1.0,
    succ_c: 1.0,
    gtp_c: 1.0,
    coa_c: 1.0
    })
SDH = Reaction('SDH')
SDH.subsystem ='TCA Cycle'
SDH.lower_bound= -1000.
SDH.upper_bound = 1000.
SDH.add_metabolites({
    succ_c: -1.0,
    fad_c: -1.0,
    fum_c: 1.0,
    fadh2_c: 1.0
    })
FMS = Reaction('FMS')
FMS.subsystem ='TCA Cycle'
FMS.lower_bound= -1000.
FMS.upper_bound = 1000.
FMS.add_metabolites({
    fum_c: -1.0,
    h2o_c: -1.0,
    mal_c: 1.0
    })
MDH = Reaction('MDH')
MDH.subsystem ='TCA Cycle'
MDH.lower_bound= -1000.
MDH.upper_bound = 1000.
MDH.add_metabolites({
    mal_c: -1.0,
    nad_c: -1.0,
    oac_c: 1.0,
    nadh_c: 1.0,
    h_c: 1.0
    })

# Transport reactions:

GLCt = Reaction('GLCt')
GLCt.subsystem = 'Transport/Exchange'
GLCt.lower_bound = -10.
GLCt.upper_bound = 1000.
GLCt.add_metabolites({
    glc_e: -1.0,
    glc_c: 1.0
    })
Ht = Reaction('Ht')
Ht.subsystem = 'Transport/Exchange'
Ht.lower_bound = -1000.
Ht.upper_bound = 1000.
Ht.add_metabolites({
    h_e: -1.0,
    h_c: 1.0
    })
H2Ot = Reaction('H2Ot')
H2Ot.subsystem = 'Transport/Exchange'
H2Ot.lower_bound = -10.
H2Ot.upper_bound = 1000.
H2Ot.add_metabolites({
    h2o_e: -1.0,
    h2o_c: 1.0
    })
PYRt = Reaction('PYRt')
PYRt.subsystem = 'Transport/Exchange'
PYRt.lower_bound = -10.
PYRt.upper_bound = 1000.
PYRt.add_metabolites({
    pyr_e: -1.0,
    pyr_c: 1.0
    })
CO2t = Reaction('CO2t')
CO2t.subsystem = 'Transport/Exchange'
CO2t.lower_bound = -10.
CO2t.upper_bound = 1000.
CO2t.add_metabolites({
    co2_e: -1.0,
    co2_c: 1.0
    })

# Exchange reactions:

EX_glc = Reaction('EX_glc')
EX_glc.subsystem = 'Transport/Exchange'
EX_glc.lower_bound = -1000.
EX_glc.upper_bound = 0.
EX_glc.add_metabolites({
    glc_e: -1.0
    })
EX_h = Reaction('EX_h')
EX_h.subsystem = 'Transport/Exchange'
EX_h.lower_bound = -1000.
EX_h.upper_bound = 0.
EX_h.add_metabolites({
    h_e: -1.0
    })
EX_h2o = Reaction('EX_h2o')
EX_h2o.subsystem = 'Transport/Exchange'
EX_h2o.lower_bound = -1000.
EX_h2o.upper_bound = 0.
EX_h2o.add_metabolites({
    h2o_e: -1.0
    })
EX_pyr = Reaction('EX_pyr')
EX_pyr.subsystem = 'Transport/Exchange'
EX_pyr.lower_bound = -1000.
EX_pyr.upper_bound = 0.
EX_pyr.add_metabolites({
    pyr_e: -1.0
    })
EX_co2  =Reaction('EX_co2')
EX_co2.subsystem = 'Transport/Exchange'
EX_co2.lower_bound = -1000.
EX_co2.upper_bound = 0.
EX_co2.add_metabolites({
    co2_e: -1.0
    })

### Add reactions to model ###

model.add_reactions([
    HEX1,
    PGI,
    PFK,
    FBA,
    TPI,
    GAPD,
    PGK,
    PGM,
    ENO,
    PYK,
    GLCt,
    Ht,
    H2Ot,
    PYRt,
    EX_glc,
    EX_h,
    EX_h2o,
    EX_pyr,
    G6PDH,
    GL6PLS,
    GO6PDH,
    RPI,
    RPE,
    TK1,
    TA,
    TK2,
    GSR,
    CO2t,
    EX_co2,
    PDH,
    CS,
    ACO1,
    ACO2,
    ICDH1,
    ICDH2,
    AKGDH,
    SCS,
    SDH,
    FMS,
    MDH
    ])

print 'Reactions'
print '---------'
for reaction in model.reactions:
    print('%s : %s' % (reaction.id, reaction.reaction))
print '\nMetabolites'
print '-----------'
for metabolite in model.metabolites:
    print('%s : %s' % (metabolite.id, metabolite.formula))


array_model = model.to_array_based_model()
print array_model.S.todense()

for reaction in model.reactions:
    print reaction.check_mass_balance()
