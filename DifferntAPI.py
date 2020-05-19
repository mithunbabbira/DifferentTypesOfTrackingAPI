import cv2

def ask_for_tracker():
    print("select the tracker")
    print("press = 0 for BOOSTING ")
    print("press = 1 for MIL ")
    print("press = 2 for KCF ")
    print("press = 3 for TLD ")
    print("press = 4 for MEDIANFLOW ")
    choice = input("Please select your tracker : ")
    
    
    if choice == '0':
        tracker = cv2.TrackerBoosting_create()
            
    if choice == '1':
        tracker = cv2.TrackerMIL_create()
        
    if choice == '2':
        tracker = cv2.TrackerKCF_create()
        
    if choice == '3':
        tracker = cv2.TrackerTLD_create()
        
    if choice == '4':
        tracker = cv2.TrackerMedianFlow_create()
        
        
    return tracker
        

tracker = ask_for_tracker()

tracker_name = str (tracker).split()[0][1:]

cap = cv2.VideoCapture(0)


ret, frame = cap.read()

# special funtion allows us to draw an the very first frame our desired ROI(region of interest)
roi = cv2.selectROI(frame,False)

# Initialize tracker with first frame and bounding box
ret = tracker.init(frame , roi)

while True:
    # Read new frame
    ret ,frame = cap.read()
    
    # Update tracker
    success, roi = tracker.update(frame)
    
    
    # roi variable is a tuple of 4 floats
    # we need each value and we need them as integers
    (x,y,w,h) = tuple(map(int,roi))
    
    
    if success:
        # Tracking success
        p1 = (x,y)
        p2 = (x+w, y+h)
        cv2.rectangle(frame,p1,p2,(0,255,0),3)
        
    else:
        print("fucked up")
    
    cv2.putText(frame,tracker_name,(20,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
    
    
    cv2.imshow(tracker_name,frame)
    
    
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    





