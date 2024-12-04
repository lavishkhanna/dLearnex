

from users.models import Channel  # Assuming Channel is the model name

def get_channel_ids(channel_names):
    channel_ids = {}  # Dictionary to store channel_name -> channel_id mapping
    
    for name in channel_names:
        try:
            # Query the database for the channel by name
            channel = Channel.objects.get(channel_name=name)  # Ensure 'channel_name' is the column name in your table
            
            # Store the result in the dictionary
            channel_ids[name] = channel.channel_id
        
        except Channel.DoesNotExist:
            channel_ids[name] = None  # If the channel does not exist, store None
            
    return channel_ids







