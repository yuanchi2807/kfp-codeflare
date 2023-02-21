from kubernetes import client, config
from openshift.dynamic import DynamicClient
import yaml

def launch_ray():
    loadedconf = config.load_incluster_config()
    api_client = client.ApiClient(configuration=loadedconf)
    v1 = client.CoreV1Api(api_client)

    dynamic_client = DynamicClient(api_client)
    v1_deployment = dynamic_client.resources.get(api_version='v1', kind='Deployment')
    with open("./codeflare-deployment_1.yml", "r") as stream:
        deployment_data = yaml.safe_load(stream)
    resp = v1_deployment.create(body=deployment_data, namespace='workflows-dev')
    print(resp)
    v1_svc = dynamic_client.resources.get(api_version='v1', kind='Service')
    with open("./codeflare-deployment_2.yml", "r") as stream:
        svc_data = yaml.safe_load(stream)
    resp = v1_svc.create(body=svc_data, namespace='workflows-dev')
    print(resp)
    with open("./codeflare-deployment_3.yml", "r") as stream:
        deployment_data = yaml.safe_load(stream)
    resp = v1_deployment.create(body=deployment_data, namespace='workflows-dev')
    print(resp)

if __name__ == "__main__":
    launch_ray()
    from time import sleep
    sleep(60)


