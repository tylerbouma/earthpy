from flask import Flask, request, jsonify
import csv
from __main__ import app

app.config["DEBUG"] = True

# A route to return all of the available entries
@app.route('/api/v1/resources/sites/all', methods=['GET'])
def api_all():
    with open('datasets/MAPPPD_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        big_list = []
        for row in csv_reader:
            big_list.append(row)


    return jsonify(big_list)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/sites', methods=['GET'])
def api_filter():
    # Get the query request from the URL
    query_params = request.args

    # All column items
    # site name,site id,ccamlr region,Longitude EPSG:4326,Latitude EPSG:4326,common name,day,month,year,season starting,count,accuracy,count type,vantage,reference,notes

    # Items that can be used to filter
    site_name = query_params.get('site_name')
    site_id = query_params.get('site_id')
    common_name = query_params.get('common_name')
    year = query_params.get('year')

    to_filter = []
    big_list = []

    if site_name:
        to_filter.append(site_name)
    if site_id:
        to_filter.append(site_id)
    if common_name:
        to_filter.append(common_name)
    if year:
        to_filter.append(year)
    if not (id or published or author):
        return page_not_found(404)

    # check csv for all of our filter items
    with open('datasets/MAPPPD_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            if set(to_filter).issubset(row):
                big_list.append(row)
    
    
    return jsonify(big_list)
    
app.run()