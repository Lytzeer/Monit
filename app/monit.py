"""Monit module
Monit is a monitoring tool for linux machines
"""

import argparse
import socket
from contextlib import closing
import json
from uuid import uuid4
import time
from os import path, listdir, mkdir
from logging import info, basicConfig, DEBUG
import sys
import discord_alerts
import psutil


def check_cpu_usage():
    """Check the cpu usage"""
    usage = psutil.cpu_percent(1)
    print(f"CPU Usage: {usage}%")
    if 50.0 < str(usage) < 80.0:
        discord_alerts.cpu_alert(str(usage))
    elif usage > 80.0:
        discord_alerts.cpu_alert_critical(str(usage))
    return usage


def check_ram_usage():
    """Check the ram usage"""
    usage = psutil.virtual_memory().percent
    print(f"RAM Usage: {usage}%")
    if 50.0 < usage < 80.0:
        discord_alerts.ram_alert(str(usage))
    elif usage > 80.0:
        discord_alerts.ram_alert_critical(str(usage))
    return usage


def check_ports_open(host, port):
    """Check if a port is open"""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print(f"Port {port} is open")
            return True
        print(f"Port {port} is closed")
        return False


def check_disk_usage():
    """Check the disk usage"""
    usage = psutil.disk_usage("/")[3]
    print(f"Disk Usage: {usage}%")
    if 50.0 < usage < 80.0:
        discord_alerts.disk_alert(str(usage))
    elif usage > 80.0:
        discord_alerts.disk_alert_critical(str(usage))
    return usage


def create_rapport(cpu_usage, ram_usage, disk_usage, ports_open):
    """Create a rapport file"""
    data = {
        "id": str(uuid4()),
        "data": {
            "time": time.strftime("%d/%m/%Y %H:%M:%S"),
            "cpu": cpu_usage,
            "ram": ram_usage,
            "disk": disk_usage,
            "ports": ports_open,
        },
    }
    json_data = json.dumps(data)
    with open(f"/var/monit/{data['id']}.json", "w", encoding="utf-8") as f:
        f.write(json_data)
        info(f"Report created with id {data['id']}")


def create_rapport_file(report_id: str):
    """Create a rapport file"""
    mkdir("/var/monit/" + report_id)


def check(config):
    """Check the machine"""
    host_ip = config["host"]
    ports = config["ports"]
    cpu = check_cpu_usage()
    ram = check_ram_usage()
    port_for_json = {}
    for p in ports:
        port_for_json[p] = check_ports_open(host_ip, p)
    disk = check_disk_usage()
    create_rapport(cpu, ram, disk, port_for_json)


def get_config():
    """Get the config file"""
    with open("/etc/monit/conf.d/conf.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    return config


def get_last_rapport():
    """Get the last rapport"""
    last = None
    report = {}
    for file in listdir("/var/monit"):
        if file.endswith(".json"):
            if last is None:
                last = file
            elif path.getmtime(f"/var/monit/{file}") > path.getmtime(
                f"/var/monit/{last}"
            ):
                last = file
    with open(f"/var/monit/{last}", "r", encoding="utf-8") as f:
        content = json.load(f)
        report[content["id"]] = content["data"]
        info(f"Get last report:{content['id']}")
        return report


def get_all_reports():
    """Get all reports"""
    rapport_list = {}
    for file in listdir("/var/monit/"):
        if file.endswith(".json"):
            with open(f"/var/monit/{file}", "r", encoding="utf-8") as f:
                report = json.load(f)
                rapport_list[report["id"]] = report["data"]
    info("Get all reports")
    return rapport_list


def get_report(name):
    """Get a report"""
    report = {}
    if not name.endswith(".json"):
        name += ".json"
    if path.exists(f"/var/monit/{name}"):
        with open(f"/var/monit/{name}", "r", encoding="utf-8") as f:
            report_data = json.load(f)
            report[report_data["id"]] = report_data["data"]
            return report
    else:
        print("File not found")
        return None


def get_rapports_younger_than(hours):
    """Get all reports younger than x hours"""
    rep = []
    for file in listdir("/var/monit/"):
        if time.time() - path.getmtime(
            f"/var/monit/{file}"
        ) < hours * 60 * 60 and file.endswith(".json"):
            rep.append(file)
    return rep


def get_avg_of_report(hours):
    """Get the average of reports younger than x hours"""
    rapports = get_rapports_younger_than(hours)
    rep = None
    for rapport in rapports:
        r = get_report(rapport)
        if rep is None:
            rep = r
        else:
            rep["data"]["cpu"] += r["data"]["cpu"]
            rep["data"]["ram"] += r["data"]["ram"]
    if rep is not None:
        rep["data"]["cpu"] /= len(rapports)
        rep["data"]["ram"] /= len(rapports)
        json_data = {"cpu": rep["data"]["cpu"], "ram": rep["data"]["ram"]}
        info(f"Get avg of reports younger than {hours} hours")
        return json_data
    return None


def log_config():
    """Config the logger"""
    basicConfig(filename="/var/log/monit/monit.log", encoding="utf-8", level=DEBUG)


def check_init():
    """Check if the init.sh script has been run"""
    if not path.exists("/var/monit"):
        print("/var/monit not found \nPlease run init.sh")
    if not path.exists("/var/log/monit"):
        print("/var/log/monit not found \nPlease run init.sh")
    if not path.exists("/etc/monit/conf.d"):
        print("/etc/monit/conf.d not found \nPlease run init.sh")
        return False
    return True


if __name__ == "__main__":
    if not check_init():
        sys.exit()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", help="Commande à executer", choices=["check", "list", "get"]
    )
    parser.add_argument(
        "parameter", help="Le paramètre de la commande", nargs="*", default=""
    )
    args = parser.parse_args()
    log_config()

    if args.command == "check":
        check(get_config())
    elif args.command == "list":
        print(get_all_reports())
    elif args.command == "get":
        if args.parameter[0] == "last":
            print(get_last_rapport())
        elif args.parameter[0] == "avg":
            print(get_avg_of_report(int(args.parameter[1])))
        else:
            print(get_report(args.parameter[0]))
    else:
        print("Commande inconnue")
