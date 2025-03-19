"""Utilities helping with the documentation build"""

from dataclasses import dataclass
import datetime
import requests
from typing import List, Mapping


# Constants
GITHUB_API_ROOT = "https://api.github.com"
GITHUB_REPOSITORY = "mantidproject/mantid"
GITHUB_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
LATEST_RELEASE_MARKER_STR = "latest"


@dataclass
class Asset:
    """Encapsulate a single downloadable asset"""

    name: str
    url: str


@dataclass
class ReleaseInfo:
    """Capture information about a single release"""

    version: str
    release_date: str
    windows: Asset
    macos: Asset
    linux: Asset


def fetch_release_info(tag_or_latest: str) -> ReleaseInfo:
    """Fetch release information

    :param tag_or_latest: A string defining the tag for a release or the string 'latest'
    to fetch information on the latest release
    :type release: str
    :return dict: A ReleaseInfo object containing the required information
    """
    if tag_or_latest == LATEST_RELEASE_MARKER_STR:
        endpoint = f"{GITHUB_API_ROOT}/repos/{GITHUB_REPOSITORY}/releases/latest"
    else:
        endpoint = (
            f"{GITHUB_API_ROOT}/repos/{GITHUB_REPOSITORY}/releases/tags/{tag_or_latest}"
        )

    response = requests.get(endpoint)
    try:
        response.raise_for_status()
    except IOError as exc:
        raise RuntimeError(
            f"Error retrieving release information from {endpoint}"
        ) from exc

    return _create_release_info(response.json())


def _create_release_info(response_content: Mapping) -> Mapping:
    """Create a lookup of information from the response on the release

    :param response: A requests.Response object. It is assumed that the request
    was successful and any errors raised before calling this function
    :return: A dictionary of release information
    """
    version = response_content["tag_name"]
    release_date = _to_pretty_date(response_content["published_at"])
    assets = response_content["assets"]
    packages = dict(
        windows=_find_asset_info(assets, ".exe"),
        macos=_find_asset_info(assets, ".dmg"),
        linux=_find_asset_info(assets, ".tar.xz"),
    )
    # sanity check we have packages
    missing = []
    for os, asset in packages.items():
        if asset is None:
            missing.append(os)
    if len(missing) > 0:
        raise RuntimeError(
            f"Unable to find required assets for {version}. "
            f"Missing: {','.join(missing)}"
        )

    return ReleaseInfo(version=version, release_date=release_date, **packages)


def _to_pretty_date(timestamp: str) -> str:
    """
    :param timestamp: _description_
    :return: A pretty date string for display to users
    """
    return datetime.datetime.strptime(timestamp, GITHUB_TIMESTAMP_FORMAT).strftime(
        "%d %B %Y"
    )


def _find_asset_info(assets: List[Mapping], asset_extension: str) -> Asset:
    """Find an asset whose filename ends with the given extension
    and return an Asset object.

    :param assets: A list of asset descriptions.
                   Each entry is a dictionary describing the asset
    :return: An asset object describing the asset
    """
    for info in assets:
        name = info["name"]
        if name.endswith(asset_extension):
            return Asset(name=name, url=info["browser_download_url"])

    return None
