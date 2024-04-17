from dotenv import load_dotenv
from openai import OpenAI
import os
import json
from tqdm import tqdm

#reads in chunks from .txt file seperated by '===' and returns a list of chunks
def read_chunks_from_file(file_path):
    chunks = []
    with open(file_path, 'r') as file:
        chunk = ''
        for line in file:
            if line == '===\n':
                chunks.append(chunk)
                chunk = ''
            else:
                chunk += line
    return chunks

# prompt gpt-4 with a chunk and query and return the response
def prompt_gpt4(chunk):
    load_dotenv()
    openai = OpenAI()
    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt_text = f"Given this information about Duke's AI MEng program: {chunk}\nPlease "
    prompt_text+="give 3 common questions that could be answered by the prompt, which are the most"
    prompt_text+="likely to be asked by a prospective student and give the very detailed"
    prompt_text+="answers to each question (include hyperlinks from prompt if useful) with a MANDATORY 'question:' and 'answer:' prefix for parsing."
    
    
    try:
        # Using the `openai.ChatCompletion.create` method to interact with GPT-4
        response = openai.chat.completions.create(
            model="gpt-4",  # Use the appropriate model, here it's gpt-4
            messages=[
                {"role": "user", "content": prompt_text}
            ]
            
        )
        #print(response)
        answer = response.choices[0].message.content
         # Extracting the text from the respo
        print(answer)
        return answer

    except Exception as e:
        return f"An error occurred: {str(e)}"
    

# a function to parse the response from gpt-4
def parse_response(response):
    questions = []
    answers = []
    response = response.split('Question:')
    for i in range(1, len(response)):
        question, answer = response[i].split('Answer:')
        questions.append(question.strip())
        answers.append(answer.strip())
    return questions, answers


#function to run through all the chunks and prompt gpt-4 with each chunk 
#and parse the responses and return the questions and answers
def run_through_chunks(chunks):
    questions = []
    answers = []
    for chunk in tqdm(chunks):
        try:
            response = prompt_gpt4(chunk)
            currentQuestions, currentAnswers = parse_response(response)
            # append the questions and answers to the lists so they make one list
            questions += currentQuestions
            answers += currentAnswers
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    return questions, answers

#function that saves the questions and answers to a json lines file
def save_to_json(questions, answers, file_path):
    with open(file_path, 'w') as file:
        for i in range(len(questions)):
            data = [
                questions[i],
                answers[i]
            ]
            json.dump(data, file)
            file.write('\n')


def main():
    chunks = read_chunks_from_file('data/dataNickC.txt')
    chunks+= read_chunks_from_file('data/data_nicks.txt')
    questions, answers = run_through_chunks(chunks)
    save_to_json(questions, answers, 'data/questions_answers.jsonl')
    
    # return response

if __name__ == "__main__":
    print(main())