from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama2", request_timeout=300.0)

def getLLM():
    return llm