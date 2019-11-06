;; Auto-generated. Do not edit!


(when (boundp 'ld_services::ServiceExample)
  (if (not (find-package "LD_SERVICES"))
    (make-package "LD_SERVICES"))
  (shadow 'ServiceExample (find-package "LD_SERVICES")))
(unless (find-package "LD_SERVICES::SERVICEEXAMPLE")
  (make-package "LD_SERVICES::SERVICEEXAMPLE"))
(unless (find-package "LD_SERVICES::SERVICEEXAMPLEREQUEST")
  (make-package "LD_SERVICES::SERVICEEXAMPLEREQUEST"))
(unless (find-package "LD_SERVICES::SERVICEEXAMPLERESPONSE")
  (make-package "LD_SERVICES::SERVICEEXAMPLERESPONSE"))

(in-package "ROS")





(defclass ld_services::ServiceExampleRequest
  :super ros::object
  :slots (_onezero ))

(defmethod ld_services::ServiceExampleRequest
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

(defclass ld_services::ServiceExampleResponse
  :super ros::object
  :slots (_turn ))

(defmethod ld_services::ServiceExampleResponse
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

(defclass ld_services::ServiceExample
  :super ros::object
  :slots ())

(setf (get ld_services::ServiceExample :md5sum-) "b6541b31be965d2ea76445e10907a742")
(setf (get ld_services::ServiceExample :datatype-) "ld_services/ServiceExample")
(setf (get ld_services::ServiceExample :request) ld_services::ServiceExampleRequest)
(setf (get ld_services::ServiceExample :response) ld_services::ServiceExampleResponse)

(defmethod ld_services::ServiceExampleRequest
  (:response () (instance ld_services::ServiceExampleResponse :init)))

(setf (get ld_services::ServiceExampleRequest :md5sum-) "b6541b31be965d2ea76445e10907a742")
(setf (get ld_services::ServiceExampleRequest :datatype-) "ld_services/ServiceExampleRequest")
(setf (get ld_services::ServiceExampleRequest :definition-)
      "int32 onezero
---
string turn

")

(setf (get ld_services::ServiceExampleResponse :md5sum-) "b6541b31be965d2ea76445e10907a742")
(setf (get ld_services::ServiceExampleResponse :datatype-) "ld_services/ServiceExampleResponse")
(setf (get ld_services::ServiceExampleResponse :definition-)
      "int32 onezero
---
string turn

")



(provide :ld_services/ServiceExample "b6541b31be965d2ea76445e10907a742")


