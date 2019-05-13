## Log-Analysis
To build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Description
Building an informative summary from logs is a real task that comes up very often in software engineering. For instance, at Udacity we collect logs to help us measure student progress and the success of our courses. The **reporting tools** we use to analyze those logs involve hundreds of lines of SQL.

 
## Screenshots
![alt text](https://github.com/Shadmanwaris/Log-Analysis/blob/master/screenshot/Screenshot%20from%202019-05-13%2000-33-04.png)

## Tech/framework used
Ex. -

<b>Built with</b>
- [python](https://www.python.org/)

## Table of Contents

1. [Project Overview](#project-overview)
1. [Setting up the project](#setting-up-the-project)
1. [Running the project](#running-the-project)
1. [Resource Links](#resource-links)

## Project Overview

This project is a part of Udacity's Full Stack Web Developer Nanodegree. In this project, server-side code
 was written to query a database and analyze the table containing the logs. The main script will go throught the logs and returns
 the three most popular articles, the three most popular authors, and the days where the error rate for requests was above 1%.

## Setting up the project

> In order to run this project, you must have [Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) set up on your computer.

```bash
# Clone the git repository into a directory using a bash terminal
git clone https://github.com/Shadmanwaris/Log-Analysis.git

# Once the project has been setup, navigate into the project directory with `Vagrantfile`
cd Log-Analysis

# Start the virtual machine
vagrant up

# Connect to the virtual machine
vagrant ssh

# Navigate to the folder where the guest/host files are shared
cd /vagrant
    
# Unzip the news database data SQL script
unzip ./data/newsdata.sql
    
# Apply SQL to Postgres to create news database
psql -d news -f newsdata.sql
```
## Running the project

```bash
# Once the project has been setup, navigate into the project directory on your home computer
cd Log-Analysis

# Then, run the following command to ssh into the vagrant box
vagrant ssh

# Navigate to the folder shared between the host and virtual machine
cd /vagrant

# Run `analyze-logs.py` and log analysis will be printed
python log.py
```

Example Output:
```bash
TOP THREE ARTICLES BY PAGE VIEWS:
(1) "Candidate is jerk, alleges rival" with 338647 views
(2) "Bears love berries, alleges bear" with 253801 views
(3) "Bad things gone, say good people" with 170098 views

TOP THREE AUTHOR OF ALL TIME:
(1) "Ursula La Multa" with 507594 views
(2) "Rudolf von Treppenwitz" with 423457 views
(3) "Anonymous Contributor" with 170098 views

DAY WITH MORE THAN 1% OF REQUESTS:

July 17, 2016  -- 2.2626862468 %

```

## Resource Links

- [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
- [Source Code](https://github.com/Shadmanwaris/Log-Analysis)

#### Anything else that seems useful

## License
A short snippet describing the license (MIT, Apache etc)

MIT © [Shadman Waris]()