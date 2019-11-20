;; Auto-generated. Do not edit!


(when (boundp 'om_aiv_navigation::QueueDropoffFeedback)
  (if (not (find-package "OM_AIV_NAVIGATION"))
    (make-package "OM_AIV_NAVIGATION"))
  (shadow 'QueueDropoffFeedback (find-package "OM_AIV_NAVIGATION")))
(unless (find-package "OM_AIV_NAVIGATION::QUEUEDROPOFFFEEDBACK")
  (make-package "OM_AIV_NAVIGATION::QUEUEDROPOFFFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude QueueDropoffFeedback.msg.html


(defclass om_aiv_navigation::QueueDropoffFeedback
  :super ros::object
  :slots (_received_data ))

(defmethod om_aiv_navigation::QueueDropoffFeedback
  (:init
   (&key
    ((:received_data __received_data) "")
    )
   (send-super :init)
   (setq _received_data (string __received_data))
   self)
  (:received_data
   (&optional __received_data)
   (if __received_data (setq _received_data __received_data)) _received_data)
  (:serialization-length
   ()
   (+
    ;; string _received_data
    4 (length _received_data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _received_data
       (write-long (length _received_data) s) (princ _received_data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _received_data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _received_data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get om_aiv_navigation::QueueDropoffFeedback :md5sum-) "0db3bc19eeede9e4ee493e93f03da761")
(setf (get om_aiv_navigation::QueueDropoffFeedback :datatype-) "om_aiv_navigation/QueueDropoffFeedback")
(setf (get om_aiv_navigation::QueueDropoffFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback
string received_data


")



(provide :om_aiv_navigation/QueueDropoffFeedback "0db3bc19eeede9e4ee493e93f03da761")

