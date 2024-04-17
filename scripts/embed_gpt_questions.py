from embed_query import embed_query
import json

#embed questions from 'questions_answers.jsonl' file and make new jsonl questions_embedded.jsonl file
def embed_questions():
    with open('data/questions_answers.jsonl', 'r') as file:
        with open('data/questions_embedded.jsonl', 'w') as file_embedded:
            count=0
            for line in file:
                count+=1
                if(count%10==0):
                    print(count)
                question, answer = json.loads(line)
                embedding = embed_query(question)
                data = {
                    'question': question,
                    'embedding': embedding,
                    'answer': answer
                }
                json.dump(data, file_embedded)
                file_embedded.write('\n')
if __name__ == "__main__":
    embed_questions()