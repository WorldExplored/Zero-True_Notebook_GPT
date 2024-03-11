from zero_true import TextInput, Slider, Button, Text, Layout, Row, Column
import openai

# Configure OpenAI with your API key
OPENAI_API_KEY = 'BLANK'
openai.api_key = OPENAI_API_KEY


# Initialize the text input, slider, and button
prompt_input = TextInput(id="prompt_input", label="Enter your prompt", placeholder="Type something...", str = '')
temperature_slider = Slider(id="temperature_slider", min=0, max=1, step=0.01, value=0.5, label="Temperature")
generate_button = Button(id="generate_button", text="Generate", value=False, disabled = "False", str = 'click')  # Button starts as not clicked
response_text = Text(id="response_text", text="Response will appear here", color="info")


def generate_text(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the correct model identifier without the version suffix
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            temperature=temperature_slider.value
        )
        generated_text = response.choices[0].message['content'].strip()
        return generated_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error generating text."


# Layout definition
layout = Layout(rows=[
    Row(components=[prompt_input.id]),
    Row(components=[temperature_slider.id]),
    Row(components=[generate_button.id]),
    Row(components=[response_text.id])
])


prompt =  prompt_input.value

if (generate_button.value):
    print(generate_text(prompt))
