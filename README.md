# Duke AIPI MEng Masters Information Platform

## Project Description
This platform leverages a Mistral 7B large language model (LLM) that has been instruction fine-tuned to specifically address queries and provide detailed information about the Duke AIPI MEng Masters program. Utilizing the technique of Retrieval-Augmented Generation (RAG), the platform dynamically interacts with a comprehensive and curated corpus of the program's documentation. This advanced method allows the system to retrieve the most pertinent and current information from the corpus, augmenting the language model's responses to ensure they are both accurate and contextually relevant.

### How It Works

1. **Query Processing**: Users submit questions or requests related to the Duke AIPI MEng Masters program via the platform interface.
2. **Information Retrieval**: The Retrieval-Augmented Generation system initiates by querying a specialized retriever that searches through a detailed corpus specifically tailored to the Duke AIPI MEng program.
3. **Response Generation**: The retrieved content is then fed into the finetuned Mistral 7B LLM, which synthesizes the information and generates a comprehensive, clear, and contextually enriched response.
4. **Delivery**: The response is presented to the user, providing them with reliable and up-to-date information about the program.

This integration of fine-tuned language modeling with retrieval-augmented generation techniques ensures that users not only receive generalized answers but also responses that are deeply rooted in the specific factual content of the Duke AIPI MEng Masters program.


### Technical Details

#### Large Language Model (LLM) - Mistral 7B
The Mistral 7B model is a type of transformer-based model that has been trained on a diverse range of internet text. For this project, the model has been instruction fine-tuned to handle question-answering and summarization tasks. Therefore, the model doesn't just generate text based on the input but understands and executes a range of instructed tasks, such as answering queries directly, summarizing information, or even comparing different aspects of the program. This makes the platform more intuitive and effective for users seeking specific information.

#### Retrieval-Augmented Generation (RAG)
Retrieval-Augmented Generation enhances the capabilities the language model by combining it with a retrieval system. In the platform, RAG involves the language model querying a retriever component that searches a pre-built corpus containing detailed information about the Duke AIPI MEng program. The retriever fetches the most relevant documents or snippets of information, which are then fed back into the language model. This combination allows the model to generate responses that are not only contextually aware but also deeply informed by the specific data contained in the program’s corpus.


## Getting Started

### Installation - Steps to Run this Locally

Clone the repository to your local machine:
```
git clone https://github.com/tommymmcguire/Duke-AI-MEng-chatbot.git
```
```
cd DUKE-RAG
```

Install the required Python libraries:
```
make install
```
OR
```
pip install -r requirements.txt
```
