#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
used to Create GeoJSON file from lon, lat

"""


from geojson import Point, Feature, FeatureCollection, dump
import json
import os


def create_geojson(lon, lat, outdir):
    """
    Create GeoJSON file

    Parameters
    ----------
    lon (float) -- longitude
    lat (float) -- latitude
    outdir (str) -- path where the output file has to be stored
    Returns
    -------
    Absolute path to the merged file
    output GeoJSOn file is saved in the specified directory.
    """

    geo =  Point((lon, lat)) 

    features = []

    features.append(Feature(geometry=geo, properties={"name": "test"}))

    feature_collection = FeatureCollection(features)

    if not os.path.exists(outdir):
        os.makedirs(outdir, exist_ok=True)

    file = os.path.join(outdir, "test" + ".geojson")

    with open(file, "w") as f:
        dump(feature_collection, f)

    return os.path.abspath(file)
