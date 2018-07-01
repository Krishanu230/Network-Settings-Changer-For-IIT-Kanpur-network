# Network-Settings-Changer-For-IIT-Kanpur-network
This python script along with the executable will simply set your internet settings using only your hall, wing and room input.

I used Selenium(Python) to automate click events and sending keys and finally getting the necessary data from https://www.iitk.ac.in/ccnew/IP_Details/Hostel_IP_Address_Details.html
After a bit of Python string manipulation, I managed to store the ip, address, subnet mask, gateway and both the DNS addresses in text files.

I made a batch program to ask for admin permission and apply the settings using netsh program.

The data will be the latest data as it takes the input from the actual website. I did not, however, add any error checking mechanism so if you enter a wrong input the programme will simply terminate.

As I did not have necessary certificates, I did not sign the exe application, so you might have to turn off windows smartscreen and defender for a while.
Contact me for more technical info or any other additional info.
Tip: You need an internet connection (maybe via a mobile hotspot) to run this program but if you have at least one time executed it properly and have not overwritten it with wrong input's data then you can use it offline too! Simply run the netset batch file!

The code can be heavily optimised. I could have used the variables more intelligently to save memory, but then again this is not a very serious project so I will leave this here. 
