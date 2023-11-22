# This repo is created to train models for a dataset of images that can be generated with the use of [PMDL_SphereDrawer](https://github.com/SanikoZmey/PMDL_SphereDrawer)
### After the generating the images it is needed to label them(for now by hand) in the following format: 
`"[class_number][class_name][in_class_image_number].png"`
### Table with class numbers and class names is following:

<table>
<tr><td>

| Class_num   |      Class_name      |
|-------------|----------------------|
|      1      |         rtro         |
|      2      |         ruro         |
|      3      |         rfro         |
|      4      |         rtrs         |
|      5      |         rurs         |
|      6      |         rfrs         |
|      7      |         ltro         |
|      8      |         luro         |
|      9      |         lfro         |
|      10     |         ltrs         |
|      11     |         lurs         |
|      12     |         lfrs         |

</td><td>

| Class_num   |      Class_name      |
|-------------|----------------------|
|      13      |         rts         |
|      14      |         rus         |
|      15      |         rfs         |
|      16      |         lts         |
|      17      |         lus         |
|      18      |         lfs         |
|      19      |         rta         |
|      20      |         rua         |
|      21      |         rfa         |
|      22      |         lta         |
|      23      |         lua         |
|      24      |         lfa         |

</td><td>

| Class_num   |      Class_name      |
|-------------|----------------------|
|      25     |         ct          |
|      26     |         cct         |

</td></tr> 
</table>

### Class names are in the form:
`[r/l][t/u/f][ro/rs/s/a] or [c/cc][t]` where:

1. r/l - right/left direction of the gesture
2. t/u/f - target/up/floor direction of the gesture
3. ro/rs/s/a - rolling/rising/strike/arc shape of the gesture
4. c/cc - clockwise/counterclockwise direction of the gesture

### In this repo a small dataset is provided by the creator for a demonstration purposes.
### For a prediction of the gesture class the user have to place an image of the gesture in `/dataset/show/` directory

### To use this repo the user is needed to have an ability to run jupyter notebooks(a short guide can be found on the main page of [PMLDL_Assignment_1](https://github.com/SanikoZmey/PMLDL_Assignment_1)). All explanations of further usage are provided in the form of comments in NN.ipynb.

### If it is a case to locally deploy the project then it is recommended to use already configured python script and Streamlit API:

Install streamlit to your python environment via instructions on a [main page](https://streamlit.io/) \
Clone this repo, open it in terminal and activate python environment with Streamlit package installed \
After that run `streamlit run Flux.py` in terminal \
Now a browser tab with streamlit page is opened and you can use interface with prepred insrtuctions
