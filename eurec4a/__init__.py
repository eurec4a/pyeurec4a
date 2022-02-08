from functools import lru_cache
import intake
import requests
import yaml

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

SEGMENT_REPO = "eurec4a/flight-phase-separation"


class GithubApi:
    def get(self, endpoint):
        url = "https://api.github.com/" + endpoint
        return requests.get(url,
                            headers={
                                "Accept": "application/vnd.github.v3+json",
                            }).json()


github = GithubApi()


def get_flight_segments(version="latest"):
    """
    Download and parse flight segmentation information.

    :param version: optional version (git-tag) of the flight segmentation release
    """
    if version == "latest":
        release_info = github.get(f"repos/{SEGMENT_REPO}/releases/latest")
    else:
        release_info = github.get(f"repos/{SEGMENT_REPO}/releases/tags/{version}")
    all_flights_asset = [a
                         for a in release_info["assets"]
                         if a["name"] == "all_flights.yaml"][0]
    all_flights_url = all_flights_asset["browser_download_url"]

    return yaml.load(requests.get(all_flights_url).content, Loader=yaml.SafeLoader)


def get_meta():
    """
    Download and parse general campaign metadata.
    This includes information about platforms, instruments, people, data access etc.
    """
    return yaml.load(requests.get("https://eurec4a_staging.pages.gwdg.de/eurec4a_meta/meta.yaml").content,
                     Loader=yaml.SafeLoader)


@lru_cache()
def get_cids():
    return requests.get("https://raw.githubusercontent.com/eurec4a/ipfs_tools/main/cids.json").json()


def get_intake_catalog(use_ipfs=False):
    """
    Open the intake data catalog.

    The catalog provides access to public EUREC4A datasets without the need to
    manually specify URLs to the individual datasets.
    """
    if use_ipfs:
        if isinstance(use_ipfs, str):
            cid = use_ipfs
        else:
            cid = get_cids()['intake']['latest']
        return intake.open_catalog(f"ipfs://{cid}/catalog.yml")
    else:
        return intake.open_catalog("https://raw.githubusercontent.com/eurec4a/eurec4a-intake/master/catalog.yml")


def get_latest_intake_cid():
    return get_cids()['intake']['latest']


__all__ = ["get_flight_segments",
           "get_meta",
           "get_intake_catalog",
           "__version__"]
