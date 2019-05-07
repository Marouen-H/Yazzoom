# Yazzoom Anomaly Detection Case

This repo contains:
- An algorithm that does anomaly detection, with 2 extra additional approaches.
- A jupyter notebook that reads this file, detects the anomalies using your algorithm, shows them in a plot and their values.
- write a script in Python that wraps this algorithm in a REST API which receives its arguments as json and returns the output of your algorithm:
Expected input sample:

{ 
	
	"data" : 
	
	[
		{
			
			"x": 7,
			"y": 5
		
		},
		{
			
			"x": 0,
			"y": 0
		
		},
		{
			
			"y": 3,
			"x": 2
			
		}
	]
}


Expected output sample:

{

    "error": "None",

    "response": 
    
    [
        1,
        1,
        0
    ],
    
    "status": 0
}


- Files in the repo:

Yazzoom.ipynb : the jupyter notebook containing the algorithm and the plots

distance.py : Python file containing a distance function

main.py : API main file


- To run the API:

Download the anomaly.csv file under Yazzoom/ directory

Run the cells 1 to 11, and uncomment the second line in cell 12 to export the pickle file.

From a terminal: run $ python3 main.py

Get the API link from the instrutions in the terminal (it should look like: http://127.0.0.1:5000)

- To query the API:

Send a json object in the expected input format(see Above) through a POST request to API_LINK/DetectAnomalies

- In case there is an error with the request, the API will return a response with a 'status'=1 and 'Error'= the exception causing the error.
