from google.cloud import secretmanager
import google_crc32c  # type: ignore


def add_secret_version(
    project_id: str, secret_id: str, payload: str
) -> secretmanager.SecretVersion:
    """
    Add a new secret version to the given secret with the provided payload.
    """

    client = secretmanager.SecretManagerServiceClient()
    parent = client.secret_path(project_id, secret_id)

    payload_bytes = payload.encode("UTF-8")
    crc32c = google_crc32c.Checksum()
    crc32c.update(payload_bytes)

    response = client.add_secret_version(
        request={
            "parent": parent,
            "payload": {
                "data": payload_bytes,
                "data_crc32c": int(crc32c.hexdigest(), 16),
            },
        }
    )

    print(f"Added secret version: {response.name}")
    return response.name
