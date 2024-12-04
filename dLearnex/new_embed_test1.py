# import numpy as np
# from tensorflow.keras.models import load_model

# # Load the trained model
# model = load_model('C:/Users/HP/django_learnex_1/dLearnex/dLearnex/recommendation_model.h5')

# # List all model layers to find the correct embedding layer
# for layer in model.layers:
#     print(layer.name)

# # Retrieve channel embeddings from the model
# channel_embedding_layer = model.get_layer('embedding_1')  # The channel embedding layer
# channel_embeddings = channel_embedding_layer.get_weights()[0]  # Channel embeddings matrix

# print("Channel Embeddings Shape:", channel_embeddings.shape)

# # Function to create a new user embedding dynamically
# def create_user_embedding(preferred_channels, scores):
#     """
#     Generate a dynamic user embedding for a new user.
    
#     Args:
#         preferred_channels (list): List of channel IDs the user prefers.
#         scores (list): Scores the user assigns to these channels.

#     Returns:
#         np.array: A new user embedding based on preferences.
#     """
#     # Normalize scores to sum to 1 (optional)
#     scores = np.array(scores)
#     normalized_scores = scores / np.sum(scores)

#     # Get embeddings for preferred channels
#     embeddings = np.array([channel_embeddings[channel_id] for channel_id in preferred_channels])

#     # Create user embedding as a weighted average of channel embeddings
#     user_embedding = np.dot(normalized_scores, embeddings)
#     return user_embedding

# # Function to predict scores for the new user
# def predict_score_for_new_user(preferred_channels, scores, target_channel_id):
#     """
#     Predict a score for a new user for a given channel.

#     Args:
#         preferred_channels (list): List of channel IDs the user prefers.
#         scores (list): Scores the user assigns to these channels.
#         target_channel_id (int): The ID of the target channel.

#     Returns:
#         float: Predicted score for the user and target channel.
#     """
#     # Create the new user embedding
#     user_embedding = create_user_embedding(preferred_channels, scores)

#     # Get the embedding of the target channel
#     target_channel_embedding = channel_embeddings[target_channel_id]

#     # Concatenate user and target channel embeddings
#     combined_input = np.expand_dims(np.concatenate([user_embedding, target_channel_embedding]), axis=0)  # Shape: (1, 100)

#     # Pass the combined input through the model layers step by step
#     x = model.get_layer('dense')(combined_input)  # Dense layer 1
#     x = model.get_layer('dense_1')(x)            # Dense layer 2
#     x = model.get_layer('dense_2')(x)            # Dense layer 3
#     prediction = model.get_layer('dense_3')(x)   # Final output layer

#     return prediction.numpy()[0][0]

# # Example usage
# if __name__ == "__main__":
#     # Example user inputs
#     preferred_channels = [2, 5, 8]  # Channel IDs user prefers
#     scores = [4, 2, 3]  # Scores user gives to these channels

#     # Predict score for a new channel
#     target_channel_id = 10
#     predicted_score = predict_score_for_new_user(preferred_channels, scores, target_channel_id)

#     print(f"Predicted score for the new user on channel {target_channel_id}: {predicted_score}")