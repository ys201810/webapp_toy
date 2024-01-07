# 0. change directory
cd ../

# 1. login aws
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/q9x9g6a9

# 2. docker build
docker build -t ecr_work .

# 3. attach tag name to docker image
docker tag ecr_work:latest public.ecr.aws/q9x9g6a9/ecr_work:latest

# 4. push docker image to ecr
docker push public.ecr.aws/q9x9g6a9/ecr_work:latest
