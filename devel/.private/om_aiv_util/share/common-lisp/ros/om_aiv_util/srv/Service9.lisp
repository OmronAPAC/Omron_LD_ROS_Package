; Auto-generated. Do not edit!


(cl:in-package om_aiv_util-srv)


;//! \htmlinclude Service9-request.msg.html

(cl:defclass <Service9-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:string
    :initform "")
   (b
    :reader b
    :initarg :b
    :type cl:string
    :initform "")
   (c
    :reader c
    :initarg :c
    :type cl:string
    :initform "")
   (d
    :reader d
    :initarg :d
    :type cl:string
    :initform "")
   (e
    :reader e
    :initarg :e
    :type cl:string
    :initform "")
   (f
    :reader f
    :initarg :f
    :type cl:string
    :initform "")
   (g
    :reader g
    :initarg :g
    :type cl:string
    :initform "")
   (h
    :reader h
    :initarg :h
    :type cl:string
    :initform "")
   (i
    :reader i
    :initarg :i
    :type cl:string
    :initform ""))
)

(cl:defclass Service9-request (<Service9-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service9-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service9-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service9-request> is deprecated: use om_aiv_util-srv:Service9-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:a-val is deprecated.  Use om_aiv_util-srv:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:b-val is deprecated.  Use om_aiv_util-srv:b instead.")
  (b m))

(cl:ensure-generic-function 'c-val :lambda-list '(m))
(cl:defmethod c-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:c-val is deprecated.  Use om_aiv_util-srv:c instead.")
  (c m))

(cl:ensure-generic-function 'd-val :lambda-list '(m))
(cl:defmethod d-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:d-val is deprecated.  Use om_aiv_util-srv:d instead.")
  (d m))

(cl:ensure-generic-function 'e-val :lambda-list '(m))
(cl:defmethod e-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:e-val is deprecated.  Use om_aiv_util-srv:e instead.")
  (e m))

(cl:ensure-generic-function 'f-val :lambda-list '(m))
(cl:defmethod f-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:f-val is deprecated.  Use om_aiv_util-srv:f instead.")
  (f m))

(cl:ensure-generic-function 'g-val :lambda-list '(m))
(cl:defmethod g-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:g-val is deprecated.  Use om_aiv_util-srv:g instead.")
  (g m))

(cl:ensure-generic-function 'h-val :lambda-list '(m))
(cl:defmethod h-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:h-val is deprecated.  Use om_aiv_util-srv:h instead.")
  (h m))

(cl:ensure-generic-function 'i-val :lambda-list '(m))
(cl:defmethod i-val ((m <Service9-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:i-val is deprecated.  Use om_aiv_util-srv:i instead.")
  (i m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service9-request>) ostream)
  "Serializes a message object of type '<Service9-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'a))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'a))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'b))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'b))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'c))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'c))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'd))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'e))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'e))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'f))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'f))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'g))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'g))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'h))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'h))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'i))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'i))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service9-request>) istream)
  "Deserializes a message object of type '<Service9-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'a) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'b) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'b) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'c) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'c) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'd) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'd) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'e) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'e) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'f) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'f) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'g) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'g) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'h) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'h) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'i) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service9-request>)))
  "Returns string type for a service object of type '<Service9-request>"
  "om_aiv_util/Service9Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service9-request)))
  "Returns string type for a service object of type 'Service9-request"
  "om_aiv_util/Service9Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service9-request>)))
  "Returns md5sum for a message object of type '<Service9-request>"
  "4b23d66356efea8d732881ac3520af2b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service9-request)))
  "Returns md5sum for a message object of type 'Service9-request"
  "4b23d66356efea8d732881ac3520af2b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service9-request>)))
  "Returns full string definition for message of type '<Service9-request>"
  (cl:format cl:nil "string a~%string b~%string c~%string d~%string e~%string f~%string g~%string h~%string i~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service9-request)))
  "Returns full string definition for message of type 'Service9-request"
  (cl:format cl:nil "string a~%string b~%string c~%string d~%string e~%string f~%string g~%string h~%string i~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service9-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'a))
     4 (cl:length (cl:slot-value msg 'b))
     4 (cl:length (cl:slot-value msg 'c))
     4 (cl:length (cl:slot-value msg 'd))
     4 (cl:length (cl:slot-value msg 'e))
     4 (cl:length (cl:slot-value msg 'f))
     4 (cl:length (cl:slot-value msg 'g))
     4 (cl:length (cl:slot-value msg 'h))
     4 (cl:length (cl:slot-value msg 'i))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service9-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Service9-request
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
    (cl:cons ':c (c msg))
    (cl:cons ':d (d msg))
    (cl:cons ':e (e msg))
    (cl:cons ':f (f msg))
    (cl:cons ':g (g msg))
    (cl:cons ':h (h msg))
    (cl:cons ':i (i msg))
))
;//! \htmlinclude Service9-response.msg.html

(cl:defclass <Service9-response> (roslisp-msg-protocol:ros-message)
  ((device
    :reader device
    :initarg :device
    :type cl:string
    :initform ""))
)

(cl:defclass Service9-response (<Service9-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Service9-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Service9-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name om_aiv_util-srv:<Service9-response> is deprecated: use om_aiv_util-srv:Service9-response instead.")))

(cl:ensure-generic-function 'device-val :lambda-list '(m))
(cl:defmethod device-val ((m <Service9-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader om_aiv_util-srv:device-val is deprecated.  Use om_aiv_util-srv:device instead.")
  (device m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Service9-response>) ostream)
  "Serializes a message object of type '<Service9-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'device))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'device))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Service9-response>) istream)
  "Deserializes a message object of type '<Service9-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'device) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'device) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Service9-response>)))
  "Returns string type for a service object of type '<Service9-response>"
  "om_aiv_util/Service9Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service9-response)))
  "Returns string type for a service object of type 'Service9-response"
  "om_aiv_util/Service9Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Service9-response>)))
  "Returns md5sum for a message object of type '<Service9-response>"
  "4b23d66356efea8d732881ac3520af2b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Service9-response)))
  "Returns md5sum for a message object of type 'Service9-response"
  "4b23d66356efea8d732881ac3520af2b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Service9-response>)))
  "Returns full string definition for message of type '<Service9-response>"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Service9-response)))
  "Returns full string definition for message of type 'Service9-response"
  (cl:format cl:nil "string device~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Service9-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'device))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Service9-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Service9-response
    (cl:cons ':device (device msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Service9)))
  'Service9-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Service9)))
  'Service9-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Service9)))
  "Returns string type for a service object of type '<Service9>"
  "om_aiv_util/Service9")