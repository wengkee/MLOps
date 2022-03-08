
# Install MinIO

## Prerequisite
* Install `kubectl` and `oc` CLI
* Login to the OpenShift cluster

## Instructions
* Install MinIO using kubectl with Kustomize

        cd base
        kubectl apply -k .

* Get the URL

        oc get route