service_nums =3

service_names = ['name1','name2','mame3']

router_ids = ["router1","router2","router3"]

subnet_ids = ['subnet41','subnet42','subnet43',
              'subnet51','subnet52','subnet53',
              'subnet61','subnet62','subnet63']

subnet4_ids = subnet_ids[0:len(subnet_ids)//len(router_ids)]
subnet5_ids = subnet_ids[len(subnet_ids)//len(router_ids):2*len(subnet_ids)//len(router_ids)]

# print(subnet4_ids)
merges_ids = [subnet4_ids,subnet5_ids]

def create_services(service_name,router_id,*args):
    print(args)

for i in range(service_nums-1):
    create_service = create_services(service_names[i],router_ids[i],merges_ids[i])


