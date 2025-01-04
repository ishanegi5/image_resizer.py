import cv2
source=input("Enter the image name to be resized: ")
destination=input("Enter the final image name: ")
format_desired=input("Enter the format of output image: ")
reduction_required=int(input("Enter the percent of reduction you need: "))
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)
percentage_change=reduction_required
new_width=int(src.shape[1]*percentage_change/100)
new_length=int(src.shape[0]*percentage_change/100)
output=cv2.resize(src,(new_width,new_length))
cv2.imwrite(f"{destination}.{format_desired}",output)
cv2.waitKey(0)