from transformers import pipeline, logging
from zero_true import TextInput, Slider, Button, Text, Layout, Row, Column
import torch

# Ignore warnings for a cleaner output
logging.set_verbosity(logging.CRITICAL)

# Initialize the text input, slider, and button
prompt_input = TextInput(id="prompt_input", label="Enter your prompt", placeholder="Type something...")
temperature_slider = Slider(id="temperature_slider", min=0, max=1, step=0.01, value=0.5, label="Temperature")
generate_button = Button(id="generate_button", text="Generate", value=False)  # Ensure the button starts as not clicked
response_text = Text(id="response_text", text="Response will appear here", color="info")

# Assuming 'model' and 'tokenizer' are defined elsewhere in your code

# Function to generate text
def generate_text():
    prompt = prompt_input.value
    temperature = temperature_slider.value
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Prepare the prompt
    prompt_formatted = f"<s>[INST] {prompt} [/INST]"
    
    # Initialize the pipeline with the appropriate device
    pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200, device=device)
    result = pipe(prompt_formatted, max_length=50, num_return_sequences=1, temperature=temperature)
    
    # Update the response text
    generated_text = result[0]['generated_text']
    response_text.text = generated_text

# Function or mechanism to watch for button value changes is needed here
# In the absence of explicit event binding in Zero-True, one must use the framework's way of handling state changes

# Layout definition
layout = Layout(rows=[
    Row(components=[prompt_input.id]),
    Row(components=[temperature_slider.id]),
    Row(components=[generate_button.id]),
    Row(components=[response_text.id])
])

# Display the layout
#zt.display(layout)
