docker build -t registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:3.0.1 -f Dockerfile src/
docker tag registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:3.0.1 registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:latest
docker login --username=aliyun4438435934 registry.cn-hangzhou.aliyuncs.com

docker push registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:3.0.1
docker push registry.cn-hangzhou.aliyuncs.com/zhao-leo/pythonadmin:latest