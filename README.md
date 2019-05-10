# napoleon API
An extensible REST API to store data of IOT sensors.

## Introduction

This REST API was designed with the purpouse of store and serve data collected by all kind of sensors.

Every user can create different clusters of sensor data, E.g. a cluster that have a air humidity sensor and a wind speed sensor, and this two informations have a relation.

### Relationships

 - One user has one or more data clusters
 - One data cluster has one or more data
 - One sensor data has one or more fields (`int`, `float`, `boolean`, `string`)


### URL mapping

[`POST`] *Register a new user:*
 - https://napoleon.api/v1/register

[`POST`] *Authentication to get user token:*
 - https://napoleon.api/v1/auth

[`GET`] *Get all user data clusters:*
 - https://napoleon.api/v1/data-clusters/all

[`GET`] *Get detailed user data cluster information:*
 - https://napoleon.api/v1/data-clusters/<:id>/detail

 [`GET`] *Get detailed sensor data information:*
 - https://napoleon.api/v1/sensor-data/<:id>/detail

 [`POST`] *Save a new data cluster:*
 - https://napoleon.api/v1/data-cluster/add/
