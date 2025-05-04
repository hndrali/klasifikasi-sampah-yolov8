from ultralytics import YOLO
import streamlit as st
import cv2
import pickle
import settings
import numpy as np

#loaded_model=pickle.load(open('C:/Users/MY PC/Desktop/yolov8/yolov8-streamlit-detection-tracking/weights/yolov8.pkl', 'rb'))
with open(settings.MODEL_DIR + '/yolov81.pkl', 'rb') as file:
    model1= pickle.load(file)



def load_model(model_path):
    """
    Loads a YOLO object detection model from the specified model_path.

    Parameters:
        model_path (str): The path to the YOLO model file.

    Returns:
        A YOLO object detection model.
    """
    model = YOLO(settings.MODEL_DIR + '/yoloooo.pt')
    return model


def display_tracker_options():
    is_display_tracker = True
    if is_display_tracker:
        return is_display_tracker, "bytetrack.yaml"
    return is_display_tracker, None


def _display_detected_frames(conf, model, st_notif, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    # hasil = res_plotted

    if(np.where(res_plotted =="BIODEGREDABLE")[0].size != 0):
        st_notif.success("Sampah terdeteksi berjenis: Organik")
    else:
        st_notif.warning("Sampah terdeteksi berjenis: Anorganik")

    st_frame.image(res_plotted,
                   caption='Hasil Foto',
                   channels="BGR",
                   use_container_width=True
                   )


def play_webcam(conf, model, st_notif):
    """
    Plays a webcam stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None

    Raises:
        None
    """
    st_notif.info("Masukkan sampah untuk dikelompokkan. Alat akan mendeteksi secara otomatis", icon="🚮", width="stretch")

    source_webcam = settings.WEBCAM_PATH
    is_display_tracker, tracker = display_tracker_options()
    if st.sidebar.button('Detect Trash'):
         
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(conf,
                                             model,
                                             st_notif,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker,
                                             )
                    vid_cap.release()
                   
        except Exception as e:
            st.sidebar.error("Mohon Maaf, kamera bermasalah")

