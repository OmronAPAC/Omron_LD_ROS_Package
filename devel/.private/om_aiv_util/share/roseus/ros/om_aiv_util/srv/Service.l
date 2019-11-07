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
    ((:a __a) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:serialization-length
   ()
   (+
    ;; int64 _a
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _a
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _a (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _a) (= (length (_a . bv)) 2)) ;; bignum
              (write-long (ash (elt (_a . bv) 0) 0) s)
              (write-long (ash (elt (_a . bv) 1) -1) s))
             ((and (class _a) (= (length (_a . bv)) 1)) ;; big1
              (write-long (elt (_a . bv) 0) s)
              (write-long (if (>= _a 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _a s)(write-long (if (>= _a 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _a
#+(or :alpha :irix6 :x86_64)
      (setf _a (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _a (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass om_aiv_util::ServiceResponse
  :super ros::object
  :slots (_device ))

(defmethod om_aiv_util::ServiceResponse
  (:init
   (&key
    ((:device __device) 0)
    )
   (send-super :init)
   (setq _device (round __device))
   self)
  (:device
   (&optional __device)
   (if __device (setq _device __device)) _device)
  (:serialization-length
   ()
   (+
    ;; int64 _device
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _device
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _device (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _device) (= (length (_device . bv)) 2)) ;; bignum
              (write-long (ash (elt (_device . bv) 0) 0) s)
              (write-long (ash (elt (_device . bv) 1) -1) s))
             ((and (class _device) (= (length (_device . bv)) 1)) ;; big1
              (write-long (elt (_device . bv) 0) s)
              (write-long (if (>= _device 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _device s)(write-long (if (>= _device 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _device
#+(or :alpha :irix6 :x86_64)
      (setf _device (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _device (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass om_aiv_util::Service
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service :md5sum-) "04de0574add1d5e8526e6869cdd49c0c")
(setf (get om_aiv_util::Service :datatype-) "om_aiv_util/Service")
(setf (get om_aiv_util::Service :request) om_aiv_util::ServiceRequest)
(setf (get om_aiv_util::Service :response) om_aiv_util::ServiceResponse)

(defmethod om_aiv_util::ServiceRequest
  (:response () (instance om_aiv_util::ServiceResponse :init)))

(setf (get om_aiv_util::ServiceRequest :md5sum-) "04de0574add1d5e8526e6869cdd49c0c")
(setf (get om_aiv_util::ServiceRequest :datatype-) "om_aiv_util/ServiceRequest")
(setf (get om_aiv_util::ServiceRequest :definition-)
      "int64 a
---
int64 device

")

(setf (get om_aiv_util::ServiceResponse :md5sum-) "04de0574add1d5e8526e6869cdd49c0c")
(setf (get om_aiv_util::ServiceResponse :datatype-) "om_aiv_util/ServiceResponse")
(setf (get om_aiv_util::ServiceResponse :definition-)
      "int64 a
---
int64 device

")



(provide :om_aiv_util/Service "04de0574add1d5e8526e6869cdd49c0c")


