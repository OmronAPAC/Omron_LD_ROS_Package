;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::Location)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'Location (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::LOCATION")
  (make-package "OM_AIV_UTIL::LOCATION"))

(in-package "ROS")
;;//! \htmlinclude Location.msg.html


(defclass om_aiv_util::Location
  :super ros::object
  :slots (_x _y _theta ))

(defmethod om_aiv_util::Location
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:theta __theta) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _theta (float __theta))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:theta
   (&optional __theta)
   (if __theta (setq _theta __theta)) _theta)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _theta
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _theta
       (sys::poke _theta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _theta
     (setq _theta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get om_aiv_util::Location :md5sum-) "938fa65709584ad8e77d238529be13b8")
(setf (get om_aiv_util::Location :datatype-) "om_aiv_util/Location")
(setf (get om_aiv_util::Location :definition-)
      "# This contains the position of a point in free space
float64 x
float64 y
float64 theta

")



(provide :om_aiv_util/Location "938fa65709584ad8e77d238529be13b8")


