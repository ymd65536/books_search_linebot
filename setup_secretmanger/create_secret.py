import os
from lib import create_secret, set_secret

project_id = os.environ.get("PROJECT_ID", None)

if project_id is None:
    raise ValueError("PROJECT_ID is not set")
else:

    try:
        create_secret.create_secret(
            project_id,
            "PROJECT_ID"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "PROJECT_ID",
            os.environ.get("PROJECT_ID", None)
        )
        print(secret_path)

        create_secret.create_secret(
            project_id,
            "BIGQUERY_DATASET"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "BIGQUERY_DATASET",
            os.environ.get("BIGQUERY_DATASET", None)
        )
        print(secret_path)

        create_secret.create_secret(
            project_id,
            "BIGQUERY_TABLE"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "BIGQUERY_TABLE",
            os.environ.get("BIGQUERY_TABLE", None)
        )
        print(secret_path)

        create_secret.create_secret(
            project_id,
            "USE_CHAT_MODEL_NAME"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "USE_CHAT_MODEL_NAME",
            os.environ.get("USE_CHAT_MODEL_NAME", None)
        )
        print(secret_path)

        create_secret.create_secret(
            project_id,
            "USE_EMBEDDING_MODEL_NAME"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "USE_EMBEDDING_MODEL_NAME",
            os.environ.get("USE_EMBEDDING_MODEL_NAME", None)
        )
        print(secret_path)

        create_secret.create_secret(
            project_id,
            "CHANNEL_ACCESS_TOKEN"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "CHANNEL_ACCESS_TOKEN",
            os.environ.get("CHANNEL_ACCESS_TOKEN", None)
        )
        print(secret_path)

        create_secret.create_secret(
            project_id,
            "CHANNEL_SECRET"
        )
        secret_path = set_secret.add_secret_version(
            project_id,
            "CHANNEL_SECRET",
            os.environ.get("CHANNEL_SECRET", None)
        )
        print(secret_path)
    except Exception as e:
        print(e)
