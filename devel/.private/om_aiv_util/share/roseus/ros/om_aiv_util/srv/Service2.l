;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::Service2)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'Service2 (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::SERVICE2")
  (make-package "OM_AIV_UTIL::SERVICE2"))
(unless (find-package "OM_AIV_UTIL::SERVICE2REQUEST")
  (make-package "OM_AIV_UTIL::SERVICE2REQUEST"))
(unless (find-package "OM_AIV_UTIL::SERVICE2RESPONSE")
  (make-package "OM_AIV_UTIL::SERVICE2RESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::Service2Request
  :super ros::object
  :slots (_a _b ))

(defmethod om_aiv_util::Service2Request
  (:init
   (&key
    ((:a __a) "")
    ((:b __b) "")
    )
   (send-super :init)
   (setq _a (string __a))
   (setq _b (string __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; string _a
    4 (length _a)
    ;; string _b
    4 (length _b)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _a
       (write-long (length _a) s) (princ _a s)
     ;; string _b
       (write-long (length _b) s) (princ _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _a
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _a (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _b
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _b (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass om_aiv_util::Service2Response
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::Service2Response
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

(defclass om_aiv_util::Service2
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service2 :md5sum-) "4f7d11ca1dbd936717b1bb3469c922e4")
(setf (get om_aiv_util::Service2 :datatype-) "om_aiv_util/Service2")
(setf (get om_aiv_util::Service2 :request) om_aiv_util::Service2Request)
(setf (get om_aiv_util::Service2 :response) om_aiv_util::Service2Response)

(defmethod om_aiv_util::Service2Request
  (:response () (instance om_aiv_util::Service2Response :init)))

(setf (get om_aiv_util::Service2Request :md5sum-) "4f7d11ca1dbd936717b1bb3469c922e4")
(setf (get om_aiv_util::Service2Request :datatype-) "om_aiv_util/Service2Request")
(setf (get om_aiv_util::Service2Request :definition-)
      "string a
string b
---
string device

")

(setf (get om_aiv_util::Service2Response :md5sum-) "4f7d11ca1dbd936717b1bb3469c922e4")
(setf (get om_aiv_util::Service2Response :datatype-) "om_aiv_util/Service2Response")
(setf (get om_aiv_util::Service2Response :definition-)
      "string a
string b
---
string device

")



(provide :om_aiv_util/Service2 "4f7d11ca1dbd936717b1bb3469c922e4")


