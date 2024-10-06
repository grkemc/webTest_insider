from kubernetes import client, config
import time

config.load_kube_config()

v1 = client.CoreV1Api()

def create_chrome_node_pod(node_name):
    pod = client.V1Pod(
        metadata=client.V1ObjectMeta(name=f"chrome-node-{node_name}"),
        spec=client.V1PodSpec(
            containers=[client.V1Container(
                name="selenium-chrome",
                image="seleniarm/standalone-chromium:latest",
                ports=[client.V1ContainerPort(container_port=4444)]
            )]
        )
    )
    api_response = v1.create_namespaced_pod(namespace="default", body=pod)
    print(f"Pod {node_name} created. Status: {api_response.status.phase}")

def create_test_controller_pod():
    pod = client.V1Pod(
        metadata=client.V1ObjectMeta(name="test-controller"),
        spec=client.V1PodSpec(
            containers=[client.V1Container(
                name="test-runner",
                image="gorkemc/webtest_insider:latest",
                env=[client.V1EnvVar(name="SELENIUM_SERVER_URL", value="http://chrome-node:4444/wd/hub")],
                command=["sh", "-c", "pytest --base-url=$SELENIUM_SERVER_URL"]
            )]
        )
    )
    api_response = v1.create_namespaced_pod(namespace="default", body=pod)
    print("Test Controller Pod created.")

def is_pod_ready(pod_name):
    pod = v1.read_namespaced_pod(name=pod_name, namespace="default")
    return pod.status.phase == "Running"

def wait_for_pods_ready(pod_prefix, node_count):
    for i in range(node_count):
        pod_name = f"{pod_prefix}-{i+1}"
        while not is_pod_ready(pod_name):
            print(f"Waiting for {pod_name} to be ready...")
            time.sleep(5)
        print(f"{pod_name} is ready!")