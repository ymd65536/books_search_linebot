from google.cloud import bigquery

project_id = "project_id"
client = bigquery.Client(location="asia-northeast1", project=project_id)

dataset_id = f"{project_id}.linebot2"
dataset = bigquery.Dataset(dataset_id)
dataset = client.create_dataset(dataset, timeout=30)

table_ref = dataset.table("data-table")
table = bigquery.Table(table_ref)
table = client.create_table(table)

print(f"Created dataset {client.project}.{dataset.dataset_id}")
print(f"Table Name:{table.table_id}")
