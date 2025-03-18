from AI import generate_text  # Importing function from test.py

def sentiment_analyzer(text_to_analyse):
    prompt = f"Analyze the sentiment of this text: {text_to_analyse}"
    sentiment_result = generate_text(prompt)  # Using function from AI.py
    return sentiment_result  # Return the result

print(sentiment_analyzer("I love this new technology!"))