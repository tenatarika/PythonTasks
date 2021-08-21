# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 03:37:44 2021

@author: Furcas
"""

import sys
import socket

import click
import psutil

def python_version():
    return sys.version_info

def ip_address():
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(socket.gethostname(), None)
    
    address_info = []
    
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))
    return address_info

def cpu_load():
    return psutil.cpu_percent(interval=0.1)

def ram_available():
    return psutil.virtual_memory().available

def ac_conncted():
    return psutil.sensors_battery().power_plugged()



@click.command(help="Отображает значения датчиков")
def show_sensors():
    click.echo("Python version: {0.major}.{0.minor}".format(python_version()))
    for address in ip_address():
        click.echo("IP-адреса {0[1]} ({0[0]})".format(address))
    click.echo("Загрузка ЦП: {:.1f}".format(cpu_load()))
    click.echo("Доступная память: {} Mib".format(ram_available() /1024**2))
    #click.echo("Кабель АС подключен {}".format(ac_conncted()))
    
    
if __name__ == '__main__':
    show_sensors()





