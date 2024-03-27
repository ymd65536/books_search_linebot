import os
from lib import create_secret

project_id = os.environ.get("PROJECT_ID", None)

if project_id is None:
    raise ValueError("PROJECT_ID is not set")
else:

    try:
        create_secret.create_secret(
            project_id, os.environ.get("PROJECT_ID", None)
        )
        create_secret.create_secret(
            project_id, os.environ.get("BIGQUERY_DATASET", None)
        )
        create_secret.create_secret(
            project_id, os.environ.get("BIGQUERY_TABLE", None)
        )
        create_secret.create_secret(
            project_id, os.environ.get("USE_CHAT_MODEL_NAME", "text-bison-32k@002")
        )
        create_secret.create_secret(
            project_id, os.environ.get("USE_EMBEDDING_MODEL_NAME", "textembedding-gecko@latest")
        )
    except Exception as e:
        print(e)
