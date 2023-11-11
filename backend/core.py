from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.vectorstores import Pinecone
from langchain.prompts import PromptTemplate

INITIAL_PROMPT="""
Please write a cover letter for the following role: 

{role}

below is the resume of the applicant:

{resume}


Do not say that the applicant has some experience that is not on their resume! For example, if the job description mentions they're looking for MongoDB and the applicant doesn't have MongoDB in their resume, don't say they have experience with MongoDB. Instead, if they have some similar technology, say Cassandra, you may highlight that. 

Please make the cover letter around 200 words. You can omit any contact information above the introduction or below the signature. Please start the letter with "Dear Hiring Manager,"

Cover letter:
"""

def run_llm(role, resume):
    pt = PromptTemplate(template=INITIAL_PROMPT, input_variables=['role, resume'])
    llm = ChatOpenAI(verbose=True, temperature=0, model='gpt-4')
    chain = LLMChain(
        llm=llm, verbose=True, prompt=pt
    )

    return chain.run({ 
        'role': role,
        'resume': resume 
    })

if __name__=='__main__':
    print(run_llm())