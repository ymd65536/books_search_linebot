# BigQueryにデータをセットする

## SetUp

```bash
export PROJECT_ID=project_id # GCPのプロジェクトID
export BIGQUERY_DATASET=linebot2
export BIGQUERY_TABLE=data-table
export USE_CHAT_MODEL_NAME=gemini-1.0-pro-001
export USE_EMBEDDING_MODEL_NAME=textembedding-gecko@latest
pip install --user --no-cache-dir --upgrade pip && pip install --user --no-cache-dir -r requirements.txt
```
