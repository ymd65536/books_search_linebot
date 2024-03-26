# Setup

## docker

```bash
gcp_project=`gcloud config list --format 'value(core.project)'` && echo $gcp_project
image_name=linebot2

gcloud auth login
gcloud config set project $gcp_project

gcloud auth configure-docker asia-northeast1-docker.pkg.dev
gcp_project_id=`gcloud projects list --format 'value(PROJECT_ID)' | grep line` && echo $gcp_project_id
gcloud artifacts repositories create $image_name --location=asia-northeast1 --repository-format=docker --project=$gcp_project_id

docker rmi asia-northeast1-docker.pkg.dev/$gcp_project_id/$image_name/$image_name && docker rmi $image_name
docker build . -t $image_name --platform linux/amd64
docker tag $image_name asia-northeast1-docker.pkg.dev/$gcp_project_id/$image_name/$image_name && docker push asia-northeast1-docker.pkg.dev/$gcp_project_id/$image_name/$image_name":latest"
```
