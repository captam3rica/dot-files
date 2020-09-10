#!/usr/bin/env python3

"""latestiosversion.py.

A script to pull the latest iOS versions.
"""

#
#   Host link: http://api.ipsw.me/v2/firmwares.json
#


import requests


URL = "https://api.ipsw.me/v2.1/firmwares.json"

PAYLOAD = {}
HEADERS = {}

IPHONE_MODEL_IDENTIFIERS = [
    "iPhone10,1",
    "iPhone10,4",
    "iPhone10,2",
    "iPhone10,5",
    "iPhone10,3",
    "iPhone10,6",
    "iPhone11,8",
    "iPhone11,2",
    "iPhone11,6",
    "iPhone11,4",
    "iPhone12,1",
    "iPhone12,3",
    "iPhone12,5",
]


def get_ipsw_me_data(url):
    """Return iOS version data"""
    response = requests.get(url, headers=HEADERS, data=PAYLOAD)
    return response.json()


def get_all_device_models(data):
    """Return all device types
    Takes in the parsed ios data returned from get_ipsw_me_data
    """
    all_device_models = data["devices"]
    return all_device_models


def get_all_iphone_models(models):
    """Return all iPhone models from a dictionary of device models
    Returns a dictionary containing all iPhone models and the information about each
    model.
    """
    all_iphone_models = {}
    for model, data in models.items():
        if "iPhone" in model:
            all_iphone_models.update({model: data})

    return all_iphone_models


def get_information_about_relevant_iphone_models(iphone_models, identifiers_list):
    """Return relevant iPhone information
    Returns a dictionary pertaining to relevant iPhone models found in the
    IPHONE_MODEL_IDENTIFIERS list
    """
    relevant_iphone_models = {}
    for iphone, data in iphone_models.items():
        for identifier in identifiers_list:
            if iphone not in identifier:
                pass
            else:
                relevant_iphone_models.update({iphone: data})
    return relevant_iphone_models


def get_relevant_iphone_firmware_version(relevant_iphone_models):
    """Return iPhone firmware information
    Returns firmware versions for the iPhones in the relevant list.
    """

    relevant_firmware_versions = []

    for data in relevant_iphone_models.values():
        firmwares = data["firmwares"]
        name = data["name"]

        for firmware in firmwares:
            version = firmware["version"]
            release_date = firmware["releasedate"].split("T")[0]
            upload_date = firmware["uploaddate"].split("T")[0]

            if "2020" in upload_date:
                # print(f"{name}: iOS {version}: {date}")
                # relevant_firmware_versions.append(f"{name}, iOS {version}, {data}")
                goods = f"{name}, iOS {version}, Uploaded: {upload_date}, Released: {release_date}"
                relevant_firmware_versions.append(goods)

    return relevant_firmware_versions


def main():
    """Run the main logic"""

    ipsw_me_data = get_ipsw_me_data(URL)
    all_device_models = get_all_device_models(ipsw_me_data)
    all_iphone_models = get_all_iphone_models(models=all_device_models)
    relevant_iphone_models = get_information_about_relevant_iphone_models(
        iphone_models=all_iphone_models, identifiers_list=IPHONE_MODEL_IDENTIFIERS
    )
    firmware_versions = get_relevant_iphone_firmware_version(relevant_iphone_models)

    for iphone in firmware_versions:
        print(iphone)


if __name__ == "__main__":
    main()
