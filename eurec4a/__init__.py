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
    return yaml.load(requests.get("https://eurec4a_staging.pages.gwdg.de/eurec4a_meta/meta.yaml").content,
                     Loader=yaml.SafeLoader)


__all__ = ["get_flight_segments", "get_meta", "__version__"]
