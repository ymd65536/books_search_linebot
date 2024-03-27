import os

from langchain_google_vertexai import VertexAI
from langchain.chains import RetrievalQA

from langchain_google_vertexai import VertexAIEmbeddings

from langchain.vectorstores.utils import DistanceStrategy
from langchain_community.vectorstores import BigQueryVectorSearch

NUMBER_OF_RESULTS = 3
PROJECT_ID = os.environ.get("PROJECT_ID", "")
REGION = "asia-northeast1"

BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "")
BIGQUERY_TABLE = os.environ.get("BIGQUERY_TABLE", "")

USE_LLM_MODEL_NAME = os.environ.get("USE_CHAT_MODEL_NAME", "text-bison-32k@002")
USE_EMBEDDING_MODEL_NAME = os.environ.get(
    "USE_EMBEDDING_MODEL_NAME", "textembedding-gecko@latest")

embedding = VertexAIEmbeddings(
    model_name=USE_EMBEDDING_MODEL_NAME, project=PROJECT_ID
)

store = BigQueryVectorSearch(
    project_id=PROJECT_ID,
    dataset_name=BIGQUERY_DATASET,
    table_name=BIGQUERY_TABLE,
    location=REGION,
    embedding=embedding,
    distance_strategy=DistanceStrategy.EUCLIDEAN_DISTANCE,
)

retriever = store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": NUMBER_OF_RESULTS})

chat = VertexAI(
    model_name=USE_LLM_MODEL_NAME, temperature=0, max_tokens=2048
)
qa_chain = RetrievalQA.from_chain_type(
    llm=chat, chain_type="stuff",
    retriever=retriever
)

prompt = """
タイトルにChatGPTが含まれる本を教えてください。

回答方法
番号で箇条書き
リンクや値段を含める
"""

res = qa_chain.invoke(prompt)

ai_response = f"""

質問内容:
{res['query']}

回答:
{res['result']}

"""

print(ai_response)
