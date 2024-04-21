## Deploying Autonity Container with Kubernetes

1. **Prepare Kubernetes Manifest File**: Create a Kubernetes manifest file, typically with a `.yaml` extension, that describes the Autonity deployment and service configurations.

2. **Write Deployment Configuration**:
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: autonity
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: autonity
      template:
        metadata:
          labels:
            app: autonity
        spec:
          containers:
          - name: autonity
            image: ghcr.io/autonity/autonity:latest
            ports:
            - containerPort: 8545
            - containerPort: 8546
            - containerPort: 30303
            - containerPort: 20203
            - containerPort: 6060
            args:
            - "--datadir"
            - "/autonity-chaindata"
            - "--piccadilly"
            - "--http"
            - "--http.addr=0.0.0.0"
            - "--http.api=aut,eth,net,txpool,web3,admin"
            - "--http.vhosts=*"
            - "--ws"
            - "--ws.addr=0.0.0.0"
            - "--ws.api=aut,eth,net,txpool,web3,admin"
            - "--nat"
            - "extip:<IP_ADDRESS>"
            - "--consensus.nat"
            - "<CONSENSUS_NAT>"
            - "--consensus.port"
            - "<CONSENSUS_PORT_NUMBER>"
          volumes:
          - name: autonity-chaindata
            persistentVolumeClaim:
              claimName: autonity-chaindata
    ```
    - Replace `<IP_ADDRESS>`, `<CONSENSUS_NAT>`, and `<CONSENSUS_PORT_NUMBER>` with appropriate values.

3. **Write Service Configuration**:
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: autonity
    spec:
      selector:
        app: autonity
      ports:
      - protocol: TCP
        port: 8545
        targetPort: 8545
      - protocol: TCP
        port: 8546
        targetPort: 8546
      - protocol: TCP
        port: 30303
        targetPort: 30303
      - protocol: TCP
        port: 20203
        targetPort: 20203
      - protocol: TCP
        port: 6060
        targetPort: 6060
    ```

4. **Apply Configuration**: Apply the Kubernetes manifest file using the `kubectl apply -f your-manifest.yaml` command.

5. **Verify Deployment**: Use `kubectl get pods` to check the status of the Autonity deployment and ensure that it's running without errors.

6. **Access Autonity**: If needed, expose the Autonity service outside the Kubernetes cluster using an appropriate method like NodePort, LoadBalancer, or Ingress.

7. **Monitor Logs**: Monitor the logs of the Autonity container using `kubectl logs autonity-[pod-id]` to troubleshoot any issues.
