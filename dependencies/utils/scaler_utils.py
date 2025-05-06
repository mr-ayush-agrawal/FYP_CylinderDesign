import tensorflow as tf
from dependencies.load_scaler_objects import y_scaler

def inverse_scale(scaled_data, as_tensor=False, scaler=y_scaler):
    if as_tensor:
        # build tf constants matching the scaler
        scale = tf.constant(scaler.scale_, dtype=tf.float32)
        mean = tf.constant(scaler.mean_, dtype=tf.float32)
        # (batch_size, dims) * (dims,) + (dims,) → (batch_size, dims)
        return scaled_data * scale + mean
    else:
        # fallback to numpy inverse
        return scaler.inverse_transform(scaled_data)
    
def tf_cast(x):
    return tf.cast(x, tf.float32)