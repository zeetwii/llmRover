from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.experimental.llms import JsonFormer


hf_model = pipeline(
    "text-generation", model="cerebras/Cerebras-GPT-590M", max_new_tokens=200
)


json_schema = {
    "type": "object",
    "properties": {
        "direction": {"type": "string"},
        "angle": {"type": "number"},
        "time": {"type": "number"}
    }
}



json_former = JsonFormer(json_schema=json_schema, pipeline=hf_model)


prompt = 'Go forward at 15 degrees for 9 seconds'

results = json_former.predict(prompt, stop=["Observation:", "Human:"])
print(results)



