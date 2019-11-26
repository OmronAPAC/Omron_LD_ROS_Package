;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::OmAivService)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'OmAivService (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::OMAIVSERVICE")
  (make-package "OM_AIV_UTIL::OMAIVSERVICE"))
(unless (find-package "OM_AIV_UTIL::OMAIVSERVICEREQUEST")
  (make-package "OM_AIV_UTIL::OMAIVSERVICEREQUEST"))
(unless (find-package "OM_AIV_UTIL::OMAIVSERVICERESPONSE")
  (make-package "OM_AIV_UTIL::OMAIVSERVICERESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::OmAivServiceRequest
  :super ros::object
  :slots (_a ))

(defmethod om_aiv_util::OmAivServiceRequest
  (:init
   (&key
    ((:a __a) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _a __a)
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:serialization-length
   ()
   (+
    ;; string[] _a
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _a)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _a
     (write-long (length _a) s)
     (dolist (elem _a)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _a
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _a (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _a i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass om_aiv_util::OmAivServiceResponse
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::OmAivServiceResponse
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

(defclass om_aiv_util::OmAivService
  :super ros::object
  :slots ())

(setf (get om_aiv_util::OmAivService :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get om_aiv_util::OmAivService :datatype-) "om_aiv_util/OmAivService")
(setf (get om_aiv_util::OmAivService :request) om_aiv_util::OmAivServiceRequest)
(setf (get om_aiv_util::OmAivService :response) om_aiv_util::OmAivServiceResponse)

(defmethod om_aiv_util::OmAivServiceRequest
  (:response () (instance om_aiv_util::OmAivServiceResponse :init)))

(setf (get om_aiv_util::OmAivServiceRequest :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get om_aiv_util::OmAivServiceRequest :datatype-) "om_aiv_util/OmAivServiceRequest")
(setf (get om_aiv_util::OmAivServiceRequest :definition-)
      "string[] a
---
string device

")

(setf (get om_aiv_util::OmAivServiceResponse :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get om_aiv_util::OmAivServiceResponse :datatype-) "om_aiv_util/OmAivServiceResponse")
(setf (get om_aiv_util::OmAivServiceResponse :definition-)
      "string[] a
---
string device

")



(provide :om_aiv_util/OmAivService "b2778cec932742b2c8b6d125219e8d85")


