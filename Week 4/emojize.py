# Import the ncessary module
import emoji

# Get the user's input.
message = input('Input: ').lower().strip()

# Convert the message
message_converted = emoji.emojize(message, language='alias')

# Output the message.
print("Ouput:", message_converted)
