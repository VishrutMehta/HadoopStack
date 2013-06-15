from flask import Blueprint, request, jsonify,current_app
from flask.ext.pymongo import PyMongo

from hadoopstack.services import job
from hadoopstack.services import cluster

import os
import simplejson
import json
import hadoopstack.main

app_v1 = Blueprint('v1', __name__, url_prefix='/v1')

@app_v1.route('/',methods = ['GET','POST'])
def version():
    '''
        GET request of the cluster API
    '''
    if request.method == 'POST':
        cursor = hadoopstack.main.mongo.db.cluster.find()
        allEle = []
        for obj in hadoopstack.main.mongo.db.cluster.find():
            allEle.append(obj)
        objToReturn = {}
        objToReturn['cluster'] = allEle;
        allTuples = [(objToReturn[i]) for i in objToReturn]
        allIds = [(str(ids['_id'])) for i in allTuples for ids in i]
        for i in xrange(0,len(allIds)):
            allTuples[0][i]['_id'] = allIds[i]
        return jsonify(**objToReturn)


    return "v1 API. Jobs and clusters API are accessible at /jobs and \
    /clusters respectively"

@app_v1.route('/jobs/', methods=['GET', 'POST'])
def jobs():
    if request.method == 'GET':
        return ' '.join(job.jobs_list)

    elif request.method == 'POST':
        return "To Be Implemented"

@app_v1.route('/clusters/', methods = ['GET','POST'])
def clusters():
    '''
        Cluster API
    '''
    if request.method == 'POST':
        data = request.json
        cid = cluster.create(data)
        return jsonify(**cid)
     
    return "To Be Implemented"