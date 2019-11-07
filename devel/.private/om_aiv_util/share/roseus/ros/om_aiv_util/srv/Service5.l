;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::Service5)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'Service5 (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::SERVICE5")
  (make-package "OM_AIV_UTIL::SERVICE5"))
(unless (find-package "OM_AIV_UTIL::SERVICE5REQUEST")
  (make-package "OM_AIV_UTIL::SERVICE5REQUEST"))
(unless (find-package "OM_AIV_UTIL::SERVICE5RESPONSE")
  (make-package "OM_AIV_UTIL::SERVICE5RESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::Service5Request
  :super ros::object
  :slots (_a _b _c _d _e ))

(defmethod om_aiv_util::Service5Request
  (:init
   (&key
    ((:a __a) "")
    ((:b __b) "")
    ((:c __c) "")
    ((:d __d) "")
    ((:e __e) "")
    )
   (send-super :init)
   (setq _a (string __a))
   (setq _b (string __b))
   (setq _c (string __c))
   (setq _d (string __d))
   (setq _e (string __e))
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
  (:d
   (&optional __d)
   (if __d (setq _d __d)) _d)
  (:e
   (&optional __e)
   (if __e (setq _e __e)) _e)
  (:serialization-length
   ()
   (+
    ;; string _a
    4 (length _a)
    ;; string _b
    4 (length _b)
    ;; string _c
    4 (length _c)
    ;; string _d
    4 (length _d)
    ;; string _e
    4 (length _e)
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
     ;; string _d
       (write-long (length _d) s) (princ _d s)
     ;; string _e
       (write-long (length _e) s) (princ _e s)
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
   ;; string _d
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _d (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _e
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _e (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass om_aiv_util::Service5Response
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::Service5Response
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

(defclass om_aiv_util::Service5
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service5 :md5sum-) "92b9e35a523fcf2c6affbc657156b6ea")
(setf (get om_aiv_util::Service5 :datatype-) "om_aiv_util/Service5")
(setf (get om_aiv_util::Service5 :request) om_aiv_util::Service5Request)
(setf (get om_aiv_util::Service5 :response) om_aiv_util::Service5Response)

(defmethod om_aiv_util::Service5Request
  (:response () (instance om_aiv_util::Service5Response :init)))

(setf (get om_aiv_util::Service5Request :md5sum-) "92b9e35a523fcf2c6affbc657156b6ea")
(setf (get om_aiv_util::Service5Request :datatype-) "om_aiv_util/Service5Request")
(setf (get om_aiv_util::Service5Request :definition-)
      "string a
string b
string c
string d
string e
---
string device

")

(setf (get om_aiv_util::Service5Response :md5sum-) "92b9e35a523fcf2c6affbc657156b6ea")
(setf (get om_aiv_util::Service5Response :datatype-) "om_aiv_util/Service5Response")
(setf (get om_aiv_util::Service5Response :definition-)
      "string a
string b
string c
string d
string e
---
string device

")



(provide :om_aiv_util/Service5 "92b9e35a523fcf2c6affbc657156b6ea")


