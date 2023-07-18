import os
import urllib
import json


def get_paper_mc_versions():
    with urllib.request.urlopen('https://papermc.io/api/v2/projects/paper/') as baseurl:
        basedata = json.loads(baseurl.read().decode())
    return basedata.get('versions')


def get_paper_mc_builds(version):
    pmc_url = f'https://papermc.io/api/v2/projects/paper/versions/{version}'
    with urllib.request.urlopen(pmc_url) as baseurl:
        basedata = json.loads(baseurl.read().decode())
        return basedata["builds"]


def get_paper_mc(version=None, build=None):
    if version is None:
        version = get_paper_mc_versions()[-1]

    build_num = build
    if build is None:
        builds = get_paper_mc_builds(version)
        build_num = builds[-1]

    pmc_url = f'https://papermc.io/api/v2/projects/paper/versions/{version}/builds/{build_num}'
    with urllib.request.urlopen(pmc_url) as buildurl:
        builddata = json.loads(buildurl.read().decode())
        name = builddata["downloads"]["application"]["name"]
        final = f"{pmc_url}/downloads/{name}"
    return final


def download_file(path, url, name):
    if not os.path.exists(path):
        os.makedirs(path)
    urllib.request.urlretrieve(url, os.path.join(path, name))


def get_vanilla_mc_versions():
    with urllib.request.urlopen("https://launchermeta.mojang.com/mc/game/version_manifest.json") as url:
        data = json.loads(url.read().decode())
    return data['versions']


def get_vanilla_mc(version=None):
    mc_versions = get_vanilla_mc_versions()
    if version is None:
        return mc_versions[0]
    json_url = None
    for mc_version in mc_versions:
        if mc_version['id'] == version:
            json_url = mc_version['url']
    if json_url is None:
        raise ValueError(f"Invalid version {version}")
    with urllib.request.urlopen(json_url) as versionUrl:
        dataUrl = json.loads(versionUrl.read().decode())
    return dataUrl["downloads"]["server"]["url"]
