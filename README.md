# 🔗 **LLMChainFusion**

This repository aims to develop a comprehensive collection of use cases for the LangChain framework. Our goal is to integrate Large Language Models (LLMs) with LangChain's interface, enabling seamless development and deployment of natural language processing (NLP) applications.

*** [Newest update] Check capacity of local GPU memory before building applications with a specific model.

* Nvidia NIM endpoints to build applications with Llama 3.1-405B.

* Langchain Ollama with latest Meta model [Llama 3.1](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/MODEL_CARD.md).


[OPTIONAL] You do not need to download model manually. Ollma code can download automatically. But you can download specific pretrained models compatible with your machine by your own as following:
- Llama 3.1 (8B params): ```ollama run llama3.1 ```
- Llama 3.1 (70B params):  ```ollama run llama3.1:70b```
- Llama 3.1 (405B params): ```ollama run llama3.1:405b```

For more information, check out official [Ollama repo](https://github.com/ollama/ollama/blob/main/README.md).

## Quick Installs [MANDATORY]

With pip:
```bash
pip install torch pynvml ollama
# If used Nvidia service.
pip install langchain-nvidia-ai-endpoints 
```

With conda:
```bash
conda install ollama -c conda-forge
# If used Nvidia service.
conda install langchain-nvidia-ai-endpoints -c conda-forge 
```

## Use Cases
- [x] Coding Assistant
- [x] Sentiment
- [x] Question/Answer
- [ ] On going 

## How to use:
- Run with terminal command:
```
python main.py [model_name]
```
For example:
```
python main.py llama3.1
python main_nim.py
```
- Run with GUI:
```
Coming soon
```

## 🙋🏻‍♂️ Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

## 🏆 Contributors

<a href="https://github.com/bradduy">
  <img src="https://avatars.githubusercontent.com/u/33892919?v=4" style="border-radius: 50%; width: 50px; height: 50px; object-fit: cover;" alt="LLMChainFusion contributors">
</a>