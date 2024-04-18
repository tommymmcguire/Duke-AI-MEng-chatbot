from embed_query import embed_query
import json

#embed questions from 'questions_answers.jsonl' file and make new jsonl questions_embedded.jsonl file
def embed_questions():
    with open('data/questions_answers_3.jsonl', 'r') as file:
        with open('data/questions_embedded.jsonl', 'a') as file_embedded:
            count=0
            for line in file:

                count+=1
                if(count%10==0):
                    print(count)
                a=json.loads(line)
                question, answer = a[0]
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