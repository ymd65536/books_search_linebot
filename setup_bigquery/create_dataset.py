from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client(location="asia-northeast1", project="project-id")
dataset_id = "linebot2"
dataset = bigquery.Dataset(dataset_id)

dataset = client.create_dataset(dataset, timeout=30)
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

table_ref = dataset.table("data-table")
table = bigquery.Table(table_ref)
table = client.create_table(table)
