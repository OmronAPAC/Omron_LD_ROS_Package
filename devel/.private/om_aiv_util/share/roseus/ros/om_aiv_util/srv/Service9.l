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
    ((:a __a) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:b __b) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:c __c) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:d __d) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:e __e) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:f __f) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:g __g) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:h __h) (let (r) (dotimes (i 0) (push "" r)) r))
    ((:i __i) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _a __a)
   (setq _b __b)
   (setq _c __c)
   (setq _d __d)
   (setq _e __e)
   (setq _f __f)
   (setq _g __g)
   (setq _h __h)
   (setq _i __i)
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
    ;; string[] _a
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _a)) 4
    ;; string[] _b
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _b)) 4
    ;; string[] _c
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _c)) 4
    ;; string[] _d
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _d)) 4
    ;; string[] _e
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _e)) 4
    ;; string[] _f
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _f)) 4
    ;; string[] _g
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _g)) 4
    ;; string[] _h
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _h)) 4
    ;; string[] _i
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _i)) 4
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
     ;; string[] _b
     (write-long (length _b) s)
     (dolist (elem _b)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _c
     (write-long (length _c) s)
     (dolist (elem _c)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _d
     (write-long (length _d) s)
     (dolist (elem _d)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _e
     (write-long (length _e) s)
     (dolist (elem _e)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _f
     (write-long (length _f) s)
     (dolist (elem _f)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _g
     (write-long (length _g) s)
     (dolist (elem _g)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _h
     (write-long (length _h) s)
     (dolist (elem _h)
       (write-long (length elem) s) (princ elem s)
       )
     ;; string[] _i
     (write-long (length _i) s)
     (dolist (elem _i)
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
   ;; string[] _b
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _b (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _b i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _c
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _c (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _c i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _d
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _d (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _d i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _e
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _e (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _e i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _f
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _f (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _f i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _g
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _g (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _g i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _h
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _h (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _h i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;; string[] _i
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _i (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _i i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
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
    ((:device __device) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _device __device)
   self)
  (:device
   (&optional __device)
   (if __device (setq _device __device)) _device)
  (:serialization-length
   ()
   (+
    ;; string[] _device
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _device)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _device
     (write-long (length _device) s)
     (dolist (elem _device)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _device
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _device (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _device i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass om_aiv_util::Service9
  :super ros::object
  :slots ())

(setf (get om_aiv_util::Service9 :md5sum-) "8f3b2965311f37d071bd387981e3ad17")
(setf (get om_aiv_util::Service9 :datatype-) "om_aiv_util/Service9")
(setf (get om_aiv_util::Service9 :request) om_aiv_util::Service9Request)
(setf (get om_aiv_util::Service9 :response) om_aiv_util::Service9Response)

(defmethod om_aiv_util::Service9Request
  (:response () (instance om_aiv_util::Service9Response :init)))

(setf (get om_aiv_util::Service9Request :md5sum-) "8f3b2965311f37d071bd387981e3ad17")
(setf (get om_aiv_util::Service9Request :datatype-) "om_aiv_util/Service9Request")
(setf (get om_aiv_util::Service9Request :definition-)
      "string[] a
string[] b
string[] c
string[] d
string[] e
string[] f
string[] g
string[] h
string[] i
---
string[] device

")

(setf (get om_aiv_util::Service9Response :md5sum-) "8f3b2965311f37d071bd387981e3ad17")
(setf (get om_aiv_util::Service9Response :datatype-) "om_aiv_util/Service9Response")
(setf (get om_aiv_util::Service9Response :definition-)
      "string[] a
string[] b
string[] c
string[] d
string[] e
string[] f
string[] g
string[] h
string[] i
---
string[] device

")



(provide :om_aiv_util/Service9 "8f3b2965311f37d071bd387981e3ad17")


