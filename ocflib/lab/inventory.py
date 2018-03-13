from os import listdir
from os import mkdir
from os.path import isdir

from yaml import safe_dump
from yaml import safe_load

INVENTORY_FOLDER = '/home/c/ca/carterturn/inventory'


def get_devices():
    devices = []
    for host_inventory_file in listdir(INVENTORY_FOLDER):
        with open(INVENTORY_FOLDER + '/{}'.format(host_inventory_file)) as f:
            host_inventory = safe_load(f)
            if 'devices' in host_inventory.keys():
                devices.extend(host_inventory['devices'])
    return devices


def add_host_inventory(host_inventory):
    if 'hostname' not in host_inventory.keys():
        return
    if not isdir(INVENTORY_FOLDER):
        mkdir(INVENTORY_FOLDER)
    with open(INVENTORY_FOLDER + '/{}.yaml'.format(host_inventory['hostname']), 'w+') as f:
        f.write(safe_dump(host_inventory))
