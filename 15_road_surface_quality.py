import pandas as pd
import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
from snowflake import connector
from snowflake.snowpark import Session
from snowflake.cortex import Summarize, Complete, ExtractAnswer, Sentiment, Translate
from snowflake import connector
from snowflake.snowpark import Session
import snowflake.connector
import pandas as pd
import string
import plotly.express as px

st.header(':blue[ROAD SURFACE ASSEMENT USING COMPUTER VISION]', divider="gray")
st.subheader('upload a relatively uniformly lit image of road and we will give you a score')
st.subheader('Lower score indicates a better surface. Ideal score is less than hundread.')

# Importing OpenCV
import cv2

# Importing numpy
import numpy as np

image_arr=["px1.jpg","px2.jpg","px3.jpg","px4.jpg","px5.jpg","px6.jpg","px7.jpg","px8.jpg","px9.jpg","px10.jpg","px11.jpg","px12.jpg"]


st.image(image_arr, width=100, caption=image_arr)

sel_img=st.selectbox("Select an Image",image_arr,index=image_arr.index("px1.jpg"))

# Reading image
# img = cv2.imread("p1.jpg")
# img = cv2.imread("pothole5.jpg")
# img = cv2.imread("pothole4.jpg")
# img = cv2.imread("pothole6.jpg")
# img = cv2.imread("pothole7.jpg")
# img = cv2.imread("pothole8.jpg")
# img = cv2.imread("pothole9.jpg")
# #img = cv2.imread("pothole10.jpg")
# #img = cv2.imread("pothole11.jpg")


#img = cv2.imread("px1.jpg")#98  372*228  121
#img = cv2.imread("px2.jpg")#559 737*506  530
#img = cv2.imread("px3.jpg")#3819 300*201 2476
#img = cv2.imread("px4.jpg")#3819 300*201 2476
#img = cv2.imread("px5.jpg")#211  392*178 202
#img = cv2.imread("px6.jpg")#211  432*280 148
#img = cv2.imread("px7.jpg")#247  395*288  173
#img = cv2.imread("px8.jpg")#115 302*211 106
#img = cv2.imread("px9.jpg")#88 357*182   216
#img = cv2.imread("px10.jpg")#290 488*335   120
#img = cv2.imread("px11.jpg")#95 325*435    49 
#img = cv2.imread("px12.jpg")#73 325*435   64 

# st.image("px11.jpg")
# image=img
# b = image.copy()
# # set green and red channels to 0
# b[:, :, 1] = 0
# b[:, :, 2] = 0


# g = image.copy()
# # set blue and red channels to 0
# g[:, :, 0] = 0
# g[:, :, 2] = 0

# r = image.copy()
# # set blue and green channels to 0
# r[:, :, 0] = 0
# r[:, :, 1] = 0
# img=b

def img_score(img):
    # # # cv2.imshow(img)
    # # # #Finding edges of the image
    edge_image = cv2.Canny(img,250,200)
    # cv2.imshow("edge_image",edge_image)


    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



    ####################################################


    # Defining kernel
    kernel = np.ones((2,2),dtype=np.uint8)
    # Applying dilation operation
    img_dilate = cv2.dilate(edge_image, kernel, iterations=10)
    #Displaying the dilated image

    img_dilate = (255-img_dilate)

    # cv2.imshow('Dilate', img_dilate)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    ####################################################


    # Defining kernel
    kernel = np.ones((2,2),dtype=np.uint8)
    # Applying erosion operation
    img_erode = cv2.erode(img_dilate, kernel, iterations=2)
    #Displaying the eroded image

    # cv2.imshow('Erode', img_erode)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    idi=list(img_erode)

    list1 = [[i] for i in idi]


    list1=[]
    for k in idi:
        list1.append(list(k))


    list_f=[]
    list_x=[]
    for j in list1:
        for i in j:
                if i==np.uint8(255):
                        list_f.append(1)
                else:
                        list_f.append(0)
        list_x.append(list_f)



    # Python Program to find area of the largest region of 1s

    from collections import deque

    # A function to check if cell(r, c) can be included in BFS
    def isSafe(M, r, c, rows, cols):
        
        # row number is in range, column number is in range and
        # value is 1
        return (r >= 0 and r < rows) and (c >= 0 and c < cols) and (M[r][c] == 1)

    # Breadth-First-Search to visit all cells in the current island
    def BFS(M, r, c, rows, cols):
        
        # These arrays are used to get row and column
        # numbers of 8 neighbours of a given cell
        dirR = [-1, -1, -1, 0, 0, 1, 1, 1]
        dirC = [-1, 0, 1, -1, 1, -1, 0, 1]

        area = 0

        # create a queue for bfs traversal
        q = deque()

        # Push the cell(r, c) into queue and mark it as visited
        q.append((r, c))
        M[r][c] = 0
        while q:
            curr = q.popleft()
            
            # Increment the area of region
            area += 1

            # Recur for all 8 connected neighbours
            for i in range(8):
                newR = curr[0] + dirR[i]
                newC = curr[1] + dirC[i]

                if isSafe(M, newR, newC, rows, cols):
                    M[newR][newC] = 0
                    q.append((newR, newC))
        
        return area

    # Function to find area of the largest region of 1s
    def largestRegion(M):
        rows = len(M)
        cols = len(M[0])
    
        # Initialize result as 0 and traverse through the
        # all cells of given matrix
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                
                # If a cell with value 1 is found
                if M[i][j] == 1:
                    area = BFS(M, i, j, rows, cols)

                    # Maximize the area 
                    maxArea = max(maxArea, area)
        
        return maxArea

    # if __name__ == "__main__":
    #     # M = [
    #     #     [1, 0, 0, 0, 1, 0, 0],
    #     #     [0, 1, 0, 0, 1, 1, 1],
    #     #     [1, 1, 0, 0, 0, 0, 0],
    #     #     [1, 0, 0, 1, 1, 0, 0],
    #     #     [1, 0, 0, 1, 0, 1, 1]
    #     # ]
    M=list_x
        
    st.write(str(largestRegion(M)))


# img_score(img)

# for i in image_arr:
#    image = cv2.imread(i)
#    resized_image = cv2.resize(image, (200, 200))
#    st.write("Image Name: "+i)
#    st.image(resized_image)
#    img_score(image)

i=sel_img
image = cv2.imread(i)
resized_image = cv2.resize(image, (200, 200))
st.write("Image Name: "+i)
st.image(resized_image)
st.write("Image Score for surface is:")
im_score=img_score(image)




st.subheader("Upload your JPG file(please maintain the same format). Refer Format of file below Find your score.")
uploaded_files = st.file_uploader(
    "Choose a jpg file", accept_multiple_files=True
)

try:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        if uploaded_file.name.endswith(".jpg"):
            st.write("filename:", uploaded_file.name)
            image = cv2.imread(uploaded_file.name)
            resized_image = cv2.resize(image, (200, 200))
            st.write("Image Name: "+uploaded_file.name)
            st.image(resized_image)
            st.write("Image Score for surface is:")
            img_score(image)
        else:
            st.write("Upload Correct format")
except:
    st.write("File Format not Supported.Using Default data")
    i=sel_img
    image = cv2.imread(i)
    resized_image = cv2.resize(image, (200, 200))
    st.write("Image Name: "+i)
    st.image(resized_image)
    st.write("Image Score for surface is:")
    img_score(image)