# Peanuts

<img src = "peanutLogo.png" title = "Peanut" width="200" height="200"/>

**Disclaimer: currently proof of concept**

Peanuts is a cloud-enabled, mobile-ready, offline-storage, azure web server powered grocery management app and IoT kitchen camera that provides a seamless end-to-end grocery experience.

  1. Tracks stock and quality of kitchen groceries
  2. Employs data-analytics magic to optimise your food consumption and grocery purchasing patterns

## Proof of concept demo
<a href = "https://flask-iot-kitchen.azurewebsites.net/">
<img src="https://appservice.azureedge.net/images/linux-landing-page/v3/python.svg" alt="Kitten"
	title="Proof of concept" width="150" height="100" />
</a>

## Video demo

> ![Demo](https://imgur.com/a/EH6pAYQ.gif)


## Proof of concept
> ![Proof of concept](https://www.youtube.com/watch?v=5LCXWCDCLPI&feature=youtu.be)


### Tech

Peanuts uses a number of open source projects to work properly:

##### Software
* [Flutter](https://flutter.dev/) - HTML enhanced for web, mobile and desktop apps!(to create the mobile user interface )
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - python web app framework
* [Azure web server] - platform to host web server
* [MongoDB](https://www.mongodb.com/) - Popular NoSQL document database
* Data analytics (not in proof of concept) for tracking and recommending consumption pattern

##### Hardware
* [Nvidia Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) - small, powerful computer that can run multiple neural networks in parallel for applications like image classification, object detection, segmentation, and speech processing

    *Software*: [YOLO](https://pjreddie.com/darknet/yolo/), [OpenCv](https://opencv.org/)
#### UI/UX
* [Figma](https://www.figma.com) - Design, prototype, and gather feedback all in one place

## How tech work
- Household's inventory is stored in MongoDB cloud and on household members' mobile devices for offline use (syncing with database)
- Items are added to the database via scanning of a QR code containing a temporary link to a receipt of groceries from local supermakret
- This temp link is created from the supermarket's server, and essentially outputs the receipt in JSON format to the mobile app. The mobile app would post this to our flask server hosted by Azure and in turn post this to MongoDB
- Cameras are connected to a Jetson Nano houses an object identification model that identifies the food that a member of the household is going to comsume. It would post an update to MongoDB of the items that are just consumed Front end slider mechanisms can also be used
- Inventory data from supermarkets helps to recommend when and where is best to purchase

## How it flows
[![Presentation slides](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAABCFBMVEX0tAD////++Ob/4Wi3hwD3tQD4+Pj2+f/yvBz0sgDwtQC+vr7k5OSXnKXyqgD/++399uDs7e/4yWP0rwD636j///n//vP98NP52JX2w1zkw0/3xmf75r3z6922gQD2vkr1uj3/53D4znn95Hv94nO7igDNlwD0thn98dHkqAD1uir63qDcogDDkADUnADsrgDS0tLZ2dn3xkD33ZX42Yfzxlfm1rrsxFrjw1/4znHxoAD0tS774rD97sb1vU/4y3nGs4zl3szgtlTV0cbltj/Tu4jVun3NxrC7sJPkryS0ucTNq1a2tbHGxsi0pIGnqq6ko5vEpWK4pHarnHzEpFTOpz2jmYWjop6izAkoAAAF1UlEQVR4nO3dfXfaNhQGcGEmNoU0tiExyZo1LKULgaaQlqzLRrZ1W7fSjpB26/b9v8kMWU55Cb6yJSFdnfv8m3Ny+B0/siRjG1byPcz2BzAeEuIPCfGHhPgjL4y6xzVjuQhtC5Or54xzLkyFP47sCts1zpnBCPb144ZN4YsvjPpmwnIrsSbcG9TN+m6F5ZaZosLCvYHhA3gnLJsZi7Cwa9x3JzRTVFCYGK/oJ6GRokLCvQvzHf0kNFFUSHi4Ad+c0EBRAWF4ITYrLLd0z4uAMNjaBHBeqL2ogPDbTYzCRWG5pXeNCghfWhBqPqNmCiuljg2h3qICQtML0vuF5Vbgu1BnUbOFn9sSaiyqq0J9Z1RnhdqK6q6wrGnX77BQ0xrVZaGeojot1HJGdVuoo6iOCzUU1XWhelGdFypP/e4LVXf9CISKRcUgVNtMoRAqnVFxCFWKikSoUFQswuJFRSMsvJnCIyw69SMSFiwqJmGxoqISFtpM4RIWKSoyYYGpH5swf1HRCXNvpvAJ8xYVoTDn1I9RmK+oKIW5iopTmGczhVSYY+rHKpQvKlqhdFHxCmWLilgouZnCLJSb+lELpYqKWyhTVORCic0UdiG8RnVDyPiXhfMdcLpxRMhOPyuaR19VUAgZ+8Z7IX9WVBgbE4r6jmLqC/fJP3VMKMRR9yoIVdLYrZ3MGbk4c0ko2H4UhoFawmDYmT+MvQKD0ZiwvqvKuzW2mWJTTQnrg0QHMCUuPpXDT5+4IRSdhh5gEESXi4/l9HIORlPCy0iXMOwuCnnOmdGUcF/LKJwJrzpLz1bxp3maakqo5zwzS7u5/PRYrsGIQNhYEeYajEiFnEmv4ZAKcwxGtELpwYhXmBqlBiNmIRMyg9G0cE8hCSSU2vobFja+V9gdNiNQyOFpw7Aw2ln74cCII1iYEqE1HHZhGmAweiAEpg0PhMAazgshExmD0Q9huobzXZgOxnVN9UW4fjD6I2T8/sHokXDNhsonYdpU74X3fUPlm3B1DYdA2P6hDiTzuj8CYTQc7mZk2L1sivlvqJamDQRC+Bu6aH/hovHiGg6DEE44PFlo6jPvhEFytfDqP9574pswSGpLxDPfhOHiQZx+Q/XIL2EQLc+adxsqf4QHK+uC2w2VP8KH96x8zrwXTqcNz4Xs1HshP/VdyHg98lzIOAJhkh1AKNwXNo4fZuUgwi/M3AGLHQ+E2VcxSEhCEpKQhCQkIQlJSEIJocIPdeEQ/nhQPD9hEEK7V5m9reNCDSEhCUlIQhIqJ1x9sssJ4UAXcHoXQhbQmrCm7wnL/exboiwJmWjrqmkE/HidNeHzQA8xgX7l1JaQ1Y8jDcQw3BXZh9CeMB2KV0kC3K41J7k3STRgANCikIn60YvhYWbuBuuaP3drog4BbQqnxuzsXN5ukKLmzpovliTuLLUqhCKO/xceKfzWJwlJSEJdwsIhoRvCoKGQdoBBqCEkJCEJSUhCEkoIV+/Vd0F4oA0YNJbfCOaGsKPtilx4uO6ClVWhxte6JWuvOVoW6jqIyXDtNUe7QiZOdBDD5ecPHRKmR7HbUHuNaxIG7cF6oHUhE6J5ua+UQa2ZdU3OunBqhJ7VBpJ9zdEBoeGQkIQktB8SkpCE9kNCEpLQfkhIQhLaDwlJSEL7ISEJSWg/JCQhCe3H0JuwHIra28zil+4LxSsl4c/OC/mWirAUv1K4QXtD+eVc4ddyS/Gvv7l+EPlrJWGl/7vjQj76Y1tJuF11/CDy1/3sYQgIS3H/jdNCPnoLlBQSVrbfvnOYyLfeQIcQEpbi8z/dJfKT6yowCmFhJR47S+TsGuwoLEx7OiW6aOS9DxOwoxLCKXFyPXLNmH6edzeT8xg8hBLCGfHm/Sj9p44wpx+k9/HDg2pfAigjTIn96uTmr79HW45k9PH9P/9OxjJHUE6Ynm6mxskDZzKZVCV9ksKZ8bw/rjqS8bif+uSAssLUWInjbVcSS/tyCNGGhPhDQvzxX/gfnhu+EP9ms28AAAAASUVORK5CYII=)](https://docs.google.com/presentation/d/1SoCnFtdbRhlorfWPjvCNIBzC6zK7TQDaetXBJoY2R90/edit#slide=id.g893141ec5d_8_10)


[![Mock up](https://prototypr.gumlet.com/wp-content/uploads/2020/03/www_figma_com_logo.png?w=70&dpr=2.6)](https://www.figma.com/file/qZsXa4wuyLhiAXG0lgX1pY/JunctionXAsia?node-id=0%3A1 "Mock up")
### Installation

## Credits
- [Chia Yong Kang](https://github.com/ExtremelySunnyYK)
- [Tan Jia Yue]
- [Hoe Jun Leong]
- [Joseph Low]
- [Dhanush Kumar]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>


  
