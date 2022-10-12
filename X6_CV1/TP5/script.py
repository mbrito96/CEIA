# # # Consigna TP5
# Parte 1:
# Implementar el detector de fondo naive usando la mediana como
# estimador El algoritmo debe recibir el parámetro N (cantidad de
# frames utilizados para la estimación) y el intervalo de tiempo para
# recalcular el fondo

# Parte 2:
# Se deben generar las mascaras de foreground y aplicarlas a los frames
# para segmentar los objetos en movimiento

# Parte 3:
# Comparar con alguno de los métodos vistos en la practica basados en
# mezcla de gaussianas

# importing libraries
from types import NoneType
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Naive background substraction')
parser.add_argument('-F', type=int, help='Cantidad de frames utilizados para la estimacion')
parser.add_argument('-S', type=int, help='Segundos para recalcular el fondo')

args = parser.parse_args()
variables = vars(args)
print(variables['F'])
bkg_n_frames = variables['F']	# Number of frames to use when calculating the background
bkg_sec_recalc = variables['S']	# Seconds between background calculations

# while(1):
#     pass
# Create a VideoCapture object and read from input file
videos = ['slow_traffic_small.mp4', 'vtest.mp4']
cap = cv.VideoCapture(videos[1])

# Check if camera opened successfully
if (cap.isOpened()== False):
	print("Error opening video file")

frame_count = cap.get(cv.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv.CAP_PROP_FPS)
length_s = frame_count / fps
print(f'Frame count= {frame_count} ; FPS= {fps} ; Length(s)= {length_s}')

bkg_frame_delta = bkg_sec_recalc * fps	# number of frames between bkg recalc attempts
frameIds = (bkg_frame_delta * np.random.uniform(size=bkg_n_frames, low=0.1, high=0.9)).astype(int) # frame ids to extract
frames=[]
last_bkg_update = 0
bkg_is_live = False  # True if background was extracted

print((frameIds))
medianFrame = 0
grayMedianFrame = 0

cap.set(cv.CAP_PROP_POS_FRAMES, 0)	# Start the video from the beginning
while(cap.isOpened()):
	ret, frame = cap.read()
	curr_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
	if ret == True:
		if((curr_frame - last_bkg_update) in frameIds):
			print('this frame')
			frames.append(frame)
		if( (curr_frame - last_bkg_update) > bkg_frame_delta):	# Check if enough frames have elapsed since las update
			medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)   # Compute background
			grayMedianFrame = cv.cvtColor(medianFrame, cv.COLOR_BGR2GRAY)
			last_bkg_update = curr_frame
			# frames.clear()
			# frames.append(medianFrame)	# Append last median for history


		frame_bw = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		dframe = cv.absdiff(frame_bw, grayMedianFrame)
		th, mask_foreground = cv.threshold(dframe, 30, 255, cv.THRESH_BINARY)
		mask_background = cv.bitwise_not(mask_foreground)
		foreground = cv.bitwise_and(frame, frame, mask= mask_foreground)
		background = cv.bitwise_and(frame, frame, mask= mask_background)
		cv.imshow('Frame', foreground)
		cv.imshow('Background', background)

		
		if cv.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

cap.release()
cv.destroyAllWindows()