from google.cloud import secretmanager


def create_secret(project_id: str, secret_id: str) -> secretmanager.CreateSecretRequest:
    """
    シークレットの作成
    """

    client = secretmanager.SecretManagerServiceClient()
    parent = f"projects/{project_id}"

    response = client.create_secret(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"replication": {"automatic": {}}},
        }
    )

    print(f"Created secret: {response.name}")
