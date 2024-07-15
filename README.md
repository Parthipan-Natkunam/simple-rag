### Simple Local RAG With Llama2
> An AI assistant that can answer your questions based on the sources from a local directory.   

- Powered by llama2.
##### Local Setup:
1. Install [Ollama](https://ollama.ai)
2. Pull & run the llama2 model locally
```bash
ollama run llama2
```
3. clone this repo, cd into the cloned repository & create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
4. Install the required packages
```bash
pip install -r requirements.txt
```
5. Create a directory named `retrievables` in the root of the project & add your document(s) into it.
6. Run the assistant
```bash
python3 main.py
```

>[!NOTE]
> Depending on your compute power this may take a while to index the documents and initialize the model.