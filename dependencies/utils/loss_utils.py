import tensorflow as tf
import numpy as np

from dependencies.constants import input_cols, output_cols
from dependencies.utils.scaler_utils import inverse_scale, tf_cast
from dependencies.load_scaler_objects import x_scaler, y_scaler

layer_thickness_hoop = tf.constant(0.2)
layer_thickness_helical = tf.constant(0.45)
layer_thickness_doily = tf.constant(0.5)

def physics_loss(x_input, y_pred):
    # Cast all inputs to float32 (or match your model's dtype)
    x_input = tf_cast(inverse_scale(x_input, as_tensor = True, scaler=x_scaler))
    y_pred = tf_cast(inverse_scale(y_pred, as_tensor = True, scaler= y_scaler))
    
    # Access features using indices
    diameter = x_input[:, input_cols.index('diameter')]
    liner_thickness = y_pred[:, output_cols.index('liner_thickness')]
    sigma_liner = x_input[:, input_cols.index('ult_tensile_strength')]
    n_hoop = y_pred[:, output_cols.index('hoop_layer_count')]
    sigma_cf = x_input[:, input_cols.index('tensile_str')]
    n_helical = y_pred[:, output_cols.index('helical_layer_count')]
    helical_angle = y_pred[:, output_cols.index('helical_angle')]
    n_doily = y_pred[:, output_cols.index('doily_layers')]
    input_brust_pressure = x_input[:, input_cols.index('bust_pressure')]
    

    liner_pressure = liner_thickness * sigma_liner
    hoop_pressure = layer_thickness_hoop * sigma_cf * n_hoop 
    helical_pressure = layer_thickness_helical * sigma_cf * n_helical * (tf.cos(tf.cast(helical_angle * np.pi / 180.0, tf.float32)) ** 2)
    doily_pressure = layer_thickness_doily * sigma_cf * n_doily

    burst_pressure = 2 * (liner_pressure + hoop_pressure + helical_pressure + doily_pressure) / diameter

    loss = tf.reduce_mean(tf.abs(burst_pressure - input_brust_pressure))
    return loss

def data_loss(y_true, y_pred):
    # y_pred = inverse_scale(y_pred, as_tensor = True)
    # y_ture = inverse_scale(y_true, as_tensor = True)
    loss = tf.reduce_mean(tf.abs(y_true - y_pred))
    return loss

def loss_function(x_input, y_true, y_pred, physics_loss_factor=0.2):
    return data_loss(y_true, y_pred) + physics_loss_factor * physics_loss(x_input, y_pred)


