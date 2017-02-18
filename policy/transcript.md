demo prereqs:

export ETCD_ENDPOINTS=http://m1.dcos:2379
# http://mesos.apache.org/documentation/latest/cni/#accessing-container-network-namespace

# Demo: Modify default pools
calicoctl get ippool -o yaml > pools.yaml
# (open file and change)
calicoctl apply -f pools.yaml


# Launch App 1 & app 2
app-a-1.json
app-a-2.json

# Enter app's 1's NS
ls /var/run/mesos/isolators/network/cni/
sudo ln -s ls /var/run/mesos/isolators/network/cni/<tab>/ns /var/run/netns/a1

# Demo: Inspect application namespace:
sudo ip netns exec a1 ifconfig

# Demo: Apps in same network can connect
sudo ip netns exec a1 curl <a1-ip>

# Demo: Add policy to block that connection
calicoctl apply -f block-from-two.yaml
sudo ip netns exec a1 curl <a1-ip>

# Demo: Remove that policy, connection restored
calicoctl delete -f block-from-one.yaml

# Kill app 2 for simplicity

# Show how we created second calico network
# calico network maps to a profile, so print profiles.

# Demo: Apps in different networks can't
Launch app-b-2.json

# curl from one to other, can't
# allow curls, still can't ping
calicoctl apply -f policy/allow-curl.yaml

# delete
calicoctl delete -f policy/allow-curl.yaml

# allow pings, can't curl
calicoctl apply -f policy/allow-ping.yaml
