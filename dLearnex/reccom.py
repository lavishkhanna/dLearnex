from tensorflow.keras.models import load_model
import numpy as np

# Load the pre-trained model
model = load_model('dLearnex/recommendation_model.h5')

def func_pred(user_id, channel_id):
    pred_score = model.predict([np.array([user_id]), np.array([channel_id])])
    print(f"Predicted score for User {user_id} and Channel {channel_id}: {pred_score}")
    return pred_score

# Example usage:
# func_pred(1, 2)
# func_pred(7, 3)
