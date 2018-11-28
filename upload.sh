#!/bin/bash
source aws.secret
aws s3 sync content/portfolio s3://vincent.khougaz.com
