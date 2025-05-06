import streamlit as st
import pandas as pd
import numpy as np
from warnings import filterwarnings

from dependencies.constants import *
from dependencies.load_scaler_objects import x_scaler, y_scaler
from dependencies.load_model_obj import model
from dependencies.utils.scaler_utils import inverse_scale

filterwarnings('ignore')

st.title("Cylinder Desing parameters")

# Taking the input from the user
input_data = {}

st.header("Enter the following parameters:")

target_burst_pressure = st.slider("Target Burst Pressure of cylinder in bar", min_value=50.0, max_value=2000.0, value=500.0)
tensile_strength = st.slider("Tensile Strength of Carbon Fibre in MPa", min_value=float(TENSILE_STRENGTH_LB), max_value=float(TENSILE_STRENGTH_UB), value=650.0)
e1_gpa = st.slider("E1 of Carbon Fibre in GPa", min_value=float(E1_LB), max_value=float(E1_UB), value=100.0)
youngs_modulus = st.slider("Young's Modulus of Carbon Fibre in GPa", min_value=float(YOUNGS_MODULUS_LB), max_value=float(YOUNGS_MODULUS_UB), value=57.5)
poison_ratio = st.slider("Poison Ratio of Carbon Fibre", min_value=float(POISSONS_RATIO_LB), max_value=float(POISSONS_RATIO_UB), value=0.33)
yeild_strength = st.slider("Yeild Strength of Carbon Fibre in MPa", min_value=float(YEILD_STRENGTH_LB), max_value=float(YEILD_STRENGTH_UB), value=240.0)
diameter = st.slider("Diameter of Cylinder in mm", min_value=float(DIAMETER_LB), max_value=float(DIAMETER_UB), value=130.0)
ult_tensile_strength = st.slider("Ultimate Tensile Strength of Liner Material in MPa", min_value=float(ULT_STRENGTH_LB), max_value=float(ULT_STRENGTH_UB), value=600.0)


input_data['bust_pressure'] = target_burst_pressure
input_data['tensile_str'] = tensile_strength
input_data['e1_gpa'] = e1_gpa
input_data['youngs_modulus'] = youngs_modulus
input_data['poision_ratio'] = poison_ratio
input_data['yeild_strength'] = yeild_strength
input_data['diameter'] = diameter
input_data['ult_tensile_strength'] = ult_tensile_strength

st.subheader("Input features : ")
input_data = pd.DataFrame([input_data], columns=input_cols)
st.write(input_data)

predict_button = st.button('Predict')

if predict_button : 
    scaled_input = x_scaler.transform(input_data)
    
    predictions = model.predict(scaled_input)

    pred_values = inverse_scale(predictions, as_tensor = False, scaler=y_scaler)
    pred_df = pd.DataFrame(pred_values, columns=output_cols)
    pred_df[['helical_layer_count', 'hoop_layer_count', 'doily_layers']] = np.ceil(pred_df[['helical_layer_count', 'hoop_layer_count', 'doily_layers']])
    pred_df[['helical_angle', 'liner_thickness']] = np.round(pred_df[['helical_angle', 'liner_thickness']], 2)

    st.subheader("Predicted values : ")
    st.write(pred_df)