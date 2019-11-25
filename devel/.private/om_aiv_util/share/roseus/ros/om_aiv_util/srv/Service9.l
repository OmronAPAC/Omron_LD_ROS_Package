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
  :slots (_a _b _c _d _e _f _g _h _i ))

(defmethod om_aiv_util::Service9Request
  (:init
   (&key
    ((:a __a) "")
    ((:b __b) "")
    ((:c __c) "")
    ((:d __d) "")
    ((:e __e) "")
    ((:f __f) "")
    ((:g __g) "")
    ((:h __h) "")
    ((:i __i) "")
    )
   (send-super :init)
   (setq _a (string __a))
   (setq _b (string __b))
   (setq _c (string __c))
   (setq _d (string __d))
   (setq _e (string __e))
   (setq _f (string __f))
   (setq _g (string __g))
   (setq _h (string __h))
   (setq _i (string __i))
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
  (:f
   (&optional __f)
   (if __f (setq _f __f)) _f)
  (:g
   (&optional __g)
   (if __g (setq _g __g)) _g)
  (:h
   (&optional __h)
   (if __h (setq _h __h)) _h)
  (:i
   (&optional __i)
   (if __i (setq _i __i)) _i)
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
    ;; string _f
    4 (length _f)
    ;; string _g
    4 (length _g)
    ;; string _h
    4 (length _h)
    ;; string _i
    4 (length _i)
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
     ;; string _f
       (write-long (length _f) s) (princ _f s)
     ;; string _g
       (write-long (length _g) s) (princ _g s)
     ;; string _h
       (write-long (length _h) s) (princ _h s)
     ;; string _i
       (write-long (length _i) s) (princ _i s)
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
   ;; string _f
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _f (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _g
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _g (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _h
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _h (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _i
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _i (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
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

(setf (get om_aiv_util::Service9 :md5sum-) "4b23d66356efea8d732881ac3520af2b")
(setf (get om_aiv_util::Service9 :datatype-) "om_aiv_util/Service9")
(setf (get om_aiv_util::Service9 :request) om_aiv_util::Service9Request)
(setf (get om_aiv_util::Service9 :response) om_aiv_util::Service9Response)

(defmethod om_aiv_util::Service9Request
  (:response () (instance om_aiv_util::Service9Response :init)))

(setf (get om_aiv_util::Service9Request :md5sum-) "4b23d66356efea8d732881ac3520af2b")
(setf (get om_aiv_util::Service9Request :datatype-) "om_aiv_util/Service9Request")
(setf (get om_aiv_util::Service9Request :definition-)
      "string a
string b
string c
string d
string e
string f
string g
string h
string i
---
string device

")

(setf (get om_aiv_util::Service9Response :md5sum-) "4b23d66356efea8d732881ac3520af2b")
(setf (get om_aiv_util::Service9Response :datatype-) "om_aiv_util/Service9Response")
(setf (get om_aiv_util::Service9Response :definition-)
      "string a
string b
string c
string d
string e
string f
string g
string h
string i
---
string device

")



(provide :om_aiv_util/Service9 "4b23d66356efea8d732881ac3520af2b")


