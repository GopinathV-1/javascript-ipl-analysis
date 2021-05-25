# Dataproject :: JavaScript

## IPL-ANALYSIS-JAVASCRIPT

This repo consists of a source code of a python script and JavaScript to make specific anaylsis in IPL dataset using **Data-structure**.

[![IPL](pictures/IPL.png)](https://en.wikipedia.org/wiki/Indian_Premier_League)

## How is it done?

You might be wondering on how graphs were plotted on a raw dataset is done, well it was not that complicated as you may think.

We all know that computers are good at numbers, so in order to plot graph we were designing a definite structure to the data in this case
we used dictionaries to select required data from csv file and made a json file , with the data in json file we have plotted Highcharts graphs using JavaScript.

This repo consists of a basic example of how to do that.


## Getting started

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
git clone git@gitlab.com:mountblue/cohort-16-python/gopinath_v/dataproject-javascript.git
```

## Running the App

#### Part 1 Creating Json file

To run this, code you need to have to download [dictionaries, matches](https://www.kaggle.com/manasgarg/ipl/version/5) and [umpires](https://www.kaggle.com/subhodeepchandra/ipl-umpires-by-country) csv files and place these datasets in the same directory. If you want to **install and setup virtualenv** follow from **step 1** or if you want to **directly run it in editor** follow from **step2**.

#### open the terminal

## step1
### Install the virtualenv package
```bash
pip install virtualenv
```
### Create the virtual environment
To create a virtual environment, you must specify a path. You may provide any name in the place of <mypython>:
```bash
virtualenv <mypython>
```
  
### Activate the virtual environment
```bash
source mypython/bin/activate
```
  
## step2
  
```bash
$-> cd dataproject-javascript
$ cd dataproject-javascript-> python3 total_runs.py

```

```bash
$ cd dataproject-javascript-> python3 rcb_top_batsman.py

```

```bash
$ cd dataproject-javascript-> python3 foreign_umpire.py

```

```bash
$ cd dataproject-javascript-> python3 total_matches_by_team.py

```


#### Part 2 Running the app in Python server

```bash
$ cd dataproject-javascript-> python3 -m http.server

```
Now you can access the app on your local server

When you open your local server, you will see all the files in the data-project in that select **index1.html** 
to run the app.

### Deactivate the virtual environment
if you have followed step1, use this command to get out of virtualenv
```bash
deactivate

```


