;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::Service)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'Service (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::SERVICE")
  (make-package "OM_AIV_UTIL::SERVICE"))
(unless (find-package "OM_AIV_UTIL::SERVICEREQUEST")
  (make-package "OM_AIV_UTIL::SERVICEREQUEST"))
(unless (find-package "OM_AIV_UTIL::SERVICERESPONSE")
  (make-package "OM_AIV_UTIL::SERVICERESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::ServiceRequest
  :super ros::object
  :slots (_a ))

(defmethod om_aiv_util::ServiceRequest
  (:init
   (&key
    ((:a __a) "")
    )
   (send-super :init)
   (setq _a (string __a))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:serialization-length
   ()
   (+
    ;; string _a
    4 (length _a)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _a
       (write-long (length _a) s) (princ _a s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _a
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _a (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass om_aiv_util::ServiceResponse
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::ServiceResponse
  (:init
   (&key
    ((:device __device) "")
    )
   (send-super :init)
   (setq _device (string __device))
   self)
  (:device
   (&optional __device)
   (if __device (setq _device __device)) _device)
  (:serialization-length
   ()
   (+
    ;; string _device
    4 (length _device)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _device
       (write-long (length _device) s) (princ _device s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _device
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _device (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass om_aiv_util::Service
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service :md5sum-) "9965534556d6f239219ba39e543ce36b")
(setf (get om_aiv_util::Service :datatype-) "om_aiv_util/Service")
(setf (get om_aiv_util::Service :request) om_aiv_util::ServiceRequest)
(setf (get om_aiv_util::Service :response) om_aiv_util::ServiceResponse)

(defmethod om_aiv_util::ServiceRequest
  (:response () (instance om_aiv_util::ServiceResponse :init)))

(setf (get om_aiv_util::ServiceRequest :md5sum-) "9965534556d6f239219ba39e543ce36b")
(setf (get om_aiv_util::ServiceRequest :datatype-) "om_aiv_util/ServiceRequest")
(setf (get om_aiv_util::ServiceRequest :definition-)
      "string a
---
string device

")

(setf (get om_aiv_util::ServiceResponse :md5sum-) "9965534556d6f239219ba39e543ce36b")
(setf (get om_aiv_util::ServiceResponse :datatype-) "om_aiv_util/ServiceResponse")
(setf (get om_aiv_util::ServiceResponse :definition-)
      "string a
---
string device

")



(provide :om_aiv_util/Service "9965534556d6f239219ba39e543ce36b")


