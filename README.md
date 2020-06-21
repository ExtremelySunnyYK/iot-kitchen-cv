# Peanuts

<img src = "./Assets/peanutLogo.png" title = "Peanut" width="200" height="200"/>


Peanuts is a cloud-enabled, mobile-ready, offline-storage, azure web server powered grocery management app and IoT kitchen camera that provides a seamless end-to-end grocery experience.

  1. Tracks stock and quality of kitchen groceries
  2. Employs data-analytics magic to optimise your food consumption and grocery purchasing patterns


## App demo

<img src = "./Assets/foodapp.gif" title = "gif demo" height="480"/>


## IOT Proof of Concept Demo

<a href = "https://youtu.be/5LCXWCDCLPI?t=70"><img src = "https://i.imgur.com/NCkj6A4.png" title = "IOT Demo Video" height="300"/>

### Tech

Peanuts uses a number of open source projects to work properly:

##### Software
* [Flutter](https://flutter.dev/) - HTML enhanced for web, mobile and desktop apps!(to create the mobile user interface )
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - python web app framework
* [Azure web service](https://azure.microsoft.com/en-us/services/app-service/web/) - platform to host web server
* [MongoDB](https://www.mongodb.com/) - Popular NoSQL document database
* [OpenCV](https://opencv.org/) - Library for Computer Vision
* Data analytics (not in proof of concept) for tracking and recommending consumption pattern

##### Hardware
* [Nvidia Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit) - small, powerful computer that can run multiple neural networks in parallel for applications like image classification, object detection, segmentation, and speech processing

*Software*: [YOLO](https://pjreddie.com/darknet/yolo/), [OpenCv](https://opencv.org/)
#### UI/UX
* [Figma](https://www.figma.com) - Design, prototype, and gather feedback all in one place

## How tech work
- The Video of the kitchen is captured by the Nvdia Jetson Nano which is inputed into a Computer Vision model (YOLO).
- The Output of the classification of the Computer Vision model is stored on MongoDB Cloud.



## How it flows



#### App Mockup
[![Mock up](https://prototypr.gumlet.com/wp-content/uploads/2020/03/www_figma_com_logo.png?w=70&dpr=2.6)](https://www.figma.com/file/qZsXa4wuyLhiAXG0lgX1pY/JunctionXAsia?node-id=0%3A1 "Mock up")

### Installation
You will need
* Nvdia Jetson Nano
* Python
* Mongo DB


## Future Plans
- Household's inventory is stored in MongoDB cloud and on household members' mobile devices for offline use (syncing with database)
- Items are added to the database via scanning of a QR code containing a temporary link to a receipt of groceries from local supermakret
- This temp link is created from the supermarket's server, and essentially outputs the receipt in JSON format to the mobile app. The mobile app would post this to our flask server hosted by Azure and in turn post this to MongoDB
- Cameras are connected to a Jetson Nano houses an object identification model that identifies the food that a member of the household is going to comsume. It would post an update to MongoDB of the items that are just consumed Front end slider mechanisms can also be used
- Inventory data from supermarkets helps to recommend when and where is best to purchase

## Credits
- [Chia Yong Kang](https://github.com/ExtremelySunnyYK)
- [Tan Jia Yue]
- [Hoe Jun Leong](https://github.com/hjunleon1999)
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

**Disclaimer: currently proof of concept stage**

  
