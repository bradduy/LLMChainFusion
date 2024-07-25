# import torch
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

task = 'sentiment'

template = """
    Answer: {input}
    """
    
if task.lower() == 'sentiment':
    template = """
    Interprete the text and evaluate the text.
    sentiment: is the text in a positive, neutral or negative sentiment?
    subject: What subject is the text about? Use exactly one word.

    Format the output as JSON with the following keys:
    sentiment
    subject

    Answer: {input}
    """
user_input = 'I study Tiramisu has been 4 years.'

prompt_template = PromptTemplate.from_template(template=template)
chain = LLMChain(llm=Ollama(model="llama2"), prompt=prompt_template)
if task.lower() == 'sentiment':
    out = chain.invoke(user_input)
    out = out['text']
else:
    user_input = 'which is sweeter: Tiramisu or candy?'
    out = chain.predict(input=user_input)

print(out)