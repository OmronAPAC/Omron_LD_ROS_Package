;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::Service9)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'Service9 (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::SERVICE9")
  (make-package "OM_AIV_UTIL::SERVICE9"))
(unless (find-package "OM_AIV_UTIL::SERVICE9REQUEST")
  (make-package "OM_AIV_UTIL::SERVICE9REQUEST"))
(unless (find-package "OM_AIV_UTIL::SERVICE9RESPONSE")
  (make-package "OM_AIV_UTIL::SERVICE9RESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::Service9Request
  :super ros::object
  :slots (_a ))

(defmethod om_aiv_util::Service9Request
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

(defclass om_aiv_util::Service9Response
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::Service9Response
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

(defclass om_aiv_util::Service9
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service9 :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get om_aiv_util::Service9 :datatype-) "om_aiv_util/Service9")
(setf (get om_aiv_util::Service9 :request) om_aiv_util::Service9Request)
(setf (get om_aiv_util::Service9 :response) om_aiv_util::Service9Response)

(defmethod om_aiv_util::Service9Request
  (:response () (instance om_aiv_util::Service9Response :init)))

(setf (get om_aiv_util::Service9Request :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get om_aiv_util::Service9Request :datatype-) "om_aiv_util/Service9Request")
(setf (get om_aiv_util::Service9Request :definition-)
      "string[] a
---
string device

")

(setf (get om_aiv_util::Service9Response :md5sum-) "b2778cec932742b2c8b6d125219e8d85")
(setf (get om_aiv_util::Service9Response :datatype-) "om_aiv_util/Service9Response")
(setf (get om_aiv_util::Service9Response :definition-)
      "string[] a
---
string device

")



(provide :om_aiv_util/Service9 "b2778cec932742b2c8b6d125219e8d85")


