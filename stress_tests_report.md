Type	Name	Request Count	Failure Count	Median Response Time (ms)	Num. users	 Spawn rate(users/s)	RPS	  Fail(%)
								
GET	    /	          129	           0	            5				
POST	/predict	  131	           3	           160				
	    Aggregated	  260	           3	            21	                    10	            20	            2.5	     1
													
GET	    /	          462	           0	            5				
POST	/predict	  432	           8	           160				
	    Aggregated	  894	           8	            9	                    30	            100	            7.1	     1
								
GET	    /	          1051	           0	           3000				
POST	/predict	  1019	          18	           4500				
	    Aggregated	  2070	          18	           3800	                   100	            1000	        13.2	 1
								
GET	    /  	          1004	           0	           75000				
POST	/predict	  1135	          16	           76000				
	    Aggregated	  2139	          16	           75000	              1000	           10000	         14	     1
								
GET	    /	           963	         409	           22000				
POST	/predict	  1014	         467	           22000				
	    Aggregated	  1977	         876	           22000	             10000	           10000	         15     44


Conclusions:

We can analyze the Median Response Time (MRT) as we increment the number of users:

    * When we go from 10 to 30 users, the MRT doesn't change and maintains a negligible value.
    * When we go to 100 users, the responses time increases and has a considerable value for the users.
    * Beyond 100 users, the MRT goes unacceptable.

Also, we can analyze the Failures (%). Here we can see that we have acceptable values (1%) until 1000 users, which grows a lot between 1000 and 10.000 users. 

Evaluating MRT and Failures(%), we can conclude that the service responds well with less than 100 users. Perhaps between 70-80 users, we can find a compromise relationship for the API.


