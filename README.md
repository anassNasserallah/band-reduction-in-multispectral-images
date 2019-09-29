# band-reduction-in-multispectral-images
A multispectral image is an image that has several components. For example, a color image has 3 components: 
red, green and blue and each pixel can be viewed as a vector in R 3 . More generally a multispectral image of size N × M with P spectral bands can be stored as a N × M × P array. 
There are N × M pixels living in R p . When the number of spectral bands P is too large, it is desirable to somehow reduce that number ultimately to 3 for viewing purposes. 
This process is called band reduction.

We propose a method using the PCA performing a band reduction to 3 bands and use it on
the provided multispectral image.
Some multispectral images are available on the internet to test your band reduction
algorithm. See for example the following website
• http://lesun.weebly.com/hyperspectral-data-set.html
