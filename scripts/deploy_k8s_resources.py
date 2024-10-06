from k8s_manager import create_chrome_node_pod, create_test_controller_pod, wait_for_pods_ready

node_count = 2

for i in range(node_count):
    create_chrome_node_pod(f"node-{i+1}")

wait_for_pods_ready("chrome-node-node", node_count)

create_test_controller_pod()