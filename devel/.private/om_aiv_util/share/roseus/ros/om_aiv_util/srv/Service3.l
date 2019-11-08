;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::Service3)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'Service3 (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::SERVICE3")
  (make-package "OM_AIV_UTIL::SERVICE3"))
(unless (find-package "OM_AIV_UTIL::SERVICE3REQUEST")
  (make-package "OM_AIV_UTIL::SERVICE3REQUEST"))
(unless (find-package "OM_AIV_UTIL::SERVICE3RESPONSE")
  (make-package "OM_AIV_UTIL::SERVICE3RESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::Service3Request
  :super ros::object
  :slots (_a _b _c ))

(defmethod om_aiv_util::Service3Request
  (:init
   (&key
    ((:a __a) "")
    ((:b __b) "")
    ((:c __c) "")
    )
   (send-super :init)
   (setq _a (string __a))
   (setq _b (string __b))
   (setq _c (string __c))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:c
   (&optional __c)
   (if __c (setq _c __c)) _c)
  (:serialization-length
   ()
   (+
    ;; string _a
    4 (length _a)
    ;; string _b
    4 (length _b)
    ;; string _c
    4 (length _c)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _a
       (write-long (length _a) s) (princ _a s)
     ;; string _b
       (write-long (length _b) s) (princ _b s)
     ;; string _c
       (write-long (length _c) s) (princ _c s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _a
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _a (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _b
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _b (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _c
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _c (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass om_aiv_util::Service3Response
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::Service3Response
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

(defclass om_aiv_util::Service3
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service3 :md5sum-) "6d29793b95b92fdf3218d77308234efd")
(setf (get om_aiv_util::Service3 :datatype-) "om_aiv_util/Service3")
(setf (get om_aiv_util::Service3 :request) om_aiv_util::Service3Request)
(setf (get om_aiv_util::Service3 :response) om_aiv_util::Service3Response)

(defmethod om_aiv_util::Service3Request
  (:response () (instance om_aiv_util::Service3Response :init)))

(setf (get om_aiv_util::Service3Request :md5sum-) "6d29793b95b92fdf3218d77308234efd")
(setf (get om_aiv_util::Service3Request :datatype-) "om_aiv_util/Service3Request")
(setf (get om_aiv_util::Service3Request :definition-)
      "string a
string b
string c
---
string device

")

(setf (get om_aiv_util::Service3Response :md5sum-) "6d29793b95b92fdf3218d77308234efd")
(setf (get om_aiv_util::Service3Response :datatype-) "om_aiv_util/Service3Response")
(setf (get om_aiv_util::Service3Response :definition-)
      "string a
string b
string c
---
string device

")



(provide :om_aiv_util/Service3 "6d29793b95b92fdf3218d77308234efd")


