from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from auditrail.sdk import Auditrail
from auditrail.sdk.decorators import task
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


auditrail_processor = Auditrail.get_default_span_processor(disable_batch=True)

console_processor = SimpleSpanProcessor(ConsoleSpanExporter())

Auditrail.init(processor=[auditrail_processor, console_processor])


@task(name="joke_creation", version=1)
def create_joke():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Tell me a joke about opentelemetry multiple span processors"}],
    )

    result = completion.choices[0].message.content
    print(result)
    return result


def main():
    create_joke()


if __name__ == "__main__":
    main()
