
# 1.6 workaround, run before any tasks, create the default tier
etcdctl set /calico/v1/policy/tier/default/metadata '{"order": 0}'

or

docker run --net=host quay.io/coreos/etcd etcdctl set /calico/v1/policy/tier/default/metadata '{"order": 0}'

- Binary dir:
  ```
  /opt/mesosphere/etc/dcos/network/cni
  ```

- Configuration
  ```
  /opt/mesosphere/active/cni/
  ```

- install etcd
  ```
	docker run --detach \
		--net=host \
		--name calico-etcd quay.io/coreos/etcd:v2.0.11 \
		--advertise-client-urls "http://m1.dcos:2379" \
		--listen-client-urls "http://m1.dcos:2379,http://127.0.0.1:2379"
  ```
