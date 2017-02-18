

0. prereqs
m1:
docker pull etcd

a's:
docker pull calico/calico-dcos:v0.3.1
docker pull calico/node:v0.22.0
docker pull calico/node-libnetwork:v0.9.0

etcdctl --endpoints=http://m1.dcos:2379 set /calico/v1/policy/tier/default/metadata '{"order": 0}'
docker network create --driver=calico --ipam-driver=calico calico3
./calicoctl profile calico rule add inbound allow from tag .....

install etcd
	docker run --detach \
		--net=host \
		--name calico-etcd quay.io/coreos/etcd:v2.0.11 \
		--advertise-client-urls "http://m1.dcos:2379" \
		--listen-client-urls "http://m1.dcos:2379,http://127.0.0.1:2379"


# Configuration
/opt/mesosphere/etc/dcos/network/cni

# Bin
/opt/mesosphere/active/cni/
