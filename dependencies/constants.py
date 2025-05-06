# Defining some constants for ranges 

HELICAL_ANGLE_LB = 10
HELICAL_ANGLE_UB = 30

HELICAL_LAYER_LB = 3
HELICAL_LAYER_UB = 15

HOOP_LAYER_LB = 1
HOOP_LAYER_UB = 15

TENSILE_STRENGTH_LB = 600
TENSILE_STRENGTH_UB = 1100

E1_LB = 95
E1_UB = 110

YOUNGS_MODULUS_LB = 55
YOUNGS_MODULUS_UB = 150

POISSONS_RATIO_LB = 0.25
POISSONS_RATIO_UB = 0.35

YEILD_STRENGTH_LB = 230
YEILD_STRENGTH_UB = 250

ULT_STRENGTH_LB = 310
ULT_STRENGTH_UB = 370

LINER_THICKNESS_LB = 0.4
LINER_THICKNESS_UB = 0.6

DIAMETER_LB = 120
DIAMETER_UB = 150

DOLIY_LB = 7
DOLIY_UB = 25

input_cols = ['bust_pressure',  'tensile_str', 'e1_gpa', 'youngs_modulus', 'poision_ratio', 'yeild_strength', 'diameter', 'ult_tensile_strength']
output_cols = ['helical_angle', 'helical_layer_count', 'hoop_layer_count', 'liner_thickness', 'doily_layers']