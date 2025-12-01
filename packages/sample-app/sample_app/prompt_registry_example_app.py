import os
from openai import OpenAI


from auditrail.sdk import Auditrail
from auditrail.sdk.decorators import task, workflow
from auditrail.sdk.prompts import get_prompt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

Auditrail.init(app_name="prompt_registry_example_app")


@task(name="generate_joke")
def generate_pirate_joke():
    prompt_args = get_prompt(key="joke_generator", variables={"persona": "pirate"})
    completion = client.chat.completions.create(**prompt_args)

    return completion.choices[0].message.content


@workflow(name="joke_generation_using_prompt_registry")
def generate_joke():
    print(generate_pirate_joke())


generate_joke()
