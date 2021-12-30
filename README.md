# snowfall
helpful image handling utils - abstracts various file and opencv and pil features into result oriented functions

# usage examples:

~~~ 
from image_handlers import *
~~~

load an image - a simple task in theory but often set with details...is the file there? is the argument a string and not a PathLib object, should it be loaded as rgb or bgr format?

![cv_load_func](https://user-images.githubusercontent.com/46302957/147787954-4fe6d5c5-beb9-454a-865d-0d38e366b6b9.png)
</br>

example: </br>
![cv_load_usage](https://user-images.githubusercontent.com/46302957/147788608-6b483010-eaa0-4693-8888-256152f6c535.png)


# toggle channel order with toRgb and toBgr - a common issue with opencv
opencv continues to have BGR as it's channel format, vs PIL and the rest of the world use RGB format.  A common source of confusion is thus confusing the channel format, resulting in blue tinted images. 

Snowfall thus adds simple cover functions, toRgb and toBgr, to wrap the openCV cvtColor function to switch back and forth.  
Note that the numpy trick of [...,::-1] and similar simply switch the view of the data using that can greatly slow down future openCV operations on that image since it's no longer contiguous memory, forcing OpenCV to have to copy the data for every function.

![toRgb](https://user-images.githubusercontent.com/46302957/147788372-623c5b05-181c-4038-a2c9-22c6c29438b5.png)

vs common mistake:

![opencv_load_mistake](https://user-images.githubusercontent.com/46302957/147788389-e0844cfd-a9a7-4dfd-b38f-122767087b82.png)




