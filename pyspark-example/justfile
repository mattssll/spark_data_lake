image_name := 'pyspark-example:dev'
google_service_account_path := './google_sa.json'
bucket_name := 'vectux-bucket'
postgres_user := ''
postgres_password := ''
postgres_host := ''
postgres_port := ''
postgres_db_name := ''
table_name := ''

build:
    docker build -t {{image_name}} .

run:
    docker run --mount type=bind,source="$(pwd)",target=/opt/application \
        -e SERVICE_ACCOUNT_PATH={{google_service_account_path}} \
        -e BUCKET_NAME={{bucket_name}} \
        {{image_name}} driver local:///opt/application/main.py

shell:
    docker run -it {{image_name}} /opt/spark/bin/pyspark 


