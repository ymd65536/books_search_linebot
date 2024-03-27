import os

from langchain_google_vertexai import VertexAIEmbeddings
from langchain.vectorstores.utils import DistanceStrategy
from langchain_community.vectorstores import BigQueryVectorSearch

NUMBER_OF_RESULTS = 3
PROJECT_ID = os.environ.get("PROJECT_ID", "")
REGION = "asia-northeast1"

BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", "")
BIGQUERY_TABLE = os.environ.get("BIGQUERY_TABLE", "")

USE_LLM_MODEL_NAME = os.environ.get("USE_LLM_MODEL_NAME", "text-bison-32k@002")
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

all_texts = [
    "タイトル:「AWS認定 高度なネットワーキング専門知識」は2024/03/25に発売されます。本体価格は¥3,600です。リンク: https://www.ric.co.jp/book/new-publication/detail/2688",
    "タイトル:「Terraformの教科書」は2024年03月21日に発売されました。本体価格は¥3,980です。リンク: https://book.mynavi.jp/ec/products/detail/id=142721",
    "タイトル:「ChatGPT/LangChainによるチャットシステム構築[実践]入門」は2023年10月18日に発売されました。本体価格は¥3,000です。リンク: https://gihyo.jp/book/2023/978-4-297-13839-4",
    "タイトル:「Azure OpenAI ServiceではじめるChatGPT/LLMシステム構築入門」は2024年1月24日に発売されました。本体価格は¥3,200です。リンク: https://gihyo.jp/book/2024/978-4-297-13929-2"
]

metadatas = [{"len": len(t)} for t in all_texts]
store.add_texts(all_texts, metadatas=metadatas)

print("OK")
