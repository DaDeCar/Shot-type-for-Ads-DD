Both in "stress_tests_report.md" and in the present report we use a sever to run the service with the folowing characteristics:

* CPU: AMD Ryzen 7 5700G
* RAM memory: 32 GB  

### TEST SCALED SERVICES

* SERVICE= 4

Type	Name	Request Count	Failure Count	Median Response Time	Num. Of users	Spawn rate (users/s)   RPS	Failures (%)
								
GET	    /	         513	                0	                5				
POST	/predict	 515	               18	              160				
	    Aggregated  1028	               18	               33	              30	            100	             7	    2
								
GET	    /	        1069                	0	             3300				
POST	/predict	1048	                5	             4600				
	    Aggregated	2117	                5	             3900	             100	           1000	            14	   0.1


* SERVICE= 8

Type	Name	Request Count	Failure Count	Median Response Time	Num. Of users	Spawn rate (users/s)   RPS	Failures (%)
								
GET	    /	         658	                 0	                5				
POST	/predict	 609	                14	              160				
	    Aggregated	1267	                14	                7	               30	             100	    7.1	     1
								
GET	    /	        1207	                 0	             3300				
POST	/predict	1185	                 6	             4500				
	    Aggregated	2392	                 6	             3900	              100	            1000         13	     0.1


* SERVICE = 40
Type	Name	Request Count	Failure Count	Median Response Time	Num. Of users	Spawn rate (users/s)	RPS	 Failures (%)
								
GET	    /	         477	                 0	                5				
POST	/predict     463	                 9	              210				
	    Aggregated   940	                 9	               40	                30	             100	     7.5	  1
								
GET	    /	         939	                 0	             3000				
POST	/predict     921	                 7	             4400				
	    Aggregated  1860	                 7	             3800	               100	            1000	     10	      0.1


* SERVICE = 500

Type	Name	Request Count	Failure Count	Median Response Time	Num. Of users	Spawn rate (users/s)	RPS	 Failures (%)
								
GET	    /	         693	                0	                5				
POST	/predict	 659	               11	              210				
	    Aggregated	1352	               11               	8	                30	             100	      7	        1
								
								
GET	    /	         928	                0	             3500				
POST	/predict	 943	               10	             4800				
	    Aggregated	1871	               10	             4200	               100	            1000	     12	        1


* SERVICE = 5000

Type	Name	Request Count	Failure Count	Median Response Time	Num. Of users	Spawn rate (users/s)	RPS	 Failures (%)
								
GET	    /	          34	                0	            43000				
POST	/predict	  29                   29	            71000				
	    Aggregated	  63	               29	            57000	               30	             100	     0.3	    47


### Conclusions:
As we can see, above 5000 active services the Failures (%) and the Median Response Time (ms) rise until unaceptable values. 
So we must conclude that the max quantity of services availables are between 500 and 5000. 