from jsonformer import Jsonformer
from transformers import AutoModelForCausalLM, AutoTokenizer


model = AutoModelForCausalLM.from_pretrained("databricks/dolly-v2-3b")
tokenizer = AutoTokenizer.from_pretrained("databricks/dolly-v2-3b")

json_schema = {
    "type": "object",
    "properties": {
        "direction": {"type": "string"},
        "angle": {"type": "number"},
        "time": {"type": "number"}
    }
}

while True:

    text = input("Enter the direction, angle, and time you want the rover to move:  ")

    prompt = f"Generate navigation instructions based on the following schema and user input:  user input: {text} schema: "
    jsonformer = Jsonformer(model, tokenizer, json_schema, prompt)
    generated_data = jsonformer()

    print(generated_data)
