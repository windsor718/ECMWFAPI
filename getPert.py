#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    'origin'    : "ecmf",
    'levtype'   : "sfc",
    'number'    : "1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23/24/25/26/27/28/29/30/31/32/33/34/35/36/37/38/39/40/41/42/43/44/45/46/47/48/49/50",
    'expver'    : "prod",
    'dataset'   : "tigge",
    'step'      : "0/6/12/18",
    'grid'      : "0.5/0.5",
    'param'     : "167",
    'time'      : "00/12",
    'date'      : "2014-11-01",
    'type'      : "pf",
    'class'     : "ti",
    'target'    : "tigge_2014-11-01_0012.grib"
})
