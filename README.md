# JSON-REST-API  

In this project, I look to receive the sunrise and sunset of a certain location by using two free web REST APIs:  
1) [Position Stack API](https://positionstack.com/documentation)
2) [Sunrise Sunset API](https://sunrise-sunset.org/api)

I start by sending an API call to Position Stack API with a location & API authentication key to receive data in JSON format. Then I extract latitude and longitude coordinates from that data.  I then send an API call to Sunrise Sunset API with those coordinates to receive data in JSON format.  I transform that data to receive the sunrise and sunset in the time format: hour:minute:seconds.
