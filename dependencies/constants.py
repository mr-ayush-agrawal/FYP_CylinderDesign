# Defining some constants for ranges 

HELICAL_ANGLE_LB = 10
HELICAL_ANGLE_UB = 50

HELICAL_LAYER_LB = 2
HELICAL_LAYER_UB = 17

HOOP_LAYER_LB = 1
HOOP_LAYER_UB = 15

TENSILE_STRENGTH_LB = 600
TENSILE_STRENGTH_UB = 1100

E1_LB = 20
E1_UB = 120

YOUNGS_MODULUS_LB = 55
YOUNGS_MODULUS_UB = 200

POISSONS_RATIO_LB = 0.25
POISSONS_RATIO_UB = 0.35

YEILD_STRENGTH_LB = 230
YEILD_STRENGTH_UB = 250

ULT_STRENGTH_LB = 310
ULT_STRENGTH_UB = 370

LINER_THICKNESS_LB = 0.2
LINER_THICKNESS_UB = 0.8

DIAMETER_LB = 100
DIAMETER_UB = 180

DOLIY_LB = 1
DOLIY_UB = 20

input_cols = ['bust_pressure',  'tensile_str', 'e1_gpa', 'youngs_modulus', 'poision_ratio', 'yeild_strength', 'diameter', 'ult_tensile_strength']
output_cols = ['helical_angle', 'helical_layer_count', 'hoop_layer_count', 'liner_thickness', 'doily_layers']