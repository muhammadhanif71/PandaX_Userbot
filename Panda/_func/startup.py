import asyncio
import glob
import importlib
import logging
from ..Config import Config
import ntpath
import shlex
from typing import Tuple

REPO_ = Config.UPSTREAM_REPO
BRANCH_ = "PandaUserbot"



def load_modulesPyro(plugin_name, assistant=False):
    """Load PLugins - Assitant & User Using ImportLib"""
    if plugin_name.endswith("__"):
        pass
    else:
        if plugin_name not in Config.MAIN_NO_LOAD:
            if assistant:
                plugin_path = "assistant." + plugin_name
            else:
                plugin_path = "ModulesPyro." + plugin_name
            loader_type = "[🤖 Assistant]" if assistant else "[👤 User]"
            importlib.import_module(plugin_path)
            logging.info(f"{loader_type} - Connection : " + str(plugin_name))


def plugin_collecter(path):
    """Collects All Files In A Path And Give Its Name"""
    if path.startswith("/"):
        path = path[1:]
    if path.endswith("/"):
        pathe = path + "*.py"
    else:
        pathe = path + "/*.py"
    Poppy = glob.glob(pathe)
    final = []
    Pop = Poppy
    for x in Pop:
        k = ntpath.basename(x)
        if k.endswith(".py"):
            lily = k.replace(".py", "")
            final.append(lily)
    return final  


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

