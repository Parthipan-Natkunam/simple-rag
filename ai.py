from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama2", request_timeout=300.0)

def get_llm():
    return llm