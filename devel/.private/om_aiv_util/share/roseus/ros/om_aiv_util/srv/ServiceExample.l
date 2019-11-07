;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_util::ServiceExample)
  (if (not (find-package "OM_AIV_UTIL"))
    (make-package "OM_AIV_UTIL"))
  (shadow 'ServiceExample (find-package "OM_AIV_UTIL")))
(unless (find-package "OM_AIV_UTIL::SERVICEEXAMPLE")
  (make-package "OM_AIV_UTIL::SERVICEEXAMPLE"))
(unless (find-package "OM_AIV_UTIL::SERVICEEXAMPLEREQUEST")
  (make-package "OM_AIV_UTIL::SERVICEEXAMPLEREQUEST"))
(unless (find-package "OM_AIV_UTIL::SERVICEEXAMPLERESPONSE")
  (make-package "OM_AIV_UTIL::SERVICEEXAMPLERESPONSE"))

(in-package "ROS")





(defclass om_aiv_util::ServiceExampleRequest
  :super ros::object
  :slots (_onezero ))

(defmethod om_aiv_util::ServiceExampleRequest
  (:init
   (&key
    ((:onezero __onezero) 0)
    )
   (send-super :init)
   (setq _onezero (round __onezero))
   self)
  (:onezero
   (&optional __onezero)
   (if __onezero (setq _onezero __onezero)) _onezero)
  (:serialization-length
   ()
   (+
    ;; int32 _onezero
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _onezero
       (write-long _onezero s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _onezero
     (setq _onezero (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass om_aiv_util::ServiceExampleResponse
  :super ros::object
  :slots (_turn ))

(defmethod om_aiv_util::ServiceExampleResponse
  (:init
   (&key
    ((:turn __turn) "")
    )
   (send-super :init)
   (setq _turn (string __turn))
   self)
  (:turn
   (&optional __turn)
   (if __turn (setq _turn __turn)) _turn)
  (:serialization-length
   ()
   (+
    ;; string _turn
    4 (length _turn)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _turn
       (write-long (length _turn) s) (princ _turn s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _turn
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _turn (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass om_aiv_util::ServiceExample
  :super ros::object
  :slots ())

(setf (get om_aiv_util::ServiceExample :md5sum-) "b6541b31be965d2ea76445e10907a742")
(setf (get om_aiv_util::ServiceExample :datatype-) "om_aiv_util/ServiceExample")
(setf (get om_aiv_util::ServiceExample :request) om_aiv_util::ServiceExampleRequest)
(setf (get om_aiv_util::ServiceExample :response) om_aiv_util::ServiceExampleResponse)

(defmethod om_aiv_util::ServiceExampleRequest
  (:response () (instance om_aiv_util::ServiceExampleResponse :init)))

(setf (get om_aiv_util::ServiceExampleRequest :md5sum-) "b6541b31be965d2ea76445e10907a742")
(setf (get om_aiv_util::ServiceExampleRequest :datatype-) "om_aiv_util/ServiceExampleRequest")
(setf (get om_aiv_util::ServiceExampleRequest :definition-)
      "int32 onezero
---
string turn

")

(setf (get om_aiv_util::ServiceExampleResponse :md5sum-) "b6541b31be965d2ea76445e10907a742")
(setf (get om_aiv_util::ServiceExampleResponse :datatype-) "om_aiv_util/ServiceExampleResponse")
(setf (get om_aiv_util::ServiceExampleResponse :definition-)
      "int32 onezero
---
string turn

")



(provide :om_aiv_util/ServiceExample "b6541b31be965d2ea76445e10907a742")


